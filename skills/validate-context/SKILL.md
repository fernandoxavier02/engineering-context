---
name: validate-context
description: "This skill should be used when the user asks to 'validate context', 'check engineering rules', 'verify context system', 'test context setup', or 'run context validation'. Generates and runs validation tests for the engineering context system."
---

# Validate Context

Generate and run validation tests for the engineering context system.

## What to Validate

### Rule Existence

Check that all 4 rules exist:
- `.claude/rules/50-architecture-contract.md`
- `.claude/rules/51-engineering-principles.md`
- `.claude/rules/52-testing-strategy.md`
- `.claude/rules/53-anti-patterns.md`

### Rule Structure

Each rule MUST have:
1. YAML frontmatter with `description` field
2. NO `paths:` frontmatter (always-loaded, no path filtering)
3. `⛔ NUNCA` section at top (compactation-safe)
4. Vault trigger references (`SE [situation] -> vault:engineering/...`)

### Vault Cards

Check that vault engineering cards exist:
- `vault/engineering/adr-*.md`
- `vault/engineering/layer-contract.md`
- `vault/engineering/pattern-*.md`
- `vault/engineering/testing-strategy-*.md`

## Test Generation

Generate a test file adapted to the project's test framework.

### Python (pytest)

```python
# src/tests/test_context_engineering.py
from pathlib import Path

RULES_DIR = Path(".claude/rules")
VAULT_DIR = Path("vault/engineering")

class TestEngineeringContext:
    def test_rule_50_exists(self):
        assert (RULES_DIR / "50-architecture-contract.md").exists()

    def test_rule_has_nunca_section(self):
        for i in range(50, 54):
            matches = list(RULES_DIR.glob(f"{i}-*.md"))
            assert matches, f"Rule {i} not found"
            content = matches[0].read_text(encoding="utf-8")
            assert "NUNCA" in content, f"Rule {i} missing NUNCA section"

    def test_rule_has_no_paths_frontmatter(self):
        for rule in RULES_DIR.glob("5[0-3]-*.md"):
            content = rule.read_text()
            assert "paths:" not in content, f"{rule.name} has paths frontmatter"

    def test_vault_cards_exist(self):
        assert VAULT_DIR.exists()
        assert len(list(VAULT_DIR.glob("*.md"))) >= 3
```

### TypeScript (Jest/Vitest)

```typescript
import { existsSync, readFileSync } from 'fs';
import { globSync } from 'glob';

describe('Engineering Context', () => {
  test('rule 50 exists', () => {
    expect(existsSync('.claude/rules/50-architecture-contract.md')).toBe(true);
  });

  test('rules have NUNCA section', () => {
    const rules = globSync('.claude/rules/5[0-3]-*.md');
    rules.forEach(rule => {
      const content = readFileSync(rule, 'utf-8');
      expect(content).toContain('NUNCA');
    });
  });
});
```

### Go (go test)

```go
package context_test

import (
    "os"
    "testing"
)

func TestRule50Exists(t *testing.T) {
    if _, err := os.Stat(".claude/rules/50-architecture-contract.md"); os.IsNotExist(err) {
        t.Error("Rule 50 does not exist")
    }
}
```

## Validation Report

After running tests, produce:

```
## Context Validation Report

| Check | Status |
|-------|--------|
| Rule 50 (architecture contract) exists | ✅/❌ |
| Rule 51 (engineering principles) exists | ✅/❌ |
| Rule 52 (testing strategy) exists | ✅/❌ |
| Rule 53 (anti-patterns) exists | ✅/❌ |
| Rules have NUNCA section | ✅/❌ |
| Rules have no paths frontmatter | ✅/❌ |
| Rules have vault triggers | ✅/❌ |
| Vault cards exist | ✅/❌ |

**Result:** [N]/[total] PASSED -> GO / NO-GO
```

## Integration

Run after `generate-rules` to verify the complete system. Re-run after any rule changes.
