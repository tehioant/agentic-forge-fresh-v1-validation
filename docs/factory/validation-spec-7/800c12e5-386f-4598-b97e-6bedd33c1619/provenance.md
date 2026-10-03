# Fresh factory interview and planning decisions

This is the genuine completed originating interview, replayed for ticket #7 acceptance, not a new live interview. Source: Hermes session `20261002_173951_e80aca92`, Discord thread `1555635434036396065`. No unrelated history or beta content.

## Final settled meaning

- Q6/Q11: the agent judges sufficient clarification and transitions without routine spec/batch approval; product and technical decisions remain Antoine’s.
- Q8/Q30: Python for the factory controller, using supported Hermes/GitHub interfaces; every future product’s programming language and user-facing language are decisions for its own interview. This validation has no separate product UI and invents no locale.
- Q5/Q17/Q26: whole-product vision, synthesized finite milestone and original Q/A log are separate docs in GitHub. Only the current milestone is eligible for later to-tickets.
- Q16/Q19: ordinary merges freeze on broken main; recovery changes may pass through unchanged required gates. The later clarification resolves the earlier absolute wording.
- Q7/Q29/Q37/Q38: no new spending without approval, no paid fallback, enforce isolation and preserve independent review/tests/security.
- Latest narrowing: ticket #7 only composes grill-me → to-spec → GitHub. Ticket #8 performs to-tickets. No custom semantic decision schema or second interview engine.

## Latest operator scope

Source: current Discord thread `1555860008137138218`, direct Antoine message during this acceptance run:

> The only goal of this feature is that the forge runs a grill-me against the user, then run /to-spec to create the specs in github, then next ticket #8 is solving  running /to-tickets on the specs.
> That's it. everything is handed off through github.
> Keep it simple stupid. Be pragmatic.

## Original questions and exact answers

### Q1

❓ **Q1 — What does the factory actually produce?**  
Give me one concrete example: “I give it **X**, it does **Y**, and I receive **Z**.” What would make that first result genuinely useful—not merely an impressive agent demo?

➡️ **Recommendation:** Start with one narrow software-delivery flow: an approved task goes in, a tested, review-ready pull request comes out. Treat that as a candidate, not an assumption about your goal.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555640460935041045):

> "Regarding question one, I give it an idea it grills me and I receive a set of specs of all the questions has already asked me with the girl me skill"

### Q2

❓ **Q2 — Who are we building it for?**  
Is this your personal engineering tool, something your team will operate, or a product for other users? Who is accountable when its output is wrong?

➡️ **Recommendation:** Build for you as the first operator and accountable reviewer. Prove the loop before taking on a shared platform’s permissions and coordination problems.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555640539146092717):

> "Question two will building this for me. It's for me to operate and build products"

### Q3

❓ **Q3 — What are the hard limits on its autonomy?**  
What must it never do without your approval? Also, are there non-negotiable constraints on spending, data access, or where it runs?

➡️ **Recommendation:** Let it investigate, implement, test, and revise in an isolated workspace. Require approval for merges, deployments, destructive actions, and external communications. Give each run an explicit budget and a stop condition.

Answer **Q1–Q3** in rough terms. We’ll resolve the architecture only after these roots are settled.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555640631207002224):

> "For now, I don't see any hard limits except start a new project without my approval or my idea."

### Q4

❓ **Q4 — Where does the factory end?**  
Is generating the specs the entire initial loop, or is it the first stage of a factory that also implements, tests, and delivers the product?

➡️ **Recommendation:** Design the intended end-to-end loop now, but make **idea → approved specs** the first working increment. That lets us validate how it captures your intent before it writes code.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555642876380184586):

> "The factory ends with a fully developed product. That's for question four, for question five In the specs the whole product and the first step belongs in the specs and deciding on The language that's going to be done in the product the angle or the factory will be to loop around realme, bill specs, bill tickets, take the ticket, implement the ticket, simplify the code with this code, review the code, merge the code, pick up a notebook ticket, enter your p, until all the tickets are done, and then you start with another realme and the loop has started again."

### Q5

❓ **Q5 — What belongs in the specs?**  
Do you want a record of every question and answer, implementation-ready specifications derived from those answers, or both?

