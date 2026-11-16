# Python Conventions

Follow PEP 8 for Python code and PEP 257 for docstrings. [PEP 8](https://peps.python.org/pep-0008/) · [PEP 257](https://peps.python.org/pep-0257/)

## Naming

| Element | Convention | Example |
| --- | --- | --- |
| Modules and packages | Short lowercase names. Use underscores in module names where helpful. | `mission_status.py` |
| Classes | PascalCase | `MissionStatus` |
| Functions, methods, and variables | snake_case | `read_status()`, `search_area` |
| Constants | UPPER_SNAKE_CASE | `MAX_RETRIES` |
| Internal attributes and helpers | Single leading underscore | `_last_update` |

Use `self` for instance methods and `cls` for class methods.

## Layout and imports

- Indent with four spaces. Keep lines within 79 characters and wrap flowing comments and docstrings at 72 characters.
- Put imports near the top of the module, after the module docstring. Separate standard library, third-party, and local imports with blank lines.
- Prefer explicit imports and give each imported module its own line.
- Use two blank lines between top-level definitions and one between methods in a class.
- Put spaces around assignment and comparison operators and after commas.

## Documentation and interfaces

- Add docstrings to modules, public classes, and public functions and methods. Start with a short summary such as `"""Return the current mission status."""`.
- Document arguments, return values, exceptions, and side effects where callers need them. Include units and coordinate frames when they affect interpretation.
- Use type hints on public interfaces where they clarify expected inputs and outputs.
- Catch specific exceptions you can handle. Let unexpected errors propagate to the layer responsible for reporting or recovery.

See the [software development conventions](software-development-conventions.md) for how we document interfaces, write tests, and review changes.

## Run Python checks

Ruff checks Python in `packages/` and `scripts/`. The root `pyproject.toml` uses Ruff's default lint rules, Python 3.12, and a 79-character formatting target.

From the repository root, activate a Python virtual environment and run the same commands as CI.

```bash
python -m pip install ruff==0.16.8
ruff check packages scripts
ruff format --check packages scripts
```

`ruff check` reports lint violations. `ruff format --check` reports files that need formatting. To apply formatting, run `ruff format packages scripts` and review the diff.

GitHub Actions runs both checks on pull requests into `Development` and `main`. The Python job runs independently of the Jazzy build. In VS Code, the Ruff extension can use the same repository configuration. [Ruff tutorial](https://docs.astral.sh/ruff/tutorial/) · [Ruff editor setup](https://docs.astral.sh/ruff/editors/setup/)
