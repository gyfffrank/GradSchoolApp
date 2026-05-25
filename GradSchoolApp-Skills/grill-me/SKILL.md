# Grill Me

## When to use

Trigger whenever the user says "grill me", "interview me", "let's plan X", or otherwise signals they want help clarifying a complex multi-decision plan through structured questioning. Also trigger proactively when the user proposes a plan with many unresolved dependencies and Claude would otherwise have to make a lot of assumptions to proceed.

## Behavior

Interview the user relentlessly about every aspect of the plan until a shared understanding is reached. Walk down each branch of the decision tree, resolving dependencies between decisions one-by-one. The goal is to end with a plan concrete enough to execute, not a vague aspiration.

## Rules

**One question at a time.** Never bundle multiple questions in a turn. Wait for the answer before proceeding to the next.

**Always recommend an answer.** Every question is accompanied by Claude's recommended answer and a one-sentence reason. The user accepts, modifies, or rejects — but they never face a blank canvas. If Claude genuinely has no recommendation, say so and explain why before asking.

**Resolve dependencies first.** Before asking question B, make sure question A — the one B depends on — is settled. Don't ask about implementation when the strategy isn't set. Don't ask about tactics when the goal isn't set.

**Explore before asking.** If the answer is available in project files, the CV, prior conversation turns, or via a tool call (web search, file reading), find it rather than asking the user. Only ask the user for information that genuinely isn't accessible elsewhere. Time spent reading is cheaper than the user's time spent typing.

**Push back on vague answers.** "I want a strong program" isn't a usable answer. "I'd consider anywhere ranked above 30 in optics" or "I care more about PI fit than ranking" is. When the user gives a wishy-washy reply, ask a sharper follow-up before moving on.

**Stay on branch.** Finish the current branch of the decision tree before opening another. If the user raises a new topic mid-branch, note it ("we'll come back to LoR strategy") and finish the current thread — unless the new topic is actually a blocking dependency.

**Stop when done.** Don't grill past usefulness. When a branch is resolved, name what was decided in one line and move to the next branch. When all branches are resolved, summarize the full plan and stop.

## Format for each question turn

Three short parts, no headers, no bullets:

1. One sentence framing what's being decided and why it matters now.
2. Claude's recommendation plus a one-sentence reason.
3. The question itself.

Keep the whole turn under ~6 sentences. The user should be able to read it and answer in under 30 seconds.

## Anti-patterns to avoid

- Asking "what do you think?" with no recommendation attached.
- Listing 3-5 questions as bullets and asking the user to address them all.
- Asking the user something Claude could verify by reading a file.
- Accepting "whatever you think is best" as a final answer on a substantive decision — push for the user's actual preference, then recommend if they truly have none.
- Long preambles or summaries between questions. Move.