➡️ **Recommendation:** **Both, kept distinct:** a question-and-answer decision log for traceability, plus specs covering goals, behavior, constraints, non-goals, and verifiable acceptance criteria. A transcript alone isn’t a build specification.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555642876380184586):

> "The factory ends with a fully developed product. That's for question four, for question five In the specs the whole product and the first step belongs in the specs and deciding on The language that's going to be done in the product the angle or the factory will be to loop around realme, bill specs, bill tickets, take the ticket, implement the ticket, simplify the code with this code, review the code, merge the code, pick up a notebook ticket, enter your p, until all the tickets are done, and then you start with another realme and the loop has started again."

### Q6

❓ **Q6 — Who decides the grilling is finished?**  
Should it continue until every identified decision is resolved, or can you end the interview with unresolved points?

➡️ **Recommendation:** It proposes when the design is sufficiently settled and explicitly lists remaining uncertainties. **You approve the specs before implementation.** You can stop earlier, but unanswered points remain visible—not silently converted into assumptions.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555642969170772079):

> "The agent is autonomous with deciding what it needs with me, and therefore decides when the grilling is finished."

### Q7

❓ **Q7 — External consequences**  
You haven’t answered this part yet: does approving an idea also authorize spending money, deploying publicly, and deleting real data?

➡️ **Recommendation:** Autonomous development and merges; separate approval for new spending, public releases, and destructive changes to real data.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555645249076859021):

> Q7: spending must always be asked for approval
> Deploying must always be secure.

### Q8

❓ **Q8 — “Language” in the specs**  
Do you mean the programming language, the product’s user-facing language, or both? Should the agent choose, or settle this with you during grilling?

➡️ **Recommendation:** Cover both. The agent recommends a stack based on the product, checks whether you have constraints, and records the decision before generating tickets.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555645249076859021):

> Q8: agent recommend and decision is with the user.

### Q9

❓ **Q9 — What does the next grilling round investigate?**  
After all tickets are completed, does it ask you for the next improvement to **the same product**, evaluate gaps against the original specs, or wait for a new product idea?

➡️ **Recommendation:** First verify the existing product against its specs. Then grill you about its next iteration. A new product remains blocked until you supply or approve its idea.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555645249076859021):

> Q9: next grilling we’ll be for next iteration of the product. A product is never finished.

### Q10

❓ **Q10 — What counts as a fully developed product?**  
Is it enough that it runs locally, or must it be deployed and usable by its intended users?

➡️ **Recommendation:** Define this during each product’s initial grilling: required user journeys, acceptance tests, runtime environment, and delivery requirements. Completion is measured against those—not the agent’s feeling that it is finished.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555645249076859021):

> Q10: fully developed is maybe the wrong wording. The  step is finished when the tickets created by the specs and the grilling are all finished. 
> A ticket is finished when all tests are green. It answers the ticket description/feature/changes/requirements.

### Q11

❓ **Q11 — What authorizes implementation?**  
After the agent finishes grilling and generates the specs and tickets, should implementation start automatically, or should you approve that package first?

➡️ **Recommendation:** One approval of the iteration’s specs and ticket scope, then autonomous execution of that batch. This catches misunderstandings without requiring approval of every ticket.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555647245297254421):

> Q11: implementation starts right away. If necessary the user will stop it.

### Q12

❓ **Q12 — Does “finished” include review and merge?**  
Can a ticket close when its implementation satisfies the requirements and passes tests, or only after simplification, successful review, and merge?

➡️ **Recommendation:** Close it **only after merge**, with tests green on the resulting integrated code. Review must check the requirements independently; green tests alone can miss functionality—or pass because the agent weakened a test.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555647245297254421):

> Q12: a ticket is closed only when it is merged on main. If it is not merged, it doesn’t exist. The agents must be able to merge the tickets autonomously.

### Q13

❓ **Q13 — What happens when a ticket gets stuck?**  
If tests keep failing, review keeps rejecting the changes, or a dependency blocks progress, how should the factory respond?

➡️ **Recommendation:** Retry autonomously within a bounded attempt budget. Then mark the ticket blocked, preserve the evidence, and notify you. Continue with another independent ticket if possible. Never silently reduce requirements to make the ticket pass.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555647245297254421):

> Q13: great question. A debug agent comes in and investigates. Create a report and the user can make the decision for the direction the project has to take to resolve the ticket being stuck.

