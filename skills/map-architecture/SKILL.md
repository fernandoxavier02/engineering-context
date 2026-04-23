---
name: map-architecture
description: "This skill should be used when the user asks to 'map architecture', 'identify layers', 'map dependencies', 'architecture mapping', 'dependency rules', or 'understand project structure'. Maps architecture layers, dependencies, and boundary rules from directory structure."
---

# Map Architecture

Map the project's architecture layers, dependencies, and boundary rules.

## Prerequisites

A PROJECT_PROFILE from `detect-stack`. If not available, invoke `detect-stack` first.

## Step 1: Layer Discovery

Scan the directory structure to identify layers. Match against known patterns:

| Pattern | Layers |
|---------|--------|
| Clean Architecture | domain -> usecases -> adapters -> infra -> entry |
| MVC | models -> views -> controllers |
| Hexagonal | domain -> ports -> adapters -> config |
| Layered | presentation -> business -> data -> infra |
| Vertical Slices | features/{feature}/ (handler, model, tests) |

Use Glob to find the actual structure and map it.

## Step 2: Entry Point Identification

Find entry points: `main.*`, `app.*`, `index.*`, `run.*`, `cli.*`, `manage.py`, `cmd/`.

## Step 3: Dependency Rules

For each layer, determine what it CAN and CANNOT import. General rule: **dependencies point inward**.

| Layer | CAN import | CANNOT import |
|-------|-----------|---------------|
| Core/Domain | External libs only | Any internal layer |
| UseCases/Services | Core/Domain | Adapters, Infra, Entry |
| Adapters/Handlers | UseCases, Core | Other adapters |
| Infra/Data | Core domain types | Presentation, Handlers |
| Entry/Scripts | All internal layers | Contain business logic |

Adapt this table to the ACTUAL layers found in the project.

## Step 4: Mandatory Flows

Identify critical paths that must never be bypassed:
- Authentication/authorization flow
- Data validation flow
- Error handling flow
- Any "gate" or "middleware" pattern

Use Grep to find these patterns in the codebase.

## Step 5: User Confirmation

Present the detected architecture via AskUserQuestion:

"Detected architecture: [layer diagram]. Is this correct?"

Options: "Correct", "Adjust layers", "Different architecture"

## Output Format

```yaml
ARCHITECTURE_MAP:
  style: [architecture style]
  layers:
    - name: [layer name]
      path: [directory path]
      can_import: [list of allowed layers]
      cannot_import: [list of forbidden layers]
  mandatory_flows:
    - description: [flow description]
      pattern: "[e.g., Signal -> RiskEngine -> Order -> Connector]"
  forbidden_patterns:
    - description: [what not to do]
      grep_pattern: [pattern to detect violation]
```

## Integration

The ARCHITECTURE_MAP feeds into `generate-rules` (rule 50) and `validate-context`.
