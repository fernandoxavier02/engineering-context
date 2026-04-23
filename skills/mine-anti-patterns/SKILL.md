---
name: mine-anti-patterns
description: "This skill should be used when the user asks to 'scan for anti-patterns', 'find code smells', 'detect anti-patterns', 'mine anti-patterns', or 'check for common errors'. Scans the codebase for anti-patterns and generates a catalog of real issues found."
---

# Mine Anti-Patterns

Scan the codebase for anti-patterns and generate a catalog of real issues.

## Step 1: Generic Scan

Search for common issues across any codebase using Grep:

| Anti-pattern | Detection Pattern |
|-------------|-------------------|
| Print/logging in production | `print(`, `console.log(` |
| Hardcoded secrets | `api_key = "`, `password = "`, `secret = "` |
| God files (over 300 lines) | Files with > 300 lines |
| Empty error handling | `except:`, `catch {}`, bare except |
| Duplicated constants | Same name in 2+ files |
| Business logic in wrong layer | Domain terms in UI/infra code |

## Step 2: Language-Specific Scan

Based on PROJECT_PROFILE language:

### Python
- `except Exception:` or `except:` (bare catch)
- `import *` (wildcard imports)
- Mutable default arguments (`def f(x=[])`)
- Missing type hints on public functions

### TypeScript
- `any` type usage
- `@ts-ignore` or `@ts-expect-error`
- Non-null assertions (`!.`)
- Missing return types on exports

### Go
- `panic()` in library code
- Exported functions without doc comments
- Naked goroutines without error handling

### Ruby
- Monkey-patching (reopening core classes)
- `eval()` usage
- Global variables (`$var`)

## Step 3: Architecture-Specific Scan

Based on ARCHITECTURE_MAP:
- Cross-layer imports (violating dependency rules)
- Business logic in entry points
- Missing mandatory flow steps (e.g., bypassing RiskEngine)

## Step 4: Build Catalog

Create an entry for each issue found:

| # | Anti-pattern | What happened | How to avoid |
|---|-------------|---------------|--------------|
| 1 | [name] | [specific instance with file:line] | [concrete fix] |

Only include issues ACTUALLY found in the codebase. Do NOT invent hypothetical issues.

## Output Format

```yaml
ANTI_PATTERN_CATALOG:
  total_found: [N]
  by_severity:
    critical: [list]
    warning: [list]
    info: [list]
  entries:
    - id: [N]
      name: [anti-pattern name]
      description: [what was found]
      location: [file:line or "general"]
      severity: [critical | warning | info]
      fix: [how to avoid]
```

## Detailed Detection Patterns

Full patterns by language and severity are in `references/catalog.md`.

## Integration

The anti-pattern catalog feeds into `generate-rules` (rule 53) and `validate-context`.
