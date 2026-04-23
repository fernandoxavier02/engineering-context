---
name: setup
description: "This skill should be used when the user asks to 'set up engineering context', 'create engineering rules', 'configure engineering best practices', 'generate architecture contract', 'initialize context system', or 'set up engineering for this project'. Orchestrates the full 5-phase pipeline to create a mandatory engineering context system."
---

# Engineering Context Setup — Full Pipeline

Orchestrate the complete engineering context setup pipeline. This is the main entry point that coordinates all sub-skills to generate a mandatory engineering context system.

## What It Produces

1. **4 always-loaded rules** (`.claude/rules/50-53`) — architecture contract, engineering principles, testing strategy, anti-patterns
2. **Vault engineering cards** (`vault/engineering/`) — ADRs, examples, detailed patterns (pull on demand)
3. **Validation test** — ensures the context system is correct

## Pipeline

```
Phase 1: DETECT STACK
  → invoke `detect-stack` skill
  → output: PROJECT_PROFILE (language, framework, test framework, layers)

Phase 2: MAP ARCHITECTURE
  → invoke `map-architecture` skill
  → output: layer diagram, dependency rules, mandatory flows
  → confirm with user via AskUserQuestion

Phase 3: MINE ANTI-PATTERNS
  → invoke `mine-anti-patterns` skill
  → output: anti-pattern catalog (real issues from codebase)

Phase 4: GENERATE RULES
  → invoke `generate-rules` skill
  → output: 4 rules + vault cards

Phase 5: VALIDATE
  → invoke `validate-context` skill
  → output: validation test + results
```

## Execution

Run phases sequentially. Each produces artifacts that feed into the next.

### Phase 1: Detect Stack

Invoke `detect-stack`. Store the resulting PROJECT_PROFILE.

### Phase 2: Map Architecture

Invoke `map-architecture` with the PROJECT_PROFILE. Present the detected architecture via AskUserQuestion for user confirmation before proceeding.

### Phase 3: Mine Anti-Patterns

Invoke `mine-anti-patterns`. The anti-pattern catalog feeds into rule generation.

### Phase 4: Generate Rules

Invoke `generate-rules` with PROJECT_PROFILE, architecture map, and anti-pattern catalog.

Generate these files:
- `.claude/rules/50-architecture-contract.md`
- `.claude/rules/51-engineering-principles.md`
- `.claude/rules/52-testing-strategy.md`
- `.claude/rules/53-anti-patterns.md`
- Vault cards in `vault/engineering/`

### Phase 5: Validate

Invoke `validate-context`. Generate and run the validation test.

## Output

Present a summary:

```
╔════════════════════════════════════════════════════╗
║  ENGINEERING CONTEXT SETUP — COMPLETE              ║
╠════════════════════════════════════════════════════╣
║  Project: [name]                                   ║
║  Stack: [language] / [framework]                   ║
║  Architecture: [style]                             ║
║  Rules Created: 4                                  ║
║  Vault Cards: [N]                                  ║
║  Anti-Patterns Found: [N]                          ║
║  Validation: [N]/[N] PASSED                        ║
║  FINAL DECISION: GO / NO-GO                        ║
╚════════════════════════════════════════════════════╝
```

## Critical Rules

1. NEVER use generic examples — every example from the actual codebase
2. NEVER assume architecture — detect from directory structure, confirm with user
3. NEVER skip validation — always create and run the validation test
4. ALWAYS use AskUserQuestion for architecture confirmation
5. ALWAYS add vault triggers in each rule for deep consultation
