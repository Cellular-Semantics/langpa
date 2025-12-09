#!/usr/bin/env python3
"""Configuration management CLI for DeepSearch YAML configurations.

Provides commands for managing presets and templates without editing code.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from langpa.services.yaml_config import ConfigurationError, YAMLConfigManager


def list_presets(config_manager: YAMLConfigManager) -> None:
    """List all available presets with descriptions."""
    try:
        presets = config_manager.list_available_presets()
        if not presets:
            print("No presets found.")
            return

        print("Available Presets:")
        print("-" * 50)
        for name, description in presets.items():
            print(f"  {name:20} - {description}")
    except ConfigurationError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def list_templates(config_manager: YAMLConfigManager) -> None:
    """List all available templates with descriptions."""
    try:
        templates = config_manager.list_available_templates()
        if not templates:
            print("No templates found.")
            return

        print("Available Templates:")
        print("-" * 50)
        for name, description in templates.items():
            print(f"  {name:20} - {description}")
    except ConfigurationError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def show_preset(config_manager: YAMLConfigManager, preset_name: str) -> None:
    """Show complete details for a specific preset."""
    try:
        config = config_manager.get_preset_config(preset_name)

        print(f"Preset: {preset_name}")
        print("=" * (len(preset_name) + 8))
        print(f"Description: {config.description}")
        print(f"Provider: {config.provider}")
        print(f"Model: {config.model}")
        print(f"Timeout: {config.timeout}s")
        print(f"Prompt Template: {config.prompt_template}")
        print("\nProvider Parameters:")
        print(yaml.dump(config.provider_params, indent=2, default_flow_style=False))
    except ConfigurationError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def show_template(config_manager: YAMLConfigManager, template_name: str) -> None:
    """Show complete details for a specific template."""
    try:
        template = config_manager.get_template(template_name)
        metadata = config_manager.get_template_metadata(template_name)

        print(f"Template: {template_name}")
        print("=" * (len(template_name) + 10))
        print(f"Description: {metadata['description']}")
        print(f"Supports JSON Schema: {metadata['supports_json_schema']}")
        print(f"Optimized For: {', '.join(metadata['optimized_for'])}")

        # Show schema instruction if present
        if metadata.get("schema_instruction"):
            print("\nSchema Instruction:")
            print("-" * 40)
            print(metadata["schema_instruction"])

        print("\nTemplate Text:")
        print("-" * 40)
        print(template["template"])
        print("-" * 40)
        print("\nExample Usage:")
        print("  genes: ['TP53', 'BRCA1']")
        print("  context: 'cancer tumor suppressor genes'")

        # Show formatted example
        example_genes = ["TP53", "BRCA1"]
        example_context = "cancer tumor suppressor genes"
        formatted = config_manager.format_prompt_template(
            template_name, example_genes, example_context
        )
        print("\nFormatted Example (first 200 chars):")
        print(formatted[:200] + "..." if len(formatted) > 200 else formatted)
    except ConfigurationError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def validate_config(config_manager: YAMLConfigManager, preset_name: str | None = None) -> None:
    """Validate configuration files."""
    try:
        if preset_name:
            # Validate specific preset
            config_manager.get_preset_config(preset_name)
            print(f"✅ Preset '{preset_name}' is valid")
        else:
            # Validate all configurations
            presets = config_manager.list_available_presets()
            templates = config_manager.list_available_templates()

            print(f"✅ Loaded {len(presets)} presets successfully")
            print(f"✅ Loaded {len(templates)} templates successfully")
            print("✅ All configurations are valid")
    except ConfigurationError as e:
        print(f"❌ Validation failed: {e}", file=sys.stderr)
        sys.exit(1)


def get_user_config_path(config_manager: YAMLConfigManager) -> Path:
    """Get path to user configuration directory, creating if needed."""
    if config_manager.config_dir:
        user_config_dir = config_manager.config_dir / "user"
    else:
        user_config_dir = Path.cwd() / "config" / "user"

    user_config_dir.mkdir(parents=True, exist_ok=True)
    return user_config_dir


def copy_preset(config_manager: YAMLConfigManager, source_name: str, target_name: str) -> None:
    """Copy a preset to create a new one."""
    try:
        # Get source preset
        source_config = config_manager.get_preset_config(source_name)

        # Load existing user presets or create new structure
        user_config_dir = get_user_config_path(config_manager)
        user_presets_file = user_config_dir / "presets.yaml"

        if user_presets_file.exists():
            with open(user_presets_file) as f:
                user_data = yaml.safe_load(f) or {}
        else:
            user_data = {}

        if "presets" not in user_data:
            user_data["presets"] = {}

        # Add new preset
        user_data["presets"][target_name] = {
            "description": f"Copy of {source_name} - {source_config.description}",
            "provider": source_config.provider,
            "model": source_config.model,
            "timeout": source_config.timeout,
            "prompt_template": source_config.prompt_template,
            "provider_params": source_config.provider_params,
        }

        # Write updated configuration
        with open(user_presets_file, "w") as f:
            yaml.dump(user_data, f, indent=2, default_flow_style=False)

        print(f"✅ Created preset '{target_name}' as copy of '{source_name}'")
        print(f"📝 Edit with: python scripts/manage_config.py edit-preset {target_name}")
    except ConfigurationError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error creating preset: {e}", file=sys.stderr)
        sys.exit(1)


def edit_preset(config_manager: YAMLConfigManager, preset_name: str) -> None:
    """Open preset for editing in user's default editor."""
    try:
        user_config_dir = get_user_config_path(config_manager)
        user_presets_file = user_config_dir / "presets.yaml"

        # Create file if it doesn't exist
        if not user_presets_file.exists():
            print(f"Creating new user presets file at {user_presets_file}")
            user_data = {"presets": {}}
            with open(user_presets_file, "w") as f:
                yaml.dump(user_data, f, indent=2, default_flow_style=False)

        # Open in editor
        editor = shutil.which("code") or shutil.which("vim") or shutil.which("nano")
        if not editor:
            print(f"Please edit the file manually: {user_presets_file}")
            return

        print(f"Opening {user_presets_file} in {editor}...")
        subprocess.run([editor, str(user_presets_file)])

        # Validate after editing
        try:
            config_manager._presets_cache = None  # Clear cache
            if preset_name in config_manager.list_available_presets():
                config_manager.get_preset_config(preset_name)
                print(f"✅ Preset '{preset_name}' is valid after editing")
            else:
                print(f"ℹ️  Preset '{preset_name}' not found - may have been renamed or removed")
        except ConfigurationError as e:
            print(f"⚠️  Warning: Configuration has validation errors: {e}")

    except Exception as e:
        print(f"Error editing preset: {e}", file=sys.stderr)
        sys.exit(1)


