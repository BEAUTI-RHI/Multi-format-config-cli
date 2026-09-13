
# Multi-format Config CLI Tool 

## GOAL 

A CLI that reads config from JSON/YAML/TOML/env vars, merges them by precedence, and outputs a resolved config (or validates it against a schema).

## What it teaches 

Real CLI design (argparse/click), separating I/O from logic (testability), packaging as an installable command (pyproject.toml entry points), exit codes as a contract, config precedence patterns used in real tools (like git config).