### Q14

❓ **Q14 — How do we enforce secure deployment?**  
May the factory deploy automatically once security checks pass, or should deployment also require your approval? “Secure” needs a checkable gate, not an agent’s assurance.

➡️ **Recommendation:** Allow automatic deployment to an isolated preview environment after mandatory checks. Require approval for production initially. Define the concrete security requirements during each product’s grilling, with failed checks blocking deployment.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555647245297254421):

> Q14: quality gates, security checks must pass in CI and then CD. Agents must monitor their deployment in main. If it fails they need to fix it.

### Q15

❓ **Q15 — When is a ticket “stuck”?**  
What should trigger the debug agent: repeated unsuccessful fixes, lack of progress, an explicit blocker, or any failure?

➡️ **Recommendation:** Ordinary failures get an autonomous fix attempt. Repeated failure of the same check, no meaningful progress, or a blocker requiring a new product/architecture decision triggers diagnosis. The report should contain evidence, attempted fixes, the likely cause, and recommended options—not just logs.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555650915921567804):

> Q15: agents responsible for the ticket decides when it is stuck. It still has to try to fix it and iterate.

### Q16

❓ **Q16 — What happens while `main` is broken?**  
Should other tickets keep merging while an agent repairs a failed CI/CD run or deployment? And if that repair becomes stuck, does your debug-report-and-user-decision rule apply?

➡️ **Recommendation:** Pause new merges and prioritize restoring healthy `main`. Attempt repairs autonomously; escalate through the debug agent if stuck. Permit a safe revert of the offending change when appropriate, and reopen its ticket if its requirements are no longer delivered.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555650915921567804):

> Q16: agent comes in to fix main. No commit can be merged on main. Roll forward is a possible quick solution if possible. Agents decide on the situation.

### Q17

❓ **Q17 — Where does the factory keep its authoritative state?**  
Where should specs, tickets, dependencies, progress, and debug reports live so that a restart doesn’t lose the project’s position?

➡️ **Recommendation:** Versioned specs and decision records in the product repository; tickets and dependencies in GitHub Issues; debug reports linked to the affected ticket. Use a small durable execution record for the factory’s current stage—chat history shouldn’t be its only memory.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555650915921567804):

> Q17: tickets are in repository projects board. Specs are in code under docs/

### Q18

❓ **Q18 — How independent are the agents?**  
Should one agent carry a ticket through implementation, simplification, review, and merge, or should those stages use separate agents?

➡️ **Recommendation:** Separate implementation and review agents with fresh contexts. The reviewer receives the ticket, specs, standards, and diff—not the implementer’s persuasive summary. Use a separate debug agent for investigation. A deterministic controller manages transitions and verifies stage results rather than letting agents declare themselves done.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555650915921567804):

> Q18: proceed as recommended

### Q19

❓ **Q19 — Does the merge freeze exempt repairs?**  
“No commit can be merged on `main`” conflicts with roll-forward: a repair usually needs a new commit.

➡️ **Recommendation:** Freeze **ordinary ticket merges**, but allow the repair agent to merge recovery changes through the required quality/security gates. Resume ordinary merges only after `main` and its deployment are healthy.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555652059267735564):

> Q19: as recommended

### Q20

❓ **Q20 — One ticket at a time, or parallel tickets?**  
Separate agents can collaborate on one ticket without implementing multiple tickets concurrently. Which execution model do you want?

➡️ **Recommendation:** Start with **one active implementation ticket**, chosen from tickets whose dependencies are satisfied. Parallelize its independent review work. Add concurrent ticket implementation later once isolation and integration are proven.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555652059267735564):

> Q20: as recommended

### Q21

❓ **Q21 — What runs the factory?**  
Should this be a reusable controller that runs independently of our chat, or a workflow I execute inside a Hermes conversation?

➡️ **Recommendation:** A reusable, deterministic controller independent of chat, with agents executing the skill-based stages. It persists progress, resumes after interruption, and exposes start, status, pause, and stop controls. Hermes can be your interface without being the sole place the loop exists.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555652059267735564):

> Q21: grill me starts from conversation. Factory runs in the background. Hermes comes back to the thread if it needs something or there is an issue. Otherwise no interactions.

### Q22

