#!/usr/bin/env python3
"""
Direct API comparison test: sonar-deep-research vs sonar-reasoning-pro

This script tests:
1. Direct HTTP calls to sonar-deep-research with response_format parameter
2. Current sonar-reasoning-pro implementation via deep-research-client

Purpose: Determine if sonar-deep-search + response_format bypasses the
deep-research-client limitations we encountered earlier.
"""

import json
import os
import time
from pathlib import Path
from typing import Dict, Any, Optional
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add src to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from langpa.schemas import load_schema
from langpa.services.deepsearch_service import DeepSearchService


class DirectAPITester:
    """Test direct Perplexity API calls with response_format parameter."""

    def __init__(self):
        self.api_key = os.getenv("PERPLEXITY_API_KEY")
        if not self.api_key:
            raise ValueError("PERPLEXITY_API_KEY not found in environment")

        self.base_url = "https://api.perplexity.ai/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Load our deepsearch schema for response_format
        self.schema = load_schema("deepsearch_results_schema.json")

    def create_test_prompt(self, genes: list[str], context: str) -> str:
        """Create the research prompt for gene list analysis."""
        genes_str = ", ".join(genes)

        return f"""Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: {genes_str}

**Biological Context**: {context}

**Analysis Strategy**:
1. Search current scientific literature for functional roles of each gene in the input list
2. Identify clusters of genes that act together in pathways, processes, or cellular states
3. Treat each cluster as a potential gene program within the list
4. Interpret findings in light of both normal physiological roles and disease-specific alterations
5. Prioritize well-established functions with strong literature support, but highlight emerging evidence if contextually relevant

**Guidelines**:
* Anchor all predictions in either the normal physiology and development of the cell type and tissue specified in the context OR the alterations and dysregulations characteristic of the specified disease
* Connect gene-level roles to program-level implications
* Consider gene interactions, regulatory networks, and pathway dynamics
* Highlight cases where multiple genes collectively strengthen evidence
* Ensure all claims are backed by experimental evidence with proper attribution

Provide a structured analysis identifying biological programs and their predicted cellular impacts within the given context.

IMPORTANT: Return ONLY valid JSON that follows the provided schema structure. Do not include any explanatory text."""

    def test_sonar_deep_research_direct(self, genes: list[str], context: str) -> Dict[str, Any]:
        """Test sonar-deep-research with direct API call and response_format."""
        print("🔬 Testing sonar-deep-research with direct API call...")

        prompt = self.create_test_prompt(genes, context)

        payload = {
            "model": "sonar-deep-research",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "response_format": {
                "type": "json_schema",
                "json_schema": {
                    "schema": self.schema
                }
            }
        }

        start_time = time.time()

        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                timeout=300  # 5 minute timeout
            )

            duration = time.time() - start_time

            if response.status_code == 200:
                result = response.json()
                content = result.get("choices", [{}])[0].get("message", {}).get("content", "")

                return {
                    "success": True,
                    "duration_seconds": duration,
                    "status_code": response.status_code,
                    "model": "sonar-deep-research",
                    "content": content,
                    "raw_response": result,
                    "method": "direct_api"
                }
            else:
                return {
                    "success": False,
                    "duration_seconds": duration,
                    "status_code": response.status_code,
                    "error": response.text,
                    "model": "sonar-deep-research",
                    "method": "direct_api"
                }

        except Exception as e:
            return {
                "success": False,
                "duration_seconds": time.time() - start_time,
                "error": str(e),
                "model": "sonar-deep-research",
                "method": "direct_api"
            }

    def test_current_implementation(self, genes: list[str], context: str) -> Dict[str, Any]:
        """Test current sonar-reasoning-pro implementation via deep-research-client."""
        print("🧠 Testing current sonar-reasoning-pro implementation...")

        start_time = time.time()

        try:
            service = DeepSearchService()
            result = service.research_gene_list(genes=genes, context=context)

            duration = time.time() - start_time

            return {
                "success": True,
                "duration_seconds": duration,
                "model": getattr(result, 'model', 'sonar-reasoning-pro'),
                "provider": getattr(result, 'provider', 'perplexity'),
                "content": getattr(result, 'markdown', ''),
                "citations": getattr(result, 'citations', []),
                "method": "deep_research_client"
            }

        except Exception as e:
            return {
                "success": False,
                "duration_seconds": time.time() - start_time,
                "error": str(e),
                "method": "deep_research_client"
            }

    def validate_json_response(self, content: str) -> Dict[str, Any]:
        """Validate if response contains valid JSON matching our schema."""
        from langpa.services.output_manager import OutputManager

        output_manager = OutputManager()

        try:
            # Try direct JSON parsing first
            if content.strip().startswith('{'):
                parsed_json = json.loads(content.strip())
            else:
                # Use our existing extraction logic for complex responses
                parsed_json = output_manager.extract_json_from_markdown(content)

            if parsed_json is None:
                return {
                    "valid_json": False,
                    "schema_valid": False,
                    "error": "Could not extract valid JSON"
                }

            # Validate against schema
            is_valid, error_msg = output_manager.validate_against_schema(parsed_json)

            return {
                "valid_json": True,
                "schema_valid": is_valid,
                "extracted_json": parsed_json,
                "schema_error": error_msg if not is_valid else None
            }

        except Exception as e:
            return {
                "valid_json": False,
                "schema_valid": False,
                "error": str(e)
            }

    def run_comparison_test(self, genes: list[str], context: str) -> Dict[str, Any]:
        """Run full comparison test between both approaches."""
        print(f"\n🧬 Running comparison test:")
        print(f"   Genes: {genes}")
        print(f"   Context: {context}")
        print("=" * 60)

        # Test 1: Direct API with sonar-deep-research
        direct_result = self.test_sonar_deep_research_direct(genes, context)
        direct_validation = self.validate_json_response(direct_result.get("content", "")) if direct_result.get("success") else {}

        print(f"✅ Direct API test completed: {direct_result.get('success', False)} ({direct_result.get('duration_seconds', 0):.1f}s)")

        # Test 2: Current implementation
        current_result = self.test_current_implementation(genes, context)
        current_validation = self.validate_json_response(current_result.get("content", "")) if current_result.get("success") else {}

        print(f"✅ Current implementation test completed: {current_result.get('success', False)} ({current_result.get('duration_seconds', 0):.1f}s)")

        # Compile results
        return {
            "test_metadata": {
                "genes": genes,
                "context": context,
                "timestamp": time.time()
            },
            "direct_api_result": {
                **direct_result,
                "validation": direct_validation
            },
            "current_implementation_result": {
                **current_result,
                "validation": current_validation
            }
        }


