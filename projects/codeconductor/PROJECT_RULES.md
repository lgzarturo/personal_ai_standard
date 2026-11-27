# CodeConductor — Project Rules

## Identity

- Project: CodeConductor
- Repository: https://github.com/lgzarturo/codeconductor
- Website: https://codeconductor.appsutiles.dev/
- Package: cc-codeconductor

## Context

CodeConductor is an open-source framework for structured,
reproducible AI-assisted software engineering workflows.

It coordinates specialized agents through versioned contracts,
task cards, risk-based routing and verifiable deliverables.

CodeConductor is a workflow framework, not a prompt collection.

## Language

- User interaction: Spanish.
- Source code: English.
- Public documentation: English.
- Commit messages: English.
- Issues: English.
- Pull requests: English.

Preserve the language of existing artifacts when appropriate.

## Sources of truth

Base URL: https://github.com/lgzarturo/codeconductor

- AGENTS.md: agent instructions and project conventions.
- CLAUDE.md: project-specific agent context.
- README.md: public capabilities and limitations.
- CONTRIBUTING.md: contribution requirements.
- docs/philosophy.md: engineering philosophy.
- docs/current-status.md: implementation status.
- BACKLOG.md: pending work.
- ROADMAP.md: product direction.
- CHANGELOG.md: release history.
- policy.yml: declared policies.
- schemas/: structured contracts.

Prefer the active checkout over remote documentation when working locally.

## Engineering

- Preserve agent contracts, schemas and public interfaces.
- Follow the established risk-based routing.
- Respect approved Technical Plans and implementation scope.
- Apply TDD, OpenSpec, Council and RDD according to the applicable workflow.
- Preserve acceptance tests and verification evidence.
- Distinguish shipped functionality from experimental capabilities.
- Prefer enforceable validation over additional prose instructions.
- Do not introduce unnecessary dependencies or abstractions.

## Local development

Use Bun and the existing TypeScript toolchain.

Execute the local CLI with `bun run dev`.

Do not use the published npm package to validate changes in
the active checkout.

Preserve the distinction between maintainer-only functionality
and consumer artifacts.

## Terminology

Use the established project vocabulary:

- Task Card
- Conductor Agent
- Agent Contract
- Routing Policy
- Skills
- Deliverable
- Scorecard

Do not replace established concepts with generic terminology
that changes their meaning.

## Version control

- Use Conventional Commits.
- Write commit messages in English.
- Follow the contribution and release processes.
- Include relevant verification evidence in pull requests.

## Restrictions

- Do not bypass applicable delivery gates.
- Do not modify acceptance tests to conceal implementation failures.
- Do not manually modify generated artifacts when their source should be updated.
- Do not claim uniform enforcement or runtime isolation where the product does not provide it.

## Definition of done

A task is complete when its approved scope is satisfied, applicable
checks pass and verification evidence corresponds to the current candidate.

Follow the repository's authoritative delivery requirements.

## Scope

These rules complement PAIS and provide context about CodeConductor.

The project repository remains the source of truth for
technical implementation and workflow enforcement.