❓ **Q22 — How does the next iteration begin?**  
When the batch is merged and deployment is healthy, does the factory immediately invite you into another grilling session, or wait for you to request the next iteration?

➡️ **Recommendation:** It delivers an iteration report and invites you to the next grilling. It then waits for your input—no self-invented feature batch while you’re absent. The next interview starts from the existing product and its updated specs.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555652059267735564):

> Q22: as recommended

### Q23

❓ **Q23 — Do new bugs extend the current iteration?**  
If agents discover bugs while executing the planned tickets, do all of them join the current batch, or can some wait for the next iteration?

➡️ **Recommendation:** Fix broken `main` immediately. Include bugs that prevent the current iteration from satisfying its requirements. Put unrelated, non-blocking bugs on the board for the next grilling. Otherwise, discovering new work can keep an iteration open indefinitely.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555654226800287906):

> Q23: as recommended

### Q24

❓ **Q24 — What continues while you’re deciding on a stuck ticket?**  
After the debug agent posts its report, should the entire factory wait, or may it work on another independent ticket?

➡️ **Recommendation:** Block the affected ticket and its dependents, then continue independent work. If `main` is broken, keep ordinary execution paused until recovery is resolved. Your decision unblocks the relevant work—not necessarily the whole factory.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555654226800287906):

> Q24: as recommended

### Q25

❓ **Q25 — What does “stop” mean operationally?**  
When you interrupt the factory, should it stop immediately, finish its active ticket, or pause at a safe checkpoint? What should happen after a server restart?

➡️ **Recommendation:** A normal pause prevents new work and checkpoints the active stage without merging further changes. An emergency stop terminates workers immediately. Preserve work and diagnostic state in both cases; after a restart, reconcile repository, board, and CI state before resuming.

I’m checking the supported background execution and thread-notification mechanisms separately, without touching the beta.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555654226800287906):

> Q25: pause. as recommended

### Q26

❓ **Q26 — Which part of the product becomes tickets?**  
The specs describe the whole product and its first step. Should the factory generate executable tickets for the **current milestone only**, or for everything in the product vision?

➡️ **Recommendation:** Keep the whole-product vision in `docs/`, but generate and execute tickets only for the milestone settled during grilling. Future capabilities remain documented without becoming an enormous committed backlog.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555655064360718367):

> Q26: as recommended

### Q27

❓ **Q27 — Is GitHub the repository platform?**  
By “repository projects board,” do you mean GitHub Projects? Should GitHub Issues represent both feature tickets and bugs, with pull requests delivering them?

➡️ **Recommendation:** Yes: GitHub Issues on a GitHub Projects board, linked to their specs and delivery PRs. Use the same required work-item format for features and bugs, with additional reproduction details for bugs.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555655064360718367):

> Q27: GitHub repo is the platform. User must specify if there is a different account or platform.

### Q28

❓ **Q28, clarified — Are you happy with dedicated Hermes role profiles launching fresh workers, rather than using Codex CLI as the executor?**

➡️ That is my recommendation. **No profiles have been created or changed.**

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555657800804208840):

> Okay proceed with workers as recommended

### Q29

❓ **Q29 — What counts as spending that needs approval?**  
Does using an existing subscription or previously approved service count, or is the approval boundary any **new charge or financial commitment**? Metered model calls matter here too.

➡️ **Recommendation:** Existing subscription allowances can be used autonomously. Any chargeable API usage, purchase, or infrastructure allocation requires approval with a clear spending scope and ceiling. Exhausting an allowance pauses the affected work—it must not silently switch to a paid alternative.

**Actual operator answer** (operator `1551666201732587670`, source hermes-session:20261002_173951_e80aca92:message:15252):

> Q29: as recommended

### Q30

❓ **Q30 — What should the factory itself be built with?**  
This is separate from the programming language chosen for each product.

➡️ **Recommendation:** Python for the deterministic controller, using supported Hermes and GitHub interfaces. Keep it outside Hermes’s core so it can be versioned and tested independently.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555658675836948572):

> Q30: as recommended

### Q31

❓ **Q31 — Where should it run?**  
Should the background controller and workers run on this server, or somewhere else?

➡️ **Recommendation:** Initially, this server, under a supervised service with persistent state and restart recovery. Grilling and decision requests stay in the originating thread. No new infrastructure spending.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555658675836948572):