def main():
    """Run the comparison test."""
    try:
        tester = DirectAPITester()

        # Use the same test case as our working example
        genes = ["FOXP1", "NKX2-1"]
        context = "lung development"

        results = tester.run_comparison_test(genes, context)

        # Save results
        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)

        timestamp = int(time.time())
        results_file = output_dir / f"api_comparison_test_{timestamp}.json"

        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2, default=str)

        print(f"\n📊 Results saved to: {results_file}")

        # Print summary
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)

        direct = results["direct_api_result"]
        current = results["current_implementation_result"]

        print(f"Direct API (sonar-deep-research):")
        print(f"  ✅ Success: {direct.get('success', False)}")
        print(f"  ⏱️  Duration: {direct.get('duration_seconds', 0):.1f}s")
        print(f"  📝 Valid JSON: {direct.get('validation', {}).get('valid_json', False)}")
        print(f"  ✅ Schema Valid: {direct.get('validation', {}).get('schema_valid', False)}")

        print(f"\nCurrent Implementation (sonar-reasoning-pro):")
        print(f"  ✅ Success: {current.get('success', False)}")
        print(f"  ⏱️  Duration: {current.get('duration_seconds', 0):.1f}s")
        print(f"  📝 Valid JSON: {current.get('validation', {}).get('valid_json', False)}")
        print(f"  ✅ Schema Valid: {current.get('validation', {}).get('schema_valid', False)}")

        # Print errors if any
        if not direct.get("success"):
            print(f"\n❌ Direct API Error: {direct.get('error', 'Unknown error')}")

        if not current.get("success"):
            print(f"\n❌ Current Implementation Error: {current.get('error', 'Unknown error')}")

        print("\n" + "=" * 60)

    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()