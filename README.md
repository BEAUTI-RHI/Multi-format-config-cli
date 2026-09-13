
# Multi-format Config CLI Tool 

## GOAL 

A CLI that reads config from JSON/YAML/TOML/env vars, merges them by precedence, and outputs a resolved config (or validates it against a schema).

## What it teaches 

Real CLI design (argparse/click), separating I/O from logic (testability), packaging as an installable command (pyproject.toml entry points), exit codes as a contract, config precedence patterns used in real tools (like git config).

# Project Brief ( provided by the client i.e. AI ):

The problem I have

I run this application in different environments — my laptop, a CI pipeline, a Docker container in production — and I'm tired of hardcoding config or juggling five different ways of setting the same value. I want one tool that looks at all the places config could be coming from, figures out what actually wins when they conflict, and gives me a single, predictable, final answer. I also want it to tell me when my config is wrong, not just merge broken values silently.

What "sources" means to me

I want config pulled from:

A base config file (could be JSON, YAML, or TOML — I don't want to be locked into one format, and I want the tool to figure out which one it's looking at, not make me specify it every time)
Environment variables (these need some kind of naming convention so the tool knows which env vars belong to it — I don't want it slurping up my entire environment)
Possibly more than one config file at once — e.g. a system-wide default, then a project-local override, the way git has a global ~/.gitconfig and a repo-local .git/config

Precedence — this is the part I care about most

When the same setting shows up in more than one place, I need a clear, documented, consistent rule for which one wins. Think of how git resolves config: system-level < global/user-level < local/repo-level < command-line flag. I want that same mental model here — lowest-priority defaults at the bottom, most-specific/most-explicit source at the top. I should be able to explain the precedence order to someone else in one sentence, and it should never surprise me.

I also care about how merging happens, not just which file wins outright. If my base file sets five keys and my override file only changes one, I want the other four to survive — not get wiped out because "the higher-priority source won." Nested settings need to merge sensibly too, not just get replaced wholesale at the top level.

What I want out the other end

Two modes of output:

Resolve — show me the final, fully-merged config, after all sources and precedence have been applied. I want to actually see what my app is going to run with, as a sanity check, before I trust it.
Validate — check that final config against a schema I define, and tell me clearly if something's missing, the wrong type, or otherwise invalid. If it's invalid, I want to know exactly what's wrong and where it came from — not a stack trace.

Behavior when things go wrong

This tool needs to be trustworthy enough to drop into a script or CI pipeline unattended. That means:

It has to fail loudly and specifically when something's actually broken (malformed file, missing required setting, wrong type) — not silently produce a half-correct config.
It has to succeed quietly and predictably when everything's fine.
Whatever calls this tool (a shell script, a CI job) needs to be able to tell success from failure without parsing my output text — the exit code itself needs to mean something specific and be documented, not just "0 good, 1 bad."

How I expect to use it day to day

I want to be able to install this as a real command on my machine — not run python some_script.py, but type the tool's name directly, like any other CLI I've got installed (git, docker, whatever). It should have discoverable help text, so if I forget the exact flag I need I can ask it and get an answer, the way any well-behaved CLI does.

One more expectation

I'm going to want to test this thing — thoroughly, and without needing real files on disk or real environment variables set every time I run a test. So however you build it, I need to be able to verify the merging/precedence/validation logic in isolation from wherever the config actually comes from. That's on you to figure out architecturally — I just need the end result to be testable.