> Q31: as recommended

### Q32

❓ **Q32 — How should workers get credentials and permissions?**  
Should every role have the same access, or should access depend on its responsibilities?

➡️ **Recommendation:** Separate capabilities: reviewers inspect and run checks; implementers change their worktree and push a branch; only the controlled merge path can merge. CI/CD handles deployment credentials. Workers should not receive your personal assistant’s unrelated credentials. Actual isolation must enforce this—not just prompts.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555658675836948572):

> Q32: as recommended

### Q33

❓ **Q33 — What model policy should workers use initially?**  
Should roles use the existing approved provider/model setup, or should we choose different models for implementation, review, and debugging?

➡️ **Recommendation:** Start with the existing approved setup, make model selection configurable per role, and introduce differences only when evaluation shows a benefit. No automatic switch to a chargeable provider when quotas run out.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555658675836948572):

> Q33: as recommended

### Q34

❓ **Q34 — New products, existing repositories, or both?**  
Should the factory create a repository for an approved new product, work in an existing repository you explicitly identify, or support both?

➡️ **Recommendation:** Both. New repositories are private by default; existing repositories require an explicit selection. It must never infer that an unrelated repository—including the beta—is a target.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555659634470297633):

> Q34-36: as recommended

### Q35

❓ **Q35 — Can multiple products run simultaneously?**  
We agreed on one active implementation ticket. Should that limit apply across the whole factory, or separately to each product?

➡️ **Recommendation:** Initially, one active product iteration across the factory. Other products can retain their state while paused. This keeps resource use, repair priority, and operator attention predictable.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555659634470297633):

> Q34-36: as recommended

### Q36

❓ **Q36 — What happens when requirements change mid-iteration?**  
If you change the product direction or materially edit a ticket while workers are implementing it, should they immediately adapt, or pause for clarification?

➡️ **Recommendation:** Pause the affected work, resolve the change with you, update the specs and tickets, then resume. Preserve completed work where useful. Minor clarifications can proceed, but agents must not silently reinterpret a changed requirement or merge against an obsolete ticket version.

I’m auditing the existing model setup, GitHub identity, and available isolation mechanisms read-only before we finalize the technical design; no beta inspection or configuration changes.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555659634470297633):

> Q34-36: as recommended

### Q37

❓ **Q37 — Approve containerized workers?**  
Should each worker run entirely inside an isolated container, rather than merely sending its terminal commands to Docker?

➡️ **Recommendation:** Yes. Keep the trusted controller outside worker containers. Give workers only their assigned workspace, scratch space, and necessary model access—no Docker socket, personal credentials, or deployment credentials. The reviewer gets read-only access to the submitted code plus writable scratch space for running checks. GitHub writes go through controlled operations that enforce the role’s permissions.

This is the proposed design; its isolation must be tested before we call it enforced.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555660260457451612):

> Q37-39: as recommended

### Q38

❓ **Q38 — Can agents change the checks that gate them?**  
Agents sometimes “fix” a failing build by removing a test, disabling a scanner, or relaxing a threshold. What authority should they have here?

➡️ **Recommendation:** They may add or legitimately update tests, with independent review against the requirements. They may **not bypass required checks, weaken security policy, or disable branch protection** to obtain a green result. Changes to those policies require your decision.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555660260457451612):

> Q37-39: as recommended

### Q39

❓ **Q39 — How should we validate the factory itself?**  
May we create a private, disposable GitHub validation repository alongside the factory’s own repository?

➡️ **Recommendation:** Yes, explicitly for testing—not as a new product. Exercise the real loop and deliberately test rejection, a stuck ticket, broken `main`, pause/restart, and spending approval. We should prove those paths work, not just demonstrate a successful agent-generated commit.

**Actual operator answer** (operator `1551666201732587670`, source https://discord.com/channels/1551691688291074168/1555635434036396065/1555660260457451612):

> Q37-39: as recommended

## Sufficiency judgment

The genuine interview has actual answers for Q1–Q39. The original final synthesis settled the fresh factory architecture. The latest instruction settles this ticket’s narrower planning boundary. This run reuses those real decisions and does not claim another user answered new questions. Missing answers in a new interview would remain pending.
