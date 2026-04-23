#!/usr/bin/env python3
"""Auto-detect project stack and output PROJECT_PROFILE YAML."""

import json
import os
import subprocess
from pathlib import Path


def detect_language() -> dict:
    """Detect primary language from project files."""
    indicators = {
        "Python": ["pyproject.toml", "setup.py", "requirements.txt", "Pipfile"],
        "TypeScript": ["tsconfig.json", "package.json"],
        "Go": ["go.mod"],
        "Rust": ["Cargo.toml"],
        "Java": ["pom.xml", "build.gradle", "build.gradle.kts"],
        "Ruby": ["Gemfile"],
    }
    found = {}
    for lang, files in indicators.items():
        for f in files:
            if Path(f).exists():
                found[lang] = f
    return found


def detect_framework() -> str | None:
    """Detect framework from imports."""
    checks = {
        "FastAPI": ("from fastapi", "*.py"),
        "Flask": ("from flask", "*.py"),
        "Django": ("from django", "*.py"),
        "Express": ("require('express')", "*.js"),
        "Next.js": ("next", "package.json"),
        "Rails": ("rails", "Gemfile"),
    }
    for name, (pattern, glob) in checks.items():
        try:
            result = subprocess.run(
                ["grep", "-r", "-l", pattern, "--include", glob, "."],
                capture_output=True, text=True, timeout=5
            )
            if result.stdout.strip():
                return name
        except Exception:
            pass
    return None


def detect_test_framework() -> str | None:
    """Detect test framework."""
    if Path("pyproject.toml").exists():
        content = Path("pyproject.toml").read_text()
        if "pytest" in content:
            return "pytest"
        if "unittest" in content:
            return "unittest"
    if Path("package.json").exists():
        content = Path("package.json").read_text()
        data = json.loads(content)
        deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
        if "jest" in deps:
            return "jest"
        if "vitest" in deps:
            return "vitest"
    if Path("go.mod").exists():
        return "go test"
    return None


def detect_layers() -> list[str]:
    """Detect architecture layers from directory structure."""
    known = [
        "src/core", "src/domain", "src/usecases", "src/adapters",
        "src/infra", "src/api", "src/models", "src/views",
        "src/controllers", "src/services", "src/repositories",
        "app", "lib", "internal", "pkg", "cmd",
        "src/features", "src/verticals", "src/ml",
    ]
    return [l for l in known if Path(l).exists() and Path(l).is_dir()]


def detect_architecture_style(layers: list[str]) -> str:
    """Guess architecture style from layers."""
    layer_set = set(l.replace("src/", "") for l in layers)
    if {"domain", "usecases"} & layer_set:
        return "Clean Architecture"
    if {"models", "views", "controllers"} & layer_set:
        return "MVC"
    if {"domain", "ports", "adapters"} & layer_set:
        return "Hexagonal"
    if "features" in layer_set:
        return "Vertical Slices"
    if {"core", "verticals"} & layer_set:
        return "Layered"
    return "Unknown"


def main():
    lang_map = detect_language()
    language = next(iter(lang_map), "Unknown")
    layers = detect_layers()
    entry_points = []
    for name in ["main.py", "main.go", "main.ts", "app.py", "index.ts", "run.py", "cli.py"]:
        if Path(name).exists():
            entry_points.append(name)

    profile = {
        "name": Path(".").resolve().name,
        "language": language,
        "framework": detect_framework(),
        "test_framework": detect_test_framework(),
        "build_command": None,
        "test_command": None,
        "lint_command": None,
        "layers": layers,
        "entry_points": entry_points,
        "architecture_style": detect_architecture_style(layers),
        "has_claude_md": Path("CLAUDE.md").exists(),
        "existing_rules": len(list(Path(".claude/rules").glob("*.md"))) if Path(".claude/rules").exists() else 0,
    }

    if language == "Python":
        profile["build_command"] = "pip install -e ."
        profile["test_command"] = "pytest"
        profile["lint_command"] = "ruff check ."
    elif language == "TypeScript":
        profile["build_command"] = "npm run build"
        profile["test_command"] = "npm test"
        profile["lint_command"] = "eslint ."

    # Output as YAML
    print("PROJECT_PROFILE:")
    for k, v in profile.items():
        if isinstance(v, list):
            print(f"  {k}:")
            for item in v:
                print(f"    - {item}")
        elif isinstance(v, bool):
            print(f"  {k}: {'true' if v else 'false'}")
        elif v is None:
            print(f"  {k}: null")
        else:
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
