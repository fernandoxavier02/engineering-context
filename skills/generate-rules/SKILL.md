---
name: generate-rules
description: "This skill should be used when the user asks to 'generate engineering rules', 'create architecture contract', 'write engineering principles', 'set up testing strategy', or 'create anti-pattern rules'. Generates 4 mandatory always-loaded engineering rules and vault cards adapted to the project's stack and architecture."
---

# Generate Engineering Rules

Generate 4 mandatory always-loaded engineering rules and vault cards adapted to the project.

## Prerequisites

- PROJECT_PROFILE from `detect-stack`
- ARCHITECTURE_MAP from `map-architecture`
- Anti-pattern catalog from `mine-anti-patterns`

## Rules to Generate

### Rule 50: Architecture Contract

Create `.claude/rules/50-architecture-contract.md`:

- `⛔ NUNCA` section with forbidden imports (from ARCHITECTURE_MAP)
- Layer diagram showing dependency direction
- Dependency rules table (CAN import / CANNOT import)
- Mandatory flows (from ARCHITECTURE_MAP)
- Vault triggers: `SE implementing [X] -> vault:engineering/adr-*`

### Rule 51: Engineering Principles

Create `.claude/rules/51-engineering-principles.md`:

- `⛔ NUNCA` section (no premature abstraction, no silenced exceptions, no YAGNI, no DRY violations)
- SOLID table with REAL examples from the codebase (not generic)
- DRY / YAGNI / KISS rules with concrete examples
- Coupling detection rules
- Error handling section (adapted to project's language)
- Vault triggers for deep consultation

### Rule 52: Testing Strategy

Create `.claude/rules/52-testing-strategy.md`:

- `⛔ NUNCA` section (no task without test, no silenced failures, no implementation-coupled tests, no continuing on regression failure)
- Test type by layer table (adapted to project's test framework)
- Test type by situation table (bug fix -> regression, new feature -> behavior, refactor -> existing suite)
- Regression rules (THE MOST IMPORTANT — pytest/ equivalent after ANY change)
- Test directory structure (adapted to project)
- Vault triggers

### Rule 53: Anti-Patterns

Create `.claude/rules/53-anti-patterns.md`:

- `⛔ NUNCA` table with anti-patterns found during scan
- Evolution rule: when fixing bug without test -> MUST add entry + regression test + vault card
- Vault triggers

## Vault Cards

Generate in `vault/engineering/`:

| Card | Content |
|------|---------|
| `adr-001-[key-decision].md` | Most important architectural decision |
| `adr-002-[second-decision].md` | Second most important decision |
| `layer-contract.md` | Detailed import rules with code examples |
| `pattern-srp-examples.md` | 3 real SRP examples from codebase |
| `testing-strategy-examples.md` | Example of each test type in project's framework |

## Language Adaptation

Adapt code examples and patterns:

- **Python**: `pytest`, `pydantic`, `structlog`, `ValueError`, `ruff`
- **TypeScript**: `jest`/`vitest`, `zod`, typed error classes, `eslint`
- **Go**: `go test`, stdlib, `fmt.Errorf`, sentinel errors, `golangci-lint`
- **Ruby**: `rspec`, Rails conventions, custom exceptions, `rubocop`

## Critical Rules

1. NEVER use generic examples — use REAL names and paths from the codebase
2. ALWAYS include `⛔ NUNCA` section at top of each rule (compactation-safe)
3. ALWAYS add vault triggers: `SE [situation] -> vault:engineering/[card]`

## Detailed Templates

Rule templates with full examples are in `references/templates.md`.
