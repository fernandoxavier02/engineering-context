---
name: detect-stack
description: "This skill should be used when the user asks to 'detect project stack', 'identify tech stack', 'what language is this project', 'analyze project technology', or 'what framework does this use'. Auto-detects language, framework, test framework, build tools, and architecture style from project files."
---

# Detect Project Stack

Auto-detect the project's technology stack by scanning project files.

## Step 1: Language Detection

Check for indicator files (run in parallel):

| File | Language |
|------|----------|
| `pyproject.toml`, `setup.py`, `requirements.txt` | Python |
| `package.json`, `tsconfig.json` | TypeScript/JavaScript |
| `go.mod` | Go |
| `Cargo.toml` | Rust |
| `pom.xml`, `build.gradle` | Java |
| `Gemfile`, `*.gemspec` | Ruby |

## Step 2: Framework Detection

Use Grep to search for framework imports:

| Pattern | Framework |
|---------|-----------|
| `from fastapi` or `import fastapi` | FastAPI |
| `from flask` | Flask |
| `from django` | Django |
| `next.config` | Next.js |
| `import express` or `require("express")` | Express |
| `Rails` in Gemfile | Rails |

## Step 3: Test Framework Detection

| Pattern | Framework |
|---------|-----------|
| `import pytest` or `[pytest]` in pyproject.toml | pytest |
| `import unittest` | unittest |
| `describe(` or `test(` in JS files | Jest/Vitest |
| `func Test` in Go files | go test |
| `RSpec.describe` | RSpec |

## Step 4: Build and Lint Commands

Detect from `package.json` scripts, `Makefile`, `pyproject.toml` tool configs, or `Cargo.toml`.

## Step 5: Existing Context

Check for `CLAUDE.md`, `.claude/rules/*.md`, `.kiro/steering/*.md`, `docs/`.

## Step 6: Architecture Style

Scan directory structure:

| Pattern | Style |
|---------|-------|
| `src/core/`, `src/domain/`, `src/usecases/` | Clean Architecture |
| `models/`, `views/`, `controllers/` | MVC |
| `src/domain/`, `src/ports/`, `src/adapters/` | Hexagonal |
| `src/features/*/` | Vertical Slices |
| `app/`, `lib/`, `internal/`, `pkg/` | Go Standard |

## Output Format

```yaml
PROJECT_PROFILE:
  name: [project name]
  language: [Python | TypeScript | Go | Rust | Ruby | Java | Mixed]
  framework: [name or None]
  test_framework: [name or None]
  build_command: [command or None]
  test_command: [command or None]
  lint_command: [command or None]
  layers: [list of detected layers]
  entry_points: [list of entry points]
  architecture_style: [Clean | MVC | Hexagonal | Layered | Vertical Slices | Unknown]
  has_claude_md: [true | false]
  existing_rules: [count]
```

## Utility Script

For automated detection, execute `scripts/detect.py` in the project root. The script outputs a PROJECT_PROFILE YAML to stdout.

## Integration

The PROJECT_PROFILE feeds into `map-architecture`, `generate-rules`, and `validate-context`.
