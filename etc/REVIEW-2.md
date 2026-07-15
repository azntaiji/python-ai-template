# Repository Review Request

## Context

This repository is an **agent-neutral framework for developing Python-based projects**. It currently contains:

- Basic project scaffolding
- Instruction sets intended to be followed by an AI/LLM agent

**Critical design constraint:** The *consumers* of this framework are **local LLMs with small context windows** (e.g., 8k–28k tokens) — not you. Work is executed in discrete implementation tracks (phases), with a **fresh session between each track**, so no conversational memory carries over. All context an executing agent needs for a given track must be explicitly available in the files it's directed to read.

You are reviewing this framework as a frontier model with full-repository visibility. Use that advantage: reason across files, trace instruction chains end-to-end, and evaluate whether a much weaker model could execute each track successfully.

## Your Task

Review the framework and provide recommendations to streamline tool-calling so that it is model-agnostic - specifically using the Pi agent harness, which is centered around four tools: `read`, `write`, `edit`, and `bash`. For more information you can search through the Pi documentation: https://pi.dev/docs

Provide a written recommendation report. Do NOT edit any files yet.
