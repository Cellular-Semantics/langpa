Excellent questions! These are important design considerations. Let me clarify both:

  1. Notebook/Ad-Hoc Usage

  Yes, designed for it! The modules should be independently callable, not just
  CLI-oriented.

  Example notebook usage:
  # Direct function imports for ad-hoc analysis
  from langpa.comparison.metrics import compute_gene_jaccard, compute_name_similarity
  from langpa.embeddings import load_embeddings, compute_cosine_similarity
  from langpa.services.output_manager import OutputManager

  # Load your data
  manager = OutputManager()
  container_a =
  manager.load_container("outputs/project/query/timestamp_1/container.json")
  container_b =
  manager.load_container("outputs/project/query/timestamp_2/container.json")

  # Compute similarities directly
  programs_a = container_a["report"]["programs"]
  programs_b = container_b["report"]["programs"]

  for prog_a in programs_a:
      for prog_b in programs_b:
          jaccard = compute_gene_jaccard(
              prog_a["supporting_genes"],
              prog_b["supporting_genes"]
          )
          name_sim = compute_name_similarity(
              prog_a["program_name"],
              prog_b["program_name"]
          )
          print(f"{prog_a['program_name']} vs {prog_b['program_name']}: {jaccard:.2f}")

  Key design principle: Each function should be:
  - Importable and usable standalone
  - Well-documented with docstrings
  - Return values (not just print/save)
  - Accept standard Python types (not CLI args)

  2. Multiple Runs Handling

  Good catch! Current validation_tools assumes pairs. Here's the proposed behavior:

  Default Behavior (MVP)

  For >2 runs in same query folder:
  outputs/project/0_Gliosis/
    ├── run_1/container.json
    ├── run_2/container.json
    ├── run_3/container.json  # What to do?

  Recommended default: All pairwise combinations
  - Compare: (1,2), (1,3), (2,3)
  - Rationale: Complete analysis, useful for consistency checking
  - Output: Each pair gets row in program_matches.csv

  Add columns to identify pairs:
  run_a_id,run_b_id,program_a_idx,program_b_idx,gene_jaccard,name_sim,combined_sim
  0_Gliosis_run1,0_Gliosis_run2,0,0,0.85,0.92,0.885
  0_Gliosis_run1,0_Gliosis_run3,0,0,0.78,0.88,0.830
  0_Gliosis_run2,0_Gliosis_run3,0,1,0.82,0.90,0.860

  Configurable Behavior

  CLI flag for comparison strategy:
  langpa-validate compare --project my_project \
    --strategy {all-pairs|sequential|vs-first|vs-reference}

  Strategies:

  1. all-pairs (default)
    - n choose 2 combinations
    - Complete comparison matrix
    - May be slow for many runs (10 runs = 45 comparisons)
  2. sequential
    - Compare consecutive runs: 1vs2, 2vs3, 3vs4
    - Useful for tracking changes over time
    - Always n-1 comparisons
  3. vs-first
    - Compare all to first run: 1vs2, 1vs3, 1vs4
    - First run as reference/baseline
    - Always n-1 comparisons
  4. vs-reference
    - Specify reference run explicitly
    - --reference-run run_2
    - All others compared to that one

  Implementation Details

  In langpa_validation/analysis/run_comparison.py:
  def compare_runs(
      project: str,
      output_dir: Path,
      strategy: str = "all-pairs",
      reference_run: str | None = None
  ) -> pd.DataFrame:
      """
      Compare runs in a project.
      
      Args:
          project: Project name
          output_dir: Output directory
          strategy: Comparison strategy (all-pairs, sequential, vs-first, vs-reference)
          reference_run: Reference run ID (required for vs-reference strategy)
      
      Returns:
          DataFrame with program matches
      """
      containers = load_all_containers(project, output_dir)

      if strategy == "all-pairs":
          pairs = list(itertools.combinations(containers.keys(), 2))
      elif strategy == "sequential":
          pairs = list(zip(containers.keys()[:-1], containers.keys()[1:]))
      elif strategy == "vs-first":
          first = list(containers.keys())[0]
          pairs = [(first, other) for other in containers.keys()[1:]]
      elif strategy == "vs-reference":
          if not reference_run:
              raise ValueError("--reference-run required for vs-reference strategy")
          pairs = [(reference_run, other) for other in containers.keys() if other !=
  reference_run]

      # Compare all pairs
      results = []
      for run_a_id, run_b_id in pairs:
          matches = compare_pair(containers[run_a_id], containers[run_b_id])
          results.extend(matches)

      return pd.DataFrame(results)

  Deferred: Multi-Run Statistics

  For later (post-MVP):
  - Compute consistency scores across all runs (not just pairwise)
  - Identify "consensus programs" appearing in N/M runs
  - Clustering/dimensionality reduction of programs across runs
  - Temporal analysis (if runs have timestamps)

  For MVP:
  - Pairwise comparisons only
  - User can aggregate/analyze DataFrame results themselves in notebooks
  - Master report shows pairwise tables

  Updated Plan Section

  Should I update the plan document to include:

  1. Design Principle: "Notebook-first API design" section
  2. Multiple Runs: Default all-pairs strategy with configurable options
  3. Future Work: Multi-run statistics deferred to post-MVP

  

