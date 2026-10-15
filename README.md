# Paperclip autonomy test

Public, disposable development project for VPS OS acceptance tests.

This repository contains the initial scaffold for **TextKit**, a dependency-free Python text utility package. The three software features in [ROADMAP.md](ROADMAP.md) are intentionally unimplemented: GLM-5.3 will implement them only after the owner authorizes Phase F.

## Local checks

Requires Python 3.13 and no third-party packages.

```sh
python -m compileall -q textkit tests
python -m unittest discover -s tests -v
```

## Workflow

Codex plans and assigns one GLM implementation task at a time. GLM implements, tests and opens a PR; Claude independently reviews; Codex waits for successful required CI and merges only this repository. Paperclip native issue stages carry review and approval decisions. No GitHub approval is required from the shared PAT identity.

The only workflow is CI. There are no deployments, publishing steps, environment secrets, schedules or infrastructure operations. Branch main requires the `test-and-validate` check.
