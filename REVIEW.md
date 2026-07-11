# Repository Review Request

## Context

This repository is an **agent-neutral framework for developing Python-based projects**. It currently contains:

- Basic project scaffolding
- Instruction sets intended to be followed by an AI/LLM agent

**Critical design constraint:** The *consumers* of this framework are **local LLMs with small context windows** (e.g., 8k–32k tokens) — not you. Work is executed in discrete implementation tracks (phases), with a **fresh session between each track**, so no conversational memory carries over. All context an executing agent needs for a given track must be explicitly available in the files it's directed to read.

You are reviewing this framework as a frontier model with full-repository visibility. Use that advantage: reason across files, trace instruction chains end-to-end, and evaluate whether a much weaker model could execute each track successfully.

## Your Task

### 1. Correctness
- Code errors, bugs, or broken scaffolding
- Internal inconsistencies: contradictory instructions, mismatched file references, naming conflicts between documents
- Instructions referencing files, paths, or steps that don't exist
- Trace each track's instruction chain from start to finish and flag any point where an agent would stall or diverge

### 2. Fitness for small-context local LLMs
- Files or instruction sets too long/dense to fit a small context window alongside the code being worked on — estimate rough token counts where relevant
- Ambiguous language a smaller model would likely misinterpret; flag anything requiring inference rather than explicit direction
- Missing state-handoff mechanisms: since sessions reset between tracks, verify each track can bootstrap from files alone (progress/state file, explicit "read these files first" directives, per-track completion criteria)
- Instructions assuming knowledge from a prior phase without restating or referencing it

### 3. Language tightening
- Verbose, redundant, or hedged instructions
- Passive or ambiguous phrasing that should be imperative and testable
- For the worst offenders, provide a rewritten version, not just a critique

### 4. Missing scaffolding
- Suggest additional scaffolding, templates, or instruction files (e.g., state-tracking files, verification checklists, error-recovery instructions, track-completion handoff template)
- For each, provide a draft or skeleton, not just a description

## Output Format

1. **Summary** — 3–5 sentence overall assessment, including whether the framework is currently executable end-to-end by a small local model
2. **Critical issues** — errors that would cause an executing agent to fail or produce wrong output (file path + section reference for each)
3. **Small-context risks** — issues specific to the local-LLM/phased-session constraint
4. **Improvements** — language and structural fixes, ordered by impact, with concrete rewrites for high-impact items
5. **Proposed additions** — new scaffolding with rationale and draft content

Cite the specific file and section for every finding. This is a review — do not modify any files. If intent is ambiguous, say so rather than guessing.