 
scripts/run_deepsearch.py
Comment on lines +457 to +459
```python

        # Backward compatibility
service = DeepSearchService(preferred_provider=args.preferred_provider, **config_overrides)
```

Copilot AI
2 minutes ago
When using backward compatibility mode (no preset specified) and providing config_overrides, the overrides are applied but there's a logical issue: if args.preferred_provider is specified along with args.model or provider parameter overrides, the initialization on line 458 passes both preferred_provider and **config_overrides.

Looking at the DeepSearchService code, when preset is None, it loads the default "perplexity-sonar-pro" preset and only applies the preferred_provider override if it's specified (line 55-57 in deepsearch_service.py). However, the **config_overrides passed here are ignored in backward compatibility mode because the service doesn't merge them.

This means that in backward compatibility mode, --model, --reasoning-effort, and --search-recency arguments will be silently ignored, which could be confusing for users. Either document this limitation or ensure config_overrides are also applied in backward compatibility mode.