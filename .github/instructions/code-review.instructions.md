---
applyTo: "**"
excludeAgent: "cloud-agent"
---

# Code review: factory-sandbox

The project rules are in `AGENTS.md`. Review against them; this file adds only what is specific to review.

## Check every pull request for
1. **Generated code edited by hand**: this project has none.
2. **A bug fix without a test that fails without the fix.** Say which test is missing, or why the added one passes without the fix.
3. **Golden or snapshot data** rewritten wholesale, expectations changed in files unrelated to the fix, tests deleted or disabled, assertions weakened — unless the description explains it.
4. **Scope:** refactors, reformatting, renames, dependency bumps, documentation churn unrelated to the purpose.
5. **Stop-and-ask areas** from `AGENTS.md` touched without a call-out in the description.
6. **Project-specific hazards.** A function that raises, or returns a value of another type, for an empty text or a text of white space only; a changed result for input that already worked; a new dependency.

## How to report
- Only concrete defects: file and line, what goes wrong, and a scenario that triggers it.
- If unsure, say what you would need to confirm it; do not present it as a finding.
- If you find nothing, say which checks you performed. Do not just approve.
