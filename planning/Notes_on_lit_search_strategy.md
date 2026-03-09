Idea for pseudo gene set enrichment from lit, to deal with challenge - how can we efficiently and sufficiently search the lit for relevant content.

Assumptions to check

- PMC/pubmed queries have genes in keywords (check)
- PMC/pubmed queries support OR and will prioritise hits combos over single hits

Given this, one could throw a whole gene list without prioritisation and get back ranked hits with multiple genes - starting from the largest.  (Need to test - how long can the gene list be?)

This gives a starting point for ASTA snippet searches (https://allenai.org/asta/resources/mcp) within paper for combination of genes from query list that are also in the keywords (scaling might be an issue if this intersection is long, but ASTA snippet queries are cheap).

Plausible 


Thought for 55s

Your “pseudo gene-set enrichment via ranked lit hits” idea is pretty plausible — with a couple of important caveats around (a) what fields actually contain “keywords” and (b) how much you can trust ranking to behave like “more genes matched ⇒ higher rank.”

Check the assumptions
1) “PubMed/PMC queries have genes in keywords”

Mostly true, but nuanced:

In PubMed, if you don’t use a field tag, PubMed searches broadly across many fields. NLM training materials note that [tiab] (Title/Abstract) searches title, abstracts, and author keywords.

Practical implication: if you want to bias toward “genes mentioned in title/abstract/author keywords” (closer to your intent than “anywhere in record”), use GENE[tiab] for each gene.

Many PubMed records do not reliably have author keywords, and gene symbols can be missing from author keywords even when discussed heavily. So “keywords-only” is not sufficient coverage; “tiab” is usually a better compromise.

PubMed has a dedicated “gene” learning module noting that searching by gene name/symbol can be as simple as entering the symbol and PubMed will search it as an all-fields term if it doesn’t map to MeSH.

Caveat: short/ambiguous symbols (e.g., “CAT”, “MET”, “ARC”) can go sideways.

2) “PubMed/PMC supports OR and prioritises combos over single hits”

OR is supported (standard PubMed boolean logic).

Prioritises combos: kind of, but not guaranteed in the strict way you’re imagining.

PubMed’s Best Match ranking uses a learned model with many signals; it explicitly includes “number of term matches between the query and the document” among its features, but it’s not a deterministic “count matched genes and sort by that.”

So you should expect “multi-gene overlap tends to rise,” but there will be exceptions (publication type, recency effects, query length effects, etc.).

The big practical constraint: how long can the gene list be?

There isn’t a clean, user-facing “max genes” number that I’d trust universally, because limits show up as:

URL / query length limits (browser/server dependent),

internal processing limits,

and UI quirks.

What is clearly recommended in the NCBI ecosystem: for very long ESearch queries, NCBI guidance (as quoted in community discussions that reference the Entrez manual) is to use HTTP POST rather than GET.
Also, PubMed has separate length limits in some features (e.g., custom filters capped at 4,000 chars), which is a hint that “giant strings” can hit limits in some contexts even if not exactly your case.

Actionable takeaway: assume you’ll need chunking (e.g., 50–200 genes per query) and then merge results, rather than one monster OR-string.

A concrete workflow that matches your idea (and avoids the traps)
Step A — Query formulation (so you actually get “multi-gene” behaviour)

Use something like:

(G1[tiab] OR G2[tiab] OR ... OR Gn[tiab]) AND (context terms...)

Why tiab?

Because it includes author keywords plus title/abstract, and is less noisy than all-fields.

Add optional context terms early (phenotype, tissue, assay, pathway name), otherwise your top results may be dominated by broad methodology or review articles.

Step B — Pull ranked hits + compute “overlap score” yourself

Because Best Match isn’t guaranteed to sort by matched-gene-count, treat PubMed ranking as a candidate generator, then compute:

overlap = #genes in list mentioned in (title+abstract+keywords) per paper

This gets you the enrichment-like metric you actually want, independent of PubMed’s ML reranking. (You can still use Best Match as the fast first pass.)

Step C — Use overlap to drive ASTA snippet queries efficiently

Your intersection trick makes sense:

From each paper, extract the subset of genes that appear in title/abstract/keywords (or metadata keywords if you’re using PMC fulltext XML), then drive ASTA snippet queries on:

the single genes with highest frequency across top papers,

plus small combinations (pairs/triples) that co-occur often.

This avoids the combinatorial explosion when the intersection is long.

Step D — Handle gene symbol ambiguity up-front

This is the main “silent failure” mode.

Gene symbols are famously ambiguous / drifting over time; there’s a literature on symbol ambiguity and normalization.
Practical mitigations:

Prefer HGNC/Entrez canonical symbols and maintain an alias map.

For short/ambiguous symbols, require an extra qualifier in the query for that gene (e.g., ARC[tiab] AND (synaptic OR neuron)), or exclude known-bad symbols from the initial “OR sweep” and handle separately.

What I’d test first (quick validation experiments)

Ranking sanity check

Take a small gene list (say 30) and run (genes OR’ed)[tiab] with Best Match sort.

For top 200 PMIDs, compute overlap counts yourself.

Plot/inspect: does PubMed rank correlate with overlap count? (It often will, but not perfectly.)

Chunk size limit

Increase genes per query until the UI breaks or results become erratic.

In parallel, test E-utilities ESearch with POST for long strings if you want this robustly automated.

Field choice sensitivity

Compare [tiab] vs [tw] (text words) for noise/recall. NLM notes [tiab] includes author keywords; [tw] is broader.

If you want, paste a real gene list (even ~50 is enough) plus a rough topic (disease/tissue/assay), and I’ll draft a few concrete PubMed query templates (chunking + ambiguity handling) that fit this “pseudo-GSEA” pipeline.