def delete_preset(config_manager: YAMLConfigManager, preset_name: str) -> None:
    """Delete a user preset."""
    try:
        user_config_dir = get_user_config_path(config_manager)
        user_presets_file = user_config_dir / "presets.yaml"

        if not user_presets_file.exists():
            print(f"No user presets file found. Cannot delete '{preset_name}'")
            sys.exit(1)

        with open(user_presets_file) as f:
            user_data = yaml.safe_load(f) or {}

        if "presets" not in user_data or preset_name not in user_data["presets"]:
            print(f"Preset '{preset_name}' not found in user configurations")
            sys.exit(1)

        del user_data["presets"][preset_name]

        with open(user_presets_file, "w") as f:
            yaml.dump(user_data, f, indent=2, default_flow_style=False)

        print(f"✅ Deleted preset '{preset_name}'")
    except Exception as e:
        print(f"Error deleting preset: {e}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Manage DeepSearch YAML configuration presets and templates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List available configurations
  python scripts/manage_config.py list-presets
  python scripts/manage_config.py list-templates

  # Show configuration details
  python scripts/manage_config.py show-preset perplexity-sonar-pro
  python scripts/manage_config.py show-template gene_analysis_academic

  # Create and manage custom presets
  python scripts/manage_config.py copy-preset perplexity-sonar-pro my-custom-preset
  python scripts/manage_config.py edit-preset my-custom-preset
  python scripts/manage_config.py validate-preset my-custom-preset

  # Validate all configurations
  python scripts/manage_config.py validate
        """,
    )

    parser.add_argument(
        "--config-dir",
        type=str,
        help="Custom configuration directory (default: ./config or ~/.langpa/config)",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List commands
    subparsers.add_parser("list-presets", help="List all available presets")
    subparsers.add_parser("list-templates", help="List all available templates")

    # Show commands
    show_preset_parser = subparsers.add_parser("show-preset", help="Show preset details")
    show_preset_parser.add_argument("preset_name", help="Name of preset to show")

    show_template_parser = subparsers.add_parser("show-template", help="Show template details")
    show_template_parser.add_argument("template_name", help="Name of template to show")

    # Validation commands
    validate_parser = subparsers.add_parser("validate", help="Validate all configurations")
    validate_preset_parser = subparsers.add_parser(
        "validate-preset", help="Validate specific preset"
    )
    validate_preset_parser.add_argument("preset_name", help="Name of preset to validate")

    # Preset management commands
    copy_parser = subparsers.add_parser("copy-preset", help="Copy preset to create new one")
    copy_parser.add_argument("source_name", help="Name of preset to copy")
    copy_parser.add_argument("target_name", help="Name for new preset")

    edit_parser = subparsers.add_parser("edit-preset", help="Edit preset in default editor")
    edit_parser.add_argument("preset_name", help="Name of preset to edit")

    delete_parser = subparsers.add_parser("delete-preset", help="Delete user preset")
    delete_parser.add_argument("preset_name", help="Name of preset to delete")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Initialize configuration manager
    config_manager = YAMLConfigManager(args.config_dir)

    # Dispatch to appropriate command
    if args.command == "list-presets":
        list_presets(config_manager)
    elif args.command == "list-templates":
        list_templates(config_manager)
    elif args.command == "show-preset":
        show_preset(config_manager, args.preset_name)
    elif args.command == "show-template":
        show_template(config_manager, args.template_name)
    elif args.command == "validate":
        validate_config(config_manager)
    elif args.command == "validate-preset":
        validate_config(config_manager, args.preset_name)
    elif args.command == "copy-preset":
        copy_preset(config_manager, args.source_name, args.target_name)
    elif args.command == "edit-preset":
        edit_preset(config_manager, args.preset_name)
    elif args.command == "delete-preset":
        delete_preset(config_manager, args.preset_name)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
