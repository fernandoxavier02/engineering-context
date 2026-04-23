# Anti-Pattern Detection Catalog

Detailed detection patterns organized by language and severity.

## Universal Anti-Patterns (Any Language)

### Critical

| Anti-pattern | Grep Pattern | Why Critical |
|-------------|--------------|-------------|
| Hardcoded secrets | `api_key = "`, `password = "`, `secret = "`, `token = "` | Security vulnerability |
| SQL injection | `f"SELECT`, `f"INSERT`, `f"UPDATE`, `f"DELETE` (string interpolation in SQL) | Security vulnerability |
| Command injection | `os.system(`, `subprocess.call(` with string concatenation | Security vulnerability |
| Auth bypass | Missing auth middleware on mutating endpoints | Security vulnerability |

### Warning

| Anti-pattern | Grep Pattern | Why Important |
|-------------|--------------|--------------|
| Print in production | `print(`, `console.log(`, `fmt.Println(` | Debug left in code, performance impact |
| God files | Files > 300 lines (use `wc -l`) | Hard to maintain, SRP violation |
| Empty error handling | `except:`, `catch {}`, `except Exception: pass` | Silent failures |
| Duplicated logic | Similar function names in different files | DRY violation, maintenance burden |
| Magic numbers | Numeric literals without named constants | Readability, SSOT violation |

### Info

| Anti-pattern | Grep Pattern | Why Notable |
|-------------|--------------|------------|
| TODO/FIXME backlog | `TODO`, `FIXME`, `HACK`, `XXX` | Technical debt indicator |
| Commented-out code | Lines starting with `//` or `#` that look like code | Version control should handle history |
| Unused imports | Import statements not referenced in file | Dead code, context noise |

## Python-Specific Anti-Patterns

### Critical

| Anti-pattern | Grep Pattern | Fix |
|-------------|--------------|-----|
| `except:` or `except Exception` | `except\s*:`, `except\s+Exception\s*:` | Catch specific exception type |
| `import *` | `from\s+\w+\s+import\s+\*` | Import only what's needed |
| Mutable default args | `def\s+\w+\(.*=\[\]`, `def\s+\w+\(.*=\{\}` | Use `None` default, create inside function |
| `eval()` or `exec()` | `eval(`, `exec(` | Use `ast.literal_eval()` or proper parsing |

### Warning

| Anti-pattern | Grep Pattern | Fix |
|-------------|--------------|-----|
| Missing type hints on public API | `def \w+\([^)]+\):` without `->` on module-level functions | Add return type hints |
| Bare `raise` in wrong place | `raise` without exception type | Raise specific exception |
| `global` variables | `global\s+\w+` | Use dependency injection or class state |
| String concatenation in SQL | `"\s*\+\s*` near SQL keywords | Use parameterized queries |

## TypeScript-Specific Anti-Patterns

### Critical

| Anti-pattern | Grep Pattern | Fix |
|-------------|--------------|-----|
| `any` type | `:\s*any\b`, `as\s+any` | Use proper type or generic |
| `@ts-ignore` | `@ts-ignore`, `@ts-expect-error` | Fix the type error properly |
| Non-null assertions | `\w+!` (trailing `!` on identifiers) | Use proper null checks |

### Warning

| Anti-pattern | Grep Pattern | Fix |
|-------------|--------------|-----|
| Missing return types on exports | `export\s+(function\|const)` without `: Type` | Add return type annotations |
| `var` usage | `\bvar\s+\w+` | Use `const` or `let` |
| Nested promises | `.then(` inside `.then(` | Use async/await |
| Console.log in production | `console\.(log\|debug\|info)` | Use structured logger |

## Go-Specific Anti-Patterns

### Critical

| Anti-pattern | Grep Pattern | Fix |
|-------------|--------------|-----|
| `panic()` in library | `panic\(` in non-main packages | Return error instead |
| Ignored errors | `_\s*,\s*err` or `_\s*=` | Handle or explicitly document ignored error |

### Warning

| Anti-pattern | Grep Pattern | Fix |
|-------------|--------------|-----|
| Exported without docs | `func [A-Z]` without preceding comment | Add godoc comment |
| Naked goroutines | `go\s+func` without error handling | Use errgroup or proper goroutine management |
| Defer in loop | `defer\s+\w+` inside `for` loop | Move defer outside or use explicit cleanup |

## Ruby-Specific Anti-Patterns

### Critical

| Anti-pattern | Grep Pattern | Fix |
|-------------|--------------|-----|
| `eval()` | `eval\s*\(` | Use safe alternatives |
| Monkey-patching | Class redefinition of core types | Use refinement or decorator |

### Warning

| Anti-pattern | Grep Pattern | Fix |
|-------------|--------------|-----|
| Global variables | `\$\w+` | Use instance variables or constants |
| `rescue => e` without handling | `rescue\s*=>\s*e\s*$` | Handle specific exceptions |
