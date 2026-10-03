## Problem Statement

Antoine gives Forge an approved idea and expects an interview followed by usable specifications. The unfinished ticket-7 implementation built a second interview/semantic-resolution framework instead of composing the existing skills. A transcript-only export is not a build specification, and private local records cannot be the handoff to ticket synthesis.

## Solution

Compose grill-me (and its grilling dependency) in the originating conversation, then to-spec. The agent challenges assumptions and recommends choices; Antoine makes product and technical decisions. Missing answers keep the conversation pending. When clarification is sufficient, synthesize the finite current milestone and publish its spec issue to GitHub without another routine approval prompt. Retain separate whole-product vision and exact questions/recommendations/answers with source references under docs. Pin the publication to an immutable Git commit and read back the exact issue/documents. Ticket #8 later consumes these GitHub references and runs to-tickets; #7 does not generate tickets or start workers.

## User Stories

1. As Antoine, I want Forge to run the existing grill-me skill so that assumptions are challenged without a second interview engine.
2. As Antoine, I want recommendations while retaining the final decision so that the chosen behavior matches my intent.
3. As Antoine, I want unanswered questions to keep planning pending so that silence never becomes consent.
4. As Antoine, I want actual answers and their sources retained so that accepted recommendations and later clarifications are traceable.
5. As Antoine, I want settled programming language, user-facing language applicability, stack, constraints and testing choices in real prose so that developers do not have to infer them from raw answers.
6. As Antoine, I want whole-product vision separate from a finite current milestone so that future capabilities do not silently become executable work.
7. As Antoine, I want to-spec to publish a usable current-milestone issue in GitHub so that handoff does not depend on local conversation files.
8. As Antoine, I want immutable versioned docs and exact read-back so that later assignments can cite a stable specification revision.
9. As Antoine, I want explicit planning-skill paths and dependency resolution so that duplicate installed names cannot select the wrong instructions.
10. As Antoine, I want the completed planning handoff to remain execution-disabled so that ticket #8 and later safety slices retain their own responsibilities.

## Implementation Decisions

- Use a thin same-conversation skill assignment and read-back completion operation on the existing trusted Python CLI. Reuse actual selected skill bytes; no custom interview schema, semantic-resolution engine, generalized publisher or future-stage catalog.
- Python and standard-library bookkeeping were accepted in original Q30. Existing approved intake/onboarding behavior remains unchanged. GitHub was selected in Q17/Q27.
- Product-specific programming and user-facing languages are decided with the operator in grilling. This documentation-only validation has no product UI and does not invent a fixed locale for future products (Q8).
- Synthesis expands an explicitly accepted recommendation while preserving the literal answer in the decision log. Later clarifications supersede earlier meanings, not the original transcript; Q19 resolves Q16’s ordinary-merge freeze versus gated recovery.
- Retain requirements, constraints, non-goals, acceptance behavior and testing decisions in the synthesized current-milestone spec; retain future scope in vision only.
- GitHub publishes the spec issue and documentation snapshots. Completion verifies the exact onboarded repository, immutable commit, regular documentation bytes and issue identity/body, then records GitHub references in existing durable state. No worker assertion is publication evidence.
- Adapt grill-me/to-spec routine confirmations locally to the agreed autonomous transition; retain substantive user decisions and unchanged tests, independent review and security gates. No extra ticket-batch approval is introduced.

## Testing Decisions

Test the public lifecycle CLI with isolated subprocesses, durable SQLite and deterministic HTTP fixtures. Preserve all integrated intake/onboarding regressions. Exercise pending planning, explicit skill/dependency validation, idempotent restart, stale/mismatched issue and docs, repository identity, malformed inputs, immutable revision and disabled execution. Prove at least one feature regression fails on the old draft. Run Python 3.11 and 3.13 CI and a non-root network-none container with both normal and alternate TMPDIR layouts.

For real acceptance, reuse the genuine answered Q1–Q39 interview and latest narrowed scope, synthesize these Markdown documents with to-spec, publish to the already authorized private disposable repository, and read back the exact issue and immutable docs. Clearly distinguish genuine host publication/readback from any credential-blind offline CLI replay. Fresh simplification and independent requirement/security review must pass before controlled integration and closure.

### Acceptance Criteria

- Forge uses the actual grill-me/grilling → to-spec instructions in the exact originating conversation; recommendations never substitute for actual operator decisions and missing input stays pending.
- Real prose retains technical choices/applicability, finite scope, behavior, constraints, non-goals, testing and provenance; vision is separate and future scope is not dispatched.
- The GitHub spec issue and immutable docs read back exactly, with usable references for ticket #8; repeats do not falsely complete mismatched or changed publication.
- Planning resolves explicit selected skills and required dependency, adapts only routine confirmation loops, and never loads beta or unrelated memory.
- Previous integrated behavior/tests remain; independent review and candidate/integrated CI pass before #7 closes.

## Out of Scope

Running to-tickets, issue-batch/Projects publication, ticket reservation, worker execution, new products, paid resources/fallback, production deployment, generic skill graphs and custom interview/settlement state machines. Those are not missing features in this slice. The existing parent spec issue is not edited or closed.

## Further Notes

This is a genuine-interview-derived acceptance artifact in the approved disposable repository, not a claim that another live interview occurred. Historical sources are in decisions.md. Antoine’s latest direct message in Discord thread 1555860008137138218 narrows #7 to grill-me → to-spec → GitHub and leaves to-tickets to #8. All safety/delivery gates remain authoritative.
