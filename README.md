<!-- ARCHIVED BANNER -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=ff9800&height=80&text=%F0%9F%93%A6%20ARCHIVED&fontSize=28&fontColor=ffffff&width=400"/>
  <p><b>This repository has been archived.</b></p>
  <p>My public portfolio has been restructured to focus on <a href="https://github.com/fernandoxavier02">Finance + AI showcases</a>.</p>
  <p>
    <a href="https://github.com/fernandoxavier02/ifrs15-revenue-intelligence-showcase">IFRS 15</a> ·
    <a href="https://github.com/fernandoxavier02/ifrs16-lease-intelligence-showcase">IFRS 16</a> ·
    <a href="https://github.com/fernandoxavier02/controllership-reconciliation-showcase">Reconciliation</a> ·
    <a href="https://github.com/fernandoxavier02/brazilian-tax-reform-oracle-showcase">Tax Oracle</a>
  </p>
  <hr/>
</div>

# engineering-context

Claude Code plugin that generates a **mandatory engineering context system** for any project — architecture contract, engineering principles, testing strategy, and anti-pattern catalog, all adapted to the project's actual stack.

## What it does

Scans your repository, detects the stack, maps the architecture, mines anti-patterns from real code, and writes four always-loaded rules plus vault cards. The resulting rules are compactation-safe (load on every turn) and vault-linked (pull deeper detail on demand).

## Slash commands (6)

| Command | What it does |
|---------|--------------|
| `/engineering-context:setup` | Full 5-phase pipeline |
| `/engineering-context:detect-stack` | Auto-detect language / framework / tests |
| `/engineering-context:map-architecture` | Map layers + dependency rules |
| `/engineering-context:mine-anti-patterns` | Scan codebase for real anti-patterns |
| `/engineering-context:generate-rules` | Write `.claude/rules/50–53` + vault cards |
| `/engineering-context:validate-context` | Run validation tests + GO/NO-GO report |

Each command invokes the corresponding skill. Skills also activate via natural language (e.g. `"set up engineering context"`, `"detect project stack"`).

## Output artifacts

After running `setup`, the plugin writes:

- `.claude/rules/50-architecture-contract.md` — forbidden imports, layer diagram, mandatory flows
- `.claude/rules/51-engineering-principles.md` — SOLID / DRY / YAGNI / KISS with real examples from the codebase
- `.claude/rules/52-testing-strategy.md` — test type by layer, regression rules
- `.claude/rules/53-anti-patterns.md` — catalog of real issues found during scan
- `vault/engineering/` — ADRs, layer contract detail, pattern examples (progressive disclosure)
- Validation test in the project's native test framework (pytest / jest / go test)

## Install

### Via marketplace (recommended)

```
/plugin marketplace add fernandoxavier02/Pipeline-Orchestrator
/plugin install engineering-context@FX-Studio-AI
```

### Direct from this repo

```
/plugin marketplace add fernandoxavier02/engineering-context
/plugin install engineering-context
```

## Requirements

- Claude Code CLI with plugin support
- Project with detectable stack (Python, TypeScript, Go, Rust, Java, or Ruby)
- Write access to `.claude/rules/` in the target project

## Language support

Auto-adapts examples to: Python (pytest, pydantic, structlog), TypeScript (jest/vitest, zod), Go (go test, fmt.Errorf), Ruby (rspec, rubocop), Rust, Java.

## License

MIT — see [LICENSE](LICENSE).
