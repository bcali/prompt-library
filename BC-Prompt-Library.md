# BC Prompt Library

> A comprehensive collection of AI prompts for product management, strategy, and operations.
> **Total Prompts:** 85 | **Last Updated:** January 23, 2026

---

## 📚 Table of Contents

### By Category
- [AI Features](#ai-features) (6 prompts)
- [Productivity](#productivity) (14 prompts)
- [PM Artifacts](#pm-artifacts) (12 prompts)
- [Discovery](#discovery) (11 prompts)
- [Strategy & Planning](#strategy--planning) (12 prompts)
- [Analytics](#analytics) (10 prompts)
- [Operations](#operations) (8 prompts)
- [GTM](#gtm) (7 prompts)
- [Career](#career) (5 prompts)

---

## AI Features

*6 prompts in this category*

### AI Product Strategy

**📋 Use Case:** Building your AI product strategy from scratch

**🛠️ Recommended Tools:** Claude or ChatGPT Project

**💡 Technique:** Why chain-of-thought: Strategy requires step-by-step reasoning to connect capabilities → value → business model

<details>
<summary>Click to view prompt</summary>

```
<ai_product_strategy>

<strategy_inputs>
YOUR PRODUCT:
[What you build today]

TARGET MARKET:
[Who you serve]

BUSINESS GOAL:
[What AI needs to accomplish]

COMPETITIVE CONTEXT:
[Who else is doing AI in your space]

RESOURCES:
[Team, budget, timeline]
</strategy_inputs>

<strategy_framework>

You develop AI strategies that create defensible moats. Your process:

STEP 1: Capability analysisWhat AI fits your use case:
- LLMs: Text generation, understanding
- ML: Prediction, classification
- Computer vision: Image analysis
- Agents: Multi-step workflows

What's feasible with current AI:
[What's proven vs experimental]

Key limitations to design around:
[Non-determinism, hallucinations, cost]

---

STEP 2: Value propositionWhat becomes possible with AI:
[Specific capabilities that didn't exist before]

Why it's defensible:
- Proprietary data
- Network effects
- Accumulated learning
- Integration depth

Why competitors can't easily copy:
[Your specific moat]

---

STEP 3: Market positioningHow you stand out:
[Your unique AI angle]

Responsible AI narrative:
[How you address concerns]

User trust strategy:
[How users gain confidence]

---

STEP 4: Build sequenceMinimum viable AI:
[First thing to ship]

What to learn vs leverage:
- Learn: [Where you need discovery]
- Leverage: [What you can use off-shelf]

Feature sequencing:
[Order and why]

---

STEP 5: Success metricsAI product-market fit indicators:
[What proves it's working]

Realistic goals:
- 6 months: [Target]
- 12 months: [Target]
- 24 months: [Target]

Kill criteria:
[What proves you should stop]

Now create an AI product strategy for the context provided.

</strategy_framework>

---

## Example AI Strategy

### AI Product Strategy: [Product Name]

---

### 1. Capability Analysis

AI technologies we're using:
[LLMs for X, ML for Y, etc.]

What's feasible:
[What works reliably today]

Key limitations:
[What we must design around]

---

### 2. Value Proposition

What AI enables:
[Specific new capabilities]

Our defensibility:
[Why this creates moat]

Competitive advantage:
[Why we'll win]

---

### 3. Positioning

Market angle:
[How we're different]

Responsible AI:
[How we address concerns]

Trust building:
[User confidence strategy]

---

### 4. Build Plan

MVP: [First AI feature]

Learning needs: [What to discover]

Sequence:
1. [Feature] - [Why first]
2. [Feature] - [Why next]
3. [Feature] - [Why last]

---

### 5. Success Metrics

Product-market fit signals:
[What indicates it's working]

6-month goal: [Target]12-month goal: [Target]24-month goal: [Target]

Kill if: [Criteria to stop]

</ai_product_strategy>
```

</details>

---

###  AI Roadmap Prioritization

**📋 Use Case:** You have 10+ AI feature ideas and need to sequence them strategically

**🛠️ Recommended Tools:** Claude or ChatGPT Project

**💡 Technique:** Why task decomposition: Prioritization has multiple evaluation criteria that need systematic assessment

<details>
<summary>Click to view prompt</summary>

```
<ai_roadmap_prioritization>

<roadmap_inputs>
YOUR AI FEATURES:
[List features with what AI capability they need]

CURRENT STATE:
- What AI infrastructure exists: [Vector DB? Evals? Monitoring?]
- Team AI expertise: [Level]
- Model access: [What you use]

BUSINESS CONTEXT:
- North Star Metric: [What matters]
- Timeline pressure: [Any hard deadlines]
- Strategic goal: [What you're proving]
</roadmap_inputs>

<roadmap_framework>

You sequence AI features based on dependencies and learning - not arbitrary timelines. Your process:

STEP 1: Score features

For each feature:
- Impact (1-10): Effect on north star
- AI Feasibility (1-10): Is this proven AI capability or research?
- Technical Readiness (1-10): Can we build with current infrastructure?
- Confidence (1-10): Do we have evidence this will work?
- Strategic Value: Foundation feature (enables others) or standalone?

STEP 2: Map dependencies

What must be built first:
- Infrastructure: Vector DB before RAG features, Evals before production AI
- Capabilities: Simple prompting before agents
- Learning: Assisted features before fully automated

STEP 3: Identify learning sequences

What must we learn:
- Suggest before automate (learn what users accept)
- Narrow before broad (one use case well, then expand)
- Assisted before autonomous (build trust first)

STEP 4: CategorizeQuick Wins (4-6 weeks):
High impact, uses existing infrastructure, low risk

Foundation Features:
Enables multiple future features, infrastructure investment

High-Impact Bets:
Biggest business impact, needs foundation first

Not Now:
Low ROI, too risky, or doesn't fit strategy

STEP 5: Build phases

Create 3 phases showing:
- What ships when
- Why this sequence (dependencies)
- What we learn that enables next phase
- Success criteria
- Risk factors

Now sequence the provided AI features.

</roadmap_framework>

---

## Example Roadmap

(Output adapts to features provided)

### AI Feature Roadmap

Timeline: [X months]North Star: [Metric]

---

### Feature Scores

[Feature 1]:
- Impact: [Score] - [Why]
- Feasibility: [Score] - [Why]
- Readiness: [Score] - [Why]
- Confidence: [Score] - [Why]

[Feature 2]:
[Same structure]

---

### Dependencies

[Feature X] requires:
- [Infrastructure need]
- [Prior feature]
- [Learning from earlier phase]

---

### Phased Roadmap

Phase 1 (Months 1-2): [Theme]Shipping:
- [Feature A]
- [Feature B]

Why this sequence:
[Dependencies and reasoning]

Success criteria:
- [Metric]: [Target]

Enables Phase 2 by:
[What becomes possible]

Risks:
- [Risk]: [Mitigation]

---

Phase 2 (Months 3-4): [Theme]Only possible after Phase 1 because:
[Specific dependencies]

[Same structure]

---

Phase 3 (Months 5-6): [Theme]

[Same structure]

---

### Not Now

[Feature]: [Why not + when to revisit]

</ai_roadmap_prioritization>
```

</details>

---

### Debug AI Feature Quality

**📋 Use Case:** Your AI feature is giving bad outputs, need to figure out why

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Prompting Technique: Output

<details>
<summary>Click to view prompt</summary>

```
<debug_ai_quality>

<quality_inputs>
PASTE BAD EXAMPLES:
[Copy-paste 3-5 actual outputs that are wrong/bad/unhelpful]

WHAT YOU EXPECTED:
[What you wanted it to do instead]

YOUR SETUP:
- What's the AI doing: [Summarize, generate, classify, etc.]
- Your prompt (if you have it): [Paste current prompt]
- Model: [GPT-4, Claude, other]
- Context you give it: [User input, docs, etc.]

THE PROBLEM:
- [ ] Outputs are wrong/inaccurate
- [ ] Outputs are unhelpful/generic
- [ ] Outputs are too long/short
- [ ] Outputs miss the point
- [ ] Inconsistent quality
- [ ] Other: [describe]
</quality_inputs>

<debug_framework>

You debug AI features by looking at actual outputs. Your job: spot patterns in failures, suggest concrete fixes.

---

## QUALITY DIAGNOSIS

### What You're Seeing

Bad example 1:
[Paste output]

What's wrong with it:
[Specific issue]

---

Bad example 2:
[Paste output]

What's wrong:
[Issue]

---

Pattern in failures:
[What these bad examples have in common]

---

### Root Cause Hypothesis

Most likely issue:

- [ ] Prompt is too vague - Model doesn't understand what you want
- [ ] Missing context - Model doesn't have info it needs
- [ ] Wrong instructions - You told it to do X but want Y
- [ ] Model limitations - Task is too hard for this model
- [ ] Input quality - Garbage in, garbage out
- [ ] Inconsistent outputs - Model is "creative" when you want deterministic

Evidence:
[Why you think this is the issue]

---

### Quick Fixes to Try

FIX 1: Make prompt more specificCurrent prompt (probably):
"Summarize this text"

Try instead:
"Summarize this customer support ticket in 2 sentences:
1. What is the customer's main problem?
2. What do they want us to do?

Keep it under 50 words."

Why this works: Specific structure > vague instruction

---

FIX 2: Add examplesCurrent: Instructions only

Try instead:
"Here are 3 examples of good outputs:

Input: [example]
Output: [example]

Now do this for: [actual input]"

Why this works: Models learn from examples better than instructions

---

FIX 3: Add constraintsWhat to add:
- Length limits: "In exactly 3 bullet points"
- Format: "Return as JSON: {summary: ..., action: ...}"
- Tone: "Professional but friendly"
- What NOT to include: "Don't make recommendations, just summarize"

Why this works: Constraints reduce randomness

---

FIX 4: Give it more contextWhat's it missing?
- User history?
- Product documentation?
- Previous conversation?
- Business rules?

How to add:
Paste relevant context into prompt before the actual task

---

FIX 5: Test with better inputsIf inputs are low quality:
- Clean/format them first
- Extract key info before sending to AI
- Filter out noise

---

### Testing Your Fix

How to validate:

1. Take 10 real examples (including the bad ones)
2. Run through new prompt
3. Count how many are now good
4. If <80% good → iterate again

Don't:
- Test on 1-2 examples (overfitting)
- Only test on easy cases
- Ship without testing edge cases

---

### When It's Not a Prompt Issue

Model is wrong tool if:
- Task requires 100% accuracy (use rules instead)
- Task requires real-time data (model is outdated)
- Task is simple classification (use simpler ML)

Consider:
- Hybrid approach (AI + rules)
- Different model (Claude vs GPT-4 vs fine-tuned)
- Human-in-the-loop (AI suggests, human approves)

</debug_framework>

<meta_guidance>

Real talk about AI quality:You won't get perfect on first try
Expect to iterate 5-10 times

Examples > instructions
2-3 good examples in prompt worth 1000 words of instructions

Test with real data
Your edge cases are where it breaks

Most issues are prompt issues
Before blaming the model, fix your prompt

Temperature matters
- High temperature (0.7-1.0) = creative, varied
- Low temperature (0-0.3) = consistent, focused
If outputs are too random, lower temperature

Remember:
AI features are products, not magic.
They need iteration like everything else.

</meta_guidance>

</debug_ai_quality>
```

</details>

---

### Reduce AI Costs


**📋 Use Case:** OpenAI/Anthropic bill is getting expensive, need to cut costs

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Usage analysis, optimization strategies

<details>
<summary>Click to view prompt</summary>

```
<reduce_ai_costs>

<cost_inputs>
YOUR CURRENT SITUATION:
- Monthly AI spend: $[amount]
- Main use case: [What AI does in your product]
- Model: [GPT-4, Claude, etc.]
- Volume: [Requests per day/month]
- Average tokens per request: [If you know]

WHY COSTS ARE HIGH:
- [ ] High volume of requests
- [ ] Long prompts (lots of context)
- [ ] Long outputs
- [ ] Using expensive model for simple tasks
- [ ] Not sure / don't know

CONSTRAINTS:
- Can't reduce: [Features that must stay]
- Quality bar: [Acceptable trade-offs]
- Timeline: [How urgent]
</cost_inputs>

<cost_framework>

You cut AI costs without killing quality. Your job: find waste, optimize smartly.

---

## COST REDUCTION PLAN

### Where Money is Going

Quick math:
- Requests/month: [X]
- Avg cost per request: $[Y]
- = $[Total]

Biggest drivers:
1. [Input tokens or output tokens or # of requests]
2. [Second biggest factor]

Quick win: Focus on #1

---

### Cost Reduction Strategies

STRATEGY 1: Use cheaper model for simple tasksCurrent: Everything goes to GPT-4 / Claude Opus

Instead:
- Simple tasks → GPT-3.5 / Claude Haiku (10x cheaper)
- Complex tasks → Keep expensive model

What's "simple":
- Classification (spam/not spam)
- Short summaries
- Sentiment analysis
- Extraction (pull out key info)

Potential savings: [Estimate based on % of simple tasks]

How to implement:
Add logic to route by task type

---

STRATEGY 2: Reduce prompt lengthWhat's in your prompt:
- [ ] Tons of examples
- [ ] Long instructions
- [ ] Full conversation history
- [ ] Docs/knowledge base

What to cut:
- Old examples → Keep best 3
- Redundant instructions → Simplify
- Full history → Last 5 messages
- Docs → Only relevant sections

Potential savings: If prompt is 3000 tokens, cut to 1000 = 67% savings on input

How to measure:
Track avg input tokens before/after

---

STRATEGY 3: Reduce output lengthCurrent: Letting AI write however much it wants

Instead:
- Add length constraints to prompt
- "Respond in 50 words max"
- "Use exactly 3 bullet points"
- Stop sequences

Potential savings: Output is usually biggest cost

---

STRATEGY 4: Cache repeated contentIf you're sending same context repeatedly:
(Product docs, examples, instructions)

Use prompt caching:
- Anthropic Claude: Prompt caching
- OpenAI: Cached prompts feature
- Custom: Store responses for identical inputs

Potential savings: 50-90% on repeated context

---

STRATEGY 5: Reduce unnecessary callsWhere are you calling AI that you don't need to?

- [ ] Every keystroke (debounce it)
- [ ] Identical requests (cache responses)
- [ ] Already have answer (check cache first)
- [ ] Could use rules instead (simple if/then logic)

Example waste:
User types "refund" → AI categorizes
You could just check if message contains "refund"

Potential savings: 20-50% of requests are redundant

---

STRATEGY 6: Batch requestsCurrent: Individual API call per request

Instead:
- Batch multiple requests together
- Process async when possible
- Aggregate similar requests

Good for:
- Background processing
- Bulk operations
- Non-real-time features

---

### Implementation Priority

DO FIRST (Easy, high impact):
1. [Strategy X] - [X hours to implement] - [Saves $Y/month]
2. [Strategy Y] - [Effort] - [Savings]

DO NEXT (Medium effort):
3. [Strategy Z]

DO LATER (Hard but worth it):
4. [Strategy W]

---

### Monitoring & Targets

Track these metrics:
- Cost per request
- Requests per user
- Token usage (input/output)
- Cache hit rate

Targets:
- Month 1: Reduce by [X%]
- Month 2: Reduce by [Y%]
- Goal: $[Target monthly spend]

Red flags:
If quality drops, roll back and try different approach

---

### Cost/Quality Trade-offs

What you CAN do without hurting quality:
- Shorter prompts (be concise)
- Cheaper models for easy tasks
- Caching repeated content

What MIGHT hurt quality:
- Too-short outputs (users need detail)
- Over-aggressive caching (stale responses)
- Cheapest model for everything

What WILL hurt quality:
- No context
- Tiny prompts
- Always using worst model

The balance:
Test each change, measure quality impact

</cost_framework>

<meta_guidance>

Real talk about AI costs:80/20 rule applies:
- 20% of requests probably cost 80% of money
- Find those, optimize those first

Don't optimize blindly:
- Measure before/after
- A/B test changes
- Watch for quality degradation

Cheapest isn't always best:
- Sometimes expensive model is worth it
- Sometimes cheaper model is fine
- Test to find out

Hidden costs:
- Engineering time to optimize
- Quality issues from over-optimization
- Customer churn if experience degrades

Remember:
Goal isn't zero AI spend.
Goal is efficient AI spend.

Sometimes spending more is right move (if it drives more value).

</meta_guidance>

</reduce_ai_costs>
```

</details>

---

### Simple AI Eval System


**📋 Use Case:** Need to test if AI feature actually works before shipping

**🛠️ Recommended Tools:** Claude Projects for creating eval sets

**💡 Technique:**  case generation, quality criteria

<details>
<summary>Click to view prompt</summary>

```
<simple_ai_evals>

<eval_inputs>
YOUR AI FEATURE:
[What does it do? Summarize, generate, answer questions, etc.]

**MANDATORY UPLOADS:**
- [ ] test_inputs.csv - 20+ real examples [id, input, expected_output]
- [ ] failures.csv - 5+ actual failures [id, input, bad_output, issue]

YOUR QUALITY BAR:
[Pass rate to ship? Typical: 80-90%]
</eval_inputs>

<eval_framework>

You create eval systems grounded in reality, not imagination.

---

## THE EVAL PHILOSOPHY

**Why most evals fail:**
Teams build evals from hypothetical examples and wonder why production still breaks. Generic test cases miss the specific ways YOUR system fails with YOUR users on YOUR data.

**The truth about AI failures:**
- 80% of failures come from 20% of input patterns
- These patterns are hiding in your logs right now
- You can't predict them - you have to observe them
- Every domain has unique failure modes

**What makes evals valuable:**
- Built from real user inputs (not synthetic)
- Test actual failure modes (not imagined ones)
- Updated as you discover new issues
- Specific enough to debug ("fails on dates" vs "quality issues")

**The iterative approach:**
Don't try to build perfect evals upfront:
1. Start with real data → Build basic tests
2. Ship and observe → Find new failures
3. Add those failures to eval suite → Repeat

Good evals prevent yesterday's bugs from returning, while you discover tomorrow's bugs.

---

## YOUR EVAL SYSTEM

### Step 1: Verify Real Data

**If uploads missing, STOP and say:**

"I need your actual production data to create useful evals.

**Why real data matters:**
A legal AI fails differently than a marketing AI. Technical users break systems differently than casual users. Your specific prompts create unique failure modes.

**What to upload:**
1. Real inputs from logs/tickets (anonymize if needed)
2. Actual bad outputs you've seen (with notes on what broke)
3. Expert-labeled correct outputs (for comparison)

Spend 2 hours gathering real data → Get 10x better evals than I can invent."

---

### Step 2: Analyze Your Data

Use the analysis tool to inspect uploaded files:
- Load your CSVs
- Calculate actual length distributions
- Identify edge cases that exist in your data
- Extract failure patterns from your failures file

**Document what you found (using actual numbers):**

From [filename.csv]:
- Total examples: [N from file]
- Length range: [min-max from data]
- Natural clusters: [found in analysis]
- Edge cases: [specific unusual examples]

From failures:
- Failure #1: [actual issue from file]
- Failure #2: [actual issue from file]
- Common pattern: [what you observe]

---

### Step 3: Create Test Categories

**Use only uploaded examples - never invent test cases.****CATEGORY A: Happy Path**
Select 10-15 typical examples from uploaded data:

| ID | Source | Input (first 50 chars) | Expected | Why Testing |
|----|--------|------------------------|----------|-------------|
| HP-001 | Row 3 | "[actual text]..." | "[actual]" | Typical case |
| HP-002 | Row 7 | "[actual text]..." | "[actual]" | Common pattern |

**CATEGORY B: Edge Cases**
Select boundary examples found in your data:

| ID | Source | Input | Expected | Edge Type |
|----|--------|-------|----------|-----------|
| EC-001 | Row 45 | "[shortest input found]" | "[expected]" | Min length |
| EC-002 | Row 12 | "[longest input found]" | "[expected]" | Max length |
| EC-003 | Row 23 | "[special chars found]" | "[expected]" | Special chars |

**CATEGORY C: Known Failures**
Every failure from uploaded failures.csv:

| ID | Source | Input | Bad Output | Should Produce |
|----|--------|-------|------------|----------------|
| F-001 | Failure #1 | "[actual]" | "[actual bad]" | "[correct]" |

**Coverage gaps:**
After analysis, these scenarios are MISSING:
- Gap: [specific missing scenario]
- Action: User needs to provide [N] examples of [scenario]

---

### Step 4: Define Pass Criteria

**Derive from uploaded data patterns, not assumptions.****For Happy Path:**
Analyze expected outputs to establish:
- Typical length: [calculate avg ± std dev from expected_output column]
- Required elements: [extract common patterns from expected outputs]
- Forbidden content: [patterns from failures that indicate hallucination]

Example criteria:
Test HP-001:
□ Length in range [X-Y chars] (from data analysis)
□ Contains required elements: [from expected output]
□ No hallucinated content: [patterns from failures]
□ Matches structure: [observed in expected outputs]


**For Edge Cases:**
Define how system should handle boundaries found in your data:
- Minimum input: Should handle gracefully, return [based on similar examples]
- Maximum input: Should process fully or truncate predictably
- Special chars: Should preserve or handle consistently

**For Failures:**
Define regression tests:
Test F-001:
□ Does NOT repeat exact failure
□ Does NOT show similar hallucination pattern
□ DOES include content that was missing
□ Meets general quality bar


---

### Step 5: Run Evals

**Implementation approach:**
- Use analysis tool to load test data
- For each test, get your AI's actual output
- Check against pass criteria
- Report: pass rate, specific failures, patterns

**Report format:**
=== EVAL RESULTS ===
Pass rate: [X]% on YOUR data
Total: [N tests]
Passed: [P]
Failed: [F]
Failed tests:
• HP-003: [specific failure on actual input]
• EC-001: [what broke on edge case]
• F-002: [regression detected]
Patterns in failures:
• [Common thread in failures]
• [Another pattern]
Recommendations:
1. [Specific fix based on actual failures]
2. [Another specific fix]


---

### Step 6: Maintain Evals

**Eval maintenance philosophy:**

Evals decay if not maintained:
- Production reveals new edge cases → Add to eval suite
- User behavior changes → Update test distribution
- System improves → Raise quality bar

**Quarterly eval review:**
- Run evals, check pass rate
- Add last quarter's production failures
- Remove tests for fixed issues (or keep as regression tests)
- Adjust pass criteria if quality bar changed

**When to update:**
- New feature launched: Add feature-specific tests
- Bug escaped to production: Add that exact case to evals
- User segment changed: Update test distribution
- Quality expectations changed: Adjust criteria

</eval_framework>

<quality_checks>

**Before shipping your eval suite:**

□ **Data grounding check:**
Every test comes from uploaded data? (not invented)

□ **Coverage check:**
Tests cover the actual distribution of your inputs?
- If 40% of real inputs have numbers, do 40% of tests?
- If 5% are edge cases, do 5% test edges?

□ **Failure mode check:**
Every known failure has a regression test?

□ **Measurability check:**
Pass/fail is objective? Another person would judge the same way?

□ **Gap honesty:**
Explicitly called out what's NOT covered?

**Self-critique questions:**
- Did I invent ANY test cases not in uploaded files?
- Are criteria based on actual data patterns or my assumptions?
- Have I been honest about coverage gaps?
- Can someone reproduce these evals with just the uploaded files?

</quality_checks>

<meta_guidance>

**Real talk about evals:**

**Evals are not perfect:**
- They catch known issues, not unknown ones
- 90% pass rate doesn't mean 90% of production works
- Evals test what you thought to test

**Evals are still valuable:**
- Prevent regressions (yesterday's bugs stay fixed)
- Fast feedback (find issues before production)
- Shared quality bar (team agrees what "good" means)
- Debug tool (understand what changed and why)

**Start small, iterate:**
- 20 tests that catch real issues > 200 generic tests
- Ship evals, gather production data, add new tests
- Better to have imperfect evals than no evals

**Common mistakes:**
- Building evals without real data (useless)
- Never updating evals (they decay)
- Chasing 100% pass rate (wrong goal)
- Testing only happy path (misses edge cases)
- Vague criteria (not measurable)

**Success looks like:**
- Evals catch 80% of issues before production
- When bug escapes, you add it to evals same day
- Pass rate trends up as system improves
- Team trusts evals enough to ship based on them

Remember: The goal isn't perfect evals. The goal is fewer surprises in production.

</meta_guidance>

</simple_ai_evals>
```

</details>

---

### AI Product Roadmap

**📋 Use Case:** Need to figure out where to use AI in product, prioritize AI projects

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Opportunity identification, feasibility assessment

<details>
<summary>Click to view prompt</summary>

```
<ai_roadmap>

<ai_inputs>
YOUR PRODUCT:
[What you build and who uses it]

CURRENT AI USAGE:
- [ ] No AI yet
- [ ] Some AI features (which: [list])
- [ ] AI-first product

WHY YOU'RE EXPLORING AI:
- [ ] Competitive pressure
- [ ] Customer requests
- [ ] Efficiency opportunity
- [ ] New capabilities possible
- [ ] Everyone's doing it (be honest!)

CONSTRAINTS:
- Team: [Eng capacity, AI expertise level]
- Budget: [Can you spend on AI costs?]
- Timeline: [How soon do you need results?]
- Data: [Do you have training data / user content?]
</ai_inputs>

<roadmap_framework>

You build AI roadmaps that are practical, not hype. Your job: find where AI actually helps, avoid where it doesn't.

---

## AI OPPORTUNITY ASSESSMENT

### Where AI Actually Makes Sense

AI is good at:
- Summarizing/synthesizing large amounts of text
- Generating content (drafts, variations, suggestions)
- Classification/categorization
- Answering questions from knowledge base
- Extraction (pull structured data from unstructured)
- Translation/transformation

AI is bad at:
- Tasks requiring 100% accuracy
- Real-time updated information
- Simple deterministic logic
- Anything high-stakes without human review

---

### Your Product's AI Opportunities

For each, assess:
- Value to users (High/Med/Low)
- Feasibility (Easy/Med/Hard)
- Urgency (Now/Soon/Later)

---

OPPORTUNITY 1: [Specific use case]What it does:
[One sentence description]

User value:
- Saves them: [Time/effort]
- Enables them to: [New capability]
- Improves: [Quality/accuracy]

How it would work:
[Basic flow]

Feasibility:
- Model capability: [Can models do this today?]
- Data needed: [Do you have it?]
- Integration complexity: [Easy/Med/Hard]

Rough cost:
[Requests per day × cost per request]

Risks:
- Quality issues if: [What could go wrong]
- Cost blowup if: [Unexpected usage]

Priority: [High/Med/Low]

---

OPPORTUNITY 2: [Another use case]

[Same structure]

---

OPPORTUNITY 3: [Another]

[Same structure]

---

### Prioritization Framework

High priority (Do first):
- High user value
- Easy to build
- Low cost
- Clear use case

Example: Summarize long documents

---

Medium priority (Do next):
- High value but harder
- OR easier but less valuable

Example: Generate personalized email drafts

---

Low priority (Maybe later):
- Unclear value
- Very hard
- Expensive
- Better alternatives exist

Example: AI chatbot (unless chat is core product)

---

### Practical Roadmap

MONTH 1-2: Learn & ValidateGoal: Prove AI can work for one use case

Project: [Simplest, highest-value opportunity]

Approach:
- Build basic version with Claude/GPT
- Test with 10 users
- Measure: Did they find it useful?
- Budget: $500-1000

Success = Users want to keep using it

---

MONTH 3-4: Ship & IterateGoal: Get to production quality

What to build:
- Polish UX
- Add error handling
- Set up evals
- Monitor quality

Success = 70%+ of users engage with feature

---

MONTH 5-6: ExpandGoal: Add 1-2 more AI features

Pick from: [Your med-priority opportunities]

Apply learnings from first feature

---

NEXT 6 MONTHS:Theme: [Strategic focus]

Projects:
- [Feature 1]: [Timeline]
- [Feature 2]: [Timeline]
- [Infrastructure]: [If needed - evals, monitoring, cost controls]

---

### What NOT to Do

Don't:
- [ ] Build AI chatbot as first project (too hard)
- [ ] Try to use AI for everything (most things don't need it)
- [ ] Ship without testing (AI is unpredictable)
- [ ] Assume "AI will figure it out" (you need clear instructions)
- [ ] Over-promise to customers (manage expectations)

---

### Build vs Buy Decisions

When to use OpenAI/Anthropic APIs:
- General capability (summarize, generate, classify)
- Getting started
- Don't have ML team

When to consider fine-tuning:
- Very specific task
- Lots of training data
- Need lower cost at scale
- Quality issues with base models

When to build custom ML:
- Extremely high volume (cost prohibitive for APIs)
- Latency critical (<100ms)
- Offline/edge deployment
- You have ML team

For most PMs: Start with APIs

---

### Success Metrics

Don't just track:
- "AI feature usage" (vanity metric)

Track:
- User engagement (do they come back?)
- User outcomes (do they achieve goal faster?)
- Quality (thumbs up/down, issues reported)
- Cost efficiency (cost per successful outcome)

Example good metrics:
- "Users who use AI summary save 5 min per doc"
- "AI-generated drafts accepted 70% of time"
- "Cost per summary: $0.03"

</roadmap_framework>

<ai_patterns>

### Common AI Features by Product Type

B2B SaaS:
- Summarize reports/data
- Generate drafts (emails, proposals)
- Extract insights from usage data
- Autocomplete (messages, code)

---

Content/Media:
- Generate variations
- Personalized recommendations
- Auto-tagging/categorization
- Content moderation

---

Productivity:
- Meeting summarization
- Email triage/prioritization
- Task extraction
- Smart search

---

E-commerce:
- Product descriptions
- Personalized suggestions
- Customer support automation
- Search/discovery

---

Developer Tools:
- Code completion
- Bug detection
- Documentation generation
- Test case generation

</ai_patterns>

<meta_guidance>

Real talk about AI roadmaps:Most AI projects fail because:
- Unclear use case (AI for AI's sake)
- Overly ambitious first project
- No way to measure success
- Shipping without evals

Start small:
- One clear use case
- Simple implementation
- Measure everything
- Learn before scaling

AI is not strategy:
- "Add AI" is not a roadmap
- Find real user problems
- AI is one solution tool

Manage expectations:
- AI is powerful but not perfect
- 80% good is great for AI
- Some errors are expected
- Human-in-loop for important decisions

Remember:
Best AI features feel like magic but are built methodically.

Start with one valuable, achievable use case.
Ship it, learn from it, then expand.

</meta_guidance>

</ai_roadmap>
```

</details>

---


## Productivity

*16 prompts in this category*

### Catch Up on Slack Threads

**📋 Use Case:** Long slack thread to digest

**🛠️ Recommended Tools:** LLM or Workflow: Lindy, Zapier

**💡 Technique:** Asks the AI to explain dependencies between steps ("why each phase must come before the next") rather than just listing a sequence

<details>
<summary>Click to view prompt</summary>

```
<slack_thread_synthesizer>

<thread_inputs>
PASTE THE SLACK THREAD:
[Full thread content - copy/paste from Slack]

CONTEXT QUESTIONS:
1. Why are you reading this? (catching up after vacation, deciding if you need to weigh in, preparing for a meeting)
2. What's your role in this discussion? (decision-maker, contributor, FYI only)
3. Are there specific people whose opinions matter most to you?
4. What decisions or action items are you hoping to find?
5. How much detail do you need? (quick skim vs. deep understanding)
</thread_inputs>

<synthesis_process>

You are an expert at synthesizing long, meandering Slack threads into clear, actionable summaries. You identify the signal through the noise, tracking how discussions evolve and surfacing what actually matters.

PHASE 1: THREAD ANALYSIS

First, map the conversation structure:

1. CONVERSATION FLOW
- How many participants?
- How long is the thread? (timestamp of first vs. last message)
- Did the topic shift during the conversation?
- Are there multiple sub-conversations happening in parallel?
- Were there any long gaps? (discussion paused and resumed)

2. IDENTIFY PARTICIPANTS & ROLES
For key participants, note:
- Who started the thread and why?
- Who are the decision-makers?
- Who are subject matter experts?
- Who's just reacting/observing?
- Any conflicts or disagreements between people?

3. TRACK TOPIC EVOLUTION
- What was the original question/topic?
- Did it evolve? (often threads drift from initial topic)
- Were new issues raised mid-thread?
- Was the original question answered?

PHASE 2: EXTRACT KEY ELEMENTS

Pull out the important information:

1. DECISIONS MADE
For each decision:
- What was decided: [specific outcome]
- Who decided: [person or consensus]
- Rationale: [why this decision, what alternatives were considered]
- When: [timestamp]
- Finality: Is this locked in or still being debated?

Example:
❗DECISION: Will launch feature X with limited beta first, not full rollout
- Decided by: @sarah (PM lead)
- Why: Engineering raised concerns about scale; beta lets us test with 100 users first
- When: Today at 2:47 PM
- Status: Final, team aligned

2. ACTION ITEMS
For each action item:
- What needs to be done: [specific task]
- Who owns it: [person assigned, or "unassigned" if unclear]
- Deadline: [if mentioned, or "unclear"]
- Blocker status: Does this block other work?

Format as checklist:
- [ ] @jamie: Write PRD for beta launch (due Friday)
- [ ] @engineering: Estimate effort for dashboard work (due this week) - BLOCKS design work
- [ ] UNASSIGNED: Schedule follow-up meeting (no deadline mentioned)

3. OPEN QUESTIONS
Questions that were raised but not answered:
- "What's our budget for this?" - Asked by @mike, no response yet
- "Does this need legal review?" - Discussed but no clear answer
- "Who's going to handle customer comms?" - Multiple people asked, still unclear

4. KEY CONTEXT & BACKGROUND
Important facts or context shared:
- Customer X specifically requested this feature
- We tried something similar 2 years ago and it failed because [reason]
- Legal says we must comply with [regulation] for this
- Our main competitor launched this last week

5. CONCERNS & OBJECTIONS
Who raised concerns and about what:
- @engineering: Worried about performance at scale (message link)
- @design: Thinks this UX will confuse users (message link)
- @sales: Concerned this won't work for enterprise customers (message link)

Note: Did concerns get addressed or are they still hanging?

6. CONSENSUS vs. DISAGREEMENT
- What does everyone agree on?
- Where is there active disagreement?
- Are disagreements resolved or still debating?

PHASE 3: SYNTHESIZE SUMMARY

Create a structured summary:

## Thread TL;DR (2-3 sentences)
[What was this thread about and what's the current status? Bottom line up front.]

## Key Decisions
[List all decisions made, formatted as shown above]

## Action Items
[Checklist format with owners and deadlines]

## Open Questions
[List with who asked and whether discussed]

## Important Context
[Key facts, background, or constraints mentioned]

## Concerns Raised
[Who's worried about what, and whether addressed]

## Current Status
[Where does this stand? Is discussion complete or ongoing? What happens next?]

## Your Role (if specified in context)
[Based on your context, do you need to: weigh in on something, complete an action item, make a decision, or just stay informed?]

## Related Threads or Documents
[If mentioned: links to PRDs, previous threads, related discussions]

</synthesis_process>

<quality_checks>

Validate your summary:

1. COMPLETENESS CHECK
- Did you capture all decisions, even small ones?
- Are all action items accounted for, including implied ones?
- Did you note ALL open questions, not just the most recent?

2. ACCURACY CHECK
- Are you quoting decisions correctly or adding your interpretation?
- Did you attribute statements to the right people?
- Are timestamps correct?

3. CLARITY CHECK
- Can someone who wasn't in the thread understand what happened?
- Is it clear what's decided vs. still debating?
- Are action item owners unambiguous?

4. ACTIONABILITY CHECK
- Is it clear what YOU need to do (if anything)?
- Are next steps obvious?
- Would someone know what to do Monday morning?

SELF-CRITIQUE: If any check fails, strengthen that section.

</quality_checks>

<output_format>

For quick catch-ups (< 50 messages):
- TL;DR
- Decisions
- Action Items
- Your next step

For complex threads (50+ messages):
- Full structure with all sections
- Timeline of how discussion evolved
- Link to key messages for deep-dive if needed

For urgent decision threads:
- Lead with: "NEEDS YOUR INPUT ON: [specific question]"
- Then standard structure

</output_format>

<meta_guidance>

Good Slack summaries:
- Front-load the most important information (decisions and action items)
- Make it scannable (headers, bullets, formatting)
- Distinguish between facts and opinions
- Flag what still needs resolution
- Are honest about what's unclear or messy

Avoid:
- Summarizing every message chronologically (that's not synthesis)
- Losing context about WHY decisions were made
- Missing implied action items ("someone should...")
- Treating all opinions equally (flag the decision-maker's view)
- Hiding important concerns in the middle of the summary

Remember: Slack threads often meander. Your job is to extract the structure and outcomes from the chaos. When people disagree or the thread is messy, say so - don't pretend it's cleaner than it is.

</meta_guidance>

</slack_thread_synthesizer>
```

</details>

---

### Convert Meeting Transcripts to Action Items

**📋 Use Case:** Turn messy Teams/Zoom transcripts into formatted Word documents with clear action items and decisions

**🛠️ Recommended Tools:** Claude, ChatGPT, or any LLM

**💡 Technique:** Distills signal from noisy conversation, strips filler, captures substance with clear ownership

<details>
<summary>Click to view prompt</summary>

```
<transcript_to_summary>

<inputs>
PASTE YOUR TRANSCRIPT:
[Raw Teams/Zoom transcript - timestamps, speaker labels, the whole mess]

MEETING CONTEXT:
- Meeting type: [Sync, decision, brainstorm, review]
- Attendees: [If not clear from transcript]
- Your role: [What you need to track]

OUTPUT FORMAT:
- [ ] Executive summary (2-3 sentences)
- [ ] Key topics discussed
- [ ] Decisions made
- [ ] Action items with owners
- [ ] Open questions
- [ ] All of the above
</inputs>

<conversion_framework>

You're distilling signal from noisy conversation. Strip filler, capture substance.

**Create a Word document (.docx) with the following structure:**

## EXECUTIVE SUMMARY
[2-3 sentences: What was this meeting about? What was accomplished?]

## KEY TOPICS
- **[Topic 1]**: [1-2 sentence summary of discussion]
- **[Topic 2]**: [1-2 sentence summary of discussion]

## DECISIONS MADE
- [Decision 1]
- [Decision 2]
- [None explicitly made] ← flag if true

## ACTION ITEMS
| Owner | Action | Due Date |
|-------|--------|----------|
| [Name] | [Specific action] | [Date/TBD] |

## OPEN QUESTIONS / PARKING LOT
- [Unresolved topic]
- [Who owns resolution / when revisit]

</conversion_framework>

<output_instructions>

Save as: `[Meeting Name]_Summary_[YYYY-MM-DD].docx`

Use professional formatting:
- Calibri or Arial 11pt
- Bold section headers
- Table for action items
- Page header with meeting date and attendees

</output_instructions>

<transcript_specific>

Ignore:
- Filler ("um", "you know", "let me think")
- Side conversations
- Technical difficulties discussion
- Pleasantries unless context-relevant

Flag when:
- Speaker unclear on ownership
- Decision implied but not confirmed
- Timeline mentioned without commitment

</transcript_specific>

</transcript_to_summary>
```

</details>

---

### Respond to Email

**📋 Use Case:** Inbox is full, need to respond to stakeholders/customers quickly and clearly

**🛠️ Recommended Tools:** Claude Project, Lindy, Relay.app

**💡 Technique:** Context extraction, tone matching, action-oriented responses

<details>
<summary>Click to view prompt</summary>

```
<email_response>

<email_inputs>
PASTE THE EMAIL YOU NEED TO RESPOND TO:
[Full email thread]

YOUR CONTEXT:
1. Who is this from? (customer, exec, team member, external)
2. What do they want? (decision, update, approval, information)
3. What's your relationship? (direct report, peer, boss, customer)
4. Urgency level? (respond in 5 min vs. can wait)
5. Tone needed? (formal, casual, apologetic, firm)

OPTIONAL:
- Related context (Slack threads, docs, previous decisions)
- Your initial draft (if you started writing and got stuck)
</email_inputs>

<response_framework>

You're an executive communication coach who knows that most emails are too long, too vague, or too slow. Your job: Help write responses that are clear, complete, and get results.

THE REALITY:

Bad email: 3 paragraphs of context, buried request, vague next steps
Good email: Clear ask, direct answer, explicit next steps

Most people over-explain. The best emails are half the length you think they need to be.

---

## PART 1: UNDERSTAND WHAT THEY ACTUALLY WANT

### Decode The Email

What they're asking for:
[Explicit request]

What they actually need:
[Underlying need, which might be different]

What they're worried about:
[Subtext, concern, or urgency driver]

Example:
- Asking: "Can you send me the roadmap?"
- Actually need: "I need to know if feature X will ship this quarter for my customer"
- Worried: "I'm about to lose a deal if we don't have this feature"

### Determine Response Type

DECISION NEEDED:
They're asking you to decide something
→ Response: Clear yes/no with brief rationale

INFORMATION REQUEST:
They need to know something
→ Response: Direct answer, then context if needed

UPDATE REQUEST:
They want status on project
→ Response: Current state, what's next, when to expect update

PROBLEM ESCALATION:
Something's broken and they need help
→ Response: Acknowledge, action plan, timeline

Your email is: [Which type]

---

## PART 2: STRUCTURE YOUR RESPONSE

### The Formula

Line 1: Direct answer or action
[Yes/No/Here's the status/I'll do X by Y]

Lines 2-4: Brief context (if needed)
[Why/how/what happened]

Line 5: Next steps
[What happens next, who does what, by when]

That's it. Most emails should be 3-5 sentences.

### Write The Response

DRAFT:

[Opening - match their tone]

[Direct answer - first sentence]

[Context - 1-2 sentences max]

[Next steps - specific and owned]

[Closing]

---

## PART 3: RESPONSE PATTERNS BY TYPE

### Pattern 1: Saying No (Hardest One)

Structure:
1. Acknowledge request
2. Clear "no" with reason
3. Alternative if possible

Example:

"Thanks for checking on feature X for the Q2 roadmap.

We won't be shipping it in Q2—we're focused on [other priority] which addresses [customer need].

What we can do: Get you early access to [alternative] which solves [80% of use case]. Would that work for your customer?"

Key: Don't apologize excessively. Be clear, not defensive.

### Pattern 2: Giving Status Update

Structure:
1. Current status (one sentence)
2. What's changed/progress
3. Next milestone and date

Example:

"PRD for SSO integration is in final review.

Completed: Technical feasibility, design mocks, customer validation (8 enterprises confirmed they'd upgrade)
Next: Engineering sizing this week, targeting Q3 kickoff.

I'll send full PRD by Friday."

Key: Be specific about dates and deliverables.

### Pattern 3: Making a Decision

Structure:
1. The decision
2. Quick rationale
3. What happens next

Example:

"Let's go with Option B: Phased rollout starting with enterprise tier.

Rationale: Lower risk if there are bugs, and enterprise customers have been asking for this most urgently.

Next: I'll update the PRD and sync with eng tomorrow on timeline."

Key: Don't waffle. Pick something.

### Pattern 4: Asking For Something

Structure:
1. What you need
2. Why you need it (brief)
3. When you need it by

Example:

"Can you share last quarter's churn data by customer segment?

I'm sizing the impact of the new onboarding flow and need to understand which segments churn fastest.

Need this by EOD Thursday to finalize the PRD."

Key: Make it easy for them to help you.

### Pattern 5: Apologizing/Recovering

Structure:
1. Acknowledge the problem
2. What you're doing to fix it
3. When they'll see resolution

Example:

"You're right, we should have communicated the pricing change sooner—this caught your team off guard.

Here's what I'm doing:
- Email going to all customers today with 30-day notice
- FAQ doc published
- Office hours scheduled for next week

I'll personally call your top 3 customers this afternoon."

Key: Own it, fix it, move forward. Don't dwell.

---

## PART 4: TONE CALIBRATION

### Match The Situation

Responding up (to exec/boss):
- Be concise
- Lead with answer
- Show you have it handled

Responding to peer:
- Collaborative tone
- Assume good intent
- Clear on who does what

Responding to customer:
- Empathetic
- Solution-oriented
- Set expectations clearly

Your tone for this email: [Formal/Casual/Apologetic/Direct]

### Remove Weakeners

Delete these phrases:
- ❌ "Just following up..."
- ❌ "I think maybe we could..."
- ❌ "Sorry to bother you but..."
- ❌ "Does that make sense?"

Use these instead:
- ✅ "Following up on..."
- ✅ "We should..."
- ✅ [Just state your request]
- ✅ "Let me know if you need clarification."

### The Confidence Edit

Read your draft. Count the words "just," "maybe," "possibly," "probably."

Delete them. See if it's still clear. (It is.)

---

## THE OUTPUT

### Recommended Response

Subject line: [If starting new thread or clarifying]

Email:

[Opening]

[Direct answer/action]

[Brief context if needed]

[Next steps with dates/owners]

[Closing]

Estimated length: [X sentences]
Tone: [Match to relationship and situation]

### Alternative Versions

Version 1: More detailed
[If they need more context]

Version 2: More direct
[If relationship allows brevity]

Version 3: More formal
[If external or sensitive]

</response_framework>

<quality_check>

Is it clear?
- [ ] They know what you're saying in first sentence
- [ ] No ambiguity about next steps
- [ ] No jargon without definition

Is it complete?
- [ ] Answers their actual question
- [ ] Provides necessary context
- [ ] Includes next steps with timeline

Is it concise?
- [ ] Could you delete a paragraph and it still makes sense?
- [ ] Are you over-explaining?

</quality_check>

<meta_wisdom>

On email length:

Your first draft is always too long.

Cut it in half. It's probably better.

Most people write emails to think through the problem. That's fine for your draft. Delete 50% before sending.

The BLUF principle (Bottom Line Up Front):

Military communication rule: Lead with the conclusion.

Don't make people read 3 paragraphs to find out you're saying "yes."

On tone:

Match their energy:
- They're formal → You're professional
- They're casual → You're friendly
- They're stressed → You're calm and solution-oriented

The hard truth about saying no:

Most PMs are bad at saying no because they try to soften it.

"Unfortunately, we're probably not going to be able to maybe prioritize this right now due to resource constraints..."

Just say: "We won't be building this in Q2. Here's why and here's what we can do instead."

Clear no > vague maybe.

Remember:

Your job isn't to write the perfect email.
It's to communicate clearly and move things forward.

Send it. Most emails don't deserve more than 5 minutes.

</meta_wisdom>

</email_response>
```

</details>

---

### Prep for 1:1s


**📋 Use Case:** Have 1:1 meeting in an hour, need to prepare talking points and agenda

**🛠️ Recommended Tools:** Claude, ChatGPT Projects, NotebookLM

**💡 Technique:** Relationship context modeling, issue prioritization, outcome-focused agendas

<details>
<summary>Click to view prompt</summary>

```
<one_on_one_prep>

<meeting_inputs>
WHO ARE YOU MEETING WITH:
1. Person's name and role (manager, direct report, peer, cross-functional partner)
2. Your relationship (new, established, difficult, great)
3. Meeting frequency (weekly, biweekly, monthly, ad-hoc)
4. Last meeting notes (if you have them - what was discussed)

CURRENT CONTEXT:
5. What's happening in their world right now? (launches, issues, wins, stress)
6. What's happening in your world? (what you need from them or want to share)
7. Any tension points or difficult topics?
8. Meeting length (30 min, 1 hr)

OPTIONAL UPLOADS:
- Previous 1:1 notes
- Open action items
- Project status docs
- Performance review notes (if direct report)
</meeting_inputs>

<prep_framework>

You're a leadership coach who knows that most 1:1s are wasted. People show up unprepared, discuss only surface-level status, and leave without clarity. Your job: Make these 30-60 minutes actually matter.

THE REALITY:

Bad 1:1s: Rambling status updates neither person cares about
Good 1:1s: Focused on what matters, surfaces real issues, builds relationship

The best 1:1s aren't meetings. They're conversations that make both people better at their job.

---

## PART 1: CLARIFY THE PURPOSE

### Different Types of 1:1s

WITH YOUR MANAGER:
- Their job: Help you be successful, remove blockers, give guidance
- Your job: Keep them informed, ask for help, align on priorities

WITH YOUR DIRECT REPORT:
- Your job: Coach them, unblock them, help them grow
- Their job: Update you on progress, ask for guidance, flag issues

WITH PEER/CROSS-FUNCTIONAL:
- Mutual job: Align on shared work, resolve conflicts, coordinate

This meeting is: [Which type]

### What Makes This Meeting Matter Right Now

Topics that need discussion:HIGH PRIORITY (Must discuss):
- [ ] [Urgent decision needed]
- [ ] [Blocker affecting work]
- [ ] [Tension point to address]

MEDIUM PRIORITY (Should discuss if time):
- [ ] [Strategic alignment]
- [ ] [Feedback to give/get]
- [ ] [Career/growth topic]

LOW PRIORITY (Nice to discuss):
- [ ] [General updates]
- [ ] [Future planning]

The one thing that MUST come out of this meeting:
[Specific outcome]

---

## PART 2: BUILD YOUR AGENDA

### The Structure (Default Template)

FIRST 5 MIN: THEIR TOPICS
"What's on your mind?" or "What do you want to talk about?"

Let them drive. They might have something urgent you don't know about.

NEXT 15-20 MIN: YOUR KEY TOPICS
The 2-3 things you need to discuss (prioritized above)

LAST 5-10 MIN: OPEN TIME
- Action items review
- Looking ahead
- Anything else

### Prepare Your Topics

For each topic you want to discuss:

TOPIC 1: [Name it clearly]Context (1-2 sentences):
[What they need to know to discuss this]

The question/discussion:
[What you want to talk about]

What you need from them:
- Decision on X
- Input on Y
- Unblock Z
- Just venting/thinking out loud

Example:

Topic: Roadmap prioritization for Q2

Context: We have 3 big features we could build but only capacity for 1. All have customer demand.

Discussion: Walk through trade-offs and get your input on how to think about prioritization.

Need: Your perspective on what matters most strategically, then I'll make the call.

---

## PART 3: SPECIFIC PREP BY RELATIONSHIP TYPE

### If Meeting With Your MANAGER

Questions to prepare:For decisions/guidance:
- "I'm deciding between X and Y. Here's my thinking... what am I missing?"
- "I'm stuck on [problem]. What would you do?"

For visibility:
- "Here's what's going well: [wins]"
- "Here's what's at risk: [concerns]"
- "Here's where I need help: [blockers]"

For growth:
- "I want to get better at [skill]. What opportunities should I look for?"
- "How am I doing on [thing we discussed last time]?"

Prep checklist:
- [ ] List wins (make your manager look good)
- [ ] List risks (no surprises)
- [ ] Specific asks (not vague "I need help")
- [ ] Updates on action items from last meeting

The key insight: Your manager's job is to help you be successful. Make it easy by being clear about what you need.

### If Meeting With Your DIRECT REPORT

Your preparation:Check in on their work:
- What's their biggest challenge right now?
- Are they blocked on anything?
- What are they proud of?

Check in on them as a person:
- How are they doing? (energy level, stress, motivation)
- Are they growing? Learning?
- Do they feel supported?

Topics you need to cover:
- [ ] Feedback (both positive and constructive)
- [ ] Career development
- [ ] Course corrections
- [ ] Context they're missing

Questions to ask:Opening:
- "What's top of mind for you?"
- "What's going well? What's not?"

Unblocking:
- "What do you need from me?"
- "What's slowing you down?"

Growth:
- "What do you want to get better at?"
- "What was the hardest decision you made this week?"

Feedback to give:Positive feedback (be specific):
- "The way you handled [situation] was great because [impact]"

Constructive feedback:
- "I noticed [specific behavior]. Here's the impact: [consequence]. Let's talk about how to approach it differently."

The key insight: Don't wait for performance reviews. Small feedback frequently beats big feedback rarely.

### If Meeting With PEER/CROSS-FUNCTIONAL

Your preparation:Alignment topics:
- [ ] Where are we on shared project?
- [ ] Any dependencies or handoffs?
- [ ] Timeline changes affecting them?

Issues to surface:
- [ ] Misalignment on approach
- [ ] Resource conflicts
- [ ] Communication breakdown

Questions to ask:
- "How's [project] going from your side?"
- "What do you need from me to be successful?"
- "Where are we misaligned?"

The key insight: Peer relationships are about mutual success. Help them win and they'll help you win.

---

## PART 4: DIFFICULT CONVERSATIONS PREP

### If There's Tension

Name it, don't avoid it:

"I want to talk about [thing that's awkward]. I think we see it differently and I want to understand your perspective."

Prepare:
- [ ] The facts (not your interpretation)
- [ ] Your perspective (own it as "I" statements)
- [ ] What you're curious about (their view)
- [ ] Desired outcome (what good looks like)

Example:

"I noticed we disagreed in the meeting about the launch approach. I pushed for X because [reasoning]. I sensed you thought that was wrong. Can you help me understand your concern?"

### If You Need To Give Hard Feedback

Prepare the feedback:Situation: [Specific behavior, with context]
Impact: [Why it matters, who it affects]
Request: [What you want them to do differently]

Example:

"In yesterday's review, you interrupted the designer three times while she was presenting. I think you didn't realize, but it made her feel like you weren't interested in her work. In future reviews, let's let people finish their thought before jumping in."

The key principle: Be direct, be kind, be specific.

---

## THE OUTPUT

### Your 1:1 Agenda (Share Beforehand)

Meeting: [Your Name] ↔ [Their Name]
Date: [Date]
Time: [Duration]

Their topics:
- [Space for them to add]

My topics:
1. [Topic 1 - one line description]
2. [Topic 2 - one line description]
3. [Topic 3 - one line description]

Standing items:
- Action items from last time
- Looking ahead

---

### Your Prep Notes (For You Only)

My outcomes for this meeting:
1. [Specific outcome]
2. [Specific outcome]

Topics I must cover:
- [Topic with key points]

Questions to ask:
- [Specific questions]

Feedback to give:
- [Prepared feedback]

What I need from them:
- [Specific asks]

Follow-up actions I expect:
- [Likely action items]

---

### Meeting Notes Template (Fill During/After)

Date: [Date]

Discussed:
- [Topic 1: Key points]
- [Topic 2: Key points]

Decisions:
- [What was decided]

Action items:
- [ ] [Person]: [Action] by [date]
- [ ] [Person]: [Action] by [date]

Next time:
- [Topics to follow up on]

</prep_framework>

<quality_check>

Is your agenda focused?
- [ ] 2-4 topics max (not 10 updates)
- [ ] Topics that need discussion, not just FYI
- [ ] Clear what you need from them

Are you prepared to listen?
- [ ] Asking questions, not just talking
- [ ] Open to their topics
- [ ] Ready to hear things you might not want to hear

Is this actually valuable?
- [ ] Better than an email or Slack?
- [ ] Real-time discussion needed?
- [ ] Building relationship, not just transacting

</quality_check>

<meta_wisdom>

On 1:1 frequency:

Weekly is ideal for directs and manager.
Biweekly works for stable relationships.
Monthly is too infrequent—you lose continuity.

The biggest mistake:

Treating 1:1s as status meetings.

Status can be async. Use 1:1s for:
- Coaching and feedback
- Strategic thinking
- Career development
- Building trust
- Resolving tension

On preparation:

The person who prepares wins.

If you show up with clear topics, you drive the conversation.
If you show up unprepared, you waste 30 minutes of both your lives.

The hard truth:

Most people avoid difficult conversations in 1:1s.

They stick to safe topics, avoid feedback, pretend tension doesn't exist.

Great 1:1s surface the hard stuff. That's where growth happens.

Remember:

1:1s are the highest-leverage time in your calendar.

30 minutes with the right person, discussing the right thing, can unblock a week's worth of work.

Don't waste them on status updates.

</meta_wisdom>

</one_on_one_prep>
```

</details>

---

### Write Status Updates

**📋 Use Case:** Weekly team update, stakeholder email, or exec summary due

**🛠️ Recommended Tools:** Claude, ChatGPT Projects

**💡 Technique:** BLUF (Bottom Line Up Front), traffic light status, scannable formatting

<details>
<summary>Click to view prompt</summary>

```
<status_update>

<update_inputs>
WHAT YOU'RE UPDATING ON:
1. Project/initiative name
2. Who's the audience? (team, execs, stakeholders, company-wide)
3. Update frequency (weekly, biweekly, monthly)
4. What period are you covering? (this week, this sprint, this quarter)

YOUR STATUS:
5. Overall status: Green (on track), Yellow (at risk), Red (blocked)
6. Key accomplishments this period
7. What's next
8. Blockers or risks
9. What you need from audience

OPTIONAL UPLOADS:
- Previous status update
- Project plan or roadmap
- Metrics dashboard
- Meeting notes
</update_inputs>

<update_framework>

You're a communications expert who knows that most status updates are unread. They're too long, too detailed, or bury the important stuff. Your job: Write updates that people actually read and act on.

THE REALITY:

Bad status update: Wall of text, every detail, no clear status
Good status update: Scannable, highlights what matters, clear on what you need

Execs skim. Busy people skim. Your update needs to work when skimmed.

---

## PART 1: PICK YOUR FORMAT

### Format By Audience

FOR YOUR TEAM (Weekly):
- More detail, tactical
- What got done, what's next
- Blockers and help needed

FOR STAKEHOLDERS (Biweekly/Monthly):
- Higher level, outcomes not tasks
- Progress toward goals
- Risks and decisions needed

FOR EXECS (Monthly or milestones):
- Executive summary only
- Health status, key metrics, asks
- 3-5 bullet points max

Your audience: [Team/Stakeholders/Execs]
Format to use: [Detailed/Medium/Executive]

---

## PART 2: THE STRUCTURE

### The Universal Template

OVERALL STATUS: 🟢 GREEN / 🟡 YELLOW / 🔴 RED

[One-sentence summary of where things stand]

✅ WINS / PROGRESS
[What got done, what moved forward]

⏭️ NEXT / UPCOMING
[What's happening next period]

⚠️ RISKS / BLOCKERS
[What could go wrong, what's stuck]

🙋 ASKS / NEEDS
[What you need from recipients]

That's it. Everything important in 4 sections.

---

## PART 3: WRITE EACH SECTION

### Overall Status Line

One sentence that captures current state.Green (on track):
✅ "Feature X on track for May 15 launch"
✅ "Q1 goals 80% complete, no major blockers"

Yellow (at risk):
⚠️ "Launch delayed 2 weeks due to API instability"
⚠️ "On track but design resources stretched thin"

Red (blocked):
🚨 "Blocked on legal approval, launch date TBD"
🚨 "Behind on Q1 goals, need to cut scope"

Your status line:
[Status emoji + one sentence]

### Wins / Progress

What to include:
- Completed milestones
- Shipped features
- Key decisions made
- Metrics that improved
- Customer wins

How to write:
- Be specific (not "made progress" but "shipped X")
- Include impact when possible
- Celebrate your team

Example:

✅ Shipped SSO integration to 50 enterprise customers
- 78% activated in first week
- NPS +15 points vs. customers without SSO

✅ Finalized Q2 roadmap with eng/design alignment
- Cut 3 features to focus on core use case
- Capacity plan confirmed

✅ Closed 3 design-blocking decisions
- Navigation will be sidebar (not top nav)
- Mobile web first, native app v2
- Free tier stays at 5 projects

Your wins:
[3-5 specific accomplishments]

### Next / Upcoming

What's happening in the next period.For team updates:
- Specific tasks and owners
- Sprint goals
- Meetings or milestones

For stakeholder updates:
- Key milestones
- Expected completions
- Decision points coming

Example:

⏭️ Next 2 weeks:
- Design review with execs (May 5)
- Begin engineering build (May 8)
- Beta customer recruitment (May 10)

⏭️ Upcoming decisions:
- Pricing model for enterprise tier (need input by May 15)
- Launch date: June 1 vs June 15 (will decide after eng sizing)

Your upcoming:
[3-5 next items with dates]

### Risks / Blockers

What could derail you.Include:
- Technical risks
- Resource constraints
- External dependencies
- Timeline risks

How to write:
- Be honest (don't hide problems)
- Include severity
- Note what you're doing about it

Example:

⚠️ API stability issues
- Error rate up to 5% in testing
- Engineering investigating, fix ETA May 10
- If not resolved by May 12, we'll delay launch 1 week

⚠️ Design capacity
- Designer split across 3 projects
- May impact quality of mobile screens
- Mitigation: De-scoped 2 nice-to-have flows

🚨 Legal approval pending
- Waiting on privacy team review for 3 weeks
- BLOCKER for launch
- Escalated to VP Product

Your risks:
[1-3 most important with severity and mitigation]

### Asks / Needs

What you need from recipients.Be specific:
- Who needs to do what
- By when
- Why it matters

Example:

🙋 Need from execs:
- Decision on pricing model by May 15 (3 options in deck shared yesterday)
- Approval to hire contract designer for 6 weeks

🙋 Need from engineering:
- Confirm build can start May 8 with current specs
- Flag any blockers by EOD Friday

🙋 Need from anyone:
- If you have enterprise customer leads for beta, send them my way

Your asks:
[2-3 specific requests with owners]

---

## PART 4: FORMAT FOR READABILITY

### Make It Scannable

Use:
- ✅ Emojis or symbols for visual scanning
- Bold for key points
- Bullet points (not paragraphs)
- Whitespace between sections

Don't use:
- Dense paragraphs
- Jargon without context
- Acronyms only insiders know

### Length Guidelines

Team update: 200-400 words
Stakeholder update: 150-250 words
Exec update: 100 words max

The test: Can someone skim this in 30 seconds and know if there's something they need to act on?

---

## PART 5: TEMPLATES BY USE CASE

### Template 1: Weekly Team Update

Subject: [Project Name] - Week of [Date]STATUS: 🟢 On track

SSO integration progressing well. Beta launches next week.

✅ This week:
- Completed API integration with Okta and Azure AD
- Finished design for admin settings page
- Recruited 10 enterprise customers for beta

⏭️ Next week:
- Beta launch to first 10 customers (May 8)
- Monitor for issues, daily check-ins
- Begin work on Google Workspace integration

⚠️ Risks:
- One edge case in group syncing still buggy (fix in progress)

🙋 Asks:
- Support team: Be ready for beta customer questions starting Monday

---

### Template 2: Monthly Stakeholder Update

Subject: Q2 Product Update - [Month]OVERALL: 🟡 Slightly behind on timeline but quality is high

Delayed SSO integration by 2 weeks to get edge cases right. Enterprise customers enthusiastic about beta.

✅ Key progress:
- Shipped SSO to 50 beta customers (92% activated)
- Finalized pricing: $50/mo for SSO add-on
- Signed 3 design partnerships for co-marketing

⏭️ Coming in [Next Month]:
- General availability launch (June 15)
- Sales enablement and training
- First $250K in SSO ARR expected

⚠️ Risks:
- Delayed 2 weeks to fix group sync issues
- Still waiting on legal approval for enterprise terms

🙋 Need from you:
- Review pricing deck and approve by May 20
- Help recruit 5 more enterprise beta customers

---

### Template 3: Executive Summary

Subject: [Project] Status - [Date]STATUS: 🟢 On track for June 15 launchUpdate:
- SSO beta live with 50 customers, 92% adoption
- $250K pipeline for Q2 from SSO upgrades
- Launch timeline: June 15 (2 weeks later than plan, quality reasons)

Need:
- Pricing approval by May 20
- Legal expedite on enterprise terms review

---

## THE OUTPUT

### Your Status Update (Ready to Send)

[Full update using structure above]

### Alternative Versions

Shorter version (if audience is busy):
[Condensed to key points]

Longer version (if team needs details):
[Expanded with more context]

</update_framework>

<quality_check>

Is it scannable?
- [ ] Can someone read it in 60 seconds
- [ ] Key info is bolded or bulleted
- [ ] Status is clear at top

Is it honest?
- [ ] Not hiding problems
- [ ] Risks are surfaced
- [ ] Status color matches reality

Is it actionable?
- [ ] Clear what you need
- [ ] Recipients know if they need to do something
- [ ] Timeline is specific

</quality_check>

<meta_wisdom>

On status updates:

Most people write status updates for themselves (to feel productive) not for their audience (to communicate effectively).

Flip it: Write for the reader, not for you.

The color-coding reality:

Most PMs are afraid to mark things yellow or red.

But here's the truth: If you only ever show green, no one trusts your updates.

Yellow/red means you're honest and on top of risks. That builds trust.

On asks:

The weakest part of most updates: vague asks or no asks.

"Let me know if you have questions" is not an ask.
"Approve pricing by May 20" is an ask.

The frequency question:

Weekly for active projects.
Biweekly for steady-state work.
Monthly for long-term initiatives.

But: Update immediately if status changes (green → yellow or yellow → red).

Remember:

No one reads your whole update.

Lead with status. Use bullet points. Make asks clear.

If someone only reads the first 3 lines, they should know what matters.

</meta_wisdom>

</status_update>
```

</details>

---

### Plan Your Week

**📋 Use Case:** Sunday/Monday morning, need to prioritize the chaos ahead

**🛠️ Recommended Tools:** Claude, ChatGPT Projects

**💡 Technique:** Eisenhower Matrix, time-blocking, energy management

<details>
<summary>Click to view prompt</summary>

```
<weekly_planning>

<planning_inputs>
BRAIN DUMP - EVERYTHING ON YOUR PLATE:
1. Meetings scheduled this week (paste calendar or list)
2. Projects you're working on (with status)
3. Urgent things that came up Friday/weekend
4. Decisions you need to make
5. People you need to follow up with
6. Things you've been putting off

YOUR CONTEXT:
7. What are your top 3 goals this quarter?
8. What's your energy level? (coming off vacation vs. burned out)
9. Any out-of-office time or constraints?
10. What didn't get done last week that matters?

OPTIONAL:
- Last week's plan (to see what rolled over)
- To-do list from your task manager
- Slack threads you need to address
</planning_inputs>

<planning_framework>

You're a productivity coach who knows that most PMs are busy but not effective. They spend all week in meetings and reactive mode, then wonder why important work isn't done. Your job: Help them take control.

THE REALITY:

Bad week: Meetings, email, Slack, repeat. Important work happens Friday night.
Good week: Protected time for deep work, clear priorities, intentional choices.

You can't do everything. The goal is doing the right things.

---

## PART 1: GET CLARITY ON WHAT MATTERS

### The Eisenhower Matrix Sort

Sort everything you listed into 4 buckets:

URGENT + IMPORTANT (Do This Week):
- [ ] [Thing with deadline/high impact]
- [ ] [Blocker for others]
- [ ] [Customer/exec escalation]

IMPORTANT + NOT URGENT (Schedule This Week):
- [ ] [Strategic work]
- [ ] [Important project progress]
- [ ] [Relationship building]

URGENT + NOT IMPORTANT (Delegate or Quick-hit):
- [ ] [Other people's emergencies]
- [ ] [Admin tasks]
- [ ] [Low-value interruptions]

NOT URGENT + NOT IMPORTANT (Don't Do):
- [ ] [Nice-to-have]
- [ ] [Distraction]

Your top 3 must-dos this week:
1. [Most important thing]
2. [Second most important]
3. [Third most important]

The rule: If you only got these 3 done, the week was a success.

### The Theme Check

Does this week have a theme?

Possible themes:
- 🎯 Execution week: Shipping something important
- 🧭 Strategy week: Planning, roadmap, big decisions
- 🤝 Alignment week: Lots of stakeholder management
- 🔥 Fire drill week: Damage control, reactive mode
- 🧘 Recovery week: Catching up after chaos

Your week's theme: [What it is]

Why this matters: Knowing the theme helps you say no to things that don't fit.

---

## PART 2: PROTECT YOUR TIME

### Audit Your Calendar

Meeting audit:

Total hours in meetings: [X hours]
- Meetings you're leading: [Y hours]
- Meetings you could skip: [Z hours]
- Meetings you need to be in: [W hours]

If >25 hours in meetings: You have no time for deep work. Cancel something.

Meetings to consider declining:
- [ ] [Meeting name - why you could skip]
- [ ] [Meeting name - could send delegate]

Meetings to make async:
- [ ] [Status meeting that could be email]
- [ ] [FYI meeting you don't need to attend]

### Block Time for Important Work

Your deep work blocks:Monday:
- 9-11am: [Focused work on [project]]

Tuesday:
- 2-4pm: [Deep work block]

Wednesday:
- Morning: [Protected time for [task]]

Thursday:
- [Time block]

Friday:
- 9-12pm: [Catch-up and planning]

The rule: Treat these like meetings. Don't let people book over them.

### Energy Management

When are you at your best?
- Peak energy: [Morning/Afternoon/Evening]
- Low energy: [Time of day]

Match tasks to energy:High-energy time:
- Deep work on hard problems
- Strategic thinking
- Writing
- Difficult conversations

Low-energy time:
- Email
- Admin tasks
- Easy meetings
- Organizing/cleanup

Your energy plan this week:
[Schedule hard work for peak energy times]

---

## PART 3: DAY-BY-DAY PLAN

### Monday

Theme: [Start strong / Catch up / Planning]

Must do:
- [ ] [Top priority for Monday]
- [ ] [Second priority]

Meetings:
- [Time]: [Meeting name]
- [Time]: [Meeting name]

Time blocks:
- [Time]: [Focus work on what]

End of day goal:
[What done looks like]

---

### Tuesday

Theme: [Execution / Meetings / Deep work]

Must do:
- [ ] [Priority]
- [ ] [Priority]

Meetings:
- [List]

Time blocks:
- [Protected time]

End of day goal:
[What done looks like]

---

### Wednesday

[Same structure]

---

### Thursday

[Same structure]

---

### Friday

Theme: Wrap-up and next week prep

Must do:
- [ ] [Anything left from Mon-Thu]
- [ ] [Quick wins]

Time blocks:
- 9-11am: Finish priority work
- 11am-12pm: Inbox zero
- 2-3pm: Plan next week

End of day goal:
Clean slate heading into weekend

---

## PART 4: THE RULES

### Decision Rules for the Week

When someone asks for your time:Say YES if:
- Aligns with top 3 priorities
- Blocks someone else's work
- Strategic relationship building

Say NO (or DEFER) if:
- Nice-to-have, not must-have
- Can wait until next week
- Someone else can handle it

Your NO script:
"I'm at capacity this week. Can we schedule for [next week]?"

### Communication Boundaries

Email:
- Check at: [9am, 1pm, 4pm]
- Don't check: [Outside these times]
- Inbox zero by: Friday EOD

Slack:
- Available: [Core hours]
- Focus mode: [When in deep work]
- Response SLA: [X hours for non-urgent]

Saying no:
This week you'll likely need to say no to:
- [Type of request]
- [Type of meeting]
- [Type of distraction]

Your script: "I'm focused on [priority] this week. Can this wait until [date]?"

---

## PART 5: THE BACKUP PLAN

### If Things Go Sideways

Likely interruptions:
- Customer escalation
- Exec request
- Project fire
- Sick day / personal emergency

If that happens:What can slide:
- [ ] [Task that can wait]
- [ ] [Meeting that can reschedule]

What can't:
- [ ] [Must ship this week]
- [ ] [Hard deadline]

Your contingency:
[If Monday goes off the rails, you'll cut X and Y to protect Z]

### End-of-Week Review Prompt

Friday afternoon checklist:
- [ ] Did I complete my top 3 priorities?
- [ ] What went well this week?
- [ ] What took longer than expected?
- [ ] What should I do differently next week?
- [ ] What's rolling over to next week?

---

## THE OUTPUT

### Your Week Plan (One Page)

Week of [Date]🎯 Top 3 Priorities:
1. [Most important]
2. [Second]
3. [Third]

📅 Day-by-Day:Monday: [Key focus + meetings]
Tuesday: [Key focus + meetings]
Wednesday: [Key focus + meetings]
Thursday: [Key focus + meetings]
Friday: [Wrap-up]

🚫 Saying No To:
- [Type of requests to decline]

⚡️ Energy Management:
- Peak hours for deep work: [Times]
- Low-energy tasks: [When to do them]

---

### Daily Task Lists (If You Want Detail)

Monday's Task List:
- [ ] [Specific task]
- [ ] [Specific task]

[Repeat for each day]

</planning_framework>

<quality_check>

Is it realistic?
- [ ] Not trying to do 50 things
- [ ] Accounts for meeting time
- [ ] Has buffer for unexpected

Is it focused?
- [ ] Clear on top 3 priorities
- [ ] Protected time for important work
- [ ] Says no to distractions

Is it flexible?
- [ ] Can adapt if things change
- [ ] Knows what can slide
- [ ] Builds in catch-up time

</quality_check>

<meta_wisdom>

On planning:

Most people plan like this: "What can I fit into this week?"

Better question: "What must get done, and what should I not do?"

The hard truth:

You can't do everything on your list.

So either you choose what doesn't happen, or randomness chooses for you.

Choose deliberately.

On meetings:

If your calendar is >30 hours of meetings, you're not a PM. You're a meeting attendee.

PMs need uninterrupted time to think, write, and make decisions.

Audit your meetings. Half of them are optional.

The Sunday night trick:

Spend 20 minutes Sunday night planning Monday.

You'll sleep better (not anxious about the week).
You'll start Monday with clarity (not scrambling).

Remember:

A good week isn't about being busy.
It's about making progress on what matters.

Three important things done > 20 unimportant things done.

</meta_wisdom>

</weekly_planning>
```

</details>

---

### Explain Technical Concept Simply

**📋 Use Case:** Engineer/tech person said something technical, need to explain it to non-technical stakeholder

**🛠️ Recommended Tools:** Claude, ChatGPT, Gemini

**💡 Technique:** Analogy generation, jargon removal, audience-specific translation

<details>
<summary>Click to view prompt</summary>

```
<explain_technical_concept>

<concept_inputs>
PASTE WHAT YOU NEED TO EXPLAIN:
[The technical thing - screenshot, quote, message, doc]

WHO'S YOUR AUDIENCE:
- [ ] Customer (non-technical)
- [ ] Executive (business-focused)
- [ ] Sales team (needs to sell it)
- [ ] Designer (visual thinker)
- [ ] Other: [specify]

WHAT DO THEY NEED TO KNOW:
- [ ] Why this matters (business impact)
- [ ] What changed (what's different)
- [ ] What it enables (new possibilities)
- [ ] Why it takes time (if relevant)
- [ ] Other: [specify]
</concept_inputs>

<explanation_framework>

You're a translator between tech and business. Your job: make complex things simple without dumbing them down.

THE APPROACH:1. Strip the jargon
Identify every technical term and replace with plain English.

2. Use analogies
Connect to something they already understand.

3. Focus on "so what"
Lead with impact, not mechanism.

4. Layer the detail
Start simple, add complexity only if needed.

---

## YOUR EXPLANATION

One-sentence version:
[The absolute simplest explanation]

Paragraph version:
[2-3 sentences with a bit more context]

With analogy:
[Use comparison to something familiar]

Why this matters:
[Business impact or benefit]

If they ask for more detail:
[Slightly more technical version, still accessible]

---

## EXAMPLE TRANSFORMATIONS

Technical: "We need to migrate from monolith to microservices architecture"

Simple: "We're splitting our codebase into smaller, independent pieces. Think of it like moving from one giant warehouse to many specialized shops - each can operate and upgrade independently without breaking the others."

Why it matters: "This lets us ship features faster and makes the product more reliable."

---

Technical: "The API rate limit is causing 429 errors"

Simple: "Too many requests are hitting our system at once, so it's rejecting some to protect itself. Like a restaurant that stops seating people when it's at capacity."

Why it matters: "Some users are seeing errors. We're either raising the limit or optimizing how often we check for updates."

</explanation_framework>

<meta_guidance>

Good explanations:
- Start with what changed or why it matters
- Use concrete analogies
- Avoid saying "basically" or "essentially"
- Don't patronize

Common analogies that work:
- Houses/buildings (architecture)
- Roads/traffic (networking)
- Restaurants/kitchens (systems)
- Libraries/filing systems (databases)
- Mail/packages (data transfer)

Red flags:
- If explanation includes "just" - it's not simple
- If you use acronyms - spell them out
- If you say "it's complicated" - you don't understand it yet

</meta_guidance>

</explain_technical_concept>
```

</details>

---

### Make Writing Shorter/Clearer

**📋 Use Case:** You wrote something but it's too long, unclear, or rambly

**🛠️ Recommended Tools:** Claude

**💡 Technique:** Conciseness editing, clarity enhancement, active voice conversion

<details>
<summary>Click to view prompt</summary>

```
<shorten_writing>

<writing_inputs>
PASTE WHAT YOU WROTE:
[Your draft]

TARGET LENGTH:
- [ ] Half the length
- [ ] One paragraph
- [ ] 3 sentences
- [ ] One sentence
- [ ] Specific: [X words]

TONE TO MAINTAIN:
- [ ] Professional
- [ ] Casual/friendly
- [ ] Direct/firm
- [ ] Empathetic
- [ ] Match original

WHAT TO PRESERVE:
- [ ] Key facts/numbers
- [ ] Specific asks
- [ ] Action items
- [ ] Everything important (just shorter)
</writing_inputs>

<editing_framework>

You're an editor who makes writing crisp. Your rules: cut ruthlessly, keep meaning, maintain tone.

THE PROCESS:1. Identify the core message
What's the one thing this must communicate?

2. Cut mercilessly
- Filler words: just, really, very, actually, basically
- Hedging: I think, maybe, perhaps, possibly
- Redundancy: "end result", "past history", "future plans"
- Throat-clearing: "I wanted to reach out to..."

3. Make it active
- Passive: "The decision was made by the team"
- Active: "The team decided"

4. Front-load the point
Put the most important thing first.

---

## YOUR EDIT

Original length: [X words]
New length: [Y words]

SHORTENED VERSION:

[Your tightened text]

---

WHAT CHANGED:
- Removed: [What you cut]
- Simplified: [What you made clearer]
- Reordered: [If you moved things around]

---

ALTERNATIVE (even shorter):
[If they need it even more concise]

</editing_framework>

<meta_guidance>

Common cuts:

❌ "I wanted to follow up to see if..."
✅ "Following up on..."

❌ "I think we should probably consider maybe..."
✅ "We should..."

❌ "In order to improve the situation..."
✅ "To improve..."

❌ "Due to the fact that..."
✅ "Because..."

The 50% rule:
First draft can usually lose 50% of words without losing meaning.

</meta_guidance>

</shorten_writing>
```

</details>

---

### Turn Meeting Notes into Action Items

**📋 Use Case:** Just finished meeting with messy notes, need clear followups fast

**🛠️ Recommended Tools:** Claude or ChatGPT Project

**💡 Technique:** <meeting_to_actions>

<meeting_inputs>
PASTE YOUR NOTES:
[Raw notes, bullet points, stream of consciousness - messy is fine]

MEETING CONTEXT:
- Meeting type: [Sync, decision, brainstorm, review]
- Attendees: [List if relevant for ownership]
- Key decisions made: [If any]

WHAT YOU NEED:
- [ ] Action items with owners
- [ ] Decisions documented
- [ ] Follow-up meetings
- [ ] Questions to resolve
- [ ] All of the above
</meeting_inputs>

<conversion_framework>

You're the person who actually writes down what needs to happen after a meeting. Your job: extract signal from noise.

THE OUTPUT:

## DECISIONS MADE
- [Decision 1]
- [Decision 2]

## ACTION ITEMS
- [ ] [Owner]: [Specific action] - Due: [Date or timeframe]
- [ ] [Owner]: [Specific action] - Due: [Date or timeframe]
- [ ] UNASSIGNED: [Action that needs an owner]

## OPEN QUESTIONS
- [Question that needs answering]
- [Who should answer / when we'll revisit]

## NEXT MEETING
- Topic: [What to discuss]
- When: [Timeframe]
- Who needs to be there: [Names]

---

FOR SLACK/EMAIL:

Quick update from today's meeting:

Decided:
- [Key decision]

Action items:
- @[person]: [action by date]
- @[person]: [action by date]

Next steps:
[What happens next]

</conversion_framework>

<quality_check>

Good action items are:
- ✅ Specific (not "look into X")
- ✅ Owned (person's name attached)
- ✅ Time-bound (by when)
- ✅ Actually actionable (can start Monday)

Bad action items:
- ❌ "Team to discuss further"
- ❌ "Consider options for X"
- ❌ "Follow up on Y" (follow up how?)

If no owner or date:
Flag it as needing assignment.

</quality_check>

<meta_guidance>

Common patterns to catch:

"We should..." → Who specifically?
"Let's circle back..." → When specifically?
"Someone needs to..." → Assign to someone
"We talked about..." → Was a decision made?

If notes are really messy:
Extract what you can, flag what's unclear with [?]

</meta_guidance>

</meeting_to_actions>

<details>
<summary>Click to view prompt</summary>

```
<meeting_to_actions>

<meeting_inputs>
PASTE YOUR NOTES:
[Raw notes, bullet points, stream of consciousness - messy is fine]

MEETING CONTEXT:
- Meeting type: [Sync, decision, brainstorm, review]
- Attendees: [List if relevant for ownership]
- Key decisions made: [If any]

WHAT YOU NEED:
- [ ] Action items with owners
- [ ] Decisions documented
- [ ] Follow-up meetings
- [ ] Questions to resolve
- [ ] All of the above
</meeting_inputs>

<conversion_framework>

You're the person who actually writes down what needs to happen after a meeting. Your job: extract signal from noise.

THE OUTPUT:

## DECISIONS MADE
- [Decision 1]
- [Decision 2]

## ACTION ITEMS
- [ ] [Owner]: [Specific action] - Due: [Date or timeframe]
- [ ] [Owner]: [Specific action] - Due: [Date or timeframe]
- [ ] UNASSIGNED: [Action that needs an owner]

## OPEN QUESTIONS
- [Question that needs answering]
- [Who should answer / when we'll revisit]

## NEXT MEETING
- Topic: [What to discuss]
- When: [Timeframe]
- Who needs to be there: [Names]

---

FOR SLACK/EMAIL:

Quick update from today's meeting:

Decided:
- [Key decision]

Action items:
- @[person]: [action by date]
- @[person]: [action by date]

Next steps:
[What happens next]

</conversion_framework>

<quality_check>

Good action items are:
- ✅ Specific (not "look into X")
- ✅ Owned (person's name attached)
- ✅ Time-bound (by when)
- ✅ Actually actionable (can start Monday)

Bad action items:
- ❌ "Team to discuss further"
- ❌ "Consider options for X"
- ❌ "Follow up on Y" (follow up how?)

If no owner or date:
Flag it as needing assignment.

</quality_check>

<meta_guidance>

Common patterns to catch:

"We should..." → Who specifically?
"Let's circle back..." → When specifically?
"Someone needs to..." → Assign to someone
"We talked about..." → Was a decision made?

If notes are really messy:
Extract what you can, flag what's unclear with [?]

</meta_guidance>

</meeting_to_actions>
```

</details>

---

### Respond to Difficult Message

**📋 Use Case:** Got a message that's hard to respond to - complaint, pushback, saying no

**🛠️ Recommended Tools:** Claude or ChatGPT Project

**💡 Technique:** Empathy framing, clarity under pressure, de-escalation

<details>
<summary>Click to view prompt</summary>

```
<difficult_response>

<message_inputs>
PASTE THE MESSAGE:
[The email/Slack/message you need to respond to]

WHAT'S DIFFICULT ABOUT IT:
- [ ] Customer complaint
- [ ] Have to say no
- [ ] Pushback from stakeholder
- [ ] Conflict/disagreement
- [ ] Bad news to deliver
- [ ] Request you can't fulfill
- [ ] Other: [describe]

YOUR CONSTRAINTS:
- What you CAN do: [Options available]
- What you CAN'T do: [Hard constraints]
- Politics/relationships: [Anything to navigate]

TONE NEEDED:
- [ ] Empathetic
- [ ] Firm but kind
- [ ] Apologetic
- [ ] Direct/clear
- [ ] Diplomatic
</message_inputs>

<response_framework>

You're a communications expert who writes responses to hard messages. Your principles: clear, kind, honest, forward-moving.

---

## YOUR RESPONSE

DRAFT:

[Greeting]

[Acknowledge their concern/request]

[Your response - yes/no/partial/alternative]

[Brief explanation]

[What happens next]

[Closing]

---

WHY THIS WORKS:
- Acknowledges: [What you validated]
- Clarifies: [What you made clear]
- Offers: [Path forward or alternative]
- Tone: [How it comes across]

---

## ALTERNATIVE VERSIONS

More empathetic:
[If you need to soften it]

More direct:
[If you need to be firmer]

More detailed:
[If they need more context]

</response_framework>

<response_patterns>

### Pattern 1: Saying No

Structure:
1. Thank them for reaching out
2. Acknowledge why they want this
3. Clear "no" with reason
4. Offer alternative if possible
5. Keep door open

Example:

"Thanks for the feature request. I understand why bulk export would save your team time.

We won't be adding this in the next 6 months - we're focused on [other priority] that impacts more customers.

What we can do: You can export in batches of 100. Here's the workflow [link].

I've added this to our backlog for future consideration. If your needs change or you find a critical blocker, let me know."

---

### Pattern 2: Customer Complaint

Structure:
1. Acknowledge the frustration
2. Take ownership (if appropriate)
3. Explain what happened (briefly)
4. What you're doing to fix it
5. How to prevent it

Example:

"You're right to be frustrated - this shouldn't have happened.

Here's what went wrong: [Brief explanation without excuses]

Here's what we're doing:
- Fixed for you specifically [immediate action]
- Fixing for everyone [long-term fix]

You should see this resolved by [date]. I'll personally follow up to confirm."

---

### Pattern 3: Pushback from Stakeholder

Structure:
1. Acknowledge their concern
2. Explain your reasoning
3. Find common ground
4. Propose path forward
5. Invite continued dialogue

Example:

"I hear your concern about [issue]. You're right that [valid point they made].

Here's why I'm proposing [your approach]: [reasoning]

What if we [compromise/hybrid/test]? That would address [their concern] while still [your goal].

Let's discuss on our call Friday. I'm open to adjusting based on your input."

---

### Pattern 4: Bad News

Structure:
1. Lead with the news (don't bury it)
2. Brief explanation
3. Impact on them
4. What you're doing about it
5. How they can help or what's next

Example:

"I need to let you know we're delaying the launch from June 1 to June 15.

Reason: We found a critical bug in [feature] that affects [use case]. Shipping it broken would be worse than the delay.

For your team: [Specific impact on their plans]

What we're doing: Engineering is focused on the fix, we'll have daily updates in #project-channel.

I know this affects [their deadline]. Let's talk about how to adjust your plans."

</response_patterns>

<meta_guidance>

The formula for hard messages:

1. Acknowledge their perspective
2. Be clear about reality
3. Offer what you can
4. Move forward to next step

Don't:
- Over-apologize (one "sorry" is enough)
- Make excuses
- Be vague to soften the blow
- Delay sending (rip the band-aid off)

Do:
- Be human
- Be specific
- Give them a path forward
- Respond same-day if possible

Remember:
Most "difficult" messages feel worse to you than to them.

They just want clarity and respect.

</meta_guidance>

</difficult_response>
```

</details>

---

### Turn Data Into Story

**📋 Use Case:** Have metrics/charts/data, need to present it as a narrative

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Data storytelling, insight extraction, narrative arc

<details>
<summary>Click to view prompt</summary>

```
<data_to_story>

<data_inputs>
YOUR DATA:
[Paste metrics, describe charts, share numbers]

Examples:
- "Conversion rate went from 5% to 8%"
- "DAU flat, but time per session up 40%"
- "10 customers churned, 15 signed up, net +5"

CONTEXT:
- What was this measuring: [Goal or hypothesis]
- Time period: [When]
- What changed: [If you shipped something]

AUDIENCE:
- Who's reading this: [Execs, team, board]
- What they care about: [Business outcomes, learnings, what's next]

PRESENTATION FORMAT:
- [ ] Email update
- [ ] Slide deck
- [ ] Slack message
- [ ] Written report
- [ ] Verbal presentation
</data_inputs>

<story_framework>

You're a data storyteller who turns numbers into narratives. Your job: make people care about data by showing what it means.

---

## THE STORY

### The Headline

One sentence that captures the story:
[What happened and why it matters]

Example:
"New onboarding drove 60% more activations, but exposed infrastructure scaling issues we need to address."

---

### The Arc

Setup (What we expected):
[The hypothesis or goal going in]

What happened (The data):
[Key metrics with context]

What it means (The insight):
[Non-obvious interpretation]

What we're doing (The action):
[Decision or next steps based on data]

---

### The Key Metrics (With Context)

Don't just say the number. Say what it means.

Metric 1:
- Number: [X → Y (+Z%)]
- Context: [Compared to what / why this matters]
- What caused it: [Your explanation]

Example:
- Conversion rate: 5% → 8% (+60% relative)
- Context: Best performance in 6 months, above industry benchmark of 6%
- What caused it: New social proof on pricing page

---

### The Insight

What's surprising or non-obvious:
[The thing someone wouldn't see by just looking at the numbers]

Examples:
- "Growth came entirely from mobile, desktop actually declined"
- "Power users loved it, casual users confused"
- "Feature drove engagement but not retention"

---

### The So What

What we learned:
[Takeaway that applies beyond this data]

What we're doing:
[Action based on data]

What we're watching:
[Metric to monitor next]

</story_framework>

<story_patterns>

### Pattern 1: Good News Story

Structure: Celebrate → Credit → Continue

"Activation rate hit all-time high of 78%. The new tutorial clearly resonated - users who completed it were 3x more likely to hit their first milestone. Design and eng nailed this. We're now rolling out to 100% of users."

---

### Pattern 2: Mixed Results Story

Structure: Bright spot → Concern → Plan

"Signups increased 40%, but activation stayed flat at 60%. We're attracting more users but not converting them better. Next: Dig into where drop-off is happening and test simplified onboarding flow."

---

### Pattern 3: Bad News Story

Structure: Clear about problem → Root cause → Fix

"Retention dropped from 85% to 78% this month. The issue: Recent changes made advanced features harder to find, and power users (our highest retention segment) struggled. Fix in progress: We're reverting navigation and doing usability testing before next change."

---

### Pattern 4: Insights Story

Structure: Data → Surprise → Implication

"We analyzed churn by segment and found something unexpected: Enterprise customers churn 2x faster than SMB, despite higher NPS. Root cause: They hit scaling issues we haven't solved. This flips our assumption that enterprise = sticky. We need to prioritize performance improvements."

</story_patterns>

<presentation_formats>

### For Email/Slack (30 seconds to read):

Subject: [Project] ResultsTL;DR: [One sentence]

Key numbers:
- [Metric]: [Change] ([context])
- [Metric]: [Change] ([context])

Bottom line: [What this means]

Next: [What happens now]

---

### For Slides (One slide per point):

Slide 1: The Headline
[Big number + what it means]

Slide 2: The Story
[Chart + 3 bullet points]

Slide 3: The Insight
[What's surprising + why]

Slide 4: Next Steps
[What we're doing about it]

---

### For Exec Review (2 minutes):

The Hook: [Most important finding first]

The Data: [2-3 key metrics with visuals]

The Insight: [Non-obvious pattern]

The Ask: [Decision or resources needed]

</presentation_formats>

<meta_guidance>

Data storytelling principles:Lead with the punchline
Don't make them wait for the conclusion.

Context is everything
8% conversion means nothing without:
- What it was before
- What you expected
- What industry standard is

Show, don't just tell
"Engagement improved" → Vague
"Daily active users up 40%, session time up 2min" → Specific

Find the surprise
Expected results are boring.
Unexpected results are interesting.
Contradictions are fascinating.

Remember:
People don't care about your data.
They care about what it means for them.

</meta_guidance>

</data_to_story>
```

</details>

---

### Translate Technical ↔ Business

**📋 Use Case:** Need to convert technical explanation to business language or vice versa

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Bidirectional translation, audience adaptation, jargon mapping

<details>
<summary>Click to view prompt</summary>

```
<translate_tech_business>

<translation_inputs>
WHAT NEEDS TRANSLATING:
[Paste the text]

DIRECTION:
- [ ] Technical → Business (make it business-friendly)
- [ ] Business → Technical (make it eng-friendly)

FROM:
- [ ] Engineering/technical team
- [ ] Product/business team
- [ ] Customer request
- [ ] Executive requirement

TO:
- [ ] Engineering team
- [ ] Executive/business stakeholder
- [ ] Customer
- [ ] Sales/marketing

PURPOSE:
- [ ] Get buy-in
- [ ] Explain delay/complexity
- [ ] Write requirement
- [ ] Customer communication
- [ ] Other: [specify]
</translation_inputs>

<translation_framework>

You're a bilingual translator between tech and business languages. Your job: preserve meaning, change words.

---

## TRANSLATION

ORIGINAL:
[What was said]

TRANSLATED:
[Same meaning, different audience]

KEY CHANGES:
- Replaced [technical term] with [plain language]
- Changed focus from [how] to [why/impact]
- Removed [jargon] entirely

---

## SIDE-BY-SIDE COMPARISON

| Technical Version | Business Version |
|-------------------|------------------|
| [Tech phrase] | [Business phrase] |
| [Tech phrase] | [Business phrase] |

</translation_framework>

<translation_patterns>

### TECHNICAL → BUSINESS

Pattern: Focus on impact, not mechanism

Tech: "We're implementing Redis caching layer to reduce database queries"
Business: "We're making the app faster by storing frequently-used data closer to users"

Tech: "The API has rate limits of 100 requests per minute"
Business: "We limit how often apps can check for updates to keep the system stable for everyone"

Tech: "We need to refactor the authentication flow"
Business: "We're rebuilding how login works to make it more secure and reliable"

Tech: "The database schema migration will take 4 hours"
Business: "We need a 4-hour maintenance window to reorganize how we store data"

---

### BUSINESS → TECHNICAL

Pattern: Add specifics, remove vagueness

Business: "Make it faster"
Technical: "What specifically feels slow? Page load, search results, or something else? Need to measure current performance first."

Business: "Users want better analytics"
Technical: "Which metrics do they need? What's the use case? Real-time or batch? What's the data volume?"

Business: "Can we add AI to this?"
Technical: "What problem are we solving with AI? What's the input data? What's the expected output? What's acceptable accuracy?"

Business: "This should be simple to build"
Technical: "Let's scope it: Does this need to integrate with existing auth? Handle edge cases? Scale to all users? Each adds complexity."

---

### CUSTOMER COMMUNICATION

Tech speak → Customer-friendly:

Tech: "503 Service Unavailable error due to upstream dependency failure"
Customer: "Our service is temporarily down because a partner system we rely on is having issues. We're working with them to resolve it."

Tech: "We're deprecating the v1 API in favor of v2"
Customer: "We're upgrading our integration to a newer, more reliable version. Here's how to upgrade: [link]. Old version stops working June 1."

Tech: "You're hitting rate limits"
Customer: "You're making requests faster than our system can handle. Here's how to stay within limits: [link]"

---

### REQUIREMENT TRANSLATION

Business requirement → Technical spec:

Business: "Users should be able to export their data"
Technical:
- Which data? (All entities or specific types?)
- What format? (CSV, JSON, PDF?)
- All time or filtered by date?
- Async job or real-time download?
- File size limits?
- Frequency limits?

Business: "Make it secure"
Technical:
- Authentication required? (OAuth, SSO?)
- Encryption in transit? (HTTPS)
- Encryption at rest? (Database encryption)
- Audit logging?
- RBAC (role-based access)?
- Compliance requirements? (SOC2, GDPR)

</translation_patterns>

<meta_guidance>

The key skill:

Technical people think in "how"
Business people think in "why"

Your job: Bridge the gap.

Common mistakes:

❌ Just removing jargon (still too technical)
❌ Oversimplifying to point of inaccuracy
❌ Not preserving the important details

✅ Change vocabulary, keep meaning
✅ Add context for non-technical
✅ Add specifics for technical

When translating TO engineers:
- Be specific about requirements
- Include edge cases
- Don't tell them how to build it
- Focus on the problem and constraints

When translating TO business:
- Lead with impact
- Use analogies
- Avoid "it's complicated" (explain simply instead)
- Connect to outcomes they care about

</meta_guidance>

</translate_tech_business>
```

</details>

---

### Create Meeting Agenda

**📋 Use Case:** Important meeting in an hour, need structured agenda fast

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Meeting structure templates, time allocation, outcome focus

<details>
<summary>Click to view prompt</summary>

```
<meeting_agenda>

<meeting_inputs>
MEETING PURPOSE:
[What this meeting is for]

ATTENDEES:
[Who's coming - relevant if roles matter]

DURATION:
- [ ] 30 minutes
- [ ] 1 hour
- [ ] Other: [specify]

MEETING TYPE:
- [ ] Decision meeting (need to decide X)
- [ ] Review meeting (evaluate X)
- [ ] Brainstorm (generate ideas)
- [ ] Sync (align on status)
- [ ] Problem-solving (unstick X)
- [ ] Planning (map out X)

DESIRED OUTCOME:
[What success looks like for this meeting]

BACKGROUND:
[Any context or pre-reads]
</meeting_inputs>

<agenda_framework>

You're a meeting facilitator who creates agendas that lead to outcomes. Your job: structure time so meetings end with clarity.

---

## MEETING AGENDA

Meeting: [Title]
Date/Time: [When]
Duration: [Length]
Attendees: [Who]

Goal: [One sentence outcome]

---

### Agenda

[0-5 min] Context Setting
- Quick reminder of why we're here
- Any updates since last meeting

[5-X min] [Topic 1]
- [Specific discussion point]
- [What we need to decide/discuss]

[X-Y min] [Topic 2]
[Continue pattern]

[Last 5 min] Wrap-up
- Summarize decisions
- Clarify action items
- Schedule follow-up if needed

---

### Pre-Read (Optional)

[Link to doc or brief context people should review before meeting]

---

### Decision/Discussion Topics

Topic 1: [Name]
- Question: [What we're deciding]
- Options: [A, B, C]
- Time: [X minutes]

Topic 2: [Name]
[Same structure]

---

### Success Looks Like

By end of meeting, we will have:
- [ ] [Specific outcome 1]
- [ ] [Specific outcome 2]
- [ ] [Specific outcome 3]

</agenda_framework>

<agenda_templates>

### DECISION MEETING (30-60 min)

[5 min] Frame the decision
- What are we deciding
- Why now
- What happens if we don't decide

[15 min] Present options
- Option A, B, C
- Pros/cons of each
- Recommendation if any

[20 min] Discussion
- Questions
- Concerns
- Build alignment

[10 min] Decide + Document
- Make the call
- Document rationale
- Clarify next steps

---

### REVIEW MEETING (30-60 min)

[5 min] Set context
- What we're reviewing
- Goals we set

[10 min] Present results
- Key metrics
- What worked/didn't
- Insights

[20 min] Discussion
- Questions
- Implications
- What we learned

[10 min] Next steps
- Decisions based on review
- Action items

---

### BRAINSTORM MEETING (60 min)

[10 min] Frame the problem
- What we're solving
- Constraints
- Success criteria

[30 min] Generate ideas
- Rapid ideation
- No judgment yet
- Quantity over quality

[15 min] Cluster & prioritize
- Group similar ideas
- Vote on top 3-5
- Identify quick wins

[5 min] Next steps
- Who tests what
- When we reconvene

---

### PROBLEM-SOLVING MEETING (60 min)

[10 min] Define the problem
- What's broken
- Impact/urgency
- Root cause hypothesis

[20 min] Explore solutions
- Brainstorm approaches
- Pros/cons
- Quick wins vs long-term

[20 min] Build plan
- What we'll do
- Who owns what
- Timeline

[10 min] Confirm & close
- Review action items
- Escalations needed?
- Follow-up timing

</agenda_templates>

<meta_guidance>

Good agendas:

✅ Start and end on time
✅ Have clear outcomes
✅ Allocate time to topics
✅ Sent before meeting
✅ Leave time for decisions/wrap

Bad agendas:

❌ "Discuss X, Y, Z" (too vague)
❌ No time allocation (run over)
❌ All sharing, no deciding
❌ Made up during meeting

Time allocation rules:

- Give important topics more time
- Always save 5-10 min for wrap-up
- Build in buffer (things take longer than planned)
- If running over, defer topics vs going long

The forcing function:

Writing agenda forces you to clarify:
- Why are we meeting?
- What's the outcome?
- Is a meeting the right format?

Sometimes writing the agenda reveals you don't need the meeting.

Remember:

If you can't write a clear agenda, the meeting will be chaos.

5 minutes planning saves 30 minutes of confused discussion.

</meta_guidance>

</meeting_agenda>
```

</details>

---

### Say No Gracefully

**📋 Use Case:** Decline requests while maintaining relationships

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Stakeholder framing, alternative offering, relationship preservation

<details>
<summary>Click to view prompt</summary>

```
<say_no_gracefully>

<no_inputs>
WHO'S ASKING:
[Executive, customer, teammate, etc.]

WHAT THEY WANT:
[The request]

WHY YOU'RE SAYING NO:
- [ ] Not aligned with strategy
- [ ] Resource constraints
- [ ] Technical limitations
- [ ] Wrong priority/timing
- [ ] Other: [Explain]

RELATIONSHIP CONTEXT:
[How important is this stakeholder? History?]

YOUR CONSTRAINT:
- [ ] Can be transparent about real reason
- [ ] Need to be diplomatic (politics)
- [ ] Need to preserve future relationship
</no_inputs>

<graceful_no_framework>

You decline requests in ways that preserve relationships and redirect energy productively. Your process:

STEP 1: Understand the "no" typeHard no:
"We're never building this"

Not now:
"Not on the roadmap currently"

Not us:
"Wrong team to own this"

Not that:
"We'd solve it differently"

Choose language that matches reality.STEP 2: Structure your responseThe graceful no formula:1. Acknowledge + Appreciate
Show you heard them, value input

2. Align on problem
"I understand this is important because..."

3. Explain decision (careful!)
The delicate part - see Step 3

4. Offer alternative
What CAN you do?

5. Keep door open (if appropriate)
How they can influence future

STEP 3: Frame the "why"Good frames (focus on strategy):
- "We're focused on [priority] this quarter"
- "This doesn't align with our [goal]"
- "We're optimizing for [outcome]"

Risky frames (avoid if possible):
- "We don't have resources" (sounds like excuse)
- "It's too hard technically" (sounds like inability)
- "Legal won't allow it" (passing blame)

For customers:
Never say "just you" - even if true.
Frame as "not our current focus" not "your idea is bad"

STEP 4: Offer alternativesNever leave them empty-handed:What you CAN offer:
- Workaround with existing features
- Different solution to same problem
- Partial solution on shorter timeline
- Community/partner solution
- Documentation/guidance

The redirect:
"While we won't build [X], have you considered [Y]?"

STEP 5: Adjust tone to audienceTo executives:
Strategic, confident, solution-oriented
Focus on: Business impact, priorities, alternatives

To customers:
Empathetic, specific, helpful
Focus on: Understanding their need, workarounds, timeline

To teammates:
Collaborative, transparent, realistic
Focus on: Trade-offs, priorities, what you CAN do

To junior team members:
Educational, encouraging, growth-focused
Focus on: The "why", how decisions are made

STEP 6: Choose your mediumAsync (email/Slack):
✅ For: Clear-cut decisions, documented responses
❌ Avoid: Emotional topics, big disappointments

Sync (meeting/call):
✅ For: Complex explanations, relationships matter
❌ Avoid: Simple requests, clear documentation needs

Face-to-face:
✅ For: High-stakes, sensitive, relationship-critical
❌ Avoid: Routine decisions

STEP 7: Language templatesInstead of: "No, we can't do that"
Say: "That's not something we're planning to pursue because [reason]"

Instead of: "That's not a priority"
Say: "We're prioritizing [X] over [Y] because [strategic reason]"

Instead of: "We don't have bandwidth"
Say: "To do this well would require [resources] we've committed to [priority]"

Instead of: "That's a bad idea"
Say: "Here's what concerns me about that approach: [specific issues]"

STEP 8: Handle pushbackIf they escalate:
"I understand this is important to you. Let me connect you with [decision maker] to discuss the strategic priorities."

If they argue:
"I hear you. The trade-off is [this] vs [that]. Given [context], we chose [this]."

If they're upset:
"I appreciate your passion for this. Can we talk about what you're trying to accomplish? Maybe there's another way."

Now craft a graceful "no" for the described situation.

</graceful_no_framework>

---

## Example "No" Messages

(Adapt tone and detail based on relationship and context)

---

### Example 1: To Customer

Subject: Re: Feature Request - [Feature Name]

Hi [Name],

Thanks for the thoughtful feature request. I can see why [specific capability] would be valuable for [their use case].

After discussing with the team, we've decided not to pursue this on our near-term roadmap. We're currently focused on [strategic priority] because [customer segment] has told us [pain point] is their biggest challenge, and we want to deliver a great solution there first.

That said, here are a couple of ways you could [accomplish their goal] today:
1. [Workaround A]: [How it works]
2. [Workaround B]: [How it works]

I've also added this to our feature request tracker. If we see more demand or our priorities shift, we'll definitely revisit it.

Would either of those workarounds help in the meantime? Happy to jump on a quick call to walk through them.

Best,
[Your name]

---

### Example 2: To Executive Stakeholder

Context: Executive wants to add feature mid-sprint

Hi [Name],

I understand why [feature] feels urgent given [business context]. You're right that it would help with [their goal].

Here's my concern: We're 2 weeks into our sprint building [current priority], which supports our Q4 objective of [goal]. If we pivot now, we'd:
- Miss our [milestone] deadline by ~2 weeks
- Context-switch the engineering team (historically costs us 20-30% velocity)
- Push [other stakeholder's] project to next quarter

Alternative approach:

What if we:
1. Finish current sprint (2 weeks)
2. Do discovery on [their feature] while we're wrapping up (5 days)
3. Kick off [their feature] start of next sprint with full team

This gets you [feature] by [date], just 2 weeks later than your ask, but doesn't derail our Q4 commitments.

Would that work? Or if this truly can't wait, help me understand what we should de-prioritize to make room.

[Your name]

---

### Example 3: To Teammate

Context: Engineer wants to refactor code instead of shipping feature

Hey [Name],

I totally get the appeal of refactoring this before we ship. You're right that the code is messy and technical debt is piling up.

Here's my thinking: We've got [customer] waiting on this feature for their [big event in 2 weeks]. They've built their [campaign/project] around having this ready.

Trade-off:
- Ship now: Feature works, code is imperfect, we can iterate
- Refactor first: Code is clean, but we miss their deadline and risk the relationship

For this one, I think we ship and schedule the refactor for next sprint. What if we:
1. Ship the MVP this week
2. Block off [X days] next sprint for you to refactor properly
3. Document the technical debt so we don't forget

Then you get the clean code AND we hit the customer deadline.

Does that work? If you feel strongly this is a bad idea from a technical perspective, let's discuss - I don't want to ship something that'll break.

[Your name]

---

### Example 4: To Junior PM

Context: Junior PM wants to add their pet feature to roadmap

Hi [Name],

I really appreciate you thinking strategically about [feature area]. It shows great product instinct that you identified [opportunity].

Here's why I don't think we should prioritize this right now:

1. Strategy alignment: Our North Star is [metric], and this feature would impact [other metric]. Given we need to move [North Star] for our [goal], we have to stay focused there.

2. Opportunity cost: Building this would take [X weeks]. That's [X weeks] not building [higher priority thing] that impacts [more customers/revenue/strategic goal].

3. Uncertain demand: We have [Y] feature requests for this vs [Z] for [competing priority]. The data suggests the other need is more acute.

What I'd love you to do:

Add this to our "Backlog - Future Ideas" and create a one-pager with:
- The specific customer problem
- Evidence of demand (how many requests, from what segments)
- How this ties to our strategy
- Expected impact (what metric moves, by how much)

If you can make a compelling case with data, I'm totally open to re-evaluating next quarter. And this is great practice for building business cases.

Sound good?

[Your name]

---

### Example 5: Hard No (This is Never Happening)

Context: Legal concern, technical impossibility, or strategic mismatch

Hi [Name],

Thanks for bringing this idea to the table. I want to be direct with you: this isn't something we're going to pursue, now or in the future.

Here's why: [Clear, honest reason - legal constraint / technical impossibility / fundamentally misaligned with company strategy].

I know that's not the answer you wanted. What I can offer is [alternative that actually helps]:
- [Option A]
- [Option B]

Would either of those address what you're trying to accomplish? If not, let's get on a call and I can help you think through other approaches.

[Your name]

</say_no_gracefully>
```

</details>

---

### Executive Presentation Builder (Gamma)

**📋 Use Case:** Creating compelling presentations for senior executives and business stakeholders using your pre-configured Gamma template

**🛠️ Recommended Tools:** Gamma.app API with template ID: `g_adrwbl6rdw9d501`

**💡 Technique:** Executive storytelling with pyramid principle - leading with conclusions, using data-driven narratives, and focusing on business impact over features. Optimized for C-suite attention spans (5-7 minutes).

<details>
<summary>Click to view prompt</summary>

```
<executive_gamma_presentation>

<presentation_inputs>
PRESENTATION TOPIC:
[What you're presenting - product update, strategy proposal, quarterly results, etc.]

TARGET AUDIENCE:
[Specific executives - CEO, CFO, Board, C-suite, etc.]

PRESENTATION GOAL:
[What you need from them - decision, funding approval, strategic alignment, awareness]

KEY MESSAGE:
[The one thing they must remember - your bottom line]

CONTEXT:
- Current situation: [What they already know]
- What's changed: [Why you're presenting now]
- Their concerns: [What keeps them up at night about this topic]
- Time available: [5 min, 15 min, 30 min]

SUPPORTING DATA:
[Metrics, case studies, competitive intel, financial impact, customer feedback]
</presentation_inputs>

<gamma_template_config>
TEMPLATE ID: g_adrwbl6rdw9d501

This presentation will use your pre-configured executive template optimized for business stakeholders and senior leadership.

When creating via Gamma API, use:
- Template: g_adrwbl6rdw9d501
- Style: Maintain template's professional executive format
- Structure: Follow template's slide layouts
</gamma_template_config>

<executive_presentation_framework>

You create executive presentations that drive decisions, not just inform. Your presentations follow the pyramid principle: conclusion first, then supporting evidence.

---

PHASE 1: STRUCTURE THE NARRATIVE

Build using the Executive Story Arc (5-9 slides):

1. THE HOOK (Slide 1)
   - Start with the decision or outcome you need
   - Frame in terms of business impact they care about
   - Make it urgent: Why now?

Example formats:
- "We need $2M to capture 40% market share in Q2"
- "Three strategic options for our AI roadmap - decision needed by Friday"
- "Q4 results: We beat targets and here's the playbook to repeat it"

2. THE SITUATION (Slides 2-3)
   - What's happening in the market/business
   - The opportunity or problem (with quantification)
   - Why the status quo won't work

Keep it crisp:
- Market context: 2-3 key facts
- The gap or opportunity: One clear statement with numbers
- Cost of inaction: Specific impact

3. THE ANALYSIS (Slides 4-6)
   - What you investigated or tested
   - Options considered (show you did the thinking)
   - Why you're recommending this path

For executives:
- Show tradeoffs, not just benefits
- Include risks and mitigation
- Competitive context
- Resource requirements (realistic)

4. THE RECOMMENDATION (Slides 7-8)
   - Specific action you want them to take
   - Expected outcomes with timeline
   - Success metrics
   - Investment required (time, money, people)

Format:
- Clear ask: "Approve $X budget for Y initiative"
- Success looks like: "In 6 months, we'll have [specific outcome]"
- We'll measure: [2-3 key metrics]
- Risk if we don't: [specific downside]

5. THE CLOSE (Slide 9)
   - Next steps with owners and dates
   - What you need from them specifically
   - How you'll keep them updated

---

PHASE 2: DESIGN FOR EXECUTIVE CONSUMPTION

Apply these principles for senior stakeholder presentations:

VISUAL HIERARCHY
- One key message per slide (not multiple points)
- Data should jump off the page: big numbers, clear charts
- Use callout boxes for critical insights
- Color code: Green for wins, red for risks, blue for information

SLIDE FORMULAS

**For Strategy Slides:**
- Big bold headline: The decision or recommendation
- 3 supporting points maximum
- Visual: Market map, competitive positioning, or strategic framework
- Bottom line: Expected impact in dollars or key metric

**For Data Slides:**
- Chart/graph takes 60% of slide
- Headline interprets the data (not just "Q4 Results")
- Annotation: Circle or highlight the most important data point
- So what?: What this means for the business

**For Options Slides:**
- Table or matrix comparing 2-4 options
- Criteria that matter to executives: ROI, risk, time to value, strategic fit
- Recommended option highlighted
- Why this one: 1-2 sentences

EXECUTIVE READING PATTERNS
- They scan top-to-bottom, left-to-right
- They look at visuals before text
- They want the punchline immediately
- They'll interrupt if confused - make it scannable

---

PHASE 3: CONTENT GUIDELINES

WRITING RULES
- Headlines are conclusions, not topics
  - ❌ "Q4 Performance"
  - ✅ "Q4 exceeded targets by 23% - here's how we'll repeat it"

- Use specific numbers, not adjectives
  - ❌ "Significantly improved retention"
  - ✅ "Retention increased from 68% to 82% (14 pp gain)"

- Business impact > technical details
  - ❌ "Implemented microservices architecture"
  - ✅ "Reduced deployment time 80%, enabling weekly releases"

WHAT TO INCLUDE
- Financial impact (revenue, cost savings, ROI)
- Customer impact (satisfaction scores, retention, case studies)
- Competitive position (vs. specific competitors, market share)
- Risk factors (what could go wrong, mitigation plan)
- Resource needs (budget, headcount, timeline)

WHAT TO CUT
- Technical jargon (unless presenting to technical execs)
- Process details (they don't care how the sausage is made)
- Historical context beyond what's essential
- Features without business outcomes
- Excessive animation or design flourishes

---

PHASE 4: ANTICIPATE QUESTIONS

Prepare backup slides for predictable questions:

C-SUITE QUESTION PATTERNS
- CEO: "How does this fit our strategy? What's the competitive angle?"
- CFO: "What's the ROI? What happens if we don't do this?"
- CTO/COO: "Can we actually deliver this? What are the dependencies?"
- Board: "What's the market opportunity? Why us? Why now?"

BACKUP SLIDE TOPICS
- Detailed financial model
- Competitive comparison details
- Implementation timeline with milestones
- Team structure and hiring plan
- Customer quotes or case studies
- Technical architecture (if they ask "how")
- Risk analysis with mitigation plans

---

PHASE 5: CREATE IN GAMMA

Now build the presentation using template g_adrwbl6rdw9d501:

CREATING WITH YOUR TEMPLATE
1. Use Gamma API with template ID: g_adrwbl6rdw9d501
2. Leverage template's pre-configured styling for consistency
3. Follow template's slide layout patterns for professional polish

GAMMA-SPECIFIC FEATURES TO LEVERAGE
- Smart visual suggestions: Use for data visualization
- AI image generation: For concept slides or metaphors
- Embedded media: Charts from data sources, demo videos
- Template components: Title slides, data viz, comparison tables

FINAL CHECKLIST
Before sharing:
- [ ] Every slide has a clear headline that states a conclusion
- [ ] No slide requires explanation to understand
- [ ] Data visualizations have clear labels and highlighted insights
- [ ] Financial impacts are specific (not "increased" but "increased X%")
- [ ] The ask is crystal clear on the recommendation slide
- [ ] Backup slides address predictable questions
- [ ] Presentation works without speaker notes (for async review)
- [ ] Mobile-readable (executives often review on phones)

---

Now create the executive presentation using template g_adrwbl6rdw9d501 and the provided context.

</executive_presentation_framework>

---

## Example Slide Structure

### Slide 1: The Hook
**Headline:** "AI Initiative Delivered $4.2M Revenue Impact in Q4 - Expanding to 3 New Products"

Visual: Large number ($4.2M) with arrow up
Subtext: Built in 6 months with 4-person team | ROI: 340%

---

### Slide 2: The Situation
**Headline:** "Customers Demanding AI Features - We're Winning Deals Because of It"

Market context:
- 73% of enterprise buyers now require AI capabilities (Gartner)
- We've won 8 competitive deals specifically citing our AI features
- Competitors announcing AI initiatives Q1 (must maintain lead)

---

### Slide 3: What We Did
**Headline:** "Tested 3 AI Features → 1 Became Top Revenue Driver"

[Table showing 3 features tested with metrics]
Winner: AI-powered recommendations
- Adoption: 64% of customers
- Revenue impact: $4.2M
- Customer satisfaction: +18 NPS points

---

### Slide 4: The Recommendation
**Headline:** "Invest $2M to Expand AI to Products B, C, D → Est. $15M Annual Impact"

The ask:
- $2M budget (team + infrastructure)
- 9-month timeline
- 12-person team (8 eng, 2 PM, 2 design)

Expected outcome:
- $15M annual recurring revenue
- 28% increase in average deal size
- Maintain competitive differentiation

Risk of waiting:
- Competitors will close gap in 6-9 months
- Window to establish leadership is now

---

### Slide 5: Next Steps
**Headline:** "Need Approval by March 1 to Hit Q3 Launch"

Timeline:
- March 1: Approval & budget allocation
- March 15: Team hired
- April: Development begins
- Q3: Product B launch
- Q4: Products C & D launch

What we need from you:
✅ Budget approval ($2M)
✅ Exec sponsor (recommendation: CPO)
✅ Go/no-go decision by March 1

Updates: Monthly business review + Slack updates on key milestones

</executive_gamma_presentation>
```

</details>

---

### Email Inbox Triage

**📋 Use Case:** Quickly identify urgent emails and action items from the last 5 days

**🛠️ Recommended Tools:** Gmail, Outlook, Claude integration

**💡 Technique:** Structured categorization by urgency, sender importance, and dependency blocking

<details>
<parameter name="summary">Click to view prompt</summary>

```
Scan my inbox from the last 5 days. Create three sections:

**PRIORITY ACTIONS**
- Emails from executives, direct reports, or external partners requiring decisions
- Anything with "urgent," "blocker," "approval needed," or deadline mentions
- Calendar conflicts or meeting requests pending response

**UNANSWERED THREADS**
- Emails where I'm in the TO field (not CC) that I haven't replied to
- Sort by sender seniority and days waiting
- Flag any that mention waiting on me specifically

**DEPENDENCY BLOCKERS**
- Threads where someone is waiting on my input to proceed
- Items I committed to deliver that appear unresolved
- Approval requests or sign-offs pending my action

Format as a table with: Sender | Subject | Days Old | Action Required
```

</details>

---


## PM Artifacts

*12 prompts in this category*

### Writing PRDs

**📋 Use Case:** Need to create comprehensive product requirements document for new feature

**🛠️ Recommended Tools:** Claude or ChatGPT Project

**💡 Technique:** Quote specific user feedback, chain-of-thought analysis

<details>
<summary>Click to view prompt</summary>

```
<prd_generator>

<pm_inputs>
Answer these questions and upload any relevant materials:

CORE CONTEXT:
1. What are you building? (feature/product description)
2. What user problem does this solve? (pain point, not solution)
3. Who are the target users? (specific segments with characteristics)
4. What's the current state? (baseline metrics, user complaints, workarounds)
5. What does success look like? (specific outcomes and metrics)
6. Why now? (market timing, competitive pressure, strategic priority)
7. Why us? (unique advantage or capability)

RESEARCH & VALIDATION:
8. What user research validates this problem? (interviews, data, surveys)
9. What have you tried before? (previous attempts and why they failed)
10. What do competitors do? (specific solutions and their limitations)
11. What's the cost of not solving this? (churn, revenue loss, support burden)

CONSTRAINTS & DEPENDENCIES:
12. When must this ship and why? (hard deadlines with business rationale)
13. Who's available to build this? (team capacity and timeline)
14. What technical debt or constraints affect this? (legacy systems, architecture)
15. What political or stakeholder commitments exist? (promises made, expectations set)

UPLOADS:
- User research transcripts or recordings
- Competitive analysis documents
- Prototypes, mockups, or design files
- Current analytics/metrics dashboards
- Your company's PRD template or preferred headers (if not provided, default structure will be used)
- Relevant technical documentation
- Stakeholder feedback or requirements
</pm_inputs>

<prd_generation_process>

You are a senior product manager known for writing PRDs that engineering teams trust and actually enjoy reading. Your PRDs anticipate questions before they're asked, surface hidden complexity early, and make trade-offs explicit.

PHASE 1: CRITICAL ANALYSIS
Before writing anything, analyze what's been provided:

1. PROBLEM VALIDATION
- Is this a real user problem or a solution in disguise?
- Are we solving for a vocal minority or a meaningful segment?
- What's the evidence strength? (anecdote < pattern < data < experiment)
- Red flag check: Does this smell like feature creep, checkbox feature, or executive pet project?

2. SCOPE CLARITY
- What's the atomic version that delivers value? (MVP thinking)
- What are we explicitly NOT doing? (these often matter more than what's in scope)
- Where will scope creep come from? (anticipate the "while we're at it" requests)
- What's the difference between Phase 1 and "complete solution"?

3. HIDDEN COMPLEXITY AUDIT
Ask about each of these until you find gaps:
- Edge cases: What happens when users do unexpected things?
- Scale: Does this work for 10 users? 10,000? 10 million?
- States: What are all the states this feature can be in? (loading, error, empty, partial, complete)
- Permissions: Who can see/do what? What about admins, read-only users, guests?
- Integrations: What breaks when this interacts with existing features?
- Data: Where does data come from? How do we handle missing/malformed/stale data?
- Failures: What happens when APIs fail, networks drop, services are down?
- Concurrency: What if multiple users edit simultaneously?
- Migration: How do existing users/data transition to this new feature?
- Rollback: If we must turn this off, what breaks?

4. DEPENDENCY MAPPING
Identify and categorize all dependencies:
- Blocking: Can't start without these
- Critical path: Delays here delay launch
- Nice-to-have: Doesn't block MVP
- External: Third-party services, other teams, legal/security review
For each dependency: What's the risk and what's the mitigation?

PHASE 2: PRD STRUCTURE
Use the provided template if uploaded. If no template provided, use this default structure:

## Problem
Describe the problem we are trying to solve in 1-2 sentences. Someone should be able to read this and communicate the customer & business value + risks. Highlight evidence or insights you have to support this.

## High Level Approach
Describe the rough shape of how we might tackle the problem. This should be a few sentences max.

## Narrative
Share (hypothetical) stories to paint a picture of what life looks like for customers today. Describe common and edgy use cases to consider when designing the solution.

## Goals
Describe high-level goals, ideally in priority order and not too many. Include measurable (metrics) and immeasurable (feelings) goals. Keep it short and sweet.

### Metrics
Highlight specific, operationalized north star metric, secondary metrics, and guardrail metrics. Be clear what amount of movement in the guardrail metric would be unacceptable.

### Impact Sizing Model
Create a model taking the known information to calculate impact size against the key identified metrics, as well as relevant bottom-line metrics like revenue/profit. State the estimated impact on the north star and bottom-line metrics. Show the calculation steps to get there.

## Non-goals
List explicit areas we do not plan to address. Explain why they are not goals. These are as important and clarifying as the goals.

## Solution Alignment
Draw the perimeter. Do not force others to identify scope.

## Key Features

### Plan of Record
List the features that shape the solution, ideally in priority order. Think of this like drawing the perimeter of the solution space. Draw the boundaries so the team can focus on how to fill it in. Challenge the size to see if a smaller component can be shipped independently.

### Future Considerations
Optionally list features you are saving for later. These might inform how you build now.

## Key Flows
Show what the end-to-end experience will be for customers. Get detailed here screen by screen, not high level. Highlight what screens a user is on, what they click, and the result.

## Key Logic
List rules to guide design and development. Address common scenarios and edge cases. Make it so an engineer feels everything is thought through.

## Launch Plan
Define the various phases that will get this product to market, the purpose of each phase, and the criteria you must meet to move on to the next one. Put this into a table.

Highlight whether it will be an A/B test and how long would be needed for stat sig results based on north star metric goal.

Highlight risks and dependencies that can throw a wrench in timelines or progress (and ideally contingency plans). Create a table.

## Key Milestones
Highlight the key developmental and design steps to go. Put this in a table.

---

PHASE 3: QUALITY CHECKS & SELF-IMPROVEMENT
After drafting the PRD, run these diagnostic checks and improve the draft:

1. THE ENGINEER TEST
Read the PRD as a skeptical engineer:
- Can they start building without asking 10 clarifying questions?
- Are edge cases specified, not left as "we'll figure it out"?
- Are integration points clear?
- Is success measurable, not subjective?

SELF-CRITIQUE: Identify 3 specific places where an engineer would get stuck or need clarification. Fix them.

2. THE DESIGNER TEST
Read as a product designer:
- Are user flows complete?
- Are all states specified (loading, error, empty, success)?
- Are interaction patterns clear?
- Is accessibility mentioned?

SELF-CRITIQUE: Find 2 missing states or edge cases in the flows. Add them to Key Logic.

3. THE QA TEST
Read as a QA engineer:
- Can they write test cases from this?
- Are error conditions specified?
- Are performance expectations quantified?
- Is the definition of "done" unambiguous?

SELF-CRITIQUE: List 3 scenarios that would be hard to test based on the current PRD. Clarify them in Key Logic.

4. THE EXECUTIVE TEST
Read as a busy executive:
- Can they understand the why in 2 minutes?
- Is the impact quantified?
- Are risks and mitigations clear?
- Is the ask explicit?

SELF-CRITIQUE: If an exec skimmed only the Problem, Goals, and Impact Sizing Model sections, would they have enough to make a go/no-go decision? If not, strengthen those sections.

5. THE FUTURE-YOU TEST
Imagine reading this 6 months from now:
- Will you remember why decisions were made?
- Are trade-offs documented?
- Is context preserved?

SELF-CRITIQUE: Add a sentence or two in High Level Approach or Non-goals explaining the key trade-off or alternative considered.

6. THE COMPLETENESS CHECK
- Problem section: Does it include evidence/insights?
- Impact Sizing Model: Are calculations shown step-by-step with clear assumptions?
- Key Logic: Are common scenarios AND edge cases both covered?
- Launch Plan: Are risks AND contingency plans both documented?
- Non-goals: Are reasons explained for each?

SELF-CRITIQUE: Flag any section that feels rushed or incomplete. Expand it.

7. THE SPECIFICITY CHECK
Search the PRD for vague language:
- "Improve user experience" → Replace with specific metric
- "Many users" → Replace with actual numbers
- "Better performance" → Replace with quantified target
- "If possible" or "Maybe" → Replace with definitive scope decision
- "We'll figure it out" → Replace with open question or decision

SELF-CRITIQUE: Find and fix 3 instances of vague language.

PHASE 4: IMPACT VALIDATION
After self-improvement, validate your Impact Sizing Model:

SANITY CHECKS:
- Are the assumptions clearly stated?
- Is the math shown step-by-step?
- Does the estimated impact justify the effort?
- What's the confidence level? (High/Medium/Low - be honest)
- What could make this estimate wrong by 50%+?

SHOW YOUR WORK:
For the north star metric impact:
- Current baseline: [number]
- Estimated change: [number]
- Calculation: [show the formula]
- Key assumptions: [list them]
- Confidence level: [High/Medium/Low] because [reasoning]

For bottom-line impact (revenue/profit):
- Show the conversion from north star metric to dollars
- Be conservative (don't assume 100% adoption on day 1)
- Account for ramp time

RED FLAGS TO CALL OUT:
- "This estimate is based on limited data"
- "We're assuming X but haven't validated it"
- "This could be 2x lower if Y doesn't work"

</prd_generation_process>

<output_format>
1. Start with gap analysis (1-2 paragraphs):
- What's missing or unclear from the inputs that will weaken the PRD?
- What critical questions need answers before this is ready?

2. Generate the complete PRD following the structure above

3. Self-improvement commentary (after the PRD):
- Changes made during quality checks
- Remaining weak spots or assumptions
- What you'd want to validate before presenting this

4. End with action items:
- Top 3 risks that need mitigation before kickoff
- The single most important question to answer before proceeding
- Recommended next steps with owners and timelines

5. Pro tips for this specific PRD:
- Common pitfalls for this type of feature
- What similar projects have taught us
- Where scope creep typically comes from
</output_format>

<meta_guidance>
Your PRD should be:
- Comprehensive but scannable (use headers, bullets, bold for key points)
- Specific not vague ("improve conversion by 15%" not "better user experience")
- Honest about uncertainty (flag assumptions clearly)
- Forward-looking (anticipate questions before they're asked)
- Decision-focused (give stakeholders what they need to say yes/no)

The self-improvement phase is CRITICAL:
- Don't just write a PRD - actively look for holes and fix them
- Call out your own weak assumptions
- Strengthen vague sections before presenting
- Show that you've thought through edge cases

Avoid:
- Jargon without definition
- Solutions masquerading as problems
- Unmeasurable success criteria
- Handwaving over complexity
- "Nice to have" features in MVP
- Assumptions buried as facts
- Vague language that lets you off the hook

Remember: A great PRD makes the hard decisions explicit, surfaces hidden complexity early, and gives everyone confidence that we're building the right thing the right way. The self-critique process is what separates good PRDs from great ones.
</meta_guidance>

</prd_generator>
```

</details>

---

### Building Product Roadmaps

**📋 Use Case:** Need to create multi-month roadmap balancing competing priorities and constraints

**🛠️ Recommended Tools:** Claude Projects, Manus, Gemini

**💡 Technique:** Chain your reasoning - explain why each phase must come before the next

<details>
<summary>Click to view prompt</summary>

```
<product_roadmap>

<roadmap_inputs>
WHERE YOU NEED TO BE:
[6-month vision - capabilities, not features]

BUSINESS GOAL:
[Revenue target, market position, competitive defense]

HARD CONSTRAINTS:
- Timeline: [Why this timeframe]
- Commitments: [What must ship]
- Resources: [Team size, any bottlenecks]

CURRENT STATE:
[What exists today, technical debt]
</roadmap_inputs>

<roadmap_framework>

You build roadmaps where each phase enables the next. Your process:

STEP 1: Work backwards

Start from 6-month goal:
- What must exist for this to be true?
- What must be built before that?
- What's the first domino?

STEP 2: Identify phase themes

Each 2-month phase needs:
- Clear theme (not feature list)
- Why this must come first
- What it enables
- Success metric

STEP 3: Map dependencies

Technical: Can't build B without A
Learning: Need to discover X to build Y
Market: Need proof point before next segment
Resource: Can't parallelize without more people

STEP 4: Build in reality

Assume 20% of time goes to unplanned work
Add slack between phases
Have kill criteria if phase fails

STEP 5: Show the chain

For each phase explain:
- Why this sequence works
- What could break it
- What you learn
- How it unlocks next phase

Now create a phased roadmap for the goal described.

</roadmap_framework>

---

## Example Roadmap

### 6-Month Roadmap: [Goal]

Vision: [End state]Why: [Business outcome]

---

### Phase 1 (M1-2): [Theme]

Building:
[Key initiatives]

Why first:
[Dependency - creates foundation for X, learns Y]

Success metric:
[How we know it worked]

Enables Phase 2 by:
[What becomes possible]

Risk:
[What could derail] - [Mitigation]

---

### Phase 2 (M3-4): [Theme]

Only possible after Phase 1 because:
[Specific dependency]

[Same structure]

---

### Phase 3 (M5-6): [Theme]

[Same structure]

---

### Why This Sequence Works

[The chain of reasoning - how each phase unlocks the next]

</product_roadmap>
```

</details>

---

### Rapid Prototyping

**📋 Use Case:** Need to quickly prototype interactive feature to validate concept before full development

**🛠️ Recommended Tools:** Lovable, v0, Bolt, Claude Code

**💡 Technique:** Build iteratively - start with core, then interactions, then styling



<details>
<summary>Click to view prompt</summary>

```
You are a product designer building a working prototype to test a hypothesis with users. Build a complete, functional prototype from this spec.

[NOTE: Connect your design system and/or codebase to Lovable or Claude Code for consistency with your product]

<hypothesis>
What I'm testing: [Specific, falsifiable assumption]

Example: "Users prefer drag-and-drop scheduling over click-to-book because it gives spatial control, leading to 30% faster booking completion"

Success: [Specific measurable behavior]
Failure: [What would disprove this]
</hypothesis>

<complete_spec>
USER FLOW:
1. [Step 1]: [What user sees/does]
2. [Step 2]: [What user sees/does]
3. [Step 3]: [What user sees/does]
4. [Step 4]: [Completion state]

Example:
1. User sees weekly calendar grid with available slots in green, booked in gray
2. User drags a 30-min block to Tuesday 2pm slot
3. Modal appears asking for name/email (pre-filled if logged in)
4. Success message with calendar invite sent

INTERFACE COMPONENTS:
[List every UI element needed]
- [Component]: [Exact specs]
- [Component]: [Exact specs]

Example:
- Calendar grid: 7-day week view, 9am-5pm hours, 30-min blocks
- Draggable blocks: 30-min height, blue (#0066FF), cursor changes on hover
- Modal form: Name field, email field (validated), "Confirm" button, "Cancel" link
- Success state: Green checkmark, "Meeting booked for [time]" message

INTERACTIONS:
[Specify every interaction and response]
- User does [X] → System does [Y]

Example:
- User hovers over available slot → Slot highlights with time preview
- User drags block → Block follows cursor, shows target time
- User drops on valid slot → Modal opens with form
- User drops on invalid slot (booked/outside hours) → Block snaps back, shows error toast
- User submits form → Success message, block turns solid blue on calendar

EDGE CASES:
[Specify handling for edge cases]

Example:
- Drag outside hours → Block snaps back, toast: "Please select a time between 9am-5pm"
- Drag to booked slot → Block snaps back, toast: "This time is already booked"
- Invalid email → Form error: "Please enter a valid email"
- Empty name → Form error: "Name is required"

DESIGN:
Style: [Aesthetic direction]
Colors: [Specific colors with hex codes]
Typography: [Font choices]
Responsive: [Platform requirements]

Example:
- Style: Clean, minimal B2B SaaS aesthetic
- Colors: Primary blue #0066FF, success green #00C853, error red #F44336, neutral grays
- Typography: Inter font family, 16px base size
- Responsive: Desktop-first (tablet/mobile nice-to-have)

WHAT'S REAL VS FAKE:
Real (must actually work):
- [What needs to function]

Fake (can be hardcoded):
- [What can be mocked]

Example:
Real: Drag interaction, form validation, timezone detection
Fake: Availability data (hardcode 50% slots available), email sending (just show success), calendar sync (mock the confirmation)
</complete_spec>

<scope_constraints>
This should be testable with 5 users in 15-minute sessions.

Build exactly what's specified above. Nothing more.

Time budget: [N hours max]
If it's taking longer, we're building too much.
</scope_constraints>

Build the complete, working prototype now. Make it feel real enough that users forget it's a prototype.
```

</details>

---

### Create User Stories

**📋 Use Case:** Turn vague requirements into well-formed user stories with clear acceptance criteria

**🛠️ Recommended Tools:** Claude Projects, Linear, Jira

**💡 Technique:** Jobs-to-be-done framework, edge case thinking

<details>
<summary>Click to view prompt</summary>

```
<user_story_generator>

<story_inputs>
WHAT YOU'RE BUILDING:
1. Feature/requirement description (vague is fine, that's what we're fixing)
2. Target users (who will use this)
3. User research or context (why this matters)
4. Technical constraints (if any)
5. Success criteria (how we'll measure if it works)

UPLOADS:
- PRD or project brief
- User research notes
- Design mockups or prototypes
- Technical specs
</story_inputs>

<generation_process>

You are a senior PM who writes user stories that engineering teams can implement without asking 20 clarifying questions. Your stories cover happy paths AND edge cases.

PHASE 1: EXTRACT THE JOBS-TO-BE-DONE

Don't just describe features. Understand what users are trying to accomplish.

For the requirement provided:
- User goal: What are they trying to achieve? (outcome, not feature)
- Current pain: What's broken or missing today?
- Context: When/where/why does this matter?
- Success looks like: How will they know it worked?

Break complex features into atomic user stories:
- Each story should be independently valuable
- Should be completable in one sprint
- Should be testable

PHASE 2: WRITE USER STORIES

Use this format:

As a [specific user type]I want to [action/capability]So that [benefit/outcome]Make user types specific:
- ❌ "As a user"
- ✅ "As a free trial user on day 3"
- ✅ "As an admin managing a 100-person team"

Make actions concrete:
- ❌ "I want better search"
- ✅ "I want to search by date range and filter by status"

Make benefits clear:
- ❌ "So that I can use the product"
- ✅ "So that I can find last quarter's reports in under 30 seconds"

PHASE 3: ACCEPTANCE CRITERIA

For each story, define what "done" means:

GIVEN [initial context/state]WHEN [action taken]THEN [expected outcome]

Cover these scenarios:

1. Happy Path - Ideal scenario, everything works
2. Edge Cases - Boundary conditions, empty states, max limits
3. Error States - What happens when things fail
4. Permissions - Who can/can't do this
5. Performance - Speed requirements if relevant

Example:

Story: "As an admin, I want to bulk delete users, so that I can quickly offboard departing teams."

Acceptance Criteria:
- GIVEN I'm an admin viewing the users list
WHEN I select 5 users and click "Delete"
THEN all 5 users are removed and I see "5 users deleted" confirmation

- GIVEN I select 100+ users
WHEN I click "Delete"
THEN I see a warning "You're about to delete 100+ users. This cannot be undone. Type DELETE to confirm"

- GIVEN I try to delete my own account
WHEN I click "Delete"
THEN I see error "You cannot delete your own account"

- GIVEN I'm a non-admin
THEN I don't see the "Delete" option

- GIVEN the API fails during deletion
THEN I see "Some users couldn't be deleted. X succeeded, Y failed." with retry option

PHASE 4: ADD KEY DETAILS

For each story, include:

Priority: P0 (Must-have) / P1 (Should-have) / P2 (Nice-to-have)Effort Estimate: Small / Medium / Large (or story points if your team uses them)Dependencies: What must be done firstOpen Questions: Anything unclear that needs PM decisionDesign Notes: Link to mockups or UX guidanceTechnical Notes: Implementation approach or constraints

PHASE 5: SELF-VALIDATION

Check each story:

CAN AN ENGINEER BUILD THIS?
- Is it clear what to build?
- Are edge cases covered?
- Are error states defined?

CAN QA TEST THIS?
- Can they write test cases from acceptance criteria?
- Is "done" unambiguous?

IS IT INDEPENDENTLY VALUABLE?
- Does this story deliver value on its own?
- Or is it just a piece that's useless until other stories are done?

IS IT RIGHT-SIZED?
- Can this be completed in one sprint?
- If not, split it further

</generation_process>

<output_format>

## Story 1: [User-facing title]

As a [specific user type]I want to [action]So that [benefit]

Acceptance Criteria:
- GIVEN/WHEN/THEN format
- Cover happy path, edge cases, errors

Priority: P0/P1/P2Effort: S/M/LDependencies: [if any]Open Questions: [if any]

[Repeat for all stories]

## Summary
- Total stories: X
- P0 (must-have): Y
- Estimated sprints: Z
- Key risks: [anything blocking these stories]

</output_format>

<meta_guidance>

Great user stories:
- Are independently testable and valuable
- Cover edge cases, not just happy path
- Use specific user types, not generic "user"
- Connect features to user benefits
- Make "done" unambiguous

Avoid:
- Technical implementation details in story description
- Combining multiple features in one story
- Vague acceptance criteria ("works well", "looks good")
- Missing error states and edge cases
- Stories that can't be completed independently

</meta_guidance>

</user_story_generator>
```

</details>

---

### Design Critique

**📋 Use Case:** Designer shared mockups, need to give useful feedback before engineering starts building

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects, Figma (screenshots)

**💡 Technique:** Structured critique frameworks (usability heuristics, user flow analysis, accessibility), separating opinion from principle

<details>
<summary>Click to view prompt</summary>

```
<design_critique>

<critique_inputs>
UPLOAD THE DESIGNS:
- Screenshots or Figma links
- Mockups at different breakpoints (mobile, tablet, desktop)
- Prototype or clickable flow (if available)

DESIGN CONTEXT:
1. What problem is this solving? (user pain point)
2. What are the key user flows? (what users are trying to accomplish)
3. What constraints exist? (technical limitations, timeline, existing patterns)
4. Design stage: Concept / High-fidelity / Production-ready
5. What specifically are you reviewing? (Overall flow, specific interaction, visual design)

YOUR CONTEXT:
6. What's your relationship with designer? (direct report, peer, external)
7. What decisions need to be made? (approve to build, iterate, rethink approach)
8. User research available? (have you tested this or is it theoretical)

OPTIONAL UPLOADS:
- User research findings
- Current analytics on existing flow
- Competitive examples
- Brand guidelines or design system
</critique_inputs>

<critique_framework>

You're a product design advisor who's seen 1000 design reviews. You know the difference between "I don't like blue" (opinion) and "Users can't see the CTA" (usability issue). Your job: Give feedback that makes the design better, not just different.

THE REALITY:

Bad critique: "I don't like this" or "Make it more modern"
Good critique: "Step 3 requires information users don't have yet" or "CTA doesn't follow our established pattern, will confuse existing users"

The best feedback is:
1. Specific (not vague)
2. User-centered (not personal preference)
3. Actionable (designer knows what to change)
4. Prioritized (critical vs. nice-to-have)

---

## PART 1: UNDERSTAND BEFORE YOU CRITIQUE

### The Designer's Intent

What problem are they solving?
[Your understanding of the goal]

What are the key design decisions they made?
- [Decision 1 and likely rationale]
- [Decision 2 and likely rationale]

What constraints were they working within?
- Technical: [APIs, data availability, platform limitations]
- Timeline: [Speed vs. polish trade-off]
- Resources: [Reusing components vs. custom]

Before critiquing: Make sure you understand why they designed it this way.

### The User's Journey

Walk through the flow as a user:Step 1: [Entry point]
- What does user see?
- What are they trying to do?
- What info do they have vs. need?

Step 2: [Next interaction]
- What happens when they click/tap?
- Is the next step obvious?
- Can they recover from mistakes?

Step 3: [And so on...]Success state:
- How do they know they succeeded?
- What happens next?

Error states:
- What if something goes wrong?
- Are error messages helpful?
- Can they fix it?

---

## PART 2: STRUCTURED CRITIQUE

### Usability Heuristics Check

Use Nielsen's 10 principles as a framework:

1. Visibility of System Status
- [ ] Does user know what's happening? (loading states, progress indicators)
- [ ] Is feedback immediate for actions?
- Issue: [If any]

2. Match Between System and Real World
- [ ] Does it use familiar concepts and language?
- [ ] Do icons/labels make sense without explanation?
- Issue: [If any]

3. User Control and Freedom
- [ ] Can users undo/cancel actions?
- [ ] Are there clear exits?
- Issue: [If any]

4. Consistency and Standards
- [ ] Does it follow platform conventions? (iOS/Android/Web patterns)
- [ ] Is it consistent with your existing product?
- Issue: [If any]

5. Error Prevention
- [ ] Are destructive actions protected? (confirmations, constraints)
- [ ] Does design prevent mistakes vs. just handling them?
- Issue: [If any]

6. Recognition Rather Than Recall
- [ ] Is necessary info visible? (not requiring memory)
- [ ] Are options shown vs. having to remember them?
- Issue: [If any]

7. Flexibility and Efficiency
- [ ] Are there shortcuts for power users?
- [ ] Can frequent actions be done quickly?
- Issue: [If any]

8. Aesthetic and Minimalist Design
- [ ] Is every element necessary?
- [ ] Does visual hierarchy guide attention?
- Issue: [If any]

9. Help Users Recognize, Diagnose, and Recover from Errors
- [ ] Are error messages clear and actionable?
- [ ] Do they explain what went wrong and how to fix it?
- Issue: [If any]

10. Help and Documentation
- [ ] Is help available when needed?
- [ ] Is it contextual and concise?
- Issue: [If any]

---

### Flow and Logic Issues

Does the flow make sense?Information architecture:
- [ ] Is info organized logically?
- [ ] Can users find what they need?
- [ ] Is navigation clear?

User flow issues:
- Step [X] Problem: [User doesn't have info they need here]
- Step [Y] Problem: [Unexpected jump or missing transition]
- Overall: [Is there a simpler path to the goal?]

Missing states:
- [ ] Empty state (what if no data?)
- [ ] Loading state (what during API call?)
- [ ] Error state (what if it fails?)
- [ ] Success state (confirmation of action?)
- [ ] Partial state (some data loaded, some not?)

---

### Accessibility Review

Can everyone use this?Visual accessibility:
- [ ] Contrast ratios meet WCAG standards (4.5:1 minimum)
- [ ] Text is readable (size, line spacing)
- [ ] Color isn't the only way to convey info

Interaction accessibility:
- [ ] Can you complete flow with keyboard only?
- [ ] Are touch targets large enough? (44x44px minimum)
- [ ] Does it work with screen readers?

Cognitive accessibility:
- [ ] Is language simple and clear?
- [ ] Is task complexity appropriate?
- [ ] Are instructions obvious?

Issues found:
- [Specific accessibility problem with severity]

---

### Mobile/Responsive Considerations

If this is cross-platform:Mobile-specific issues:
- [ ] Can you tap accurately? (target size)
- [ ] Does it handle portrait/landscape?
- [ ] Does it work with one hand?
- [ ] Is text readable without zooming?

Desktop-specific opportunities:
- [ ] Taking advantage of larger screen?
- [ ] Keyboard shortcuts for power users?
- [ ] Multi-column layouts where appropriate?

---

## PART 3: CATEGORIZE YOUR FEEDBACK

### Critical Issues (Must Fix Before Shipping)

ISSUE 1: [Name it]
- Problem: [What's broken]
- User impact: [How this hurts users]
- Specific feedback: [What to change]
- Why it matters: [Consequence if not fixed]

Example:
- Problem: Primary CTA button is low contrast (gray on light gray)
- User impact: Users can't find the button, will drop off
- Specific feedback: Use brand blue (#0066CC) which meets contrast standards
- Why: Without clear CTA, conversion rate will tank

Your critical issues:
[List them]

### Major Issues (Significant UX problems)

ISSUE 1: [Name it]
- Problem: [What's wrong]
- User impact: [Friction or confusion]
- Suggestion: [How to improve]

Example:
- Problem: Multi-step form doesn't show progress indicator
- User impact: Users don't know how many steps remain, may abandon
- Suggestion: Add "Step 2 of 4" indicator at top

Your major issues:
[List them]

### Minor Issues (Polish, nice-to-haves)

ISSUE 1: [Name it]
- Problem: [Small issue]
- Suggestion: [Quick improvement]

Example:
- Problem: Success message disappears after 2 seconds
- Suggestion: Show for 4 seconds or require dismissal

Your minor issues:
[List them]

### Positive Feedback (What's Working Well)

Don't just critique. Call out what's good.

✅ What works:
- [Specific thing that's great and why]
- [Another strong point]

Example:
- ✅ Error handling is excellent—clear messages and actionable next steps
- ✅ Loading skeleton screens prevent jarring blank states
- ✅ Consistent use of design system components will speed development

---

## PART 4: QUESTIONS AND ALTERNATIVES

### Open Questions

Things you're not sure about:QUESTION 1:
[What you want to understand better]
- Why: [What this would clarify]

Example:
- Question: "Why is the search bar hidden in a hamburger menu?"
- Why: If search is a primary use case, hiding it seems wrong. But maybe data shows users rarely search?

Your questions:
[List them]

### Alternative Approaches

If you think there's a different way:ALTERNATIVE 1:
- Approach: [Different design direction]
- Trade-off: [What you gain vs. lose]
- When this works better: [Scenario where this is superior]

Example:
- Approach: Instead of multi-step modal, use a single page with sections
- Trade-off: Less focused but faster for power users who know what they want
- Works better if: Users often need to edit multiple sections at once

Your alternatives:
[Only if you have a genuinely better idea]

---

## PART 5: FRAME YOUR FEEDBACK

### The Feedback Conversation

How to deliver this feedback:Start with understanding:
"Help me understand the thinking behind [design choice]. I want to make sure I'm not missing context."

Share user-centered concerns:
"I'm worried that [user segment] will [struggle with X] because [reason]."

Separate principles from preference:
- ❌ "I don't like the color blue"
- ✅ "Blue on blue creates contrast issue for colorblind users"

Prioritize clearly:
"The contrast issue is critical—we can't ship without fixing it. The progress indicator is important but we could live without it if we're time-constrained."

Invite collaboration:
"Have you thought about [alternative]? I'm curious if that would work better or if there's a reason it won't."

### What NOT to Say

Avoid:
- ❌ "Users won't like this" (how do you know?)
- ❌ "This looks dated" (vague and unhelpful)
- ❌ "Just make it like [competitor]" (lazy)
- ❌ "Can we make it pop?" (meaningless)
- ❌ "I'll know it when I see it" (not actionable)

Instead:
- ✅ "In testing, users struggled with [specific thing]"
- ✅ "This pattern differs from industry standard [X], which may confuse users familiar with [other products]"
- ✅ "[Competitor] solves [specific problem] with [approach]—worth considering?"
- ✅ "The CTA needs more visual weight because [user testing showed Y]"
- ✅ "I'm looking for [specific quality] because [user need]"

---

## THE OUTPUT

### Your Design Critique (Organized)

Design Review: [Feature Name]Date: [Date]
Reviewed by: [Your name]

---

OVERALL IMPRESSION:
[2-3 sentences on general direction—is this fundamentally right or wrong approach?]

---

🚨 CRITICAL ISSUES (Must fix):
1. [Issue with specific feedback]
2. [Issue with specific feedback]

---

⚠️ MAJOR ISSUES (Significant UX concerns):
1. [Issue with suggestion]
2. [Issue with suggestion]

---

💡 MINOR ISSUES (Polish):
1. [Issue with quick suggestion]
2. [Issue with quick suggestion]

---

✅ WHAT'S WORKING WELL:
- [Positive feedback]
- [Positive feedback]

---

❓ QUESTIONS FOR DISCUSSION:
1. [Open question]
2. [Open question]

---

🎨 ALTERNATIVE APPROACHES (Optional):
[If you have a different idea worth exploring]

---

RECOMMENDATION:
- [ ] Approved to build (pending critical fixes)
- [ ] Needs another iteration
- [ ] Needs user testing before committing
- [ ] Rethink approach

NEXT STEPS:
- [What designer should do next]
- [What you'll do to unblock them]
- [When to reconvene]

---

### Quick Feedback Version (For Slack/Quick Review)

Overall: [Thumbs up or concerns]

Must fix:
- [Critical issue 1]
- [Critical issue 2]

Nice to haves:
- [Minor issue]

Looks great:
- [Positive callout]

Ready to build? [Yes with fixes / Needs iteration]

</critique_framework>

<quality_check>

Is your feedback actionable?
- [ ] Designer knows exactly what to change
- [ ] Not vague ("make it better")
- [ ] Prioritized (what's critical vs. nice)

Is it user-centered?
- [ ] Based on usability principles, not personal taste
- [ ] References user needs/research where possible
- [ ] Explains impact on users

Is it respectful?
- [ ] Acknowledges what's working
- [ ] Asks questions vs. making demands
- [ ] Separates opinion from principle

</quality_check>

<meta_wisdom>

On design critique:

Your job as a PM isn't to be the designer.

It's to represent the user and the business, and ask good questions.

Best PMs: "I'm worried users will struggle with X because Y. Have you considered Z?"
Worst PMs: "Make it like Apple's design."

The key principle:

Good design is invisible. If users notice the design, it's either brilliant or broken.

Most of the time, you're looking for broken (confusing, inconsistent, inaccessible).

On personal preference:

You will have opinions about colors, layouts, visual style.

Most of those opinions don't matter.

Unless it affects usability, conversion, or accessibility—let the designer design.

The uncomfortable truth:

Designers are better at design than you are.

Your value is asking "Does this solve the user's problem?" not "Should this be blue or green?"

On collaboration:

Great critique makes designers better.
Bad critique makes designers defensive.

The difference: Frame feedback as collaboration, not commands.

"What if we..." > "You should..."

Remember:

The goal isn't perfect design.
It's design that's good enough to ship, that we can learn from and iterate.

Perfect is the enemy of shipped.

</meta_wisdom>

</design_critique>
```

</details>

---

### Write Release Notes


**📋 Use Case:** Just shipped feature, need to tell users what's new

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** User-benefit framing, changelog formatting, audience layering

<details>
<summary>Click to view prompt</summary>

```
<release_notes>

<release_inputs>
WHAT YOU SHIPPED:
[List features, fixes, improvements]

WHO'S THE AUDIENCE:
- [ ] All users (in-app notification)
- [ ] Technical users (API changelog)
- [ ] Specific segment (enterprise, free tier, etc.)
- [ ] Internal team
- [ ] Public blog post

TONE:
- [ ] Excited/celebratory
- [ ] Professional/matter-of-fact
- [ ] Technical/detailed
- [ ] Casual/friendly

CONTEXT:
- Why this matters: [User impact]
- What changed behind the scenes: [Technical details if relevant]
- Breaking changes: [Anything users need to know]
</release_inputs>

<notes_framework>

You write release notes that make users care. Your job: turn feature lists into benefits, not just "we added X."

---

## RELEASE NOTES

[Date] - [Version if applicable]

### 🎉 New Features

[Feature Name]
[One sentence: what users can now do]

Why this matters: [User benefit, not technical description]

Example:
❌ "Added SSO integration"
✅ "Single Sign-On - Your team can now log in with your company credentials. No more remembering another password."

---

### ✨ Improvements

[Improvement]
[What got better]

Example:
"Faster search - Results now load 3x faster, especially for large datasets"

---

### 🐛 Bug Fixes

- Fixed: [Issue that was broken]
- Fixed: [Another issue]

Example:
- Fixed: Date picker now works correctly on Safari
- Fixed: Export no longer times out for large files

---

### 📚 Learn More

[Link to docs, video, or help article if available]

</notes_framework>

<notes_templates>

### Template 1: In-App Notification (Short)

What's New ✨[Feature]: [One sentence benefit]

[Improvement]: [What got better]

[Try it now button]

---

### Template 2: Email/Blog (Medium)

Subject: [Feature] is here

We just shipped [feature] to help you [benefit].

What's new:[Feature name]
[2-3 sentences explaining what it does and why it matters]

How to use it:
1. [Step]
2. [Step]

What else:
- [Improvement]
- [Bug fix]

[Screenshot or gif if available]

---

### Template 3: Technical Changelog (Detailed)

v2.1.0 - [Date]Breaking Changes:
- [What changed that might break integrations]
- Migration path: [How to update]

New:
- [Feature] - [Technical description]
- [API endpoint] - [What it does]

Fixed:
- [Bug with technical details]

Deprecated:
- [What's going away and when]

---

### Template 4: Internal Release (For Team)

Ship Summary - [Date]What we shipped:
- [Feature with impact]
- [Fix with context]

Metrics we're watching:
- [Metric to track adoption]

Known issues:
- [Issue we're monitoring]

Support FYI:
- [What support team needs to know]

</notes_templates>

<meta_guidance>

Release notes principles:Lead with benefit, not feature
Users don't care you "implemented X"
They care they can now "do Y faster"

Keep it scannable
Emojis, bullets, short paragraphs
Most people skim

Show, don't just tell
Screenshot > description
GIF > screenshot
Video > GIF

Be honest about fixes
Don't hide that something was broken
"Fixed" is better than pretending it was never an issue

Know your audience
- Customers: Benefits and "how to"
- Developers: Technical details and breaking changes
- Team: Impact and metrics

Remember:
Release notes are marketing, not just documentation.
Make users excited, not just informed.

</meta_guidance>

</release_notes>
```

</details>

---

### Create FAQ


**📋 Use Case:** Need FAQ for new feature, product, or common questions

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Question anticipation, objection handling, progressive disclosure

<details>
<summary>Click to view prompt</summary>

```
<faq_creation>

<faq_inputs>
WHAT'S THE FAQ FOR:
- [ ] New feature launch
- [ ] Product in general
- [ ] Pricing/billing
- [ ] Technical integration
- [ ] Sales enablement
- [ ] Support documentation

WHO'S ASKING:
- [ ] Customers (current users)
- [ ] Prospects (considering buying)
- [ ] Sales team (need answers to close deals)
- [ ] Support team (need to answer tickets)

WHAT YOU KNOW:
- Common questions you've heard: [List them]
- Pain points or confusion: [What trips people up]
- Objections you hear: [Why people hesitate]

CONTEXT:
[Brief description of what this is about]
</faq_inputs>

<faq_framework>

You write FAQs that actually answer questions, not marketing fluff. Your job: anticipate what users ask, give straight answers.

---

## FAQ STRUCTURE

[Category if multiple topics]

### [Question in user's words]

[Short, direct answer]

[Optional: More detail if needed]

[Optional: Link to longer doc/video]

---

EXAMPLE:

### How much does it cost?

Plans start at $29/month for up to 10 users. Enterprise pricing is custom based on your team size and needs.

https://www.notion.so/link

---

### Can I try it for free?

Yes, 14-day free trial. No credit card required. You get full access to all features.

https://www.notion.so/link

</faq_framework>

<faq_categories>

### COMMON FAQ CATEGORIES

Getting Started
- How do I sign up?
- What do I need to get started?
- How long does setup take?

Features & Capabilities
- What can I do with [feature]?
- Does it integrate with [tool]?
- What's the difference between [X] and [Y]?

Pricing & Billing
- How much does it cost?
- Can I change plans?
- What happens if I cancel?

Technical
- What are the system requirements?
- Is my data secure?
- What's your uptime SLA?

Support
- How do I get help?
- What's included in support?
- Can I talk to a human?

---

## YOUR FAQ

[Generate questions and answers based on context]

</faq_categories>

<faq_patterns>

### Pattern 1: Objection Handling

Question: "Is this hard to set up?"

Bad answer: "No, it's easy!"

Good answer: "Most teams are up and running in under 30 minutes. We'll help you import your data and our setup wizard walks you through each step. If you get stuck, chat support is available."

---

### Pattern 2: Comparison Questions

Question: "How is this different from [competitor]?"

Bad answer: "We're better!"

Good answer: "We focus on [your differentiation], while [competitor] focuses on [their strength]. Best for: You if [use case], them if [different use case]."

---

### Pattern 3: Concern Questions

Question: "What happens to my data if I cancel?"

Bad answer: "You can export it."

Good answer: "You can export all your data anytime (even after canceling). We keep your data for 30 days after cancellation, then permanently delete it. No lock-in."

---

### Pattern 4: "Will this work for me?" Questions

Question: "Does this work for [specific use case]?"

Bad answer: "Yes, it works for everyone!"

Good answer: "Yes, [specific capability that addresses use case]. For example, [customer name] uses it for [similar use case]. [Link to case study]."

</faq_patterns>

<meta_guidance>

FAQ principles:Write questions as users ask them
Not: "What are the features?"
But: "Can I do [specific thing I care about]?"

Answer the actual question
Don't dodge or market-speak
If answer is "no" or "not yet," say so

Anticipate follow-ups
After answering, think: "What would they ask next?"

Keep answers short
2-3 sentences ideal
Link to more detail if needed

Use real language
Not: "Our platform facilitates..."
But: "You can..."

Update regularly
FAQ is living document
Add new questions as they come up

Remember:
Good FAQ reduces support load.
Bad FAQ creates more questions.

</meta_guidance>

</faq_creation>
```

</details>

---

### Generate Test Plan

**📋 Use Case:** About to launch, need to document what to test before shipping

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Edge case identification, scenario coverage, acceptance criteria expansion

<details>
<summary>Click to view prompt</summary>

```
<test_plan>

<test_inputs>
WHAT YOU'RE TESTING:
[Feature or change description]

USER FLOWS:
[Main paths users will take]

KNOWN EDGE CASES:
[Unusual scenarios you're aware of]

PLATFORMS:
- [ ] Web (desktop)
- [ ] Web (mobile)
- [ ] iOS app
- [ ] Android app
- [ ] API

INTEGRATION POINTS:
[What this touches - other features, systems, APIs]

RISK AREAS:
[What you're most worried could break]
</test_inputs>

<plan_framework>

You create test plans that find bugs before users do. Your job: think of everything that could go wrong.

---

## TEST PLAN

### Test Coverage

Happy Path (Must test):
- [ ] [Main user flow works end-to-end]
- [ ] [Success states display correctly]
- [ ] [Expected outcome happens]

Edge Cases (Must test):
- [ ] [Boundary condition]
- [ ] [Unusual input]
- [ ] [Maximum/minimum values]

Error Cases (Must test):
- [ ] [What happens when it fails]
- [ ] [Error messages are clear]
- [ ] [User can recover]

Integration (Must test):
- [ ] [Works with feature X]
- [ ] [Doesn't break feature Y]
- [ ] [API calls succeed]

Cross-Platform (Must test):
- [ ] [Works on mobile]
- [ ] [Works on different browsers]
- [ ] [Responsive design works]

Performance (Should test):
- [ ] [Loads fast enough]
- [ ] [Handles expected volume]

Security (If applicable):
- [ ] [Permissions work correctly]
- [ ] [Can't access others' data]

---

### Test Scenarios

SCENARIO 1: [Happy path name]Setup:
- User state: [New user, logged in, etc.]
- Prerequisites: [What needs to be true]

Steps:
1. [Action]
2. [Action]
3. [Action]

Expected Result:
[What should happen]

Actual Result:
[Leave blank for tester to fill]

---

SCENARIO 2: [Edge case name]

[Same structure]

---

### Acceptance Criteria Checklist

From the PRD/spec, these must all pass:

- [ ] [Acceptance criteria 1]
- [ ] [Acceptance criteria 2]
- [ ] [Acceptance criteria 3]

---

### Things That Should NOT Break

- [ ] [Existing feature that this could affect]
- [ ] [Another feature]
- [ ] [Core workflow]

---

### Test Data Needed

- [ ] Test account with [specific setup]
- [ ] Sample data for [use case]
- [ ] Edge case data (empty, max, special chars)

---

### Known Issues / Won't Fix

- [Issue we're shipping with (with rationale)]
- [Edge case we're not handling yet]

</plan_framework>

<test_scenarios>

### Common Scenarios to Test

Empty States:
- What if user has no data yet?
- What if search returns nothing?
- What if list is empty?

Maximum/Minimum:
- What if user has 10,000 items?
- What if user has 1 item?
- What if field is at character limit?

Special Characters:
- What if name has apostrophe? (O'Brien)
- What if email has + in it?
- What if description has emoji?

Timing:
- What if two actions happen simultaneously?
- What if user clicks button multiple times?
- What if session expires mid-flow?

Permissions:
- What if user is admin vs regular user?
- What if user tries to access others' data?
- What if user is read-only?

Network:
- What if API call fails?
- What if request times out?
- What if user is offline?

Browser/Device:
- Does it work in Safari, Chrome, Firefox?
- Does it work on iPhone, Android, tablet?
- Does it work with keyboard only?

</test_scenarios>

<meta_guidance>

Test plan principles:Think like an attacker
How would you break this?
What's the weirdest thing a user could do?

Test the unhappy paths
Happy path usually works
It's the errors that surprise you

Don't just test features
Test that you didn't break other things

Write it before building
Test plan reveals gaps in spec
Better to find them before coding

Not everything needs testing
Focus on:
- High-risk changes
- User-facing features
- Integration points

Remember:
Good test plan finds bugs in QA.
Bad test plan finds bugs in production.

</meta_guidance>

</test_plan>
```

</details>

---

### Write Product Brief/One-Pager

**📋 Use Case:** Need concise doc to align stakeholders on what you're building and why

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Pyramid principle, executive summary format, decision-focused structure

<details>
<summary>Click to view prompt</summary>

```
<product_brief>

<brief_inputs>
WHAT'S THE BRIEF FOR:
- [ ] New feature
- [ ] New product
- [ ] Initiative/project
- [ ] Strategic direction

WHO'S READING IT:
- [ ] Execs (need to approve)
- [ ] Team (need to build)
- [ ] Stakeholders (need to align)
- [ ] Cross-functional partners

CURRENT STATUS:
- [ ] Idea/proposal (seeking buy-in)
- [ ] Approved (documenting decision)
- [ ] In progress (status update)

CONTEXT:
- What you're proposing: [Description]
- Why it matters: [Business case]
- Key trade-offs: [What you're saying no to]
</brief_inputs>

<brief_framework>

You write product briefs that get to the point. Your job: fit everything decision-makers need on one page.

---

## PRODUCT BRIEF

Project: [Name]
Owner: [Your name]
Date: [Date]
Status: [Proposal / Approved / In Progress]

---

### TL;DR (3 sentences)

[What it is, why it matters, what you need]

---

### Problem

User pain: [Specific problem users have]

Business impact: [Cost of not solving this]
- [Metric 1]: [Current state and impact]
- [Metric 2]: [Current state and impact]

Why now: [Urgency or opportunity]

---

### Solution

What we're building: [High-level approach]

How it works: [Key user flow in 3-4 bullets]
1. [Step]
2. [Step]
3. [Step]

Why this approach: [Rationale for this vs alternatives]

---

### Success Metrics

Primary: [The one metric that matters]
- Baseline: [Current]
- Target: [Goal]
- Timeline: [When]

Secondary:
- [Supporting metric]
- [Supporting metric]

---

### Scope

In scope:
- [What we're building]
- [What's included]

Out of scope:
- [What we're explicitly NOT doing]
- [Future phase considerations]

---

### Investment

Resources needed:
- Engineering: [X weeks]
- Design: [Y weeks]
- Other: [Specify]

Timeline:
- Kickoff: [Date]
- Launch: [Date]

---

### Risks & Mitigations

Risk 1: [What could go wrong]
- Mitigation: [How we'll address it]

Risk 2: [Another risk]
- Mitigation: [How we'll address it]

---

### Decision Needed

Ask: [What you need from stakeholders]
- [ ] Approval to proceed
- [ ] Resource allocation
- [ ] Prioritization decision
- [ ] Other: [Specify]

By when: [Decision deadline]

</brief_framework>

<brief_templates>

### Template 1: Feature Proposal

WHY THIS MATTERS:
[Problem and business case in 2-3 sentences]

WHAT WE'RE BUILDING:
[Solution in 2-3 sentences]

EXPECTED IMPACT:
[Metrics and estimates]

INVESTMENT:
[Time and resources]

ALTERNATIVES CONSIDERED:
[What else we looked at and why we didn't choose it]

NEXT STEPS:
[What happens if approved]

---

### Template 2: Initiative Brief

STRATEGIC CONTEXT:
[How this fits company goals]

THE OPPORTUNITY:
[Market, user, or business opportunity]

OUR APPROACH:
[High-level strategy]

SUCCESS LOOKS LIKE:
[Clear outcomes, not outputs]

WHAT WE NEED:
[Resources, decisions, support]

---

### Template 3: Technical Architecture Brief

CURRENT STATE:
[What exists today and limitations]

PROPOSED CHANGE:
[What we want to build/change]

TECHNICAL APPROACH:
[Architecture, stack, key decisions]

TRADE-OFFS:
[What we're optimizing for vs not]

MIGRATION PATH:
[How we get from current to future]

</brief_templates>

<meta_guidance>

Product brief principles:One page max
If you can't fit it on one page, it's not clear enough
Exception: Appendix for detailed specs

Lead with why
Don't bury the business case
Start with problem and impact

Make the ask clear
What decision do you need?
By when?

Show trade-offs
What are you NOT doing?
What's the downside of this approach?

Include alternatives
Shows you thought it through
Explains why this is the best path

Use visuals
Diagram > paragraphs
Screenshot > description

Remember:
Brief is sales tool AND alignment doc.
Get buy-in AND document decision.

</meta_guidance>

</product_brief>
```

</details>

---

### All-Hands Presentation

**📋 Use Case:** Need to update whole company on product progress/wins/direction

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Story arc construction, data visualization, executive messaging

<details>
<summary>Click to view prompt</summary>

```
<all_hands_presentation>

<presentation_inputs>
WHAT YOU'RE PRESENTING:
- [ ] Quarterly update
- [ ] Big launch announcement
- [ ] Strategic direction change
- [ ] Wins/milestones
- [ ] Roadmap preview

YOUR CONTENT:
- Key metrics: [What you want to share]
- Wins: [What shipped, what worked]
- Challenges: [What you're tackling]
- What's next: [Preview of roadmap]

AUDIENCE:
- Company size: [Number of people]
- Technical level: [Mix of eng/non-eng]
- What they care about: [Company goals, their work, impact]

TIME LIMIT:
[5 min / 10 min / 15 min]
</presentation_inputs>

<presentation_framework>

You create all-hands presentations that inform and inspire. Follow this structure:

STEP 1: Start with the headline

First slide = the most important thing

Bad opening:
"Hi everyone, today I'm going to talk about Q3 product updates..."

Good opening:
"We hit 1M users this quarter. Here's how we did it and what's next."

Hook formats:
- Big number: "We shipped 47 features this quarter"
- Customer win: "Fortune 500 company signed because of [feature]"
- Milestone: "We're now the #1 product in our category"
- Challenge: "We lost 15% of users to competitor. Here's our response."

STEP 2: Build narrative arcStructure:
1. Where we were (context)
2. What we did (progress)
3. What we learned (insights)
4. Where we're going (future)

Time allocation for 10-min presentation:
- 1 min: Hook + context
- 3 min: What happened (metrics, wins)
- 2 min: What we learned
- 3 min: What's next
- 1 min: Q&A setup

STEP 3: Show, don't just tellUse visuals:
- Charts for metrics (line graphs for trends)
- Screenshots for features
- Customer quotes for impact
- Simple diagrams for strategy

Don't:
- Walls of text
- Complex diagrams
- 10 bullet points per slide
- Tiny font

Do:
- One idea per slide
- Big numbers you can read from back
- Simple visuals
- High-contrast colors

STEP 4: Connect to company goals

Every update should answer: "So what?"

Formula:
"We [did thing] which moved [metric] which helps company [achieve goal]"

Example:
"We shipped mobile app which increased DAU 30% which gets us closer to our 10M user goal"

STEP 5: Be honest about challenges

Don't just show wins. Show reality.

What to share:
- Metrics that didn't move
- Features that flopped
- Competitive threats
- What you're doing about it

This builds credibility:
- Shows you're self-aware
- Invites help from company
- Realistic about challenges

STEP 6: Make it memorablePeople remember:
- Stories about customers
- Surprising data points
- Clear takeaways
- Emotional moments

People forget:
- Generic metrics
- Feature lists
- Vague strategies

Use the "rule of 3":
- 3 main points
- 3 wins
- 3 priorities

STEP 7: End with clear call-to-actionWhat do you want people to do?
- Try the new feature
- Give feedback
- Help with [specific thing]
- Celebrate the win

Bad ending:
"That's it. Any questions?"

Good ending:
"Try the new mobile app this week. We need your feedback. Slack me what you think."

</presentation_framework>

---

## ALL-HANDS PRESENTATION SCRIPT

Title: [Catchy title]Date: [When presenting]Time: [Duration]Audience: [Company all-hands]

---

### SLIDE 1: The Hook

Visual: [Big number or striking image]

What you say:
"[Opening line that grabs attention]"

Example:
Visual: "1,000,000" in huge font
Say: "We hit one million users this quarter. Three years ago, we had 100. Here's how we got here and where we're going."

Goal: Make them pay attention for next 10 minutes.

---

### SLIDE 2: Context (Where We Were)

Visual: [Timeline or before/after]

What you say:
"Quick context. [Time period] ago, we were [state]. Our goal was [objective]."

Example:
"Six months ago, we were losing users to competitors. Our goal: Win back market share by building what customers actually want."

Keep this short: 30-60 seconds max.

---

### SLIDE 3: Progress Overview

Visual: [Dashboard-style with key metrics]

Metrics to show:
- [Primary metric]: [X → Y] ([Z% change])
- [Secondary metric]: [A → B]
- [Impact metric]: [Result]

What you say:
"Here's what happened. [Metric 1] went from X to Y. [Metric 2] improved by Z%. This means [business impact]."

Example:
Visual: Chart showing user growth
Say: "Active users went from 700K to 1M - 43% growth. Revenue per user increased 20%. We're now profitable on a unit basis."

---

### SLIDE 4-6: The Wins (What We Did)

SLIDE 4: Win #1Visual: [Screenshot or customer quote]

What you say:
"First big win: [Feature/initiative]. We shipped this because [customer problem]."

Impact:
- [Metric] improved by [X%]
- [Customer quote if you have it]
- [Business result]

Example:
Visual: Screenshot of mobile app
Say: "We launched mobile app. 40% of new users now come from mobile. Customer said: 'Finally, I can use this on the go.' This opened entirely new use case."

---

SLIDE 5: Win #2

[Same format]

---

SLIDE 6: Win #3

[Same format]

---

### SLIDE 7: What We Learned

Visual: [Simple icon or image]

What you say:
"Here's what surprised us."

Lessons (pick 2-3):
- Lesson 1: [Unexpected finding]
- "We thought [assumption], but actually [reality]"
- Lesson 2: [Customer insight]
- "Customers told us [feedback]"
- Lesson 3: [Strategic insight]
- "This taught us [bigger principle]"

Example:
"Three surprises:
1. Enterprise customers care more about mobile than we thought
2. Users wanted simple, not powerful - we over-built
3. Our biggest competitor isn't who we expected"

---

### SLIDE 8: Challenges (What Didn't Work)

Visual: [Chart showing the problem]

What you say:
"Not everything worked. Let's be honest about what didn't."

Challenge format:
- What went wrong: [Specific thing]
- Why: [Root cause]
- What we're doing: [Fix]

Example:
Visual: Chart showing flat conversion rate
Say: "Conversion rate didn't move despite 10 features shipped. Why? We built what we wanted, not what users needed. Fix: We're doing 50 customer interviews this month to actually understand the problem."

Be honest, not defensive.

---

### SLIDE 9: Customer Impact

Visual: [Customer logo or quote]

What you say:
"Here's what this means for customers."

Show real impact:
- Customer story
- Quote from user
- Metric that shows value

Example:
Visual: Quote "This saved our team 10 hours per week" - Sarah, PM at TechCo
Say: "We're not just building features. We're actually saving customers time. Sarah's team cut meeting prep from 10 hours to 2 hours per week using our new templates."

Make it human, not just numbers.

---

### SLIDE 10: What's Next (Roadmap Preview)

Visual: [Timeline or 3 boxes]

What you say:
"Here's what's coming."

Show 3 things:
1. This month: [Immediate priority]
2. This quarter: [Bigger initiative]
3. This year: [Vision item]

Example:
"Next 90 days:
1. This month: Ship AI-powered search
2. This quarter: Launch enterprise tier
3. This year: Become the platform our customers build on"

Don't show detailed roadmap. Show direction.

---

### SLIDE 11: How You Can Help

Visual: [Call-to-action]

What you say:
"Here's how you can help."

Specific asks:
- [ ] "Try [feature] and give feedback in #product-feedback"
- [ ] "Refer enterprise customers to sales team"
- [ ] "If you know anyone at [target companies], introduce us"

Example:
"Three ways to help:
1. Use the mobile app this week - we need your feedback
2. Sales team: New mobile pitch deck is ready
3. Know any PM hiring managers? We're hiring 2 PMs"

Make asks concrete and easy.

---

### SLIDE 12: Thank You

Visual: [Team photo or celebratory image]

What you say:
"This wouldn't be possible without [teams who helped]. Special shoutout to [names/teams]."

Be specific about appreciation:
- Eng team shipped X features
- Design nailed the mobile experience
- Sales team provided crucial customer feedback
- Support handled 2x volume without breaking

End with energy:
"Excited for what's next. Questions?"

---

## PRESENTATION NOTES

### Tone & Delivery

Energy level: [High/Medium - match what's appropriate]

Pacing:
- Slow down for important points
- Speed up for background/context
- Pause after big reveals

Eye contact:
- Don't read slides
- Scan the room
- Look at Zoom if remote

Enthusiasm:
- Be genuinely excited about wins
- Be candid about challenges
- Be inspiring about future

---

### Anticipated Questions

Q: "Why didn't [feature] ship?"
A: [Prepared answer]

Q: "How does this compare to competitor?"
A: [Prepared answer]

Q: "What's the biggest risk?"
A: [Honest answer]

Q: "When will [requested feature] ship?"
A: [Honest timeline or "not prioritized yet, here's why"]

---

### Backup Slides (If Needed)

Detailed metrics: [Link to full dashboard]

Full roadmap: [More detailed view]

Competitive analysis: [If questions come up]

Customer case studies: [More examples]

---

### Follow-Up

After presentation:
- [ ] Share slides in #general
- [ ] Post recording for those who missed
- [ ] Send detailed metrics to leadership
- [ ] Document questions asked + answers
- [ ] Follow up on commitments made

Feedback collection:
- [ ] "How'd this presentation land?" in Slack
- [ ] Note what resonated
- [ ] Note what confused people
- [ ] Improve for next time

</all_hands_presentation>
```

</details>

---

### Board Deck Prep

**📋 Use Case:** Prepare product update for board meeting - high-level strategic view

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Executive summary, trend analysis, risk articulation

<details>
<summary>Click to view prompt</summary>

```
<board_deck>

<deck_inputs>
MEETING CONTEXT:
- Board meeting date: [When]
- Time allocated: [5 min / 10 min / 15 min]
- Last board meeting: [When, what you said]
- Board composition: [Who's on board, their backgrounds]

YOUR CONTENT:
- Metrics: [Key numbers to share]
- Progress: [What shipped since last meeting]
- Strategy: [Any direction changes]
- Asks: [What you need from board]

COMPANY STAGE:
- [ ] Seed/Series A (product-market fit)
- [ ] Series B/C (scaling)
- [ ] Late stage (optimization)
</deck_inputs>

<deck_framework>

You create board decks that inform and build confidence. Follow this approach:

STEP 1: Understand what board cares aboutBoard members want to know:
- Are we on track? (vs plan)
- What changed? (good and bad)
- What are the risks? (what keeps PM up at night)
- What do you need? (resources, decisions)

Board members DON'T care about:
- Feature details
- Day-to-day operations
- Tactical execution
- Team drama

Keep it strategic.STEP 2: Structure for boardIdeal structure:
1. TL;DR (Executive summary - 1 slide)
2. Metrics (What's happening - 2-3 slides)
3. Progress (What we did - 2 slides)
4. Strategy (Where we're going - 2 slides)
5. Risks (What could go wrong - 1 slide)
6. Asks (What we need - 1 slide)

Total: 8-10 slides for 15-min sectionSTEP 3: Lead with the bottom lineFirst slide = executive summary

Answer these questions upfront:
- Are we on track? (Yes/no/mostly)
- What's working? (1 sentence)
- What's not? (1 sentence)
- What's next? (1 sentence)

Then:
"Details follow, but happy to jump to any section."

This lets board direct conversation.STEP 4: Show trends, not snapshotsBad: "We have 100K users"
Good: "We grew from 75K to 100K users (33% QoQ), ahead of 90K target"

Always show:
- Current number
- Previous number
- Target/plan
- Trend direction

Use arrows: ↑ ↓ → to show movement

STEP 5: Be honest about problemsBoard appreciates honesty:
- Don't hide bad news
- Don't spin problems as "opportunities"
- Show you understand the issue
- Have a plan to address it

Format for bad news:
- What's wrong: [Specific problem]
- Why it matters: [Business impact]
- What we're doing: [Action plan]
- When we'll know if it worked: [Timeline/metric]

STEP 6: Frame risks properlyRisk categories:
- Execution risks: Can we build/ship this?
- Market risks: Will customers want it?
- Competitive risks: What if competitor does X?
- Resource risks: Do we have enough people/money?

For each risk:
- Likelihood (high/med/low)
- Impact if it happens
- Mitigation plan

Don't:
- List 20 risks (shows lack of focus)
- Downplay serious risks
- Present risks without mitigation

STEP 7: Make clear asksBoard can help with:
- Strategic decisions (enter new market?)
- Resource allocation (need 10 more eng?)
- Introductions (need enterprise customers?)
- Competitive intelligence (what are they hearing?)

Bad ask: "We need to hire more"
Good ask: "We need to hire 5 senior eng for platform team to hit Q3 launch. Budget implications: [X]. Alternative is 3-month delay."

Be specific about:
- What you need
- Why you need it
- What happens if you don't get it
- What you're asking them to do

STEP 8: Prepare for questionsCommon board questions:
- "Why is [metric] down?"
- "How do we compare to competitor?"
- "What's your biggest concern?"
- "What would you do with 2x the budget?"
- "What keeps you up at night?"

Have answers ready.

</deck_framework>

---

## BOARD DECK OUTLINE

Meeting: [Date]Product UpdatePresenter: [Your name]Time: [Minutes allocated]

---

### SLIDE 1: Executive Summary

Visual: [Traffic light: Green/Yellow/Red status]

Overall Status: [On track / Needs attention / Behind]

Key Points:
- Progress: [One sentence on what shipped]
- Metrics: [One sentence on performance]
- Challenge: [One sentence on biggest issue]
- Ask: [One sentence on what you need]

Example:Status: ✅ On Track  Progress: Shipped enterprise tier, acquired 3 Fortune 500 customers Metrics: ARR grew 45% QoQ to $12M, on pace for $50M target Challenge: Platform stability issues at scale (addressing with infra investment) Ask: Approve $2M budget increase for infrastructure teamThis slide should tell complete story.

---

### SLIDE 2: Metrics Dashboard

Visual: [4-6 key metrics with trends]

Format for each metric:[Metric Name] [Big number] ↑ [% change] vs [time period] Target: [Goal] Status: [On track / Behind / Ahead]Metrics to include:
- North star metric (usage/engagement)
- Growth metric (users, revenue)
- Quality metric (NPS, retention)
- Efficiency metric (CAC, LTV)

Example:Monthly Active Users 125K ↑ 35% vs Q1 Target: 120K ✅ Ahead Plan: Hit 200K by EOY  Net Revenue Retention 118% ↑ 5 pts vs Q1 Target: 115% ✅ Ahead Best in class for our stage

---

### SLIDE 3: Metrics Deep Dive (if needed)

Visual: [Chart showing trend over time]

What to show:
- Line graph of key metric over quarters
- Cohort analysis if relevant
- Segment breakdown if important

What to say:
"[Metric] has grown consistently for [time period]. Growth driven by [factor]. One concern: [potential issue]."

Keep it simple: One chart, one insight.

---

### SLIDE 4: Product Progress

Visual: [Timeline or checklist]

What shipped since last board meeting:Q[X] Deliverables:
- ✅ [Major feature] - [Impact]
- ✅ [Another feature] - [Impact]
- ✅ [Initiative] - [Impact]
- 🔄 [In progress item] - [Expected completion]

Key Wins:
- [Customer win]
- [Metric improvement]
- [Strategic milestone]

Example:Q2 Deliverables: ✅ Enterprise SSO - Unblocked 5 enterprise deals ($3M ARR) ✅ Mobile app - 40% of new users now mobile-first ✅ API platform - 20 partners integrated 🔄 AI features - Shipping Q3  Key Win: Closed Acme Corp ($1M ARR) - largest deal ever

---

### SLIDE 5: Customer/Market Traction

Visual: [Customer logos or market map]

Traction indicators:
- New customers (logos if impressive)
- Customer quotes
- Usage milestones
- Market position

Format:Customer Traction: - 3 Fortune 500 customers acquired - 95% customer satisfaction (NPS: 65) - Quote: "[Impressive customer quote]" - [Name, Title, Company]  Market Position: - #2 in G2 category (up from #5) - Mentioned in Gartner report - 15% market share (up from 8%)

---

### SLIDE 6: Strategic Direction

Visual: [Simple roadmap or 3 pillars]

What you're focused on:Current Strategy:
[One sentence describing focus]

Three Priorities:
1. [Priority 1]: [Why + Expected impact]
2. [Priority 2]: [Why + Expected impact]
3. [Priority 3]: [Why + Expected impact]

Example:Strategy: Become the platform enterprise teams build on  Priorities: 1. Platform/API: Enable 100 integrations by EOY (currently 20) 2. Enterprise features: SSO, SCIM, advanced permissions (Q3 launch) 3. AI capabilities: Stay ahead of competition in AI features  Why now: Enterprise is 70% of new ARR, they need platform capabilities

---

### SLIDE 7: Competitive Landscape

Visual: [2x2 matrix or table]

Where you stand:Our Position:
[Leader / Strong / Gaining / Behind] in [market segment]

Key Competitors:
- [Competitor A]: [Their strength / Our advantage]
- [Competitor B]: [Their strength / Our advantage]

Recent Moves:
- [Competitor] launched [feature] - Our response: [Action]
- We launched [thing] - Differentiation: [Why we win]

Win rate vs competitors: [X%] (trend: [↑/↓/→])

Example:Position: Strong #2, gaining on leader  Competitor X (market leader): - Strength: Brand, enterprise presence - Our advantage: 3x faster, modern UX, better pricing  Competitor Y (rising threat): - Strength: AI features, venture-backed - Our advantage: Enterprise-ready, proven at scale  Win rate: 65% (↑ from 55% last quarter)

---

### SLIDE 8: Risks & Mitigations

Visual: [Risk matrix or table]

Top Risks:Risk 1: [Specific risk]
- Likelihood: [High/Med/Low]
- Impact: [High/Med/Low]
- Mitigation: [What we're doing]
- Owner: [Who's responsible]

Risk 2: [Another risk]
[Same format]

Example:Risk 1: Platform instability at scale - Likelihood: High (seeing issues at 100K+ users) - Impact: High (customer churn, reputation) - Mitigation: $2M infrastructure investment, dedicated platform team - Timeline: Resolved by Q3  Risk 2: Competitor launches AI feature first - Likelihood: Medium (they're 3 months behind) - Impact: Medium (could slow growth) - Mitigation: Accelerating AI roadmap, shipping beta in 6 weeksBoard appreciates you thinking ahead.

---

### SLIDE 9: Resource Needs & Trade-offs

Visual: [Budget or headcount chart]

What you need:Current State:
- Team size: [X people]
- Budget: $[Y]/quarter
- Velocity: [What you can ship]

Request:
- Additional headcount: [+Z people] in [roles]
- Additional budget: $[W] for [purpose]
- Timeline: [When you need it]

Trade-offs:
- If approved: [What you can do]
- If not: [What you'll cut/delay]

ROI:
[Expected return on investment]

Example:Current: 20 eng, shipping 8 features/quarter  Request: +10 eng ($500K/quarter) - 5 platform eng - 3 AI/ML eng - 2 mobile eng  If approved: Ship platform + AI features in Q3 (unlocks $5M ARR) If not: Delay platform to Q4, cut AI features (risk losing to competitors)  ROI: $5M ARR from $2M investment = 2.5x in year 1

---

### SLIDE 10: Questions & Discussion

Visual: [Open for discussion]

Potential board questions:Prepared answers for:
- "Why is [metric] trending that way?"
- "How are you thinking about [competitor]?"
- "What's your biggest concern?"
- "What would you do with 2x the resources?"
- "What are you NOT doing that you should be?"

Documents available:
- Detailed metrics: [Link]
- Full roadmap: [Link]
- Competitive analysis: [Link]

---

## APPENDIX SLIDES (If Needed)

### Detailed Roadmap

Visual: [Quarter-by-quarter view]

[Show next 3-4 quarters of planned work]

---

### Customer Case Studies

Visual: [Logos + metrics]

[2-3 impressive customer stories with data]

---

### Team & Organization

Visual: [Org chart or team breakdown]

[If board asking about team structure]

---

### Financial Impact

Visual: [Revenue/cost projections]

[If board needs to connect product to financials]

---

## PRESENTATION NOTES

### Delivery Tips

Tone:
- Confident but not arrogant
- Honest about challenges
- Excited about future
- Respectful of board's time

Pacing:
- 1-2 minutes per slide
- Slow down for important points
- Be ready to skip slides if discussion emerges

Engagement:
- Pause for questions
- Make eye contact
- Read the room
- Don't be defensive

---

### Follow-Up Actions

After meeting:
- [ ] Send detailed metrics to board members
- [ ] Document decisions made
- [ ] Follow up on commitments
- [ ] Share feedback with team
- [ ] Update internal stakeholders

Before next meeting:
- [ ] Track progress on commitments
- [ ] Prepare status on asks
- [ ] Update on risks flagged

</board_deck>
```

</details>

---

### Product Document Critique

**📋 Use Case:** Get detailed, actionable feedback on product documents (PRDs, briefs, charters, one-pagers)

**🛠️ Recommended Tools:** Claude Projects, Claude Code

**💡 Technique:** Multi-phase diagnostic framework with scoring, stress tests, and surgical line-by-line critique

<details>
<summary>Click to view prompt</summary>

```
<document_critique>

<inputs>
Upload the product document you want improved (PRD, brief, charter, one-pager, etc.)

OPTIONAL CONTEXT:
1. What stage is this document? (early draft, stakeholder review, near-final)
2. Who is the primary audience? (engineers, executives, cross-functional team)
3. What feedback have you already received? (if any)
4. What's your biggest concern about this document?
5. Any constraints? (page limits, template requirements, timeline)
</inputs>

<critique_process>

You are a senior product leader who has reviewed hundreds of product documents. You're known for giving feedback that's surgical, specific, and actionable—not vague praise or generic suggestions. Your job is to make this document significantly stronger.

PHASE 1: DOCUMENT TRIAGE (30-second scan)

Read the document quickly and answer:
1. Can I explain what we're building and why in one sentence?
2. Is there a clear ask or decision needed?
3. Does this feel complete or obviously incomplete?
4. What's my gut reaction? (Confident? Confused? Skeptical?)

TRIAGE VERDICT: [READY FOR FEEDBACK | NEEDS FUNDAMENTALS | START OVER]
- READY FOR FEEDBACK: Structure exists, can be improved
- NEEDS FUNDAMENTALS: Missing core sections, major gaps
- START OVER: Problem/solution mismatch, wrong document type

---

PHASE 2: DIAGNOSTIC SCORING

Rate each dimension 1-5 and explain why:

### 2.1 PROBLEM CLARITY (Is the "why" compelling?)
- [ ] Problem is specific, not generic
- [ ] Evidence supports the problem exists
- [ ] Impact is quantified (users affected, cost, frequency)
- [ ] Reader understands why this matters NOW
- [ ] Not a solution disguised as a problem

SCORE: __/5
DIAGNOSIS: [What's weak and why]

### 2.2 SOLUTION CLARITY (Is the "what" crisp?)
- [ ] Solution directly addresses the stated problem
- [ ] Scope boundaries are explicit (what's IN and OUT)
- [ ] Key features/components are prioritized
- [ ] MVP vs. future phases are distinguished
- [ ] Reader can visualize the end state

SCORE: __/5
DIAGNOSIS: [What's weak and why]

### 2.3 SPECIFICITY (Can someone act on this?)
- [ ] Success metrics are measurable and timebound
- [ ] Edge cases and states are documented
- [ ] Dependencies are identified with owners
- [ ] Timelines have rationale, not just dates
- [ ] No weasel words ("improve," "better," "enhanced")

SCORE: __/5
DIAGNOSIS: [What's weak and why]

### 2.4 HIDDEN COMPLEXITY (Are the hard parts surfaced?)
- [ ] Technical risks are acknowledged
- [ ] Integration points are mapped
- [ ] Failure modes are considered
- [ ] Migration/rollback is addressed
- [ ] Open questions are flagged (not buried)

SCORE: __/5
DIAGNOSIS: [What's weak and why]

### 2.5 DECISION-READINESS (Can stakeholders say yes/no?)
- [ ] The ask is explicit
- [ ] Trade-offs are visible
- [ ] Risks and mitigations are paired
- [ ] Impact justifies the investment
- [ ] Next steps are clear

SCORE: __/5
DIAGNOSIS: [What's weak and why]

### 2.6 AUDIENCE FIT (Right depth for the reader?)
- [ ] Executive summary works for busy readers
- [ ] Technical depth is appropriate
- [ ] Jargon is defined or avoided
- [ ] Length matches importance
- [ ] Structure aids scanning

SCORE: __/5
DIAGNOSIS: [What's weak and why]

OVERALL SCORE: __/30
GRADE: [A: 26-30 | B: 21-25 | C: 16-20 | D: 11-15 | F: <11]

---

PHASE 3: FATAL FLAW ANALYSIS

Identify the TOP 3 issues that would cause this document to fail:

FATAL FLAW #1: [Name it]
- WHERE: [Section/paragraph]
- CURRENT TEXT: "[Quote the problematic text]"
- WHY IT'S FATAL: [Impact on reader/decision]
- THE FIX: [Specific rewrite or addition]

FATAL FLAW #2: [Name it]
- WHERE: [Section/paragraph]
- CURRENT TEXT: "[Quote the problematic text]"
- WHY IT'S FATAL: [Impact on reader/decision]
- THE FIX: [Specific rewrite or addition]

FATAL FLAW #3: [Name it]
- WHERE: [Section/paragraph]
- CURRENT TEXT: "[Quote the problematic text]"
- WHY IT'S FATAL: [Impact on reader/decision]
- THE FIX: [Specific rewrite or addition]

---

PHASE 4: LINE-BY-LINE TEARDOWN

Go section by section through the document:

### [SECTION NAME]

CURRENT STATE:
> [Quote key sentences]

ISSUES:
1. [Specific problem]
2. [Specific problem]

REWRITE:
> [Provide improved version]

WHY THIS IS BETTER:
[1-2 sentences explaining the improvement]

---

PHASE 5: MISSING PIECES

What's completely absent that should exist?

| Missing Element | Why It Matters | Suggested Content |
|----------------|----------------|-------------------|
| [Element] | [Impact] | [Draft or outline] |
| [Element] | [Impact] | [Draft or outline] |
| [Element] | [Impact] | [Draft or outline] |

---

PHASE 6: THE STRESS TESTS

Run these scenarios and document failures:

### 6.1 THE SKEPTICAL ENGINEER
"I have to build this. What questions do I have?"
- Question 1: [Question] → [Is it answered? Where?]
- Question 2: [Question] → [Is it answered? Where?]
- Question 3: [Question] → [Is it answered? Where?]
VERDICT: [PASS | PARTIAL | FAIL]

### 6.2 THE BUSY EXECUTIVE
"I have 2 minutes. Can I make a decision?"
- Problem clear in 30 sec? [Y/N]
- Impact quantified? [Y/N]
- Ask explicit? [Y/N]
- Risk/reward obvious? [Y/N]
VERDICT: [PASS | PARTIAL | FAIL]

### 6.3 THE DEVIL'S ADVOCATE
"Why shouldn't we do this?"
- Is the strongest counterargument addressed? [Y/N]
- Are alternatives considered? [Y/N]
- Is "do nothing" evaluated? [Y/N]
VERDICT: [PASS | PARTIAL | FAIL]

### 6.4 THE 6-MONTHS-LATER TEST
"We shipped. Something went wrong. Can we trace why?"
- Are assumptions documented? [Y/N]
- Are trade-off rationales captured? [Y/N]
- Is the decision context preserved? [Y/N]
VERDICT: [PASS | PARTIAL | FAIL]

---

PHASE 7: VAGUE LANGUAGE AUDIT

Find and fix every instance of weak language:

| Original | Problem | Replacement |
|----------|---------|-------------|
| "improve user experience" | Unmeasurable | "[specific metric] by [X%]" |
| "many users" | Unquantified | "[N] users representing [X%] of [segment]" |
| "quickly" | Undefined | "within [X] seconds/days" |
| "if possible" | Scope ambiguity | "[IN scope / OUT of scope / DECISION NEEDED]" |
| "better" | Compared to what? | "[X% improvement from baseline of Y]" |

---

PHASE 8: IMPROVED DOCUMENT

Produce the complete improved document with all fixes applied.

Format: [Match original format or recommend better structure]

[FULL IMPROVED DOCUMENT HERE]

---

PHASE 9: CHANGE LOG

| Section | Change Type | Original | Improved | Rationale |
|---------|-------------|----------|----------|-----------|
| [Section] | [Added/Revised/Deleted] | [Summary] | [Summary] | [Why] |

---

PHASE 10: VALIDATION CHECKLIST

Before this document is ready:

MUST DO (blocking):
- [ ] [Action item with owner]
- [ ] [Action item with owner]
- [ ] [Action item with owner]

SHOULD DO (strengthening):
- [ ] [Action item with owner]
- [ ] [Action item with owner]

COULD DO (polish):
- [ ] [Action item with owner]

</critique_process>

<output_format>
1. **Executive Summary** (3-4 sentences)
   - Overall assessment
   - Biggest strength
   - Most critical fix needed
   - Ready for [audience] after [X changes]

2. **Diagnostic Scorecard** (the Phase 2 table)

3. **Top 3 Fatal Flaws** (Phase 3 - the must-fix items)

4. **Section-by-Section Teardown** (Phase 4 - detailed rewrites)

5. **Complete Improved Document** (Phase 8 - the deliverable)

6. **Change Log** (Phase 9 - what changed and why)

7. **Next Steps** (Phase 10 - what's needed before this is ready)
</output_format>

<critique_principles>
BE SPECIFIC: "The problem statement is weak" → "The problem statement doesn't quantify impact. Add: '[X] users encounter this [Y] times per week, costing [Z] in support tickets.'"

BE CONSTRUCTIVE: Don't just identify problems—provide the fix. Every critique includes a rewrite.

BE HONEST: If the document needs fundamental rework, say so. Don't polish a document that should be restarted.

BE PRIORITIZED: Not all issues are equal. Fatal flaws first, polish last.

PRESERVE VOICE: Improve clarity without erasing the author's style. The improved version should sound like a better version of them, not a different person.

SHOW THE DELTA: Make it obvious what changed and why. The author should learn from the critique, not just receive a new document.

CONTEXT MATTERS: A scrappy early draft needs different feedback than a near-final stakeholder review document.
</critique_principles>

</document_critique>
```

</details>

---


## Discovery

*11 prompts in this category*

### Synthesizing User Research

**📋 Use Case:** Have large amounts of user research data that needs to be analyzed and synthesized into actionable insights

**🛠️ Recommended Tools:** NotebookLM, Gemini

**💡 Technique:** Quote specific user feedback to support each insight

<details>
<summary>Click to view prompt</summary>

```
<user_research_synthesizer>

<research_inputs>
Upload your research materials and answer these questions:

RESEARCH MATERIALS:
- Interview transcripts (upload all)
- Survey results and raw data
- User feedback from support tickets, reviews, or forums
- Observational notes or usability test recordings
- Analytics data showing behavioral patterns
- Any existing synthesis or insights documents

CONTEXT QUESTIONS:
1. What are you trying to learn? (research goals/questions)
2. Who are these users? (segments, demographics, use cases)
3. What decisions will this research inform? (product, strategy, roadmap)
4. Are there any hypotheses you're testing?
5. What's the timeline for using these insights? (urgency level)
6. Who's the audience for the synthesis? (executives, designers, engineers, all)
7. What format do you need? (report, presentation, insights doc, user personas)
</research_inputs>

<synthesis_process>

You are a senior UX researcher known for finding the signal in the noise and translating user feedback into actionable product insights. Your syntheses reveal patterns that others miss and prioritize insights that drive decisions.

PHASE 1: IMMERSION & INVENTORY
First, understand what you're working with:

1. SCAN ALL MATERIALS
- How many users/participants total?
- What research methods were used? (interviews, surveys, observations, etc.)
- What date ranges does this cover?
- Are there different user segments represented?
- What was the original research goal?

2. IDENTIFY DATA QUALITY
- Which sources are strongest? (direct quotes, behavioral data, repeated patterns)
- Which sources are weakest? (secondhand reports, vague feedback, one-off comments)
- Are there any biases in who was included/excluded?
- What's missing that would strengthen the synthesis?

PHASE 2: THEMATIC ANALYSIS
Use rigorous qualitative analysis:

1. OPEN CODING (First Pass)
Read through all materials and tag every distinct concept, pain point, desire, or behavior mentioned. Cast a wide net - don't filter yet.

For each code:
- Quote the specific user feedback (exact words when possible)
- Note which user(s) said it
- Note the context (what they were doing, trying to accomplish)

2. PATTERN IDENTIFICATION (Second Pass)
Group codes into themes:
- Which concepts appear repeatedly across multiple users?
- Which appear across different research methods? (stronger signal)
- Which only appear once? (might be outlier or emerging need)
- Are there contradictions? (different user segments wanting different things)

For each theme, calculate:
- Frequency: How many users mentioned this? (X out of Y participants)
- Intensity: How strongly did they feel? (blocker vs. annoyance)
- Segment distribution: Which user types does this affect?

3. FIND THE "WHY" BEHIND THE "WHAT"
Users often describe symptoms, not root causes:
- If users say "this is too slow" → Why does speed matter in their workflow?
- If users say "I can't find X" → Why were they looking for X? What were they trying to do?
- If users say "I want feature Y" → What problem would Y solve for them?

Extract the underlying jobs-to-be-done, not just feature requests.

PHASE 3: PRIORITIZATION FRAMEWORK
Not all insights are equal. Prioritize by:

1. IMPACT POTENTIAL
- Critical: Blocking users from core workflows, driving churn
- High: Causing significant friction, daily pain points
- Medium: Occasional frustration, workarounds exist
- Low: Nice-to-have, edge cases

2. EVIDENCE STRENGTH
- Strong: Mentioned by multiple users, observed in behavior data, appears across methods
- Moderate: Mentioned by several users, consistent story
- Weak: One or two mentions, anecdotal, might be outlier

3. ACTIONABILITY
- Clear: We know what to build to address this
- Fuzzy: We understand the problem but solution is unclear
- Exploratory: Needs more research to understand

Create a 2x2 matrix: Impact (High/Low) vs. Evidence Strength (Strong/Weak)
Insights in "High Impact + Strong Evidence" quadrant are your top priorities.

PHASE 4: SYNTHESIS OUTPUT

Generate a comprehensive research synthesis with these sections:

## Executive Summary
- Key findings (top 3-5 insights) in priority order
- Bottom line: What should we do based on this research?
- Confidence level in these findings (and what would increase confidence)

## Research Overview
- Participants: [number, segments, how recruited]
- Methods: [interviews, surveys, etc. with sample sizes]
- Timeline: [when research was conducted]
- Goals: [what we were trying to learn]

## Key Insights

For each insight (top 8-10):

### [Insight Title - User-Centric, Not Feature-Focused]
What we learned: [1-2 sentence summary]

Evidence:
- Quote from User A: "[exact words]"
- Quote from User B: "[exact words]"
- Behavioral data: [specific numbers/patterns observed]
- Frequency: [X out of Y users mentioned this]

Why this matters:
[Impact on user experience, business metrics, product strategy]

User segments affected:
[Which types of users care most about this]

Current user workarounds:
[How are users trying to solve this now, if at all]

Potential solutions to explore:
[2-3 directions we could take, not prescriptive]

Priority: Critical/High/Medium/Low
Evidence strength: Strong/Moderate/Weak
Actionability: Clear/Fuzzy/Needs more research

## Themes & Patterns
Group related insights into larger themes:
- What are the 3-4 big patterns across all findings?
- How do these themes connect to our product strategy?
- Which themes are table-stakes vs. differentiators?

## Segment-Specific Insights
If relevant, break out findings by user segment:
- What does Segment A uniquely care about?
- Where do segments agree vs. disagree?
- Should we optimize for one segment over another?

## Contradictions & Open Questions
Be honest about what's unclear:
- Where did users contradict each other?
- What questions does this research raise?
- What would we want to learn next?

## Recommended Next Steps
Based on these insights:

Immediate Actions (do now):
- [Specific, actionable items with owners]

Short-term (next quarter):
- [Research to validate, features to explore]

Long-term (future strategy):
- [Bigger opportunities to investigate]

What NOT to do:
- [Ideas this research invalidated]

</synthesis_process>

<quality_checks>

After creating the synthesis, validate it:

1. THE QUOTE TEST
- Is every major insight backed by at least 2-3 direct user quotes?
- Are quotes in users' own words, not paraphrased?
- Do quotes capture the emotion, not just the fact?

2. THE FREQUENCY TEST
- Is it clear how many users mentioned each insight? (X out of Y)
- Have you distinguished between "every user said this" vs. "one user mentioned it"?
- Are priorities based on patterns, not individual voices?

3. THE ACTIONABILITY TEST
- Can a PM read this and know what to consider building?
- Can a designer read this and know what problems to solve?
- Can an executive read this and make strategic decisions?

4. THE HONESTY TEST
- Have you acknowledged weak signals and contradictions?
- Are you clear about what you don't know?
- Have you avoided cherry-picking quotes to support pre-existing beliefs?

5. THE SEGMENT TEST
- If different user types want different things, is that clear?
- Have you called out any underrepresented segments?
- Are you clear about who this research does and doesn't represent?

SELF-CRITIQUE: Improve any sections that fail these tests before finalizing.

</quality_checks>

<output_format>

1. Start with the Executive Summary - Decision-makers should get the key takeaways in 2 minutes

2. Full synthesis document following the structure above

3. Appendix materials (separate from main doc):
- Full quotes database organized by theme
- Participant details table
- Raw frequency counts for each code/theme
- Methodology notes and any limitations

4. One-pager version for busy stakeholders:
- Top 3 insights only
- 1 representative quote each
- Recommended actions
- Fits on one page/slide

</output_format>

<meta_guidance>

Great research synthesis:
- Surfaces non-obvious patterns, not just confirmation of what we expected
- Uses users' exact words to bring findings to life
- Distinguishes between what users say and what they actually need
- Makes priorities clear through evidence, not opinion
- Acknowledges uncertainty and contradictions honestly
- Connects insights to business/product decisions

Avoid:
- Death by bullet points (use quotes and stories)
- Treating all feedback equally (prioritize!)
- Reporting features users asked for without understanding why
- Cherry-picking quotes to support pre-existing beliefs
- Burying key insights deep in the document
- Vague insights like "users want it to be easier" without specifics

Remember: Your job is not to report everything users said. It's to find the patterns, prioritize the insights, and make it easy for your team to make good decisions. When in doubt, include the exact user quote - it's more powerful than your paraphrase.

</meta_guidance>

</user_research_synthesizer>
```

</details>

---

### Analyze Feature Requests

**📋 Use Case:** Flooded with feature requests from customers, sales, support—need to find patterns and prioritize

**🛠️ Recommended Tools:** Claude Projects, Airtable, Linear

**💡 Technique:** Pattern recognition, clustering similar requests, extracting underlying needs

<details>
<summary>Click to view prompt</summary>

```
<feature_request_analyzer>

<request_inputs>
Upload your feature request data and answer these questions:

FEATURE REQUEST DATA:
- Raw feature requests (CSV, spreadsheet, support tickets, sales notes)
- CRM data with customer context (company size, revenue, segment)
- Usage data (which customers are active vs. churning)
- Previous feature request history (what we've heard before)

CONTEXT QUESTIONS:
1. Where are these requests coming from? (sales calls, support tickets, in-app feedback, user interviews)
2. What's the time period? (last month, quarter, year)
3. How many total requests do you have?
4. What do you already know? (patterns you suspect but haven't validated)
5. What decisions will this inform? (roadmap, prioritization, customer conversations)
6. Are there specific customers whose feedback matters more? (enterprise, high-paying, strategic)
7. What's your current prioritization challenge? (too many requests, conflicting asks, unclear patterns)
</request_inputs>

<analysis_process>

You are a product strategist who excels at finding signal in noisy customer feedback. You distinguish between what customers ask for versus what they actually need, and identify patterns that reveal strategic opportunities.

PHASE 1: DATA CLEANING & ENRICHMENT

1. STANDARDIZE THE CHAOS
Feature requests come in messy. Clean them up:
- Remove duplicates (same request worded differently)
- Standardize terminology ("reporting" = "analytics" = "dashboards")
- Extract the actual request from conversation context
- Flag vague requests that need clarification ("make it better", "improve UX")

2. ENRICH WITH CONTEXT
For each request, capture:
- Customer details: Company name, segment, ARR, tenure
- Source: Sales call, support ticket, user interview, in-app feedback
- Urgency signals: Blocker, nice-to-have, deal risk, churn risk
- Competitive context: "Competitor X has this"
- Frequency: First time mentioned or repeated ask
- Workarounds: What are they doing instead?

3. CATEGORIZE BY TYPE
Not all requests are created equal:

Feature Requests - New capabilities
- Example: "Add SSO integration"
- What to track: Complexity, strategic value

Enhancements - Improvements to existing features
- Example: "Export should include more fields"
- What to track: Impact on adoption, usage data

Bug Reports Disguised as Requests - Things that should already work
- Example: "Make loading faster" (it shouldn't be slow)
- What to track: How broken is it currently

Solutions Looking for Problems - Customer proposing implementation
- Example: "Add a button that does X"
- What to track: Underlying need, not proposed solution

Complaints - Venting, not actionable
- Example: "This sucks"
- What to track: Which part actually needs fixing

PHASE 2: PATTERN ANALYSIS

1. CLUSTER BY UNDERLYING NEED
Group requests that solve the same problem:

Example clusters:
- Better Reporting (requests for exports, dashboards, analytics, custom reports)
- Collaboration (requests for comments, sharing, notifications, @mentions)
- Mobile Access (requests for app, responsive design, offline mode)

For each cluster:
- Theme name: [Clear, user-centric description]
- Underlying need: [What problem are users trying to solve?]
- Number of requests: [X total, Y unique customers]
- ARR represented: $[amount] from customers asking
- Customer segments: [Enterprise: X%, SMB: Y%]
- Sample requests: [3-4 representative quotes]

2. FREQUENCY ANALYSIS
How often is this requested?

High Frequency (mentioned by 20%+ of requesting customers)
- Clear market signal
- Likely competitive requirement
- Risk if we don't build

Medium Frequency (5-20% of customers)
- Specific segment need
- Potential differentiator
- Validate before committing

Low Frequency (<5% of customers)
- Might be edge case
- Could be emerging need
- Might be customer-specific

For each cluster, calculate:
- Total mentions across all time
- Unique customers requesting
- Trend: Increasing, stable, or decreasing over time

3. SEGMENT ANALYSIS
Do different customer types want different things?

Break down by:
- Company size: Enterprise vs. SMB vs. Startup
- Industry: Healthcare vs. Finance vs. SaaS etc.
- Geography: US vs. EU vs. APAC
- Product tier: Free vs. Paid vs. Enterprise
- Customer health: Happy vs. At-risk vs. Churning

Key questions:
- Are high-value customers asking for different things than low-value?
- Are churning customers asking for things current customers don't care about?
- Is there a segment-specific opportunity (build for enterprise, ignore SMB)?

4. URGENCY & IMPACT ANALYSIS

For each request cluster, assess:

Deal Impact:
- How many deals are blocked by not having this? [number]
- Total ARR at risk: $[amount]
- Quote from sales: "[specific example of lost deal]"

Churn Risk:
- How many customers threatened to leave over this? [number]
- ARR at risk: $[amount]
- Quote from customer: "[their actual words about churning]"

Adoption Blocker:
- Are customers signing up but not using product because of this?
- Activation rate for customers who mention this: [%]
- Quote: "[why they're not using the product]"

Competitive Pressure:
- How many requests mention competitors having this? [number]
- Which competitors: [list]
- Quote: "[Competitor X does this and it's better]"

Create urgency tiers:
- Critical: Blocking deals/causing churn right now
- High: Significant friction, workarounds exist but painful
- Medium: Nice to have, competitive pressure
- Low: Individual preferences, edge cases

PHASE 3: STRATEGIC SYNTHESIS

1. THE TRUTH BEHIND THE REQUESTS

For top request clusters, analyze:

What they're asking for:
[Specific feature requested]

What they actually need:
[Underlying job-to-be-done]

Why the distinction matters:
[How we might solve it differently]

Example:
- Asking for: "CSV export with 50 fields"
- Actually need: "Share data with non-users"
- Better solution: Scheduled email reports, shareable links

2. PATTERN INSIGHTS

Identify non-obvious patterns:

Compensating Behaviors:
- What workarounds reveal pain: "Customers copy-paste into Excel daily"
- What this tells us: [our workflow doesn't match theirs]

Request Combinations:
- Which requests appear together: "SSO + SCIM + Audit logs"
- What this reveals: [enterprise compliance bundle]

Evolution Over Time:
- New requests appearing: [emerging needs]
- Declining requests: [we built it, or they stopped asking]

Proxy Requests:
- Request as symptom: "Add more filters"
- Real problem: [search/organization is fundamentally broken]

3. PRIORITIZATION MATRIX

Create a 2x2 framework:

Impact Axes:
- X-axis: Customer value (deal impact, churn prevention, adoption)
- Y-axis: Strategic value (differentiation, technical leverage, market position)

Plot top 15-20 request clusters.

Quadrants:High Customer Value + High Strategic Value → BUILD NOW
- [List requests here with ARR impact]

High Customer Value + Low Strategic Value → QUICK WINS
- [Features that satisfy customers but don't differentiate]

Low Customer Value + High Strategic Value → FUTURE BETS
- [Strategic but not urgent, consider for later]

Low Customer Value + Low Strategic Value → DON'T BUILD
- [Politely decline or offer workarounds]

4. BUILD vs. BUY vs. WORKAROUND

For top requests, recommend approach:

Build In-House:
- Core differentiation
- Unique to our product
- Customer pays premium

Buy/Integrate:
- Commodity capability
- Best-in-class solution exists
- Faster time-to-value

Workaround/Documentation:
- Edge case
- Existing feature can do this (they don't know)
- Document the workflow

Politely Decline:
- Out of scope
- Wrong customer segment
- Misaligned with strategy

PHASE 4: OUTPUT DELIVERABLES

## Executive Summary
Total Requests Analyzed: [number] requests from [number] unique customers representing $[ARR]

Top 3 Insights:
1. [Most important pattern found]
2. [Second most important finding]
3. [Surprising or counterintuitive insight]

Top 5 Request Clusters to Act On:
[Prioritized list with ARR impact and recommended action]

Requests to Decline:
[What we should explicitly not build and why]

## Full Analysis Report

### Request Clusters (Top 15)

For each cluster:

#### [Cluster Name]
The Ask: [What customers are requesting]
The Need: [Underlying problem to solve]
Frequency: X requests, Y customers, $Z ARR
Urgency: Critical/High/Medium/Low
Evidence:
- [Customer quote 1]
- [Customer quote 2]
- [Deal impact data]

Segment Breakdown:
- Enterprise: [%]
- SMB: [%]
- Churning customers: [%]

Competitive Context:
[Which competitors have this, customer quotes mentioning competitors]

Recommendation: Build / Buy / Workaround / Decline
Rationale: [Why this recommendation]
Estimated Effort: [T-shirt size]
Estimated Impact: [ARR, churn reduction, conversion lift]

### Segment-Specific Insights
[What Enterprise wants vs. SMB vs. different industries]

### Requests We Should NOT Build
[Explicit no's with reasoning]

### Data Quality Notes
[Any biases, gaps, or limitations in the analysis]

## Actionable Next Steps

Immediate (Next Sprint):
- [ ] [Action with owner]
- [ ] [Action with owner]

Short-term (This Quarter):
- [ ] [Initiative with owner]
- [ ] [Validation needed before committing]

Long-term (Next Year):
- [ ] [Strategic bet to explore]

Customer Communication:
- [ ] Respond to top 10 requesting customers with roadmap update
- [ ] Document workarounds for common requests
- [ ] Update sales team on what's coming vs. what's not

</analysis_process>

<quality_checks>

1. PATTERN VALIDITY
- Are clusters based on underlying need, not surface feature requests?
- Have you validated that "reporting" requests are all solving the same problem?

SELF-CRITIQUE: Find 2 clusters that might actually be solving different needs. Split them.

2. BIAS CHECK
- Are you over-weighting loud customers vs. quiet majority?
- Are enterprise requests drowning out SMB legitimate needs?
- Are recent requests over-represented vs. long-standing pain?

SELF-CRITIQUE: Identify one segment you might be ignoring.

3. EVIDENCE STRENGTH
- Is every priority backed by specific customer quotes and ARR numbers?
- Are you distinguishing "everyone wants this" from "3 vocal customers want this"?

SELF-CRITIQUE: Find vague claims like "customers want better UX". Quantify them.

4. ACTIONABILITY
- Can product team start working on this Monday?
- Are recommendations clear (build/buy/decline)?
- Is the "why" behind prioritization explicit?

SELF-CRITIQUE: Add one sentence to each top recommendation explaining the trade-off.

</quality_checks>

<output_format>

For executives:
- 1-page summary with top 5 clusters, ARR impact, recommendations

For product team:
- Full analysis with customer quotes, segment breakdowns, prioritization rationale

For customer-facing teams:
- What we're building, what we're not, how to respond to requests

Follow-up artifacts:
- Shareable roadmap update for requesting customers
- Internal FAQ for sales/support ("When will we build X?")

</output_format>

<meta_guidance>

Great feature request analysis:
- Reveals patterns customers don't see themselves
- Distinguishes must-haves from nice-to-haves with evidence
- Makes hard trade-offs explicit (build this, not that)
- Connects requests to business metrics (ARR, churn, deals)
- Honest about what you're NOT building

Avoid:
- Treating all requests equally ("customers want 47 things")
- Reporting features word-for-word without finding patterns
- Prioritizing by whoever yelled loudest
- Ignoring the "why" behind requests
- Building everything (inability to say no)

Remember: Your job isn't to build everything customers ask for. It's to understand what they need, find the patterns, and build the 20% of features that solve 80% of problems. When in doubt, talk to the customers directly—don't just read requests, understand the context.

</meta_guidance>

</feature_request_analyzer>
```

</details>

---

### Summarize a Customer Interview

**📋 Use Case:** Just finished customer interview, need to extract insights before memory fades

**🛠️ Recommended Tools:** Claude Projects, NotebookLM (if transcript), ChatGPT Projects

**💡 Technique:** Jobs-to-be-done extraction, pain point intensity scoring, quote preservation

<details>
<summary>Click to view prompt</summary>

```
<customer_interview_synthesis>

<interview_inputs>
UPLOAD:
- Interview recording or transcript
- Your interview notes (messy is fine)
- Screenshot of their product usage (if applicable)
- Follow-up Slack/email conversation

CONTEXT:
1. Who did you interview? (role, company, how they use your product)
2. Why did you talk to them? (churning, power user, prospect, feedback session)
3. What were you trying to learn? (validation, discovery, win/loss)
4. How long was the conversation? (30min, 1hr)
</interview_inputs>

<synthesis_framework>

You're a UX researcher who knows that most interview notes are useless because PMs hear what they want to hear, not what the customer said. Your job: Extract truth, preserve context, find the non-obvious insights.

THE REALITY:

Bad interview summaries: "Customer wants feature X"
Good interview summaries: "Customer is trying to accomplish Y, currently does Z workaround, mentioned X as possible solution but real problem is Y"

The goal isn't transcription. It's understanding what the customer actually needs and whether it's a pattern or an outlier.

---

## PART 1: THE FACTUAL LAYER

### Customer Profile
- Name/Company: [if not confidential]
- Role: [their job, not just title]
- Company size/segment: [5 people vs 5000 matters]
- How they use your product: [daily, weekly, monthly | power user, casual, barely adopted]
- Tenure as customer: [day 1 or year 3 changes everything]
- Customer health: [happy, neutral, churning]

### Interview Setup
- Date: [when]
- Format: [video, phone, in-person]
- Duration: [actual length]
- Who was there: [from your team]
- Interview goal: [what you were trying to learn]

---

## PART 2: WHAT THEY ACTUALLY SAID

### Their Current Workflow

The Job They're Trying to Do:
[In their words: what they're trying to accomplish]

How They Do It Today:
Step 1: [their current process]
Step 2: [next step]
Step 3: [outcome]

Where Your Product Fits:
[When/how they use your product in this workflow]

Where Your Product Doesn't Fit:
[What they have to do outside your product]

Quote: "[Exact words about their workflow]"

### Pain Points (Ranked by Intensity)

CRITICAL (blocking them, considering alternatives):
- Pain: [specific problem]
- Frequency: [daily, weekly, monthly]
- Current workaround: [what they do now]
- Cost of workaround: [time, money, frustration]
- Quote: "[Their exact words, especially emotional language]"

HIGH (significant friction, but manageable):
- [same structure]

MEDIUM (annoying, but not a priority):
- [same structure]

The key insight: Watch their energy level when describing pain. If they lean forward, talk faster, or use strong language ("it's insane that..."), that's real pain.

### What They Care About (vs What You Thought They'd Care About)

You expected them to care about:
[What you thought going in]

They actually cared about:
[What they spent time on]

They didn't mention at all:
[What you asked about that they dismissed or ignored]

The surprise:
[What caught you off guard]

Why this matters:
[What this reveals about your assumptions]

### Feature Requests (Decoded)

Don't just write down what they asked for. Understand why.

Request 1:
- What they asked for: "[Feature X]"
- What they're actually trying to do: [underlying need]
- Why this matters: [impact if solved]
- Alternative solutions: [other ways to solve this need]
- Quote: "[Exact words]"

The translation: Most feature requests are solutions, not problems. Your job is to extract the problem.

---

## PART 3: WHAT THEY DIDN'T SAY (But You Noticed)

### Behavioral Signals

Positive signals:
- [ ] They pulled up your product during call (invested user)
- [ ] They had specific examples ready (they think about this)
- [ ] They asked when features are coming (they're planning around you)
- [ ] They brought up your product unprompted (top of mind)

Warning signals:
- [ ] Vague answers (they don't actually use it much)
- [ ] "The team uses it" but they don't (adoption issue)
- [ ] Mentioned competitors (comparing options)
- [ ] Asked about pricing/contract (considering leaving)

What this tells you:
[Your interpretation of their engagement level]

### What They Avoided

Sometimes the most important thing is what they didn't say.

You asked about:
[Topic you brought up]

They deflected/changed subject:
[How they avoided it]

Why this matters:
[What they might be hiding or uncomfortable discussing]

### Energy Map

Where did they light up vs. check out?

High energy topics:
- [What made them animated, talk faster, lean in]
- Why: [What this reveals they care about]

Low energy topics:
- [What made them give short answers, look away]
- Why: [What this reveals they don't care about]

The pattern:
[What they're optimizing for in their world]

---

## PART 4: THE STRATEGIC LAYER

### Is This a Pattern or an Outlier?

Compare to other interviews:
- How many other customers have said similar things?
- Is this pain unique to this customer's setup/segment?
- Is this a leading indicator or an edge case?

Your assessment:
- Pattern: [High confidence this applies to many customers]
- Segment-specific: [Applies to enterprise/SMB/etc.]
- Outlier: [Unique to this customer's situation]

### Jobs-to-be-Done Analysis

The job they hired your product to do:
[What outcome they're pursuing]

How well are you doing that job?
- What's working: [where you deliver value]
- What's broken: [where you're failing]
- What's missing: [gaps in the solution]

Are they hiring other products to do parts of the job?
[What else they use and why]

The strategic question: Should you own this entire job, or partner/integrate?

### Confidence Level in Their Feedback

Not all feedback is equally valuable.

High confidence:
- They use the product daily
- They gave specific examples with data
- Multiple people on their team confirmed same pain
- They're willing to pay more to solve this

Medium confidence:
- They use it occasionally
- Examples were somewhat vague
- Based on memory, not current experience

Low confidence:
- They don't really use it
- Speaking theoretically ("I think users would want...")
- Contradicted themselves during conversation

Your takeaway:
[How much weight to give this feedback]

---

## PART 5: ACTION ITEMS

### What You Learned

Validated:
- [Assumptions that were confirmed]

Invalidated:
- [Assumptions that were wrong]

New insights:
- [Things you didn't know before]

### What to Do Next

Product decisions:
- [ ] [Specific feature to prioritize/deprioritize based on this]
- [ ] [Workflow to investigate further]
- [ ] [Integration to consider]

More research needed:
- [ ] [Follow-up question to ask this customer]
- [ ] [Other customers to interview to validate pattern]
- [ ] [Usage data to check]

Customer-specific actions:
- [ ] [Send them X resource]
- [ ] [Follow up on Y in 2 weeks]
- [ ] [Introduce them to Z team member]

### Quotes to Remember

The 3 quotes that capture the essence:

1. "[Most important quote]"
- Why it matters: [context]

2. "[Second key quote]"
- Why it matters: [context]

3. "[Surprising quote]"
- Why it matters: [context]

These go in: Roadmap presentations, team syncs, strategy docs

---

## THE OUTPUT

### One-Paragraph Summary

[3-4 sentences: Who you talked to, what you learned, what it means]

### Key Takeaways (For Busy Execs)

1. [Insight 1 with evidence]
2. [Insight 2 with evidence]
3. [Insight 3 with evidence]

What we're doing about it: [Specific action]

### Full Write-Up

[All sections above]

### Shareable Quotes

[Powerful quotes formatted for Slack/decks]

</synthesis_framework>

<quality_check>

Did you extract truth or just transcribe?
- [ ] Do you understand the underlying need, not just surface request?
- [ ] Did you note what they DIDN'T say?
- [ ] Did you assess if this is pattern or outlier?

Can someone who wasn't there understand it?
- [ ] Is context clear?
- [ ] Are quotes preserved accurately?
- [ ] Would this change someone's mind?

Is it actionable?
- [ ] Do you know what to do next?
- [ ] Is it clear if this changes priorities?

</quality_check>

<meta_wisdom>

On customer interviews:

Most PMs are bad at interviews because they're looking for validation, not truth.

You ask: "Would you use feature X?"
They say: "Yes"
You build it.
They don't use it.

Better approach:
- Ask about their workflow, not your features
- Watch what they get excited about
- Listen for what they're trying to accomplish

The hard truth:

One interview means almost nothing.
Five interviews showing the same pattern means something.
Ten interviews where five say X and five say Y means you have segmentation.

Your job: Know which kind of signal you have.

On what customers say vs. what they need:

Customers are great at describing their pain.
They're terrible at prescribing solutions.

When they say "I want feature X," your job is to understand:
- What are you trying to do?
- Why isn't it working today?
- How do you work around it?
- What have you tried?

The solution might not be feature X.

Remember:

The best interviews are conversations, not interrogations.
The best insights come from follow-up questions, not your script.
The best PMs know when to shut up and listen.

</meta_wisdom>

</customer_interview_synthesis>
```

</details>

---

### Customer Outreach Planning

**📋 Use Case:** Need to talk to customers but don't want to waste their time or yours with bad questions

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Research question formulation, screening criteria, hypothesis validation framework

<details>
<summary>Click to view prompt</summary>

```
<customer_outreach_plan>

<outreach_inputs>
YOUR RESEARCH GOAL:
1. What are you trying to learn? (be specific, not "get feedback")
2. What decision will this inform? (roadmap, positioning, pricing, GTM)
3. What do you already know? (don't ask questions you can answer with data)
4. What's your hypothesis? (what do you think is true that you're testing)
5. How many conversations do you need? (10 depth interviews vs 100 survey responses)

YOUR CONSTRAINTS:
6. Timeline (when do you need answers)
7. Budget (can you incentivize, or relying on goodwill)
8. Access (do you have customer list, or cold outreach)

UPLOADS:
- Current customer list with segments
- Usage data or analytics
- Previous research (don't re-ask what you know)
</outreach_inputs>

<planning_framework>

You're a research lead who knows that bad research is worse than no research. Bad research gives you false confidence. Good research gives you uncomfortable truths.

**THE REALITY:**

Most customer outreach fails because:
- You ask customers to design your product (they can't)
- You ask leading questions (they tell you what you want to hear)
- You talk to the wrong people (friendly customers who love everything)
- You don't have a plan for what to do with what you learn

Good outreach:
- Has a specific research question
- Knows who to talk to and why
- Asks about behavior, not opinions
- Results in a decision

---

## PART 1: CLARIFY WHAT YOU'RE ACTUALLY TRYING TO LEARN

### Turn Vague Goals into Research Questions

**Bad goal:** "Get customer feedback"
**Good goal:** "Understand if SMB customers would pay $50/month for advanced analytics"

**Your research question:**
[Specific, answerable question]

**Why this matters:**
[The decision this will inform]

**What good looks like:**
[How you'll know you got a useful answer]

### Identify Your Hypotheses

You already have beliefs. Make them explicit so you can test them.

**Hypothesis 1:**
- **What you think is true:** [specific belief]
- **If you're right:** [what you'll do]
- **If you're wrong:** [what you'll do instead]
- **How you'll test it:** [specific questions/observations]

**Example:**
- Hypothesis: "Enterprise customers churn because onboarding is too complex"
- If right: Invest in white-glove onboarding
- If wrong: Look elsewhere for churn drivers
- Test: Ask churned customers about onboarding vs. other factors

### What You Can Answer Without Talking to Anyone

Don't waste customer goodwill asking questions your data can answer.

**Check your analytics first:**
- Feature adoption rates
- Drop-off points in flows
- Time to value metrics
- Cohort retention

**Check support tickets:**
- Common complaints
- Feature requests
- Confusion points

**Check usage data:**
- Who uses what features
- When they use them
- What workflows they follow

**What you still need customer conversations for:**
[The "why" behind the data]

---

## PART 2: WHO TO TALK TO (THIS IS HALF THE BATTLE)

### Segment Your Target Respondents

Not all customers are equal for research purposes.

**Segment 1: Power Users**
- **Why talk to them:** Understand what "success" looks like
- **What to ask:** How they achieved value, what's missing
- **Risk:** They're not representative of most users

**Segment 2: Churned/At-Risk Customers**
- **Why talk to them:** Learn what's broken
- **What to ask:** Why they left, what would bring them back
- **Risk:** They might just be griping, not giving useful feedback

**Segment 3: Recent Sign-Ups**
- **Why talk to them:** Understand onboarding, aha moments
- **What to ask:** What confused them, what clicked
- **Risk:** They don't have long-term perspective

**Segment 4: Target Customers (Non-Users)**
- **Why talk to them:** Understand why they don't buy
- **What to ask:** Current solution, switching costs
- **Risk:** Hard to get them to talk to you

**Your target mix:**
- [X] from Segment 1
- [Y] from Segment 2
- [Z] from Segment 3

**Why this mix:** [Your reasoning]

### Screening Criteria

Not everyone who volunteers should be interviewed.

**Must have:**
- [ ] [Criterion 1: e.g., "Uses product weekly"]
- [ ] [Criterion 2: e.g., "Decision-maker for renewals"]
- [ ] [Criterion 3: e.g., "In target segment"]

**Nice to have:**
- [ ] [Bonus criterion]

**Disqualifiers:**
- [ ] [E.g., "Only used trial, never paid"]
- [ ] [E.g., "Employee of competitor"]

### Sample Size Reality Check

**Qualitative research (interviews):**
- 5 interviews: Pattern detection starts
- 10 interviews: Confident in main themes
- 15+ interviews: Diminishing returns unless highly segmented

**Quantitative research (surveys):**
- 30 responses: Directional insights
- 100 responses: Reasonable confidence
- 300+ responses: Statistical significance

**Your target:** [Number and type]

---

## PART 3: THE RESEARCH PLAN

### Interview Guide Design

**The framework: Past → Present → Future**

**PART 1: Context (5 min)**
Get them talking about their world, not your product.

Questions:
- "Walk me through a typical [workday/workflow]"
- "What does success look like in your role?"
- "What are you spending time on this quarter?"

**Why this works:** You understand their priorities before you talk about your product.

**PART 2: Behavior (20 min)**
What they actually do, not what they say they do.

Questions:
- "Last time you used [feature], walk me through exactly what you did"
- "Show me how you currently solve [problem]" (screen share if possible)
- "What workarounds have you built?"
- "What do you wish you could do but can't?"

**Why this works:** Behavior > opinions. Watch what they do.

**PART 3: Evaluation (10 min)**
Now you can ask about your product, but in context.

Questions:
- "How well does [product] fit into that workflow?"
- "What's the hardest part about using it?"
- "If you could wave a magic wand and fix one thing..."
- "What almost made you not choose us?"

**Why this works:** You understand the gap between what you offer and what they need.

**PART 4: Future (5 min)**
Understand direction, not feature requests.

Questions:
- "How is your work changing in the next year?"
- "What are you worried about?"
- "What would make you a bigger advocate for us?"

**Why this works:** You're designing for where they're going, not where they are.

**CRITICAL RULES:**
- No leading questions ("Don't you think X would be better?")
- No hypotheticals ("Would you pay $10 for Y?")
- No yes/no questions ("Do you like feature Z?")
- Ask "why" at least 3 times per topic

### Survey Design (If Going Quantitative)

**Survey structure:**

**Section 1: Qualification (2-3 questions)**
Ensure they're in your target segment.

**Section 2: Current State (5-7 questions)**
How they solve the problem today.

**Section 3: Your Product (5-7 questions if existing customers)**
Satisfaction, usage, gaps.

**Section 4: Priorities (3-5 questions)**
What matters most to them.

**Section 5: Willingness to Pay / Trade-offs (3-5 questions if testing pricing/positioning)**
Conjoint analysis or MaxDiff if sophisticated.

**Section 6: Demographics (3-5 questions)**
For segmentation analysis.

**Total length:** Under 10 minutes or completion rate tanks.

**Key principles:**
- Use scales consistently (1-5, 1-7, etc.)
- Mix question types (rating scales, multiple choice, one open-ended at end)
- Randomize answer order where possible
- Test with 3 people before sending broadly

### The Outreach Message

**Subject line that works:**
- ❌ "Product feedback requested"
- ✅ "15 minutes to help shape [specific feature]"

**Email template:**
Hi [Name],
[Personal touch: reference their usage/situation]
We're talking to [specific segment] customers to understand [specific problem/workflow].
Would you have 20 minutes in the next two weeks for a conversation? In return:
• [Incentive: early access, Amazon gift card, feature prioritization]
• You'll directly influence what we build next
[Link to calendar]
Thanks,
[Your name]


**What works:**
- Specificity (not "feedback" but "how you use X feature")
- Time-bounded (20 min, not "quick chat")
- Clear value exchange (what they get)
- Easy to say yes (calendar link)

---

## PART 4: WHAT TO DO WITH WHAT YOU LEARN

### Analysis Plan

**After each interview:**
- [ ] Write synthesis within 24 hours (memory fades fast)
- [ ] Tag themes and patterns
- [ ] Note surprising findings
- [ ] Update hypothesis tracker

**After 5 interviews:**
- [ ] Review for patterns
- [ ] Decide if you're learning new things or hearing repeats
- [ ] Adjust interview guide if needed

**After all interviews:**
- [ ] Full synthesis report
- [ ] Share findings with team
- [ ] Make recommendation

### Decision Framework

**If you learn X, you'll do Y:**

| Finding | Action |
|---------|--------|
| Customers say [X] | We'll prioritize [Y feature] |
| Customers don't care about [X] | We'll stop building [Y] |
| Customers are confused by [X] | We'll redesign [Y flow] |

**Make this explicit before you start.** Otherwise findings sit in a doc and nothing changes.

---

## THE OUTPUT

### Research Plan One-Pager

**Research Question:**
[What we're trying to learn]

**Hypothesis:**
[What we think is true]

**Who We're Talking To:**
- [X] power users
- [Y] churned customers
- [Z] prospects

**Timeline:**
- Outreach: [dates]
- Interviews: [dates]
- Synthesis: [dates]

**Decision Point:**
[What we'll do differently based on findings]

### Full Research Plan

[All sections above]

### Interview Guide

[Formatted, ready to use]

### Outreach Templates

[Email copy, screening questions, calendar invite]

</planning_framework>

<quality_check>

**Is your research question actually answerable?**
- [ ] Specific enough to know when you have an answer
- [ ] Not "what do customers want" (they don't know)
- [ ] Focused on behavior or needs, not feature requests

**Are you talking to the right people?**
- [ ] Target respondents can actually answer your question
- [ ] Mix of segments (not just friendly customers)
- [ ] Screening criteria will get you useful signal

**Will this change anything?**
- [ ] Clear decision framework
- [ ] Timeline works for roadmap/launch
- [ ] Stakeholders aligned on what happens based on findings

</quality_check>

<meta_wisdom>

**On customer research:**

Bad research: "What features do you want?"
Good research: "Walk me through what you did last Tuesday."

Bad research: "Would you pay for X?"
Good research: "Show me how you solve this problem today, and what it costs you."

Bad research: Ask 50 customers via survey
Good research: Watch 10 customers use your product

**The uncomfortable truth:**

Customers will tell you they want your product to be "faster, easier, cheaper."

This is useless. Everyone wants everything to be better.

Your job: Understand *why* speed matters, *where* it's hard, and *what* cost they're willing to pay.

**On who to talk to:**

Your friendliest customers will tell you everything is great.
Your angriest customers will tell you everything sucks.

Neither is useful.

Talk to:
- Recent switchers (they compared you to alternatives)
- Power users (they found value)
- People who tried and left (they chose something else)

**Remember:**

Research isn't about validation. It's about learning.

If you finish customer conversations feeling good because they agreed with you, you probably asked leading questions.

If you finish feeling uncomfortable because your assumptions were wrong, you probably learned something.

</meta_wisdom>

</customer_outreach_plan>
```

</details>

---

### Create User Persona


**📋 Use Case:** Need to document who your users are for team alignment

**🛠️ Recommended Tools:** Claude Projects, NotebookLM, ChatGPT Projects

**💡 Technique:** Pattern synthesis from research, behavioral clustering, jobs-to-be-done integration

<details>
<summary>Click to view prompt</summary>

```
<user_persona>

<persona_inputs>
YOUR RESEARCH:
- User interviews: [Paste notes or summaries]
- Usage data: [Key behavioral patterns]
- Customer segments: [How you currently segment]
- Feedback/quotes: [What users say]

WHAT YOU KNOW:
- Who uses your product: [Demographics, roles, company types]
- How they use it: [Workflows, frequency, features]
- Why they use it: [Problems they're solving]

PURPOSE:
- [ ] Team alignment on target user
- [ ] Design guidance
- [ ] Marketing messaging
- [ ] Prioritization framework
</persona_inputs>

<persona_framework>

You create user personas that are useful, not decorative. Your job: extract real patterns from research, not make up composite characters.

---

## USER PERSONA

[Persona Name] - [Role/Type]

"[Quote that captures their mindset]"

---

### Overview

Who they are:
[1-2 sentences describing this user type]

% of user base:
[Roughly how common this persona is]

Example companies:
[Real examples help make it concrete]

---

### Demographics & Context

Role: [Job title(s)]
Industry: [Sectors where common]
Company size: [Small/Medium/Enterprise]
Tech savviness: [Low/Medium/High]
Team structure: [Who they work with]

---

### Goals & Jobs-to-be-Done

Primary goal:
[What they're ultimately trying to achieve]

Key jobs:
1. [Job-to-be-done #1]
2. [Job-to-be-done #2]
3. [Job-to-be-done #3]

Success looks like:
[How they measure if they're winning]

---

### Behaviors & Usage Patterns

How they use the product:
- Frequency: [Daily/Weekly/Monthly]
- Session length: [Typical time spent]
- Top features: [What they use most]
- Workflow: [How it fits their day]

Typical user journey:
1. [Entry point]
2. [Common action]
3. [Outcome]

---

### Pain Points

Biggest frustrations:
1. [Pain point with evidence]
2. [Pain point with evidence]
3. [Pain point with evidence]

Current workarounds:
[How they solve these problems today]

---

### Motivations & Barriers

What drives them:
- [Motivation]
- [Motivation]

What holds them back:
- [Barrier]
- [Barrier]

Decision criteria:
[What makes them choose/stay/leave]

---

### Quotes (Real user feedback)

"[Quote about what they need]"

"[Quote about frustration]"

"[Quote about what works]"

---

### Design Implications

For product:
- [What this means for features]
- [What this means for UI/UX]

For messaging:
- [How to talk to this persona]
- [What resonates with them]

---

### How to Serve This Persona

Do:
- [Specific approach that works]
- [Another effective approach]

Don't:
- [What frustrates this persona]
- [What doesn't resonate]

</persona_framework>

<persona_patterns>

### Pattern 1: Power User

Characteristics:
- High frequency usage
- Uses advanced features
- Wants efficiency and shortcuts
- Vocal about product gaps
- Willing to learn complexity

Design implications:
- Keyboard shortcuts matter
- Customization is valued
- Don't hide advanced features
- Power features worth building

Quote: "I live in this product 8 hours a day. Every second you save me adds up."

---

### Pattern 2: Occasional User

Characteristics:
- Infrequent usage (weekly/monthly)
- Uses basic features
- Forgets how things work between uses
- Needs simple, intuitive UI
- Low tolerance for complexity

Design implications:
- Discoverability crucial
- Inline help important
- Simplicity > power
- Onboarding matters every session

Quote: "I use this once a month. If it's not obvious, I give up."

---

### Pattern 3: Admin/Buyer

Characteristics:
- Sets up for others
- Cares about control and visibility
- Not the daily end user
- Makes purchase decisions
- Needs reporting and governance

Design implications:
- Admin features matter for sales
- Reporting and analytics needed
- Permissions and controls important
- Support for rollout crucial

Quote: "I need to know my team is using this, and I need to prove ROI."

---

### Pattern 4: Evaluator

Characteristics:
- Trying to decide if to buy
- Comparing alternatives
- Time-constrained evaluation
- Skeptical, needs proof
- Looking for deal-breakers

Design implications:
- Fast time-to-value crucial
- Clear differentiation needed
- Demo/trial experience critical
- Comparison content helpful

Quote: "I'm evaluating 3 tools this week. Show me quickly why yours is best."

</persona_patterns>

<meta_guidance>

Persona principles:Base on real research
Not made-up demographics
Real patterns from real users

Focus on behavior, not demographics
"Uses product daily for X" > "Male, 35, lives in city"

Keep it actionable
"So what?" test: Does this help make decisions?
If not, it's decoration.

Don't over-personify
You don't need their favorite color
You need their pain points and goals

Limit to 2-4 personas
More than 4 = you're not focused
1-2 is often enough

Update based on data
Personas evolve
Revisit quarterly

Remember:
Personas are tools for alignment.
If team doesn't reference them in decisions, they're useless.

Make them real, specific, and useful.

</meta_guidance>

</user_persona>
```

</details>

---

### AI Customer Intelligence

**📋 Use Case:** Analyze customer feedback, reviews, or support tickets at scale

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects, NotebookLM

**💡 Technique:** Pattern extraction, theme clustering, signal detection

<details>
<summary>Click to view prompt</summary>

```
<sentiment_analysis>

<sentiment_inputs>
YOUR FEEDBACK DATA:
[Paste customer feedback, reviews, support tickets, NPS comments, etc.]

OR describe what you have:
- Source: [Where feedback came from]
- Volume: [How many pieces of feedback]
- Time period: [When collected]

WHAT YOU WANT TO KNOW:
- [ ] Overall sentiment (positive/negative/neutral split)
- [ ] Top themes/topics
- [ ] Pain points to address
- [ ] Features customers love
- [ ] Competitive mentions
- [ ] Segment differences

CONTEXT:
- Recent changes: [Anything that might affect sentiment]
- Known issues: [What you're already aware of]
</sentiment_inputs>

<sentiment_framework>

You analyze feedback to find patterns humans would miss. Your job: turn 100 comments into 5 actionable insights.

THE PROCESS:1. Sentiment scoring
How do people feel?

2. Theme extraction
What are they talking about?

3. Pain point prioritization
What hurts most?

4. Opportunity identification
What delights them?

5. Action recommendations
What should you do?

---

## SENTIMENT ANALYSIS

### Overall Sentiment

Sentiment breakdown:
- Positive: [X%]
- Neutral: [Y%]
- Negative: [Z%]

Compared to [baseline or previous period]:
[Up/down/flat and by how much]

Overall health: [Healthy/Concerning/Critical]

---

### Top Themes

THEME 1: [Most mentioned topic]Frequency: [Mentioned in X% of feedback]

Sentiment: [Mostly positive/negative/mixed]

Representative quotes:
- "[Customer quote 1]"
- "[Customer quote 2]"
- "[Customer quote 3]"

What this tells us:
[Interpretation - is this good, bad, opportunity?]

---

THEME 2: [Second most common topic]

[Same structure]

---

THEME 3: [Third topic]

[Same structure]

---

[Continue for top 5-7 themes]

---

### Pain Points (Ranked by Intensity × Frequency)

PAIN POINT 1: [Specific issue]Severity: [Critical/High/Medium]
Frequency: [Mentioned by X% of respondents]
Trend: [Getting better/worse/stable]

Customer impact:
[What this is costing them]

Quotes:
- "[Direct quote showing pain]"
- "[Another quote]"

Recommended action:
[What to do about this]

---

PAIN POINT 2:

[Same structure]

---

### What Customers Love

Delight factor 1: [What they praise]Frequency: [Mentioned by X%]

Why they love it:
[What value they get]

Quotes:
- "[Enthusiastic quote]"
- "[Another positive quote]"

Opportunity:
[How to lean into this more]

---

### Competitive Intelligence

Competitors mentioned:
- [Competitor A]: [Mentioned X times]
- Context: [Why they came up]
- Comparison: [What customers said]

- [Competitor B]: [Mentioned Y times]
- Context: [Why mentioned]
- Comparison: [How we're positioned]

What this reveals:
[Competitive insight or concern]

---

### Segment Insights (If data available)

By customer type:[Segment A]:
- Sentiment: [X% positive]
- Top concern: [Issue]
- Top praise: [What they love]

[Segment B]:
- Sentiment: [Y% positive]
- Top concern: [Issue]
- Top praise: [What they love]

Key difference:
[How segments differ in needs/satisfaction]

---

### Trends Over Time

Improving:
- [Topic/feature] sentiment went from [X%] → [Y%] positive
- Why: [Likely cause]

Declining:
- [Topic/feature] sentiment went from [X%] → [Y%] positive
- Why: [Likely cause]

New themes:
- [Topic] started appearing [timeframe]
- Signals: [What this might mean]

---

### Red Flags / Warning Signs

🚨 [Urgent issue]:
[Specific problem mentioned frequently]
- Impact: [High/Medium severity]
- Action needed: [What to do]

⚠️ [Concerning pattern]:
[Trend that's worrying]
- Monitor: [What to watch]

---

### Recommended Actions

IMMEDIATE (This week):
1. [Action addressing critical pain point] - Owner: [Name]
2. [Communication or quick fix] - Owner: [Name]

SHORT-TERM (This month):
1. [Product change or improvement]
2. [Process change]

LONG-TERM (This quarter):
1. [Strategic investment based on feedback]

VALIDATION NEEDED:
1. [Thing to investigate with customers]
- Hypothesis: [What you think]
- Validation method: [How to confirm]

---

### Quote Bank (For Marketing/Sales)

Best testimonials:
- "[Powerful positive quote]" - [Customer type]
- "[Another strong quote]" - [Customer type]

Use for: Case studies, website, sales collateral

</sentiment_framework>

<sentiment_patterns>

### Pattern Recognition

CLUSTER: Multiple complaints about same root cause

Example: "Slow," "Laggy," "Takes forever," "Performance issues"
→ All pointing to: Speed problems

Action: Don't treat as 4 separate issues. One performance fix addresses all.

---

CLUSTER: Feature requests that solve same job

Example: "Want templates," "Need examples," "Show me how others do it"
→ All pointing to: Lack of guidance/starting point

Action: Could solve with templates, or examples, or onboarding

---

CLUSTER: Praise for unexpected use case

Example: Multiple people using [feature] for [unintended purpose]
→ Signals: New market or product direction

Action: Lean into it, optimize for that use case

---

PATTERN: Sentiment changes after specific date

Example: Negative feedback spiked after [release date]
→ Signals: Recent change broke something

Action: Investigate what shipped, consider rollback

---

PATTERN: Segment divergence

Example: Enterprise loves it, SMB frustrated
→ Signals: Product-market fit for one segment, not other

Action: Consider separate products or better segmentation

</sentiment_patterns>

<meta_guidance>

Sentiment analysis principles:Themes > individual comments
Don't get distracted by one loud voice
Find patterns across many

Intensity matters
"It's okay" vs "I love it" both positive
But very different levels of satisfaction

Context is everything
"Slow" might mean:
- Feature is slow
- Learning curve is slow
- Onboarding is slow
Dig deeper to understand

Absence of complaints ≠ satisfaction
Customers rarely praise the baseline
Look for enthusiasm, not just lack of negativity

Recency bias
Recent feedback feels more important
But may not represent majority

Volume ≠ importance
10 people complaining loudly
Might be less important than
100 people quietly churning

Remember:

Sentiment analysis is starting point, not answer.

Use it to identify what to investigate deeper.

Then talk to actual customers.

</meta_guidance>

</sentiment_analysis>
```

</details>

---

### Customer Journey Map

**📋 Use Case:** Understand end-to-end user experience to find opportunities and pain points

**🛠️ Recommended Tools:** Claude Projects, NotebookLM, Miro

**💡 Technique:** Experience mapping, pain point identification, moment analysis

<details>
<summary>Click to view prompt</summary>

```
<customer_journey_map>

<journey_inputs>
WHAT YOU'RE MAPPING:
[Specific user journey - e.g., "new user onboarding", "enterprise purchase process", "daily workflow"]

USER PERSONA:
[Who you're mapping this for - specific type of user]

YOUR RESEARCH:
[What you have - interviews, analytics, support tickets, etc.]

WHAT YOU WANT TO UNDERSTAND:
- [ ] Where do users struggle?
- [ ] Where do they drop off?
- [ ] Where are opportunities?
- [ ] What's the emotional journey?
</journey_inputs>

<mapping_framework>

You create customer journey maps that reveal insights. Your analysis process:

STEP 1: Define the journey boundariesStart point:
Where does this journey actually begin?
(Often earlier than you think - awareness, not just signup)

End point:
What's the successful outcome?
(Not "completed form" but "achieved goal")

Journey stages:
Break into 3-7 distinct phases
- Too few = not useful
- Too many = overwhelming

Example journeys:SaaS onboarding:
1. First hear about product
2. Sign up / trial
3. First use / activation
4. Habit formation
5. Becoming power user

B2B purchase:
1. Problem recognition
2. Research / comparison
3. Trial / POC
4. Procurement / contracting
5. Implementation
6. Adoption across team

STEP 2: Map what user does at each stage

For each stage:

Actions:
- What are they literally doing?
- What decisions are they making?
- What tools are they using?

Touchpoints:
- Where do they interact with your product/company?
- Marketing site, sales call, product, support, etc.

Questions/needs:
- What do they need to know?
- What are they trying to accomplish?
- What concerns do they have?

STEP 3: Identify emotions and pain pointsEmotional state:
- Excited, confused, frustrated, confident?
- Use emotional curve (high/low)

Pain points:
- What's frustrating?
- What's confusing?
- What's taking too long?
- What's blocking them?

Rate pain intensity:
- 🔥🔥🔥 = Critical (blocks progress)
- 🔥🔥 = Major (significant friction)
- 🔥 = Minor (annoying but manageable)

STEP 4: Find the gapsInformation gaps:
- What do they need to know but don't?

Tool gaps:
- What do they need to do but can't?

Support gaps:
- Where do they need help but don't get it?

Experience gaps:
- Where does experience not match expectations?

STEP 5: Identify opportunities

For each pain point:
- Quick win: [Easy fix, high impact]
- Major improvement: [Bigger effort, transforms experience]
- Delight moment: [Exceeds expectations]

STEP 6: Prioritize opportunitiesImpact × Effort matrix:
- High impact, low effort = DO NOW
- High impact, high effort = ROADMAP
- Low impact, low effort = NICE TO HAVE
- Low impact, high effort = DON'T DO

STEP 7: Map to product decisions

Each insight should drive action:
- Feature to build
- Copy to change
- Flow to redesign
- Support to add
- Communication to improve

Now create a journey map adapted to the specific context provided. Don't force it into a rigid template - adjust based on what journey you're actually mapping.

</mapping_framework>

---

## Example Journey Map Structure

(Adapt this based on the actual journey being mapped)

### Journey Overview

Journey: [Name]User: [Persona]Goal: [What success looks like]Research basis: [Interviews with X users, analytics from Y sessions, Z support tickets]

---

### The Journey Stages

Stage 1: [Name]What they do:
[Actions, decisions, interactions]

Touchpoints:
[Where they interact with you]

Needs:
[What they're trying to accomplish]

Emotions: [Happy/frustrated/confused - use whatever makes sense]

Pain points:
- 🔥🔥🔥 [Critical blocker]
- 🔥🔥 [Major friction]

Opportunities:
[What could be better]

---

Stage 2: [Name]

[Same type of info, adapted to this stage]

---

[Continue for all stages in this specific journey]

---

### Key Insights

Biggest pain points:
1. [Pain point with stage and impact]
2. [Another]

Critical moments:
[Moments where users succeed or fail]

Emotional peaks/valleys:
[Where experience is great or terrible]

Drop-off points:
[Where users abandon journey]

---

### Prioritized Opportunities

QUICK WINS:
- [Opportunity 1]: [Why + expected impact]
- [Opportunity 2]

ROADMAP:
- [Bigger opportunity]: [Why + effort]

AVOID:
- [Thing not worth doing]: [Why not]

---

### Action Plan

[Specific next steps based on insights]

</customer_journey_map>
```

</details>

---

### Voice of Customer Report

**📋 Use Case:** Aggregate feedback from multiple sources into actionable insights

**🛠️ Recommended Tools:** Claude Projects, NotebookLM, ChatGPT Projects

**💡 Technique:** Multi-source synthesis, theme extraction, signal prioritization

<details>
<summary>Click to view prompt</summary>

```
<voc_report>

<voc_inputs>
YOUR FEEDBACK SOURCES:
[Paste or describe what you have]
- Support tickets: [Number/summary]
- Sales conversations: [Notes]
- User interviews: [Transcripts]
- NPS responses: [Comments]
- Social media: [Mentions]
- Reviews: [G2, App Store, etc.]

TIME PERIOD:
[What timeframe this covers]

WHAT YOU WANT TO KNOW:
- [ ] Top pain points
- [ ] Feature requests
- [ ] Competitive mentions
- [ ] Sentiment trends
- [ ] Segment differences
</voc_inputs>

<voc_framework>

You synthesize customer feedback into insights that drive decisions. Your process:

STEP 1: Aggregate all sourcesCollect feedback from:
- Support tickets (complaints, questions)
- Sales calls (objections, requests)
- User interviews (deep insights)
- Surveys (NPS, CSAT comments)
- Reviews (public feedback)
- Social (Twitter, Reddit mentions)
- Community/forum posts
- Churn interviews (why they left)

Volume matters:
Track how many mentions each theme gets.

STEP 2: Extract themesDon't just list feedback items.
Group into themes:

Pattern recognition:
- "Can't export data" + "Need CSV download" + "Want data backup" = THEME: Data portability
- "Too expensive" + "Can't afford" + "Costs too much" = THEME: Pricing concerns

Theme categories:
- Pain points (what's broken/frustrating)
- Feature requests (what they want)
- Usability issues (what's confusing)
- Competitive mentions (who they compare to)
- Praise (what's working)

STEP 3: Quantify themesFor each theme:
- Mentions: [How many times came up]
- Sources: [Which channels]
- User types: [Who mentioned it]
- Severity: [How painful]
- Trend: [Increasing/stable/decreasing]

Priority formula:
Frequency × Severity × Strategic fit

STEP 4: Add contextFor each theme, capture:
- Representative quotes (exact words)
- Specific examples
- Impact on users
- Current workarounds
- Competitive context

STEP 5: Segment analysisDo themes differ by:
- Customer size (SMB vs Enterprise)
- Industry vertical
- Product tier (free vs paid)
- User role (admin vs end user)
- Geography

Example insight:
"Pricing concerns mostly from SMB, not enterprise"

STEP 6: Connect to actionsFor each theme:
- Quick fix possible? [What]
- Roadmap item? [When]
- Already being addressed? [How]
- Not addressable? [Why]

STEP 7: Show trendsCompare to previous period:
- New themes emerging
- Old themes declining
- Sentiment shift
- Volume changes

Now synthesize the provided feedback into an actionable report.

</voc_framework>

---

## Example VOC Report Structure

(Adapt based on feedback sources and themes found)

### Voice of Customer Report

Period: [Dates]Sources: [What was analyzed]Total feedback items: [Number]

---

### Executive Summary

Top 3 themes:
1. [Theme with impact]
2. [Theme with impact]
3. [Theme with impact]

Recommended actions:
[Key priorities based on feedback]

Sentiment trend:
[Improving/stable/declining]

---

### Major Themes

THEME 1: [Name]Mentioned: [X times across Y sources]Severity: [High/Med/Low]Trend: [↑/→/↓ vs last period]

What customers say:
"[Quote 1]" - [Source]
"[Quote 2]" - [Source]

Impact:
[How this affects users]

Who's affected:
[Segment analysis]

Current state:
[What we do today / gap]

Recommendation:
[What to do about it]

---

THEME 2: [Name]

[Same structure]

---

[Continue for all major themes]

---

### Competitive Intelligence

Competitors mentioned:
- [Competitor A]: [Context of mentions]
- [Competitor B]: [Context]

Win/loss themes:
[Why we win or lose vs competitors]

---

### Sentiment Analysis

[Overall sentiment breakdown and trends]

---

### Recommended Actions

IMMEDIATE:
- [Action based on feedback]

ROADMAP:
- [Feature to prioritize]

INVESTIGATE:
- [Theme to research further]

---

### Appendix

Detailed feedback by source:
[Links or summaries]

Methodology:
[How analysis was done]

</voc_report>
```

</details>

---

### Jobs-to-be-Done Interview Guide


**📋 Use Case:** Conduct JTBD research interviews to understand customer motivations

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Interview scripting, follow-up generation, pattern recognition

<details>
<summary>Click to view prompt</summary>

```
<jtbd_interview>

<interview_inputs>
WHO YOU'RE INTERVIEWING:
[Customer segment, role, context]

WHAT YOU'RE INVESTIGATING:
[Product area, decision, or behavior]

YOUR HYPOTHESIS:
[What job you think they're hiring your product for]

INTERVIEW LENGTH:
[30 min, 45 min, 60 min]
</interview_inputs>

<jtbd_framework>

You create interview guides that uncover the real jobs customers hire products for. Your process:

STEP 1: Set interview objectivesWhat you're trying to learn:
- The job they're trying to get done
- Current solutions they use
- Switching triggers
- Success criteria
- Emotional and social dimensions

NOT just feature requests.STEP 2: Structure the interviewOpening (5 min):
Build rapport, explain purpose, set expectations

Context setting (10 min):
Understand their role, responsibilities, current workflow

Job exploration (20-30 min):
Deep dive on the specific situation

Wrap-up (5 min):
Any questions, next steps, thank you

STEP 3: Write the core questionsJTBD interview principles:Ask about PAST behavior, not future intent:
❌ "Would you use a feature that..."
✅ "Tell me about the last time you..."

Focus on SITUATION, not opinion:
❌ "What do you think about..."
✅ "Walk me through what happened when..."

Dig for CAUSATION:
❌ "Do you like this?"
✅ "What made you decide to..."

Uncover the STRUGGLE:
❌ "What features do you want?"
✅ "What's frustrating about how you do this today?"

STEP 4: Build question sequencesFor each topic, create layers:Layer 1: Situation
"Tell me about the last time you [did this job]"

Layer 2: Context
"What led up to that moment?"
"What were you trying to accomplish?"

Layer 3: Existing solutions
"How did you handle it?"
"What did you try before that?"

Layer 4: Struggles
"What was difficult about that approach?"
"What compromises did you make?"

Layer 5: Desired outcome
"What would success have looked like?"
"When you think about it now, what would have been ideal?"

STEP 5: Prepare follow-upsFor every main question, have 3-5 follow-ups:If they give surface answer:
- "Can you give me a specific example?"
- "Help me understand what you mean by [term]"
- "What happened next?"

If they jump to solutions:
- "Before we talk about solutions, help me understand the problem better"
- "What makes that solution appealing?"

If they generalize:
- "You said 'always' - tell me about one specific time"

STEP 6: Include probes for dimensionsFunctional dimension:
What practical outcome are they trying to achieve?

Emotional dimension:
How do they want to feel? What do they want to avoid feeling?

Social dimension:
How do they want to be perceived? What's their role/identity?

Timeline probes:
- First thought: "When did you first realize you needed to do this?"
- Evaluation: "How did you decide between options?"
- Acquisition: "What made you finally pull the trigger?"
- Usage: "How has it worked in practice?"

STEP 7: Add interview mechanicsConsent and recording:
[Script for permission]

Transitions between sections:
[How to move topics smoothly]

If interview goes off track:
[How to redirect politely]

If you're running out of time:
[Which questions to prioritize]

Now create a JTBD interview guide for the described scenario.

</jtbd_framework>

---

## Example Interview Guide Structure

### Jobs-to-be-Done Interview Guide: [Job/Product Area]

Interviewer: [Your name]Interview length: [Duration]Recording: [Y/N + tool]

---

### Pre-Interview Setup

Participant screener:
✅ Has done [job] in last [timeframe]
✅ [Other criteria]

Context to gather beforehand:
- [Info from CRM/usage data]

What success looks like:
[Specific insights you hope to gain]

---

### Interview Script

OPENING (5 minutes)

"Thanks for taking the time. I'm [name] and I work on [product]. We're trying to understand how people [do this job], and I'd love to hear about your experience.

This is pure research - I'm not trying to sell you anything. There are no right or wrong answers. I'm just trying to understand your world better.

I'd like to record this so I can focus on our conversation instead of taking notes. Is that okay?"

[Start recording]

"Before we dive in, tell me a bit about your role and what a typical day looks like for you."

---

CONTEXT SETTING (10 minutes)Role and responsibilities:
1. "Walk me through what you're responsible for."
2. "Who do you work with day-to-day?"
3. "How does [this area] fit into your job?"

Current state:
1. "How do you [do this job] today?"
2. "What tools or processes do you use?"

---

JOB EXPLORATION (25 minutes)Topic 1: Recent situation

"Tell me about the last time you [needed to do this job]."

Follow-ups:
- "What was happening that made you need to do this?"
- "Walk me through what you did, step by step."
- "How long did this take?"
- "Who else was involved?"

Topic 2: Existing solutions

"You mentioned using [tool/approach] - how did you end up with that solution?"

Follow-ups:
- "What did you try before that?"
- "What made you switch?"
- "What works well about it?"
- "What's frustrating about it?"

Topic 3: Struggles and workarounds

"What's the hardest part about [doing this job]?"

Follow-ups:
- "Can you give me a specific example of when that was a problem?"
- "What do you do when that happens?"
- "Have you found any workarounds?"
- "What would you do if you had unlimited time/resources?"

Topic 4: Success criteria

"When you finish [this job], what does 'done well' look like?"

Follow-ups:
- "How do you know you've succeeded?"
- "What would make you feel confident in the outcome?"
- "Who else cares about this being done well?"

Topic 5: Emotional/social dimensions

"How do you feel when you have to [do this job]?"

Follow-ups:
- "What's at stake if this doesn't go well?"
- "How would it reflect on you?"
- "What would success mean for your role/team/company?"

---

WRAP-UP (5 minutes)

"This has been incredibly helpful. A few final questions:

1. "If you could wave a magic wand and change one thing about [this process], what would it be?"

2. "Is there anything I should have asked about but didn't?"

3. "Would you be open to a follow-up conversation if questions come up?"

Thank you so much for your time. This really helps us understand [the problem space] better."

---

### Post-Interview Analysis

Within 24 hours:
- [ ] Review recording
- [ ] Pull key quotes
- [ ] Identify job dimensions (functional, emotional, social)
- [ ] Note surprises or contradictions
- [ ] Update interview guide if needed

Synthesis across interviews:
- [ ] Pattern recognition
- [ ] Job statement creation
- [ ] Forces diagram (push/pull/anxiety/habit)

</jtbd_interview>
```

</details>

---

### Opportunity Sizing

**📋 Use Case:** Quantify market opportunity and build business case

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** TAM/SAM/SOM calculation, assumption documentation, scenario modeling

<details>
<summary>Click to view prompt</summary>

```
<opportunity_sizing>

<sizing_inputs>
WHAT YOU'RE SIZING:
[Feature, product, market]

WHAT YOU KNOW:
- Market data: [Any research you have]
- User data: [Current metrics]
- Competitive data: [Benchmark info]

BUSINESS CONTEXT:
- Current ARR/revenue: [If relevant]
- Target segments: [Who you're going after]
- Pricing model: [How you'll monetize]

CONFIDENCE LEVEL NEEDED:
- [ ] Rough estimate (back of napkin)
- [ ] Business case (defendable numbers)
- [ ] Board deck (high confidence)
</sizing_inputs>

<sizing_framework>

You calculate market opportunities in ways that are both ambitious and defensible. Your process:

**STEP 1: Choose your methodology**

**Top-down (market-based):**
Start with total market, filter down
Best when: Entering existing category

**Bottom-up (customer-based):**
Start with customer units, multiply up  
Best when: Clear target customer

**Value-based:**
Start with value created, take percentage
Best when: Replacing existing spend

**Use multiple methods to triangulate.**

**STEP 2: Calculate TAM (Total Addressable Market)**

**How big is the full opportunity?**

**Top-down approach:**
- Market research (Gartner, Forrester, CB Insights)
- Industry reports
- Competitor valuations × market share assumptions

**Bottom-up approach:**
TAM = [# of potential customers] × [revenue per customer per year]


**Value-based approach:**
TAM = [total spend on problem] × [% you can capture]


**Document assumptions:**
Every number needs a source or logic.

**STEP 3: Calculate SAM (Serviceable Addressable Market)**

**Who can you realistically serve?**

**Filter TAM by:**
- Geographic reach
- Company size focus
- Industry verticals you serve
- Technical requirements
- Regulatory constraints
SAM = TAM × [% that matches your ICP]


**Example:**
- TAM: $50B (all companies needing analytics)
- SAM: $5B (B2B SaaS companies 100-1000 employees in US)

**STEP 4: Calculate SOM (Serviceable Obtainable Market)**

**What can you actually capture?**

**Consider:**
- Your GTM reach
- Sales capacity
- Product maturity
- Competitive position
- Timeline (Year 1, Year 3, Year 5)

**Common approaches:**

**Bottoms-up:**
Year 1 SOM = [sales capacity] × [close rate] × [deal size]


**Market share:**
SOM = SAM × [realistic market share %]


**Realistic market share for new entrant:**
- Year 1: 0.1-1% of SAM
- Year 3: 1-5% of SAM  
- Year 5: 5-15% of SAM (if successful)

**STEP 5: Build scenarios**

**Don't give one number. Show range:**

**Conservative scenario:**
- Lower conversion rates
- Slower adoption
- More competition

**Base case:**
- Realistic assumptions
- Documented logic

**Optimistic scenario:**
- Better execution
- Network effects
- Market growth

**STEP 6: Revenue model**

**How does market size convert to revenue?**

**For each scenario:**
Revenue = [customers] × [ARPU] × [retention]


**Break down by:**
- Customer segment
- Pricing tier
- Time to full adoption

**Year 1:** [X customers] × [$Y ARPU] = $Z revenue
**Year 3:** [Growing to...]
**Year 5:** [At scale...]

**STEP 7: Validate assumptions**

**Stress test your math:**

**Reality checks:**
- "This means we need to close X deals per month"
- "This assumes Y% of our target market buys"
- "Our sales team needs Z quota to hit this"

**Comparable checks:**
- How did similar companies grow?
- What's typical market penetration?
- Where are we being aggressive vs conservative?

**STEP 8: Build the business case**

**Connect to strategy:**
- How this fits company goals
- Resource investment needed
- Expected ROI
- Risk factors

**Create decision frameworks:**
- Break-even analysis
- Payback period
- Comparison to other opportunities

Now size the described opportunity with documented assumptions.

</sizing_framework>

---

## Example Opportunity Sizing

### Opportunity Sizing: [Feature/Product/Market]

**Date:** [When]  
**Owner:** [PM name]  
**Confidence:** [Low/Medium/High]

---

### Executive Summary

**Market opportunity:** $[X]M - $[Y]M SAM  
**3-year target:** $[Z]M revenue ([X]% of SAM)  
**Investment needed:** $[A]M over [timeframe]

**Key assumption:** [The 1-2 biggest assumptions this depends on]

---

### Market Sizing (TAM → SAM → SOM)

**TAM: Total Addressable Market**

**Methodology:** [Top-down / Bottom-up / Value-based]

**Calculation:**
[# units] × [$ per unit] = $[TAM]
Example:
50M businesses globally × $200 avg spend = $10B TAM


**Data sources:**
- [Source 1 + link]
- [Source 2 + link]

---

**SAM: Serviceable Addressable Market**

**Our focus:** [Specific segment]

**Filters applied:**
- Geography: [e.g., US only] → [%]
- Company size: [e.g., 100-1000 employees] → [%]
- Industry: [e.g., B2B SaaS] → [%]
- Technical fit: [e.g., uses Salesforce] → [%]

**Calculation:**
$[TAM] × [%] × [%] × [%] = $[SAM]
Example:
$10B × 25% (US) × 15% (size) × 40% (vertical) = $150M SAM


---

**SOM: Serviceable Obtainable Market**

**What we can realistically capture:**

| Timeframe | Market Share | Revenue | Customers |
|-----------|-------------|---------|-----------|
| Year 1 | 0.5% of SAM | $750K | ~75 |
| Year 2 | 2% of SAM | $3M | ~250 |
| Year 3 | 5% of SAM | $7.5M | ~600 |

**Assumptions:**
- Sales capacity: [X reps]
- Close rate: [Y%]
- Ramp time: [Z months]
- Churn: [A%]

---

### Three Scenarios

**CONSERVATIVE**

**Assumptions:**
- Slower adoption: [Why]
- More competition: [Who]
- Lower pricing: [How much]

**3-year outcome:** $[X]M revenue

---

**BASE CASE**

**Assumptions:**
- [Key assumption 1]
- [Key assumption 2]
- [Key assumption 3]

**3-year outcome:** $[Y]M revenue

---

**OPTIMISTIC**

**Assumptions:**
- Network effects kick in
- Faster enterprise adoption
- Expansion into adjacent markets

**3-year outcome:** $[Z]M revenue

---

### Revenue Model

**Unit economics:**
ARPU: $[X]/month
LTV: $[Y]
CAC: $[Z]
LTV:CAC = [ratio]


**Growth drivers:**
- [Driver 1]: [Expected impact]
- [Driver 2]: [Expected impact]

**Revenue breakdown:**

| Segment | % of Revenue | ARPU | Count |
|---------|-------------|------|-------|
| SMB | 30% | $100/mo | 500 |
| Mid-market | 50% | $500/mo | 200 |
| Enterprise | 20% | $2000/mo | 20 |

---

### Validation & Comparable

**Similar company benchmarks:**
- [Company A]: Reached $XM in Y years serving similar market
- [Company B]: Captured Z% market share

**Reality checks:**
- ✅ Requires [X] deals/month (achievable with [Y] reps)
- ⚠️ Assumes [Z]% of market will switch (high but possible)
- ✅ CAC payback of [A] months (healthy)

---

### Investment & Returns

**Investment needed:**
- Engineering: [FTE × months]
- Sales/marketing: $[X]
- Ops/support: [Resources]
**Total:** $[Y]M

**Expected returns:**
- Break-even: Month [X]
- ROI: [Y]% over 3 years
- NPV: $[Z]M

---

### Risks & Assumptions

**Biggest risks:**
1. [Risk 1]: [Mitigation]
2. [Risk 2]: [Mitigation]

**Key assumptions to validate:**
- [ ] [Assumption 1] - [How to test]
- [ ] [Assumption 2] - [How to test]

---

### Appendix

**Detailed calculations:** [Spreadsheet link]  
**Data sources:** [Links to research]  
**Interview notes:** [Customer validation]

</opportunity_sizing>
```

</details>

---

### Win/Loss Analysis

**📋 Use Case:** Understand why deals close or don't close

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Pattern extraction, competitive intelligence, objection categorization

<details>
<summary>Click to view prompt</summary>

```
<win_loss_analysis>

<analysis_inputs>
YOUR WIN/LOSS DATA:
- Wins: [# and context]
- Losses: [# and context]
- Time period: [When]

DATA SOURCES:
- [ ] Sales notes
- [ ] Customer interviews
- [ ] CRM data
- [ ] Call recordings
- [ ] Competitive intel

WHAT YOU WANT TO KNOW:
- [ ] Why we win vs [competitor]
- [ ] Common objections
- [ ] Deal-breaker features
- [ ] Pricing sensitivity
- [ ] Buying process insights
</analysis_inputs>

<winloss_framework>

You analyze wins and losses to find actionable patterns that improve close rates. Your process:

STEP 1: Categorize outcomesBasic buckets:
- Won: Chose us
- Lost to competitor: Chose [specific competitor]
- Lost to status quo: Chose to do nothing
- Lost to budget: No money
- Lost to other: [Build product themselves, different approach]

For losses, always identify WHERE they went.STEP 2: Extract key data pointsFor each deal, capture:Deal characteristics:
- Company size
- Industry
- Use case
- Deal size
- Sales cycle length

Competition:
- Who else they evaluated
- How far along each got

Decision factors:
- What mattered most
- What was "nice to have"
- Deal breakers (if any)

STEP 3: Find patterns in WINSWhy did we win?Look for:
- Feature differentiation
- Pricing/value perception
- Sales process effectiveness
- Timing factors
- Relationship/trust elements

Group into themes:Product reasons:
"We won because we have [feature] that [competitor] lacks"

GTM reasons:
"We won because our sales process was [faster/more consultative/better]"

Market position:
"We won with [segment] because [positioning]"

STEP 4: Find patterns in LOSSESWhy did we lose?Loss categories:Product gaps:
- Missing features
- Integration limitations
- Performance issues
- UX problems

Pricing issues:
- Too expensive
- Wrong packaging
- ROI not clear

GTM problems:
- Sales process too slow
- Wrong messaging
- Poor demo
- Lack of references

Market fit:
- Not built for their segment
- Competitor better aligned

For each loss, ask:
- Was this winnable?
- What would have changed the outcome?
- Is this a pattern?

STEP 5: Competitive analysisBy competitor:[Competitor A]
- When we win vs them: [Reasons]
- When we lose vs them: [Reasons]
- Their strength: [What they do well]
- Our advantage: [Where we beat them]
- Positioning: [How to position against them]

STEP 6: Segment analysisDo patterns differ by:Company size:
- SMB wins/losses
- Mid-market wins/losses
- Enterprise wins/losses

Industry:
- [Vertical A] patterns
- [Vertical B] patterns

Use case:
- [Use case X] patterns
- [Use case Y] patterns

Example insight:
"We lose to Competitor A in enterprise but win in mid-market because [reason]"

STEP 7: Quantify impactPrioritize themes by:
- Frequency: How often does this come up?
- Magnitude: How much revenue at stake?
- Addressability: Can we fix it?

Impact formula:
```

</details>

---


## Strategy & Planning

*12 prompts in this category*

### Feature Prioritization

**📋 Use Case:** Need to prioritize competing feature requests from multiple stakeholders with limited engineering capacity

**🛠️ Recommended Tools:** ChatGPT Projects, Claude Projects, DeepSeek

**💡 Technique:** Before scoring, reason through the trade-offs

<details>
<summary>Click to view prompt</summary>

```
<feature_prioritization>

<prioritization_inputs>
FEATURES TO EVALUATE:
1. [Feature]: [What it does]
2. [Feature]: [What it does]
3. [Feature]: [What it does]
[Add more]

YOUR CONTEXT:
[Add company goals, team size, strategic priorities to your Project]
</prioritization_inputs>

<prioritization_framework>

You prioritize by ROI - dollar impact vs dollar cost. Your process:

STEP 1: Calculate impact (annual $)

For each feature estimate:

Revenue impact:
- New sales: [# deals × $deal size]
- Expansion: [# customers × $expansion]
- Retention: [% churn reduced × $ARR at risk]

Cost savings:
- Support reduction: [% tickets × $cost per ticket]
- Operational efficiency: [time saved × hourly rate]

Strategic value:
- Market position: [$ we don't lose to competitor]
- Platform value: [Enables $ from future features]

Show your work. Force yourself to quantify.

---

STEP 2: Calculate cost (total $)Development:
- Engineering: [weeks × $cost per eng-week]
- Design: [weeks × $cost per week]
- PM/QA: [loaded cost]

Ongoing:
- Maintenance: [monthly cost × 36 months]
- Support: [incremental load]
- Infrastructure: [hosting, tools]

Hidden costs:
- Technical debt created
- Opportunity cost of not building [alternative]

---

STEP 3: Calculate ROIROI = Annual Impact / Total CostBut also consider:
- Time to value (when does $ start?)
- Reversibility (can we undo if wrong?)
- Strategic importance (unlocks market?)
- Learning value (what do we discover?)

---

STEP 4: Force tradeoffsCompounding vs One-time:
Does this enable future features or dead end?

Signal vs Noise:
Who's asking: 1 loud customer or 50 quiet ones?

Strategic tax:
Some low-ROI features are required (compliance, enterprise)
Flag these explicitly

Now prioritize the provided features by ROI.

</prioritization_framework>

---

## Example Prioritization

### Feature Prioritization Analysis

---

### High ROI (Build First)

1. [Feature Name]Impact: $[X]K annually
- [$Y]K new revenue ([breakdown])
- [$Z]K retention ([breakdown])

Cost: $[A]K
- [B] eng-weeks × $[C]
- [Ongoing costs]

ROI: [X]x

Time to value: [When]

Rationale: [Why this wins - specific dollars]

Risk: [What must be true]

---

2. [Feature Name]
[Same structure]

---

### Medium ROI (If Capacity)

[List with abbreviated detail]

---

### Low ROI (Decline)

[Feature]: $[X]K / $[Y]K = [Z]x ROI
- Why not: [Low impact relative to effort]
- Revisit if: [What would change it]

---

### Strategic Must-Haves

[Feature]: [Why required despite low ROI]

---

### Need More Info

[Feature]: Can't estimate because [specific unknown]
- Get: [Data needed] then re-evaluate

</feature_prioritization>
```

</details>

---

### RICE Feature Scoring

**📋 Use Case:** Score and prioritize features using the RICE framework

**🛠️ Recommended Tools:** Claude, ChatGPT, or any LLM

**💡 Technique:** Structured scoring with explicit rationale for assumptions and risks

<details>
<summary>Click to view prompt</summary>

```
RICE Score = (Reach × Impact × Confidence) / Effort

Feature: [NAME]
Reach: [NUMBER] | Impact: [SCORE] | Confidence: [%] | Effort: [WEEKS]
Score: [CALCULATED]
Rationale: [2-3 sentences on the biggest assumption or risk]
```

</details>

---

### Develop a GTM Strategy

**📋 Use Case:** Planning a product launch that actually drives adoption and revenue

**🛠️ Recommended Tools:** Claude Projects, NotebookLM

**💡 Technique:** Chain-of-thought through launch phases, identifying failure modes

<details>
<summary>Click to view prompt</summary>

```
<gtm_strategy>

<gtm_inputs>
PRODUCT CONTEXT:
1. What are you launching? (new product, major feature, pricing change)
2. Who's it for? (target customer segments with specifics)
3. What problem does it solve? (pain point and value prop)
4. What's the business goal? (revenue, adoption, market position)
5. How is this sold today? (if existing product) or how will it be sold?
6. What's the competitive landscape? (alternatives, substitutes)

CONSTRAINTS:
7. Launch timeline? (target date and why)
8. Budget? (marketing, sales enablement, product)
9. Team resources? (who's available to support launch)
10. Technical readiness? (GA, beta, alpha)

UPLOADS:
- Product brief or PRD
- Market research
- Competitive analysis
- Sales/customer feedback
- Pricing model
</gtm_inputs>

<gtm_process>

You are a GTM strategist who has launched 50+ products. You know that most launches fail not from bad products, but from unclear positioning, wrong audience, or poor execution.

PHASE 1: GTM FOUNDATION

1. DEFINE YOUR ICP (Ideal Customer Profile)

Who will get the most value fastest?

Firmographic:
- Company size: [employees, revenue]
- Industry: [specific verticals]
- Geography: [markets]

Behavioral:
- Current solution: [what they use today]
- Pain intensity: [how badly do they need this]
- Buying process: [who decides, how long]

Qualification criteria:
- Must-have: [non-negotiable attributes]
- Nice-to-have: [bonus attributes]
- Disqualifiers: [who this isn't for]

Your Primary ICP: [specific description]Secondary ICP: [if relevant]Explicitly NOT for: [who to avoid]

2. NAIL YOUR POSITIONING

Complete these statements:

For [target customer]Who [have this problem]Our product [does what]Unlike [alternative]We [key differentiator]

One-sentence pitch: [15 words max]Elevator pitch: [30 seconds]Key message pillars: [3-5 themes you'll emphasize]

3. SET MEASURABLE GOALSPrimary metric: [the one number that matters]
- Baseline: [current state]
- Target: [success threshold]
- Timeline: [when measured]

Secondary metrics: [2-3 supporting indicators]

Counter-metrics: [what you're watching to avoid breaking]

PHASE 2: GTM STRATEGY CHOICES

1. LAUNCH APPROACH

Choose your strategy:

Big Bang Launch - Everything at once, maximum noise
- When: You have brand power, big news, one shot to make splash
- Risk: If it flops, everyone knows

Phased Rollout - Staged release by segment/geography
- When: Testing GTM fit, iterating on messaging, reducing risk
- Risk: Slower momentum, competitors see you coming

Stealth → Loud - Beta with champions, then broad launch
- When: Need proof points before going wide, building case studies
- Risk: Competitors have time to react

Always-On Growth - No launch moment, continuous optimization
- When: Feature enhancement, not net-new capability
- Risk: Lacks urgency, harder to align team

Your choice: [approach + why]

2. PRICING & PACKAGING

How is this monetized?

Pricing model: [per user, per usage, flat fee, freemium]Price point: $[amount] because [rationale]Packaging tiers: [if multiple, what's in each]

Pricing positioning:
- Compared to alternatives: [higher/lower/similar and why]
- Launch pricing: [discount/promo or full price from day 1]

3. CHANNEL STRATEGY

How will customers discover and buy this?

Discovery channels: [where target customers will learn about this]
- Organic: SEO, word-of-mouth, community
- Paid: Ads, sponsorships, partnerships
- Sales: Outbound, account expansion
- PR: Media, analysts, influencers

Purchase path: [how they go from awareness to customer]

Your primary channel: [and why you're betting on it]

PHASE 3: EXECUTION ROADMAP

## Pre-Launch (4-6 weeks before)

Internal Readiness:
- [ ] Sales trained and confident selling this
- [ ] Support trained on key scenarios
- [ ] Docs/help content ready
- [ ] Pricing/packaging finalized
- [ ] Internal FAQ distributed

External Groundwork:
- [ ] Beta customers recruited (if applicable)
- [ ] Case studies/testimonials in progress
- [ ] Launch content calendar planned
- [ ] Analyst/press briefings scheduled
- [ ] Partners/integrations aligned

Assets Created:
- [ ] Landing page live
- [ ] Product demo video
- [ ] Sales deck
- [ ] Email nurture sequences
- [ ] Ad creative

## Launch Week

Day -1: [what happens]Launch Day: [sequence of activities]Day +1 to +7: [follow-up actions]

Launch Day Checklist:
- [ ] Product live and stable
- [ ] Landing page published
- [ ] Blog post live
- [ ] Email to existing customers
- [ ] Social posts scheduled
- [ ] Sales team activated
- [ ] Support standing by
- [ ] Monitoring dashboard active

## Post-Launch (30/60/90 days)

First 30 days: [focus on...]60 days: [optimize...]90 days: [evaluate and decide...]

Success criteria for each phase:
- 30 days: [specific milestones]
- 60 days: [specific milestones]
- 90 days: [go/no-go decision point]

PHASE 4: RISK MITIGATION

Top Launch Risks:

1. [Risk name]
- Probability: High/Medium/Low
- Impact: High/Medium/Low
- Mitigation: [specific action]
- Owner: [person responsible]

2. [Risk name]
- [same structure]

Common failure modes to plan for:
- Low initial demand: [what we'll do]
- Technical issues at launch: [incident plan]
- Competitor responds: [counter-strategy]
- Sales team doesn't prioritize: [enablement plan]
- Customers confused by positioning: [message testing]

PHASE 5: TEAM & TIMELINE

Launch Team:
| Role | Owner | Responsibilities |
|------|-------|-----------------|
| Launch Lead | [name] | Overall success |
| Product | [name] | Feature readiness |
| Marketing | [name] | Demand gen |
| Sales | [name] | Enablement & deals |
| Support | [name] | Customer success |

Timeline:
| Milestone | Date | Owner | Status |
|-----------|------|-------|--------|
| Beta launch | [date] | [name] | [on track/at risk] |
| Sales training | [date] | [name] | [status] |
| GA launch | [date] | [name] | [status] |
| First customer | [date] | [name] | [status] |

</gtm_process>

<output_format>

## Executive Summary
- What: [product in one sentence]
- Who: [target customer]
- Goal: [primary metric target]
- Launch date: [when]
- Success looks like: [specific outcome]

## Full GTM Strategy
[All sections from process]

## One-Pager for Stakeholders
- The play: [approach in 3 bullets]
- The bet: [why we think this will work]
- The ask: [what you need from stakeholders]

</output_format>

<meta_guidance>

Great GTM strategy:
- Starts with a tightly defined ICP, not "everyone"
- Makes positioning trade-offs explicit
- Has measurable goals with timelines
- Plans for failure modes, not just success
- Aligns cross-functional teams with clear owners

Avoid:
- Boil the ocean strategy ("all channels, all customers")
- Vague goals ("increase awareness")
- Assuming "build it and they will come"
- Over-optimizing launch day vs. first 90 days
- Treating GTM as marketing's job alone

</meta_guidance>

</gtm_strategy>
```

</details>

---

### Competitor Analysis

**📋 Use Case:** Competitor did something and want a thought partner to ideate on

**🛠️ Recommended Tools:** Claude Project + Research, Perplexity Research

**💡 Technique:** Reverse engineering product flows, constraint analysis, strategic intent detection

<details>
<summary>Click to view prompt</summary>

```
<competitor_analysis>

<competitor_inputs>
WHAT HAPPENED:
1. What did your competitor do? (launched feature, announced product, changed pricing, got funding)
2. Where did you see this? (upload: press release, blog post, demo video, screenshots, pitch deck)
3. What's your initial concern? (will this hurt us, do we need to respond, are we behind)

YOUR CONTEXT:
4. Your product and how it makes money
5. Customer segment overlap (are you going after same customers)
6. Your current roadmap (what were you planning to build)

UPLOADS:
- Their announcement materials
- Screenshots or demo videos
- Customer reactions (Twitter, LinkedIn, Reddit, reviews)
- Your internal Slack thread panicking about this (kidding, but also not kidding)
</competitor_inputs>

<analysis_framework>

You're a product strategist who's seen 100 competitor launches. Most fail. Most are less scary than they look. Your job: separate real threats from noise, then figure out what to do Monday morning.

THE REALITY:
When a competitor ships something, your team's first instinct is panic. Your second instinct is "we should build that too." Both instincts are usually wrong.

The right questions:
- What problem are they actually solving? (not what they say, what they're really doing)
- Why did they make this move now?
- What does this reveal about their strategy?
- Where are they making a bet we're not?
- What can they NOT do because of this choice?

---

## PART 1: WHAT DID THEY ACTUALLY DO?

### Reverse Engineer The Product

Most announcements are vaporware or half-baked. Figure out what's real.

Based on their materials, reconstruct:The User Flow (Screen by Screen)
Walk through their product like a customer would:

1. Entry point: Where does the user encounter this?
- Homepage? In-product upsell? Checkout flow?
- Screenshot/describe what they see

2. Step-by-step flow:
- Screen 1: [What user sees, what they can do]
- Screen 2: [Next interaction]
- Screen 3: [Outcome]

3. Edge cases they're handling (or not):
- What happens if user does X?
- Error states shown?
- Mobile vs desktop?

Example: Apple BNPL
- Entry point: Appears in Apple Pay checkout flow
- User sees: "Pay in 4 installments, no interest" directly in Wallet
- Flow: Select installment plan → Face ID → Done
- Integration: Native to iOS, not a separate app
- What they're NOT handling: Web checkout (iOS only initially)

What this tells you:
- How much they invested (polish level reveals commitment)
- What they're optimizing for (speed? flexibility? control?)
- What they're willing to punt on (tells you their priorities)

### Decode The Positioning

What job are they trying to own?

Their headline: [exact copy]
Translation: [what they're actually saying]
Subtext: [what they're admitting they're NOT]

Example:
- Headline: "The all-in-one workspace"
- Translation: "We're going after Slack + Docs + PM tools"
- Subtext: "We won't be best-in-class at any one thing"

Who is this for?
- Their explicit target: [who they say]
- Their actual target: [look at pricing, features, integrations]
- Who this excludes: [importantly, who can't use this]

The key question: Are they moving upmarket or downmarket? This tells you everything.

### Extract The Business Model

How are they monetizing this?
- Free? (Land grab play)
- Freemium? (Which features are gated tells you what they think is valuable)
- Paid only? (Premium positioning)
- Bundled? (Trying to increase ARPU)

What does this reveal?
- Free → They're subsidizing this with something else, find out what
- Expensive → They think this is differentiated, but are customers paying?
- Bundled → They can't sell it standalone (weakness)

Example: Apple BNPL
- Business model: No fees to users, merchant fees unclear
- What this reveals: Using it as moat for Apple Pay, not profit center
- Strategic implication: They can afford to lose money on this

---

## PART 2: WHY DID THEY DO THIS?

Most PMs stop at "what did they build."
You need to understand "why now" and "what does this reveal."

### Strategic Intent Detection

Why this move, why now?

Think through the possibilities:
- Defensive: Protecting installed base from threat
- Offensive: Going after new market/customer
- Bundling: Increasing switching costs
- Platform play: Enabling ecosystem
- Catching up: Finally building table stakes
- Distraction: Throwing spaghetti at wall

Evidence for each theory:
[What in their execution supports each explanation]

Most likely reason: [Your call]

### What This Reveals About Their Strategy

Every product decision is a breadcrumb:

They're betting on:
[The future they think is coming]

They're moving away from:
[What they're de-prioritizing]

They can no longer do:
[The doors this closes for them]

Example: Apple BNPL
- Betting on: Owning the entire payment stack, not just facilitating it
- Moving away from: Being neutral platform for 3rd party payment options
- Can no longer do: Partner deeply with Affirm, Klarna, etc.

### The Constraint Analysis

This is where you find their vulnerability.

What constraints are baked into this choice?Technical constraints:
- Architecture decisions that limit them
- Example: iOS-only = can't capture web/Android traffic

Business model constraints:
- Revenue model that creates misaligned incentives
- Example: Per-seat pricing = disincentivized to make collaboration easier

Customer constraints:
- Built for X customer = can't serve Y customer
- Example: Enterprise-first = too complex for SMB

Strategic constraints:
- Committed to platform/ecosystem that limits flexibility
- Example: Must work with existing Apple Pay = can't optimize checkout flow

The opportunity: These aren't bugs. These are permanent features. They can't fix them without breaking their strategy.

---

## PART 3: HOW DOES THIS AFFECT YOU?

### Threat Level Assessment

Be honest about impact:

Best case (for them):
[If they execute perfectly, what happens to you]

Most likely case:
[What probably happens given execution is hard]

Your exposure:
- Customer overlap: [High/Medium/Low]
- Product overlap: [High/Medium/Low]
- Time to impact you: [Immediate/Quarters/Years]

Real threat level: [Critical/High/Medium/Low/Noise]

The hard truth: Most competitor launches don't matter. The ones that do, you usually see coming.

### Direct Impact Analysis

What immediately gets harder for you:Sales/Marketing:
- Will prospects ask about this? [If yes, you need response]
- Will they use this as price leverage?
- Does this change buyer expectations?

Product:
- Is this now table stakes? [Do customers expect this]
- Does this make your roadmap obsolete?
- Do you need to shift priorities?

Customers:
- Will existing customers churn?
- Will they demand this from you?
- Can you position around it?

### The Strategic Question: Should You Respond?

Most PMs default to: "We should build that too."

The right framework:

DON'T RESPOND IF:
- They're competing on a dimension you chose not to compete on
- Their target customer isn't your target customer
- You have a differentiated path that's better
- This is their Hail Mary, not their strength

FLANK RESPONSE IF:
- You can solve the same job a different (better) way
- You can serve the same customer in adjacent use case
- You can move faster/cheaper/simpler

COPY IF (rarely):
- This is table stakes and you're behind
- Every competitor will have this
- Customers will churn without it
- You can build it 10x better

GO BIGGER IF:
- They validated demand but under-shot
- You can leapfrog with more ambitious vision
- Their version exposes them to your strength

### Your Response Plan

Immediate (This Week):
- [ ] Sales response doc: How to talk about this
- [ ] Customer outreach: Gauge reaction from top 10 accounts
- [ ] Team alignment: Make decision on whether to respond

Short-term (This Quarter):
- If building response: [Specific scope, not "build what they have"]
- If not responding: [How to position around it]
- Monitoring: [What signals say we made wrong call]

Strategic (This Year):
- Does this change your strategy? [Yes/No/Maybe]
- If yes: [Specifically how]
- If no: [Why you're confident in your path]

---

## PART 4: WHAT THEY CAN'T DO (YOUR ADVANTAGE)

### Exploit The Opening

Every move creates vulnerability.

What can they NOT do now?They can't serve: [Customer segment this alienates]
They can't build: [Features that conflict with this]
They can't partner with: [Ecosystem they just burned]
They can't change: [Commitments they're locked into]

Your move:
[How you position into their new weakness]

### The Judo Move

Best response isn't matching their move. It's using their momentum against them.

Their strength:
[What they're good at]

Flip side weakness:
[What that strength prevents them from doing]

Your positioning:
[How you own the opposite]

Example:
- Their strength: "Enterprise-grade compliance"
- Weakness: Slow, complex, requires IT involvement
- Your move: "Get started in 5 minutes, no IT needed"

---

## THE OUTPUT

### One-Pager For Your Team

What They Did:
[2 sentences max]

Why They Did It:
[Their strategic intent]

Real Threat Level:
[Critical/High/Medium/Low with brief rationale]

What We're Doing:
[Respond/Flank/Ignore with specific action]

What Sales Says:
[Exact talking points for next call]

### Detailed Analysis

[All sections above]

### Follow-Up Actions

Research Tasks:
- [ ] Test their product yourself: [Get account, walk through flows]
- [ ] Talk to 5 customers: [Do they care? Will this affect their decision?]
- [ ] Monitor metrics: [Which metrics will signal if this is working]

Decision Points:
- 30 days: [Re-assess threat level based on their traction]
- 90 days: [Go/no-go on competitive response]

</analysis_framework>

<quality_check>

Did you actually understand their product?
- [ ] Can you draw their user flow on a whiteboard?
- [ ] Do you know where in their flow this appears?
- [ ] Have you identified what they're NOT handling?

Did you understand their strategy?
- [ ] Do you know WHY they built this?
- [ ] Have you identified their constraints?
- [ ] Do you know what they can't do because of this?

Did you make a decision?
- [ ] Respond / Flank / Ignore - you picked one
- [ ] You have specific actions, not vague plans
- [ ] You know what "wrong" looks like

</quality_check>

<meta_wisdom>

The uncomfortable truth:

Most competitor analysis is theater. You build a deck, feel smart, then nothing changes.

The point of this analysis isn't to document what happened. It's to make a decision:
- Do we respond?
- How do we respond?
- What do we tell customers?
- What do we tell the team?

If you finish this analysis and don't know what to do Monday morning, you did it wrong.

On competition:

Competition isn't about features. It's about which customer, which job, which constraint.

Your competitor just made a choice. That choice:
- Opens doors for them
- Closes doors for them
- Creates space for you

Your job: Find the space.

On copying competitors:

The weakest product strategy is "build what they have."

If they're good, you'll always be behind.
If they're bad, you'll waste time.

Better question: "What can we do that they structurally can't?"

That's your answer.

</meta_wisdom>

</competitor_analysis>
```

</details>

---

### Identify ICP (Ideal Customer Profile)

**📋 Use Case:** Need to focus GTM on right customers, stop wasting time on bad-fit prospects

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Segmentation analysis, retention correlation, value realization patterns

<details>
<summary>Click to view prompt</summary>

```
<icp_definition>

<icp_inputs>
YOUR DATA:
1. Current customer list with:
- Company size, industry, geography
- Revenue/ARR per customer
- Retention rate by cohort
- Time to value
- Support ticket volume
- NPS/satisfaction scores

2. Win/loss data:
- Who you beat competitors for
- Who chose competitors
- Why you won/lost

3. Usage data:
- Feature adoption by segment
- Active vs. inactive customers
- Expansion patterns

UPLOADS:
- Customer database export
- Sales CRM data
- Usage analytics
- Customer success notes on best/worst customers
</icp_inputs>

<icp_framework>

You're a GTM strategist who knows that "everyone is our ICP" means you'll win no one. Great companies get focused. They know exactly who they're built for, and who they're not.

THE REALITY:

Most companies chase every dollar. They sell to anyone who'll pay.

Result:
- Product tries to serve everyone, delights no one
- Sales has 100 objection handlers, no sharp positioning
- Support drowns in edge cases
- High churn, low expansion

The alternative:
- Pick your ICP
- Build the perfect product for them
- Win them at high rate
- Expand from position of strength

---

## PART 1: ANALYZE YOUR BEST CUSTOMERS

### Define "Best"

Different companies optimize for different things:

Highest LTV:
- Customers who stay longest + expand most
- Why: Compound revenue

Fastest Time-to-Value:
- Customers who activate and see value quickly
- Why: Efficient go-to-market

Lowest Cost-to-Serve:
- Customers who don't need handholding
- Why: Scalable business

Strongest Advocacy:
- Customers who refer others, write reviews
- Why: Organic growth

Your definition of "best":
[What you optimize for]

### Extract the Pattern

Pull your top 20 customers by your "best" definition.

Firmographic patterns:
| Attribute | Pattern | % of Top 20 |
|-----------|---------|-------------|
| Company size | [e.g., "50-200 employees"] | [%] |
| Industry | [e.g., "SaaS, Tech"] | [%] |
| Geography | [e.g., "US, UK"] | [%] |
| Revenue | [e.g., "$10M-$50M"] | [%] |

Behavioral patterns:
- What do they use your product for? [primary use case]
- How do they use it? [frequency, workflow]
- Who uses it? [roles, team size]
- What features do they use most? [specific features]

Situational patterns:
- What problem were they trying to solve? [pain point]
- What were they using before? [previous solution]
- Why did they switch? [trigger event]
- What alternatives did they consider? [competitive set]

The pattern:
[Your description of what makes these customers successful]

### The Inverse: Your Worst Customers

Now look at bottom 20 by churn rate or support burden.

What's different:
| Attribute | Bad Fit Pattern |
|-----------|-----------------|
| Company size | [e.g., "< 10 employees"] |
| Industry | [e.g., "Non-tech"] |
| Use case | [e.g., "Trying to use it for X when built for Y"] |

Why they struggled:
- Product-market fit issues: [they wanted something you don't do]
- Expectation mismatch: [they thought you were X, you're Y]
- Wrong buying stage: [too early/late in their maturity]

The lesson:
[What these customers taught you about who NOT to target]

---

## PART 2: BUILD YOUR ICP PROFILE

### The Core ICP

Firmographic:
- Company size: [employees: X-Y, revenue: $A-$B]
- Industry: [specific verticals, or horizontal]
- Geography: [countries/regions]
- Growth stage: [startup, growth, mature]

Technographic:
- Tech stack: [what tools they already use]
- Technical sophistication: [technical team, non-technical team]
- Integration needs: [must integrate with X, Y, Z]

Behavioral:
- Primary use case: [specific job-to-be-done]
- Buying process: [who decides, how long]
- Budget: [typical deal size: $X-Y/year]

Situational:
- Trigger event: [what makes them buy now]
- Raised funding
- Hit X scale
- Current solution failing
- Compliance requirement
- Current solution: [what they're using/replacing]
- Pain intensity: [how badly they need this]

### The Persona (Who You Sell To)

Economic Buyer:
- Title: [e.g., VP Sales, CFO]
- Cares about: [business outcomes]
- Success metric: [how they're measured]

Technical Buyer:
- Title: [e.g., Engineering Lead]
- Cares about: [technical fit, security]
- Veto power: [yes/no and why]

End User:
- Title: [e.g., Sales Rep, Analyst]
- Cares about: [day-to-day workflow]
- Adoption driver: [if they don't use it, you churn]

Champion:
- Who they usually are: [role that becomes internal advocate]
- Why they champion you: [what's in it for them]

### Must-Haves vs. Nice-to-Haves

Not all ICP attributes are equal.

Must-haves (Non-negotiable):
- [ ] [Attribute 1: e.g., "Must have 50+ employees"]
- [ ] [Attribute 2: e.g., "Must use Salesforce"]
- [ ] [Attribute 3: e.g., "Must have compliance need"]

Why these are must-haves: [Your product literally can't deliver value without these]

Strong preferences (Increase win rate):
- [ ] [Attribute: e.g., "Fast-growing companies"]
- [ ] [Attribute: e.g., "Technical founder"]

Nice-to-haves (Bonus but not required):
- [ ] [Attribute]

Anti-ICP (Explicitly NOT our customer):
- [Who you should turn away and why]

---

## PART 3: VALIDATE YOUR ICP

### The Data Check

Test your ICP definition against your customer base.

How many customers fit ICP?
- Total customers: [X]
- Fit ICP: [Y] ([%])

Performance by ICP fit:
| Metric | ICP Customers | Non-ICP |
|--------|---------------|---------|
| Avg ARR | $[X] | $[Y] |
| Retention | [%] | [%] |
| Time-to-value | [days] | [days] |
| NPS | [score] | [score] |

The truth:
If ICP customers don't significantly outperform non-ICP, your ICP isn't focused enough.

### The Sales Check

Give your ICP to sales team.

Questions:
- Can they immediately name 20 companies that fit?
- Does this help them prioritize their pipeline?
- Does this give them confidence to disqualify bad fits?

If they say "but what about [exception]..."
- There will always be exceptions
- Optimize for the pattern, not edge cases
- You can always expand ICP later after you dominate core

### The Product Check

Can you build a product that's perfect for this ICP?
- Is the use case focused enough?
- Are their needs homogeneous enough?
- Can you ignore non-ICP needs and make trade-offs?

If you can't say "no" to non-ICP feature requests, your ICP isn't tight enough.

---

## PART 4: GO-TO-MARKET IMPLICATIONS

### How ICP Changes Your Strategy

Product:
- Build for: [ICP use case]
- Don't build for: [non-ICP use case]
- Roadmap filter: "Does this serve ICP?"

Marketing:
- Channels: [where ICP hangs out]
- Message: [ICP-specific pain points]
- Content: [topics ICP cares about]

Sales:
- Target list: [ICP firmographics → X companies]
- Qualification: [ICP checklist → pass/fail fast]
- Pricing: [optimized for ICP budget]

Customer Success:
- Onboarding: [ICP-specific playbook]
- Success metrics: [ICP-defined value]
- Expansion: [ICP natural growth path]

### Expansion Strategy

After dominating core ICP:Adjacent ICP #1:
- How they're similar: [overlap with core]
- How they're different: [what you'd need to change]
- Effort to serve: [High/Medium/Low]

Adjacent ICP #2:
- [Same structure]

The sequence:
1. Win core ICP at 50%+ win rate
2. Expand to adjacent #1
3. Then adjacent #2

Don't try to serve all ICPs at once. Sequential focus beats parallel mediocrity.

---

## THE OUTPUT

### One-Page ICP

Who we're built for:
[3 sentence description]

Must-haves:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

Who we're NOT for:
- [Anti-ICP description]

Why we win with ICP:
[Your unique advantage for this customer]

### Detailed ICP Profile

[All sections above]

### Sales Qualification Checklist

Pass/Fail Questions:
- [ ] [Must-have 1]
- [ ] [Must-have 2]
- [ ] [Must-have 3]

Scoring Questions:
- [Nice-to-have attributes with point values]

Qualification threshold:
- Must pass all pass/fail
- Must score X+ points

### Target Account List

Companies that fit ICP:
[List or criteria for list building]

Sources:
- [Where to find them: LinkedIn Sales Nav, ZoomInfo, etc.]

</icp_framework>

<quality_check>

Is your ICP actually focused?
- [ ] Can you describe them in 3 sentences?
- [ ] Can sales name 50 companies that fit?
- [ ] Are you willing to turn away customers who don't fit?

Does it match your data?
- [ ] ICP customers retain better than non-ICP
- [ ] ICP customers expand more
- [ ] ICP customers cost less to serve

Is it actionable?
- [ ] Clear qualification criteria
- [ ] Specific enough to build product roadmap around
- [ ] Tight enough to focus marketing

</quality_check>

<meta_wisdom>

On focus:

Weak companies: "Our ICP is companies with 1-10,000 employees who want to be more productive."

Strong companies: "Our ICP is Series A-B SaaS companies with 50-200 employees, technical founders, using Salesforce, who need to consolidate 3+ tools."

The difference: Specificity.

The uncomfortable truth:

Picking an ICP means saying no to money.

A company that doesn't fit your ICP might want to pay you.
Your job: Say no.

Why?
- They'll churn
- They'll create support burden
- They'll request features that hurt your ICP
- They'll dilute your positioning

Short-term pain, long-term gain.

On expansion:

Most companies diffuse too early.

They win 20% of their "ICP" (which is too broad) and immediately expand to adjacent segments.

Better: Win 60%+ of a narrow ICP, then expand.

Why?
- Strong reputation in focused segment
- Clear product differentiation
- Unit economics that work
- Reference customers that matter

Remember:

Your ICP isn't "who can use your product."

It's "who do you win with at highest rate, lowest cost, and strongest retention."

If you try to serve everyone, you'll serve no one well.

Pick your ICP. Dominate them. Expand from strength.

</meta_wisdom>

</icp_definition>
```

</details>

---

### Brainstorm Experiments

**📋 Use Case:** Need to validate assumptions before committing to full build

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Hypothesis testing, minimum viable test design, learning-oriented framing

<details>
<summary>Click to view prompt</summary>

```
<experiment_brainstorming>

<experiment_inputs>
WHAT YOU'RE TRYING TO VALIDATE:
1. What's your hypothesis? (specific belief about customers/product)
2. What's the risk if you're wrong? (wasted engineering, wrong direction, lost opportunity)
3. What decision does this inform? (build feature X, change pricing, pivot strategy)
4. How much are you willing to invest to learn? (time, money, engineering resources)

YOUR CONTEXT:
5. Current product state (live, beta, pre-launch)
6. Available resources (can you ship code, or just test messaging)
7. Timeline (need answer in days, weeks, months)

OPTIONAL UPLOADS:
- PRD or feature spec you're validating
- Customer research notes
- Analytics showing current behavior
</experiment_inputs>

<experiment_framework>

You're a growth PM who's run 100+ experiments. You know that most teams skip validation and build the wrong thing. Your job: Design the cheapest, fastest test that produces real learning.

THE REALITY:

Most PMs think: "Let's build a prototype and test it."
Great PMs think: "What's the smallest thing we can do to learn if this is worth building?"

Bad experiments: Take weeks, need engineering, test multiple variables
Good experiments: Take days, need minimal resources, test one thing

---

## PART 1: CLARIFY WHAT YOU'RE ACTUALLY TESTING

### Turn Vague Ideas Into Testable Hypotheses

Vague: "Will users like feature X?"
Testable: "Will 30%+ of active users click 'Try Beta' when offered feature X?"

Your hypothesis:
- We believe: [specific statement]
- We'll know we're right if: [measurable outcome]
- We'll know we're wrong if: [failure condition]

Example:
- We believe: Enterprise customers will pay $50/mo for SSO
- Right if: 40%+ of enterprise prospects say "yes" when offered
- Wrong if: <20% express interest

### Identify What You Don't Know

What do you need to learn?Desirability: Do customers want this?
Viability: Will they pay for it?
Feasibility: Can we build it well enough?
Usability: Can they actually use it?

Your biggest unknown: [which one matters most right now]

### Size the Risk

If you're wrong:
- What gets wasted? [weeks of eng time, opportunity cost]
- What gets delayed? [other features]
- What's the cost? [$X in lost revenue, Y% churn risk]

If the risk is low: Maybe you don't need an experiment. Just ship it.
If the risk is high: You definitely need to validate first.

---

## PART 2: DESIGN EXPERIMENTS (CHEAP TO EXPENSIVE)

### The Ladder of Evidence

Start cheap. Only go expensive if cheap tests validate.

LEVEL 1: FAKE DOOR TESTS (Hours to set up)

The idea: Put a button/page/email that describes the feature. See if people click.

Experiment design:
- What you show: [Fake feature announcement, landing page, in-app banner]
- Call-to-action: [Button that says what]
- What happens when they click: ["Thanks for your interest, we'll notify you" or "Sign up for beta"]
- Success metric: [X% click-through rate]
- Why this works: Tests demand without building anything

Example:
- Show "New: SSO Integration" banner to enterprise users
- Click goes to "Join waitlist" form
- If >30% click → Strong demand signal
- If <10% click → No one cares

Pros: Fast, cheap, tests real behavior
Cons: Only tests interest, not actual usage

---

LEVEL 2: CONCIERGE TEST (Days to set up)

The idea: Manually do what the feature would do. See if customers value it.

Experiment design:
- What you offer: [Manual version of automated feature]
- How you deliver it: [Email, Slack, spreadsheet]
- To whom: [5-10 friendly customers]
- Success metric: [Do they use it? Do they ask for more? Will they pay?]

Example:
- Instead of building analytics dashboard, send customers weekly email with their metrics
- If they reply "This is great, I check it every week" → Build it
- If they ignore emails → They don't actually want analytics

Pros: Tests actual value, not just interest
Cons: Doesn't scale, labor-intensive

---

LEVEL 3: WIZARD OF OZ / PROTOTYPE (Weeks to set up)

The idea: Build the UI but fake the backend. See if people try to use it.

Experiment design:
- What you build: [Clickable prototype or UI shell]
- What's real: [Frontend, flows, visual design]
- What's fake: [AI is actually human, "results" are hardcoded]
- To whom: [Beta group, specific segment]
- Success metric: [Usage rate, completion rate, satisfaction]

Example:
- Build "AI Report Generator" UI
- Requests actually go to your analyst who writes reports
- If users love it and use it weekly → Build the AI
- If they try once and never return → Problem isn't real

Pros: Tests full experience, realistic
Cons: Still requires design/dev work, not scalable

---

LEVEL 4: BETA / LIMITED LAUNCH (Months to build)

The idea: Build real feature but limit to small group.

Experiment design:
- What you build: [Real feature, feature-flagged]
- Who gets it: [10-100 users, specific segment]
- What you measure: [Adoption, retention, satisfaction, willingness to pay]
- Kill criteria: [If <X% adopt in 30 days, we kill it]

Pros: Real usage data, real technical validation
Cons: Expensive, slow, hard to kill after investing

---

### Choose Your Experiment

For your hypothesis, recommend:Experiment type: [Fake door / Concierge / Wizard of Oz / Beta]

Why this level:
[Cheap enough to learn fast, expensive enough to be convincing]

Specific design:
- What you'll build/show: [Exact description]
- To whom: [Specific segment, size]
- Timeline: [How long to run]
- Success metric: [Specific number that means "go"]
- Failure metric: [Number that means "stop"]
- Cost: [Hours/days/weeks, $$]

---

## PART 3: EXPERIMENT EXECUTION PLAN

### Setup Checklist

Before launch:
- [ ] Hypothesis written down (so you can't move goalposts later)
- [ ] Success/failure criteria defined (with numbers)
- [ ] Tracking instrumented (can you measure what you need?)
- [ ] Sample size calculated (do you have enough users?)
- [ ] Timeline set (when do you make decision?)

The honesty check: If results are negative, will you actually kill this? If not, don't waste time on experiment.

### What You'll Measure

Primary metric:
[The one number that answers your hypothesis]

Secondary metrics:
- [Supporting evidence]
- [Quality checks]

Qualitative signals:
- [ ] User interviews with participants
- [ ] Support tickets or feedback
- [ ] What people say vs. what they do

### Decision Framework

If results show:

| Outcome | Action |
|---------|--------|
| Strong yes ([X]% success) | Build it with confidence |
| Weak yes ([Y]% success) | Iterate on experiment or design |
| Unclear / mixed | Run more experiments, different approach |
| Strong no ([Z]% success) | Kill it, learn why, move on |

The hard part: Actually killing features when experiments fail.

---

## PART 4: MULTIPLE EXPERIMENT STRATEGIES

### Test Multiple Variations

If you're not sure of the best approach:

Experiment A: [Approach 1]
Experiment B: [Approach 2]Experiment C: [Approach 3]

Why multiple: You're testing different hypotheses about what customers want

Example:
- A: Test if they want feature as premium add-on ($20/mo)
- B: Test if they want it bundled in higher tier
- C: Test if they want it free but with usage limits

Cheapest test for each:
- A: Email to 100 customers offering add-on, measure interest
- B: Mock up new pricing page, test click-through
- C: Build free version with "upgrade for unlimited" prompt

### Sequential Testing (Build Confidence)

Week 1: Fake door test
- If >20% interest → Continue
- If <10% interest → Stop

Week 2: Concierge test with 5 customers
- If 4/5 use it regularly → Continue
- If <3/5 engage → Stop

Week 4: Prototype with 20 customers
- If >50% weekly active → Build real feature
- If <30% active → Redesign or kill

Why sequential: Each stage reduces risk before bigger investment

---

## THE OUTPUT

### Experiment Brief

Hypothesis:
[What we believe]

Recommended Experiment:
[Type and approach]

What we'll build/test:
[Specific description]

Who we'll test with:
[Segment, size]

Success looks like:
[Metric > X%]

Failure looks like:
[Metric < Y%]

Timeline:
[X weeks to run, Y weeks to analyze]

Cost:
[Resources needed]

Decision:
[What we'll do based on each outcome]

### Multiple Experiment Options

Option 1: Cheapest/Fastest
[Details]

Option 2: Medium Investment
[Details]

Option 3: Highest Confidence
[Details]

Recommendation: [Which to start with and why]

</experiment_framework>

<quality_check>

Is this actually an experiment?
- [ ] Tests a specific hypothesis (not "let's see what happens")
- [ ] Has clear success/failure criteria (not subjective)
- [ ] Costs less than just building it (otherwise just ship)

Will you learn something actionable?
- [ ] Results inform a real decision
- [ ] You'll actually kill feature if experiment fails
- [ ] You're testing the riskiest assumption first

Is it the simplest test possible?
- [ ] Can't make it cheaper/faster without losing signal
- [ ] Not over-engineering the validation

</quality_check>

<meta_wisdom>

On experiments:

Most teams don't run experiments because they're afraid of negative results.

But here's the truth: Negative results are good. They save you from building the wrong thing.

Positive results are expensive (you have to build it).
Negative results are cheap (you don't build it).

The key insight:

The goal isn't to validate your ideas.
The goal is to invalidate them as cheaply as possible.

If an idea survives 3 cheap experiments trying to kill it, then it's probably worth building.

On fake door tests:

Some PMs worry: "Isn't this lying to customers?"

No. You're being honest: "We're considering building X. Interested?"

What's dishonest is building something no one wants because you never asked.

Remember:

Build to learn, not to ship.

The best PMs kill 80% of ideas before writing code.
The worst PMs build 100% of ideas and wonder why adoption sucks.

Experiment early. Experiment often. Celebrate when experiments fail—you just saved the company from wasting resources.

</meta_wisdom>

</experiment_brainstorming>
```

</details>

---

### Decide Between Options


**📋 Use Case:** Stuck between 2-3 options, need framework to think through decision

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Decision matrix, trade-off analysis, second-order thinking

<details>
<summary>Click to view prompt</summary>

```
<decision_framework>

<decision_inputs>
WHAT ARE YOU DECIDING:
[The decision in one sentence]

YOUR OPTIONS:
Option A: [Description]
Option B: [Description]
Option C: [Description if applicable]

CONTEXT:
- Why this matters: [Stakes/impact]
- Timeline: [How soon you need to decide]
- Constraints: [Budget, resources, politics]
- What you're optimizing for: [Speed, quality, cost, risk, etc.]

WHAT YOU'VE TRIED:
[If you've already thought through pros/cons, share that]
</decision_inputs>

<framework>

You're a decision coach who helps PMs get unstuck. Your job: structure the thinking, surface trade-offs, recommend a path.

---

## DECISION FRAMEWORK

### The Core Trade-Off

This decision is really about:
[What you're trading - usually speed vs quality, risk vs reward, etc.]

---

### Option Analysis

OPTION A: [Name it]Pros:
- [Specific advantage]
- [Specific advantage]

Cons:
- [Specific disadvantage]
- [Specific disadvantage]

Best if:
[Scenario where this is the right choice]

Risks:
[What could go wrong]

---

OPTION B: [Name it]

[Same structure]

---

OPTION C: [Name it if exists]

[Same structure]

---

### The Questions That Matter

Before deciding, answer these:

1. Reversibility: Can you undo this decision later?
- If yes → Lower stakes, decide faster
- If no → Higher stakes, be more careful

2. Information: What would you need to know to be 100% confident?
- Can you get that info easily? → Get it
- Would it take months? → Decide with what you have

3. Second-order effects: What happens after what happens?
- If you pick A, then what? Then what?

4. Regret minimization: Will you regret NOT trying one of these?

---

## RECOMMENDATION

Go with: [Option X]Why:
[Specific reasoning based on your context]

But only if:
[Conditions that make this the right call]

How to de-risk it:
[What to do to reduce downside]

When to revisit:
[Timeline or trigger to reconsider]

---

## ALTERNATIVE: If You're Still Stuck

Could you:
- Test both cheaply? (A/B test, prototype, pilot)
- Do them sequentially? (A now, B later)
- Do a hybrid? (Combine elements)
- Get more data? (What would help you decide)

---

## RED FLAGS TO WATCH

You might be overthinking if:
- This decision is reversible
- The options are 80% similar
- You've been debating for weeks
- Analysis paralysis has set in

→ Just pick one and move forward.

</framework>

<meta_guidance>

Decision-making wisdom:

Most decisions are reversible. Make them faster.

Some decisions are one-way doors. Those deserve careful thought.

The Jeff Bezos principle:
Type 1 decisions (irreversible) → Go slow, get consensus
Type 2 decisions (reversible) → Go fast, you can fix it

The 70% rule:
If you have 70% of the info you wish you had, decide.
Waiting for 90% takes too long and costs too much.

When you're truly stuck:
Flip a coin. If you're disappointed by the result, you know what you wanted.

</meta_guidance>

</decision_framework>
```

</details>

---

### Generate Ideas/Alternatives

**📋 Use Case:** Stuck on a problem, need fresh perspectives or alternatives

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Lateral thinking, constraint removal, perspective shifting

<details>
<summary>Click to view prompt</summary>

```
<generate_ideas>

<problem_inputs>
WHAT'S THE PROBLEM:
[Describe what you're trying to solve]

WHAT YOU'VE TRIED:
[Ideas you already considered]

CONSTRAINTS:
- Budget: [Tight / Flexible / Unlimited]
- Timeline: [Urgent / Normal / No rush]
- Resources: [What you have / don't have]
- Technical: [Any limitations]

WHAT WOULD MAKE A GOOD IDEA:
- [ ] Novel/creative
- [ ] Practical/achievable
- [ ] Quick to test
- [ ] Cheap to try
- [ ] Bold/ambitious
- [ ] Safe/low-risk
</problem_inputs>

<ideation_framework>

You're a creative problem-solver who generates alternatives. Your job: break people out of their default thinking.

---

## FRESH PERSPECTIVES

### Reframe The Problem

You described it as:
[Original problem statement]

Alternative framings:
1. [Different angle on same problem]
2. [More specific version]
3. [Broader version]
4. [Opposite framing]

Which framing opens new solutions?

---

### Idea Generation

APPROACH 1: [Name it]
- The idea: [Specific approach]
- Why it could work: [Logic]
- Quick test: [How to validate cheaply]
- Risk: [What could go wrong]

APPROACH 2: [Name it]
[Same structure]

APPROACH 3: [Name it]
[Same structure]

APPROACH 4: [Wildcard - ambitious/creative]
[Same structure]

APPROACH 5: [Minimal - simplest possible]
[Same structure]

---

### Constraint Removal

If you had unlimited budget:
[What would you do?]

If you had unlimited time:
[What would you try?]

If you had 10x the team:
[What becomes possible?]

If you had to solve it in 1 week:
[What's the scrappy version?]

If you couldn't use technology:
[How would you solve it manually?]

---

### Analogies From Other Domains

How does [other industry] solve similar problems?

Examples:
- How does retail handle [your problem]?
- How does gaming handle [your problem]?
- How does healthcare handle [your problem]?

What can you borrow?

---

### Inversion

Instead of solving the problem, how would you make it worse?
[List ways to make it worse]

Now, do the opposite:
[Turn each into a potential solution]

</ideation_framework>

<idea_categories>

### Quick Wins (Do This Week)

Idea:
[Low-effort, immediate impact]

Why now:
[Why this works short-term]

---

### Experiments (Test in 2-4 Weeks)

Idea:
[Testable hypothesis]

How to test:
[Minimal viable experiment]

---

### Big Bets (Multi-Month)

Idea:
[Ambitious, requires investment]

Why it could work:
[Strategic rationale]

---

### Crazy Ideas (Probably Won't Do But Fun)

Idea:
[Out there, but creative]

Why it's interesting:
[Kernel of insight even if not practical]

</idea_categories>

<meta_guidance>

Ideation principles:Quantity before quality
Generate 20 ideas, pick the best 3.

Suspend judgment
Don't shoot down ideas during generation.
Evaluate later.

Combine ideas
The best solution is often 2-3 ideas merged.

Start with extremes
Most obvious idea + craziest idea = interesting middle ground.

When stuck:
- Work backwards from ideal outcome
- Steal ideas from adjacent industries
- Ask "What would [person] do?"
- Remove one constraint and see what opens up

Remember:
The first idea is usually the obvious one.
The good ideas come after that.

</meta_guidance>

</generate_ideas>
```

</details>

---

### Quarterly Planning


**📋 Use Case:** Need to plan next quarter's roadmap and priorities

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** OKR framework, capacity planning, strategic prioritization

<details>
<summary>Click to view prompt</summary>

```
<quarterly_planning>

<planning_inputs>
PASTE YOUR INPUTS:
- Company/team goals for quarter
- Backlog of ideas/requests
- In-flight projects
- Team capacity
- Known constraints or deadlines

CONTEXT:
- What shipped last quarter: [Key outcomes]
- What's carrying over: [Unfinished work]
- Strategic priorities: [Top company goals]
- Team size: [How many people]

PLANNING FOR:
- Quarter: [Q1/Q2/Q3/Q4 Year]
- Team: [Your team name]
</planning_inputs>

<planning_framework>

You help PMs plan quarters that are ambitious but achievable. Your job: balance strategic bets with team capacity reality.

---

## QUARTERLY PLAN

Q[X] [Year] - [Team Name]

---

### Theme

This quarter is about:
[One sentence that captures the focus]

Why this focus:
[Strategic rationale]

---

### Goals (OKRs)

Objective 1: [Ambitious, qualitative goal]

Key Results:
- KR1: [Measurable outcome] - Owner: [Name]
- KR2: [Measurable outcome] - Owner: [Name]
- KR3: [Measurable outcome] - Owner: [Name]

Objective 2: [If applicable]

[Same structure]

---

### Roadmap

MONTH 1:Focus: [What we're shipping/achieving]

Projects:
- [Project name] - [Brief description] - Owner: [Name]
- [Project name] - [Brief description] - Owner: [Name]

Milestones:
- [Key milestone and date]

---

MONTH 2:

[Same structure]

---

MONTH 3:

[Same structure]

---

### Capacity Planning

Team capacity: [X person-weeks available]

Allocated:
- Project A: [Y weeks]
- Project B: [Z weeks]
- Bug fixes/maintenance: [W weeks, usually 20%]
- Buffer: [V weeks, usually 20%]

Total: [Should equal capacity]

---

### What We're NOT Doing

[Explicitly list things you're deferring]

Deferred to Q[X+1]:
- [Feature/project]
- [Feature/project]

Not doing (saying no):
- [Request/idea]
- [Request/idea]

---

### Risks & Dependencies

Risk 1: [What could derail plan]
- Mitigation: [How you'll handle it]
- Owner: [Who's monitoring]

Dependency 1: [External dependency]
- Impact if delayed: [Consequence]
- Backup plan: [Alternative]

---

### Success Criteria

At end of quarter, we'll know we succeeded if:
- [ ] [Specific outcome]
- [ ] [Specific outcome]
- [ ] [Specific outcome]

</planning_framework>

<planning_process>

### Step 1: Gather Inputs

From leadership:
- Company OKRs for quarter
- Strategic priorities
- Revenue/growth targets

From customers/data:
- Top feature requests
- Churn reasons
- Usage patterns
- NPS feedback

From team:
- Technical debt priorities
- Infrastructure needs
- Velocity concerns

From stakeholders:
- Sales asks
- Marketing needs
- Support pain points

---

### Step 2: Categorize Work

Strategic Bets (30-40% of capacity)
[New initiatives that drive growth/differentiation]

Customer Asks (30-40% of capacity)
[High-impact feature requests]

Technical Excellence (20-30% of capacity)
[Tech debt, infrastructure, reliability]

Business as Usual (10-20% of capacity)
[Bug fixes, maintenance, support]

---

### Step 3: Prioritization

Must do (non-negotiable):
- [ ] [Hard deadline or dependency]
- [ ] [Critical to company goals]

Should do (high value):
- [ ] [Big impact, aligned to OKRs]
- [ ] [Customer commitment]

Could do (if capacity):
- [ ] [Nice to have]
- [ ] [Low-hanging fruit]

Won't do (explicit no):
- [ ] [Not aligned to goals]
- [ ] [Can wait until later]

---

### Step 4: Capacity Reality Check

Available capacity:
- [X] people × 13 weeks × 40 hrs = [Y] hours
- Minus holidays/PTO: [Z] hours
- Minus meetings/overhead (30%): [W] hours
- Net capacity: [V] hours or [P] person-weeks

Rule of thumb:
- Big project: 4-8 weeks
- Medium project: 2-4 weeks
- Small project: <2 weeks

Typical quarter:
- 2-3 big projects
- 3-4 medium projects
- Ongoing small improvements

If your plan exceeds capacity:
Cut scope, not quality.

---

### Step 5: Timeline & Sequencing

Dependencies:
What must happen before what?

Parallelization:
What can different people work on simultaneously?

Risk management:
Start risky/uncertain work earlier.

Buffer:
Always keep 20% buffer for unknowns.

</planning_process>

<meta_guidance>

Quarterly planning principles:Be ambitious but realistic
Plan for 70% capacity, not 100%
Things take longer than you think

Choose a theme
Don't do 10 unrelated things
Pick a focus and commit

Say no explicitly
Document what you're not doing
Prevents scope creep

Build in flexibility
Plans change
Don't over-commit to rigid timeline

Get buy-in early
Share draft with team and stakeholders
Adjust before committing

Review monthly
Quarterly plans aren't set-it-and-forget-it
Check in and adjust as needed

Remember:
The goal isn't to plan perfectly.
It's to align team on what matters.

Done quarterly plan > perfect quarterly plan.

</meta_guidance>

</quarterly_planning>
```

</details>

---

### Pricing Analysis

**📋 Use Case:** Need to set or change pricing, or analyze pricing strategy

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Value-based pricing, competitive positioning, willingness-to-pay analysis

<details>
<summary>Click to view prompt</summary>

```
<pricing_analysis>

<pricing_inputs>
CURRENT STATE:
- Current pricing: [What you charge now, or "not set yet"]
- Revenue model: [Per user, per usage, flat fee, freemium]
- Competitors' pricing: [What others charge]

YOUR PRODUCT:
- What it does: [Core value prop]
- Target customers: [Who buys this]
- Cost to serve: [Rough COGS or operational cost per customer]

THE QUESTION:
- [ ] Set initial pricing (new product)
- [ ] Change pricing (increase/decrease)
- [ ] Add new tier
- [ ] Move to different model

RESEARCH/DATA:
- Customer feedback on pricing: [What you've heard]
- Willingness to pay signals: [Any data on what customers would pay]
- Churn related to pricing: [If relevant]
</pricing_inputs>

<pricing_framework>

You help PMs think through pricing strategy. Your job: connect pricing to value, not just costs.

---

## PRICING ANALYSIS

### Value-Based Pricing Foundation

What value does your product create?Quantifiable value:
- Saves time: [X hours/week]
- Saves money: [$Y/month in costs eliminated]
- Generates revenue: [$Z in new revenue enabled]
- Reduces risk: [$ value of problems prevented]

Your product's value: $[Calculated total]

Pricing rule of thumb:
Charge 1/10th to 1/3rd of value created.

If product saves customer $10K/month, you can charge $1-3K/month.

---

### Competitive Positioning

Competitive pricing landscape:

| Competitor | Price | Positioning |
|------------|-------|-------------|
| [Name] | [$X/mo] | [Premium/Mid/Budget] |
| [Name] | [$Y/mo] | [Premium/Mid/Budget] |
| Your target | [?] | [Where you want to be] |

Where do you want to be?
- [ ] Premium (20-30% above market)
- [ ] Market rate (within 10% of competition)
- [ ] Value option (20-30% below market)

Why that positioning:
[Strategic rationale]

---

### Pricing Model Options

OPTION 1: Per-User Pricing
- Structure: $[X]/user/month
- Good if: Value scales with team size
- Bad if: Encourages limiting users (adoption blocker)

OPTION 2: Usage-Based Pricing
- Structure: $[X] per [action/event/GB]
- Good if: Costs scale with usage, perceived as fair
- Bad if: Unpredictable bills scare customers

OPTION 3: Flat-Fee Pricing
- Structure: $[X]/month for unlimited
- Good if: Simple, predictable, encourages adoption
- Bad if: Heavy users cost you more than they pay

OPTION 4: Tiered Pricing
- Structure: Starter/Pro/Enterprise
- Good if: Different segments want different things
- Bad if: Complexity can confuse

OPTION 5: Freemium
- Structure: Free tier + paid upgrades
- Good if: PLG motion, network effects, low marginal cost
- Bad if: Free users never convert, support burden

Recommendation: [Which model and why]

---

### Tiered Pricing Structure (If Applicable)

FREE/TRIAL TIERPrice: $0
Target: Individuals, evaluators
Includes:
- [Limited feature set]
- [Usage limits]

Conversion path: [How they upgrade]

---

STARTER/BASIC TIERPrice: $[X]/month
Target: [Segment]
Includes:
- [Core features]
- [Support level]

Why this price: [Rationale]

---

PROFESSIONAL TIERPrice: $[Y]/month (X.X% increase)
Target: [Segment]
Includes:
- Everything in Starter
- [Additional features that matter]
- [Better support]

Value gap: [Why someone upgrades]

---

ENTERPRISE TIERPrice: Custom (typically $[Z]+ range)
Target: [Large companies]
Includes:
- Everything in Pro
- [Enterprise features: SSO, SCIM, etc.]
- [Dedicated support]
- [SLAs]

Sold via: [Sales team vs self-serve]

---

### Pricing Principles

Good pricing:
- Simple to understand
- Aligns with value received
- Has natural upgrade path
- Predictable for customer

Avoid:
- Too many tiers (confusing)
- Pricing on features (wrong incentive)
- Nickel-and-diming (annoying)

---

### Testing Strategy

Before committing:Test 1: Customer interviews
- Ask: "At what price does this become expensive but still worth it?"
- Ask: "At what price does this become too expensive?"
- Gap between = your pricing range

Test 2: A/B test pricing page
- Show different prices to different visitors
- Measure conversion rate × revenue per customer
- Optimize for revenue, not conversions

Test 3: Grandfather existing customers
- New pricing for new customers only
- Measure uptake before forcing migration

---

### Migration Plan (If Changing Pricing)

Existing customers:
- [ ] Grandfather at current price (indefinite)
- [ ] Grandfather for X months, then migrate
- [ ] Force migration (with advance notice)

Communication:
- Announce: [X weeks ahead]
- Message: [Focus on value added]
- Support: [How to help customers adjust]

Risk mitigation:
- Watch churn closely
- Have win-back offer ready
- Support team prepared for objections

</pricing_framework>

<meta_guidance>

Pricing strategy principles:Price on value, not cost
Your costs don't matter to customers
What matters: value you create for them

Simple > complex
If your pricing needs a calculator, it's too complex

Room to grow
Have upgrade path built in
Easy to move from $10→$50→$200/mo

Raise prices regularly
Many startups charge too little
Easier to lower than raise

Test and iterate
First pricing is always wrong
Be willing to change

Remember:
Pricing is positioning.
Premium price = premium product (in customers' minds)
Cheap price = cheaper product

Most PMs undercharge.

</meta_guidance>

</pricing_analysis>
```

</details>

---

### Brainstorm Growth Loops

**📋 Use Case:** Design viral or scalable growth mechanisms for product

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Systems thinking, network effects, incentive design

<details>
<summary>Click to view prompt</summary>

```
<outcome_roadmap>

<roadmap_inputs>
STRATEGIC GOALS:
[Company/team OKRs or north star]

CURRENT STATE:
- Key problems: [What's broken or limiting]
- Customer pain points: [From research]
- Business gaps: [What's holding back growth]

CONSTRAINTS:
- Team capacity: [Size and timeline]
- Technical dependencies: [Platform limitations]
- Market timing: [Competitive or seasonal factors]

ROADMAP HORIZON:
- [ ] This quarter
- [ ] Next 2 quarters
- [ ] This year
</roadmap_inputs>

<roadmap_framework>

You build roadmaps that preserve flexibility while giving direction. Your job: define outcomes to achieve, not features to ship.

THE DIFFERENCE:Feature-based roadmap:
"Q2: Build SSO integration"
"Q3: Add analytics dashboard"

Outcome-based roadmap:
"Q2: Enable enterprise buyers to deploy across teams (may require SSO, may not)"
"Q3: Help users understand what's working (analytics is one option)"

Why outcomes are better:
- Preserves solution flexibility
- Focuses on impact, not output
- Easier to prioritize
- Less commitment to specific features

---

## OUTCOME-BASED ROADMAP

Team: [Your team]
Timeframe: [Period]
Last updated: [Date]

---

### Strategic Context

Company goal:
[What the company is trying to achieve]

Our role:
[How your team contributes to that goal]

Success looks like:
[Specific outcome that shows you're winning]

---

### Roadmap Theme

This period is about:
[One sentence focus - the through-line connecting everything]

---

### Now (Current Quarter)

OUTCOME 1: [User outcome or business result]Why this matters:
[Connection to strategy and impact]

Current state:
- Problem: [Specific pain point]
- Impact: [Who affected, how often]
- Baseline metric: [Current performance]

Target outcome:
- Success metric: [What improves]
- Target: [Specific number or %, timeframe]

How we might solve it:
[Possible approaches - note the flexibility]
- Option A: [Approach]
- Option B: [Alternative approach]
- TBD: [Will decide based on research]

What we'll learn:
[Validation or insights we need]

---

OUTCOME 2: [Another outcome]

[Same structure]

---

### Next (Following Quarter)

OUTCOME 1: [Future outcome]

[Similar structure but less detail]

Dependencies:
[What needs to happen first]

Open questions:
[What we'll learn in current quarter that informs this]

---

### Later (Future Quarters)

OUTCOME 1: [Longer-term outcome]Why eventually:
[Strategic importance but not urgent]

What could change our mind:
[Signals that would make us pull this forward]

---

### What We're NOT Doing

Intentionally deferred:
- [Outcome or area we considered but postponed]
- Why not now: [Reasoning]
- Reconsidered: [When we'll revisit]

Explicitly out of scope:
- [Request or area we're not addressing]
- Why no: [Strategic reason]

---

### How We'll Measure Success

Metrics we're moving:

| Metric | Baseline | Target | Timeframe |
|--------|----------|--------|-----------|
| [Metric] | [Current] | [Goal] | [When] |
| [Metric] | [Current] | [Goal] | [When] |

Leading indicators:
[Early signals we're on track]

Lagging indicators:
[Proof of long-term success]

---

### Dependencies & Risks

Depends on other teams:
- [Team]: [What we need from them]
- [Team]: [What we need from them]

Technical dependencies:
- [Dependency] - Risk: [What if it's delayed]

Market/external factors:
- [Factor] - Contingency: [How we'll adapt]

---

### Flexibility & Decision Points

We'll decide by [date]:
[Specific choice between options]

We'll pivot if:
[Conditions that would change our plan]

We'll know we're wrong if:
[Metrics or signals that indicate we should change course]

</roadmap_framework>

<roadmap_examples>

### Example 1: Growth Team Roadmap

Strategic Context:
Company goal: Double paid conversions
Our role: Improve trial → paid conversion

Theme: Make value obvious before trial ends

---

NOW: Enable users to see value in first 3 daysCurrent state:
- 40% of trials never complete setup
- Users who complete setup in first week convert at 60% vs 15%

Target:
- 70% complete setup in first 3 days
- 50% overall conversion rate

How we might solve:
- Guided onboarding flow
- Pre-populated demo data
- Templated quick starts
- [Will test and decide]

---

NEXT: Help users prove ROI to stakeholdersWhy eventually:
Users love product but can't get buy-in

Possible approaches:
- Usage reports they can share
- ROI calculator
- Integration with their tools

[Will validate in customer interviews]

---

### Example 2: Platform Team Roadmap

Strategic Context:
Company goal: Support 10x growth
Our role: Infrastructure that scales

Theme: Performance and reliability at scale

---

NOW: Zero customer-impacting outagesCurrent state:
- 2-3 incidents per month
- Average 30min downtime
- Root cause: Database connection limits

Target:
- <1 incident per month
- <5min MTTR

How we might solve:
- Connection pooling
- Circuit breakers
- Better monitoring
- [Architecture review to decide]

---

NEXT: Support 100K concurrent usersCurrent: Starts degrading at 10K

Approaches to evaluate:
- Horizontal scaling
- Caching layer
- Database sharding

</roadmap_examples>

<meta_guidance>

Outcome roadmap principles:Outcomes > Outputs
Not "ship feature X"
But "enable outcome Y"

Problems > Solutions
Not "build analytics dashboard"
But "help users understand what's working"

Flexibility > Commitment
Don't commit to specific features
Commit to solving problems

Metrics > Vague goals
"Improve onboarding" is vague
"70% complete setup in 3 days" is measurable

Themes > Random list
Roadmap should tell a story
Not disconnected feature list

Regular updates
Outcome roadmaps are living docs
Update monthly as you learn

When to be specific:
- Current quarter: More detail
- Next quarter: Less detail
- Future: Themes only

Remember:

Best roadmaps give teams direction without micromanaging.

You're aligning on the destination, not dictating the route.

</meta_guidance>

</outcome_roadmap>
```

</details>

---

### Build vs Buy Analysis

**📋 Use Case:** Deciding whether to build feature in-house or buy/integrate external tool

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** TCO calculation, strategic fit assessment, risk analysis

<details>
<summary>Click to view prompt</summary>

```
<build_vs_buy>

<decision_inputs>
WHAT YOU NEED:
[Specific capability or feature - e.g., "payment processing", "analytics", "auth system"]

WHY YOU NEED IT:
- Problem it solves: [Specific pain point]
- Users affected: [Who needs this]
- Timeline: [How urgent]

OPTIONS YOU'RE CONSIDERING:
- Build in-house
- Buy/integrate: [Specific vendor(s) you're evaluating]
- Hybrid: [If applicable]

YOUR CONTEXT:
- Team capacity: [Eng resources available]
- Budget: [Available funding]
- Technical debt tolerance: [Can you maintain another system?]
- Strategic importance: [Core to product or peripheral?]
</decision_inputs>

<decision_framework>

You analyze build vs buy decisions systematically. Follow this process:

STEP 1: Define what you actually need

Be specific about requirements:

Functional requirements:
- [ ] Must-haves (deal-breakers)
- [ ] Nice-to-haves (can live without)
- [ ] Won't-need (out of scope)

Non-functional requirements:
- Performance (latency, throughput)
- Scale (current and 2 years out)
- Reliability (uptime needs)
- Security (compliance requirements)
- Integrations (what it must connect to)

Avoid:
Over-specifying (building for problems you don't have)

STEP 2: Calculate true cost of buildingInitial build cost:
- Eng time to build: [X weeks × Y engineers]
- Design time: [Z weeks]
- Testing/QA time: [W weeks]
- Total hours × hourly cost = $[Initial cost]

Ongoing maintenance cost (annual):
- Bug fixes: [~20% of build time per year]
- Updates/improvements: [Another 20%]
- Scaling/operations: [Infrastructure + eng time]
- Security patches: [Ongoing vigilance]
- Documentation: [Keeping it current]
- Annual maintenance = 40-60% of initial build costOpportunity cost:
- What else could team build instead?
- What revenue could those features generate?
- What strategic initiatives get delayed?

Technical debt:
- Complexity added to codebase
- Knowledge burden (only your team understands it)
- Future migration cost (if you eventually replace it)

STEP 3: Calculate true cost of buyingVendor costs:
- Subscription: $[X/month or /user]
- Setup/onboarding: $[One-time]
- Training: [Time + cost]
- Overage charges: [If you exceed limits]
- 5-year total: $[X × 60 months]Integration costs:
- Eng time to integrate: [Y weeks]
- Ongoing integration maintenance: [Z hours/month]
- API rate limits (does it constrain you?)

Customization costs:
- Can you customize it?
- Cost to customize: [If needed]
- Limitations you'll hit: [Features you can't have]

Switching costs (if vendor goes away):
- Data export difficulty
- Vendor lock-in risk
- Migration effort to alternative

Hidden costs:
- Support tickets (your team still helps users)
- Feature requests you can't fulfill
- Waiting for vendor to ship what you need

STEP 3: Assess strategic fitIs this core to your product?Core (should probably build):
- Unique differentiation
- Competitive advantage
- Deep integration with product
- IP you want to own

Non-core (should probably buy):
- Commodity feature (everyone has it)
- Not differentiated
- Peripheral to main value prop
- Complex domain you don't need to own

Example:
- Stripe for payments (buy) - not core unless you're fintech
- Proprietary algorithm (build) - this IS your differentiation

STEP 4: Evaluate vendor options

For each vendor:

Product fit:
- [ ] Meets must-have requirements
- [ ] Has nice-to-haves
- [ ] Missing deal-breakers

Company viability:
- Funding/profitability
- Customer count
- Market position
- Longevity risk

Integration quality:
- API documentation
- SDK availability
- Integration examples
- Support responsiveness

Customer experience:
- Reviews (G2, Capterra)
- Reference customers
- Known issues

STEP 5: Run decision matrix

Score each option on key criteria:

| Criteria | Weight | Build | Vendor A | Vendor B |
|----------|--------|-------|----------|----------|
| Cost (5yr) | 0.3 | [Score 1-10] | [Score] | [Score] |
| Time to market | 0.2 | [Score] | [Score] | [Score] |
| Feature fit | 0.2 | [Score] | [Score] | [Score] |
| Maintenance burden | 0.15 | [Score] | [Score] | [Score] |
| Strategic control | 0.15 | [Score] | [Score] | [Score] |
| Total | 1.0 | [Weighted] | [Weighted] | [Weighted] |

Highest score = recommended approachSTEP 6: Consider hybrid approaches

Sometimes best answer is "both":

Build wrapper around vendor:
- Use vendor for heavy lifting
- Build thin layer for customization
- Insulates from vendor changes

Build MVP, buy later:
- Build quick version to validate
- Replace with vendor when proven
- Reduces risk of building wrong thing

Buy now, build later:
- Use vendor to move fast
- Build in-house once you understand needs
- Common path for growing companies

STEP 7: Make the recommendationDecision framework:Build if:
- Core differentiation
- Vendor options don't fit
- Long-term cost of buying > building
- Team has capacity
- Low complexity

Buy if:
- Not core differentiation
- Good vendor options exist
- Faster time to market matters
- Team at capacity
- High complexity/risk to build

Be honest about:
- Bias toward building (engineers love to build)
- Bias toward buying (easier short-term)
- Pressure from stakeholders

</decision_framework>

---

## BUILD VS BUY ANALYSIS

Capability Needed: [What you're evaluating]Decision Owner: [Name]Decision Deadline: [When you need to decide]Current Status: [Under evaluation]

---

### Executive Summary

Recommendation: [Build / Buy / Hybrid]

Rationale (one paragraph):
[Why this is the best choice given context, cost, strategy, and timeline]

Key factors:
- Cost: [Build vs buy comparison]
- Time: [How long each takes]
- Strategy: [Core vs non-core]
- Risk: [What could go wrong]

If approved, next steps:
[What happens immediately]

---

### What We Need

The problem:
[Specific pain point or gap]

Who needs it:
- User segment: [Which users]
- Usage pattern: [How often, how critical]
- Volume: [Scale requirements]

Why now:
- Business driver: [What's pushing this]
- Timeline: [Urgency]
- Competition: [Are competitors doing this]

---

### Requirements

MUST HAVE (Deal-breakers):
- [ ] [Requirement 1]
- [ ] [Requirement 2]
- [ ] [Requirement 3]

NICE TO HAVE:
- [ ] [Feature 1]
- [ ] [Feature 2]

OUT OF SCOPE:
- [Thing we don't need]
- [Another thing we don't need]

Non-functional requirements:
- Performance: [Latency/throughput needs]
- Scale: [Current + 2-year projection]
- Uptime: [How critical]
- Security: [Compliance/standards]
- Integration: [What it must connect to]

---

### Option 1: Build In-House

What we'd build:
[High-level description of solution]

Approach:
[Technical approach, architecture]

Timeline:
- Design: [X weeks]
- Build: [Y weeks]
- Test: [Z weeks]
- Total: [W weeks to production]Team required:
- [N] engineers × [M] weeks
- [P] designer × [Q] weeks
- PM/QA time: [Estimate]

---

COST ANALYSIS:Initial build:
- Engineering: [Hours × rate] = $[X]
- Design: [Hours × rate] = $[Y]
- Infrastructure: $[Z/month]
- Total initial: $[A]Ongoing (annual):
- Maintenance: $[40-60% of build cost]
- Improvements: $[Estimated]
- Infrastructure: $[Cost × 12]
- Support: $[Estimated]
- Annual recurring: $[B]5-year total cost of ownership:
$[A] + ($[B] × 5) = $[Total]

---

PROS:
✅ Full control over features
✅ Exact fit to our needs
✅ No vendor dependency
✅ IP ownership
✅ [Other advantages]

CONS:
❌ Longer time to market ([W] weeks)
❌ Opportunity cost (team could build [X])
❌ Maintenance burden
❌ Complexity added to codebase
❌ [Other disadvantages]

---

RISKS:
- Technical risk: [What could go wrong technically]
- Mitigation: [How to reduce risk]
- Timeline risk: [Could take longer than expected]
- Mitigation: [Buffer, phasing]
- Maintenance risk: [Ongoing burden]
- Mitigation: [Team capacity plan]

---

### Option 2: Buy [Vendor Name]

What they provide:
[Description of vendor solution]

How it works:
[Integration approach]

Timeline:
- Evaluation: [1-2 weeks]
- Contract: [1 week]
- Integration: [X weeks]
- Testing: [Y weeks]
- Total: [Z weeks to production]

---

COST ANALYSIS:Vendor pricing:
- Subscription: $[X/month] or $[Y/user/month]
- Setup fee: $[One-time]
- Support: [Included or $Z/month]

Integration costs:
- Eng time: [N weeks × rate] = $[A]
- Ongoing maintenance: $[B/month]

5-year total cost of ownership:
($[X] × 60) + $[A] + ($[B] × 60) = $[Total]

---

PROS:
✅ Faster time to market ([Z] weeks vs [W] weeks)
✅ Proven solution (used by [customers])
✅ No maintenance burden
✅ Regular updates included
✅ [Other advantages]

CONS:
❌ Monthly cost ($[X])
❌ Less control over features
❌ Vendor dependency
❌ May not fit perfectly
❌ [Other disadvantages]

---

VENDOR EVALUATION:Product fit:
- Must-haves met: [X of Y] ✅/❌
- Nice-to-haves met: [A of B]
- Missing features: [List]

Company viability:
- Funding: [Stage, amount]
- Customer base: [Size, notable customers]
- Market position: [Leader/challenger/niche]
- Risk assessment: [Low/medium/high]

Integration quality:
- API quality: [Good/okay/poor]
- Documentation: [Link, assessment]
- Support: [Response time, quality]
- Community: [Active/moderate/none]

Customer references:
- [Company 1]: "[Quote about experience]"
- [Company 2]: "[Quote]"
- Common complaints: [From reviews]

---

RISKS:
- Vendor risk: [Could go out of business, raise prices]
- Mitigation: [Contract terms, exit plan]
- Feature gap risk: [Missing features we need]
- Mitigation: [Workarounds, roadmap]
- Lock-in risk: [Hard to switch later]
- Mitigation: [Data export, abstraction layer]

---

### Option 3: [Another Vendor or Hybrid]

[Same analysis structure if evaluating multiple vendors or hybrid approach]

---

### Side-by-Side Comparison

| Factor | Build | Vendor A | Vendor B |
|--------|-------|----------|----------|
| Time to market | [W weeks] | [Z weeks] | [Y weeks] |
| Initial cost | $[X] | $[Y] | $[Z] |
| 5-year TCO | $[A] | $[B] | $[C] |
| Feature fit | 100% | 85% | 70% |
| Control | Full | Limited | Limited |
| Maintenance | High | Low | Low |
| Strategic fit | [Core/Non-core] | [Score] | [Score] |

---

### Decision Matrix

Weighted scoring (1-10 scale):

| Criteria | Weight | Build | Vendor A | Vendor B |
|----------|--------|-------|----------|----------|
| 5-year cost | 30% | 6 (1.8) | 8 (2.4) | 7 (2.1) |
| Time to market | 20% | 4 (0.8) | 9 (1.8) | 8 (1.6) |
| Feature fit | 20% | 10 (2.0) | 8 (1.6) | 7 (1.4) |
| Maintenance | 15% | 3 (0.45) | 9 (1.35) | 8 (1.2) |
| Strategic control | 15% | 10 (1.5) | 5 (0.75) | 5 (0.75) |
| TOTAL | 100% | 6.55 | 7.9 | 7.05 |

Winner by score: [Vendor A with 7.9]

---

### Strategic Considerations

Is this core to our business?
[Yes/No - explain]

If YES (core):
Lean toward build because:
- Competitive differentiation
- Want full control
- Long-term strategic asset

If NO (non-core):
Lean toward buy because:
- Commodity capability
- Not differentiated
- Let experts handle it

Our assessment:
[This is core/non-core because...]

---

Competitive landscape:
- Do competitors build or buy? [Pattern]
- Industry best practice: [What leaders do]
- Our differentiation: [How this factors in]

---

Team capacity reality:
- Current sprint velocity: [Points/sprint]
- This would consume: [X% of capacity for Y months]
- Impact on roadmap: [What gets delayed]
- Opportunity cost: [Revenue/value of delayed work]

---

### Recommendation

Decision: [Build / Buy Vendor A / Buy Vendor B]

Primary rationale:
[2-3 sentences explaining why]

Supporting factors:
1. [Reason 1]
2. [Reason 2]
3. [Reason 3]

Trade-offs accepted:
- We're accepting: [Downside of chosen option]
- In exchange for: [Benefit we're prioritizing]

---

Why not the alternatives:Why not [other option]:
[Specific reason this doesn't work]

Why not [other option]:
[Specific reason]

---

### Implementation Plan

If [recommended option] approved:PHASE 1: [Timeframe]
- [ ] [Action 1]
- [ ] [Action 2]
- Owner: [@Name]

PHASE 2: [Timeframe]
- [ ] [Action]
- Owner: [@Name]

PHASE 3: [Timeframe]
- [ ] [Action]
- Owner: [@Name]

Success criteria:
[How we'll know this decision was right]

Timeline to value:
[When users/business benefits]

---

### Risk Mitigation

Top risks with chosen option:Risk 1: [Specific risk]
- Likelihood: [High/Med/Low]
- Impact: [High/Med/Low]
- Mitigation: [What we'll do]
- Contingency: [Plan B if this happens]

Risk 2: [Another risk]
[Same structure]

---

### Exit Strategy

If this doesn't work out:Decision points:
- Month 3: [What we check]
- Month 6: [Assessment criteria]
- Month 12: [Go/no-go on continuing]

How we'd reverse course:
[Specific steps to undo decision]

Cost of switching:
[Time and money to pivot]

---

### Open Questions

Before final decision:
- [ ] [Question to resolve]
- [ ] [Another question]
- [ ] [Another]

Who needs to approve:
- [ ] Engineering lead
- [ ] Finance (budget)
- [ ] Legal (contracts if buying)
- [ ] CEO/CTO

---

### Appendix

Detailed vendor evaluation:
[Link to full analysis]

Financial model:
[Link to spreadsheet]

Reference calls:
[Link to notes]

Contract terms:
[If buying, key terms to negotiate]

</build_vs_buy>
```

</details>

---


## Analytics

*10 prompts in this category*

### Identify North Star Metric

**📋 Use Case:** Find the one metric that best captures product value delivery

**🛠️ Recommended Tools:** Claude Projects, analytics platform

**💡 Technique:** Chain of reasoning through what drives business value

<details>
<summary>Click to view prompt</summary>

```
<north_star_metric>

<metric_inputs>
BUSINESS CONTEXT:
1. What does your product do? (core value proposition)
2. How do you make money? (business model)
3. What's your growth stage? (early, growth, mature)
4. Current key metrics you track? (and why you picked them)

CUSTOMER CONTEXT:
5. When do customers get value? (aha moment, activation point)
6. What makes customers stick? (retention drivers)
7. What makes customers churn? (common reasons)
8. How do customers use the product? (daily, weekly, monthly)

UPLOADS:
- Analytics dashboards
- Business model canvas
- User journey map
- Cohort analysis
</metric_inputs>

<metric_process>

You are a product strategist who helps companies identify their North Star Metric - the single metric that best captures the value you deliver to customers and predicts business success.

PHASE 1: UNDERSTAND VALUE DELIVERY

1. MAP THE VALUE CHAIN

Customer value → Product usage → Business outcome

What value do you deliver?
[Specific benefit customers get, not features]

When do customers experience that value?
[The moment they realize "this works for me"]

What actions lead to value?
[Specific behaviors that predict success]

How does customer value drive revenue?
[Connection between usage and money]

2. IDENTIFY CANDIDATE METRICS

Brainstorm metrics across categories:

Activation metrics (new user experience)
- Time to first value
- Completion of key setup steps
- First core action taken

Engagement metrics (ongoing usage)
- DAU, WAU, MAU
- Actions per session
- Feature adoption

Value creation metrics (delivered outcome)
- Projects created
- Messages sent
- Reports generated
- Transactions completed

Retention proxy metrics (predicts stickiness)
- Return rate
- Habit formation indicators
- Cross-feature usage

Revenue metrics (business outcome)
- MRR/ARR
- Expansion revenue
- LTV

Your candidate list: [8-12 potential NSMs]

PHASE 2: EVALUATE CANDIDATES

For each candidate metric, score against criteria:

1. Does it capture VALUE DELIVERY?
- Does this metric go up when customers get more value?
- Can you game this metric without delivering value? (if yes, bad sign)

2. Does it PREDICT REVENUE?
- Do customers with higher [metric] pay more / retain longer?
- Show the correlation if you have data

3. Is it a LEADING INDICATOR?
- Does it predict future success before revenue shows up?
- Or is it lagging? (revenue itself is lagging)

4. Can the WHOLE COMPANY influence it?
- Can product, marketing, sales, support all drive this up?
- Or is it only one team's responsibility?

5. Is it EASY TO UNDERSTAND?
- Can you explain it to your grandmother?
- Do employees intuitively get why it matters?

6. Can you MEASURE IT reliably?
- Do you have the data today or can you instrument it?
- Is it consistent across platforms?

Score each: High / Medium / Low

Top 3 finalists: [metrics with highest scores]

PHASE 3: TEST NORTH STAR CANDIDATES

For your finalists, validate:

Historical Analysis (if you have data):
- Cohorts with high [NSM] → retention rate
- Cohorts with low [NSM] → retention rate
- Correlation between [NSM] and revenue

Customer Interview Validation:
- Do power users have high [NSM]?
- Do churned customers have low [NSM]?
- What do customers say about value?

The "So What" Test:
If this metric goes up 20%, does that definitely mean:
- Customers are getting more value? [yes/no]
- The business is healthier? [yes/no]
- The team knows what to build? [yes/no]

PHASE 4: RECOMMENDATION

## Your North Star Metric: [specific metric]

Definition:
[Exact formula, what counts, what doesn't]

Why this metric:
- Captures customer value because: [reason]
- Predicts business success because: [reason]
- Whole company can influence because: [reason]

Current baseline: [number if known]

What "good" looks like:
- This month: [target]
- This quarter: [target]
- This year: [target]

How to move it:
[3-5 levers that increase NSM]

What NOT to do:
[Ways to game metric that don't create value]

## Supporting Metrics

Your NSM needs context. Track these too:

Input metrics (drive NSM up):
- [Metric]: [why it matters]
- [Metric]: [why it matters]

Output metrics (validate NSM):
- Revenue/retention: [to confirm NSM→ business value]
- Quality metrics: [to avoid gaming NSM]

The Dashboard:
- NSM: [big number]
- Trend: [↑↓ vs last period]
- Inputs: [metrics that drive it]
- Outputs: [metrics that validate it]

PHASE 5: OPERATIONALIZING

How to use your NSM:In roadmap prioritization:
- Ask: "Will this feature increase [NSM]?"
- Estimate: "By how much?"

In experiment design:
- Primary metric: [NSM] or input to NSM
- Success criteria: [% increase]

In team goals:
- Company OKR: Increase [NSM] from X to Y
- Team OKRs: Improve [input metrics]

In stakeholder communication:
- Board decks: Lead with NSM trend
- All-hands: Celebrate NSM wins
- New hires: Explain why we picked this NSM

Review cadence:
- Daily: Monitor NSM for anomalies
- Weekly: Review with product/growth team
- Monthly: Deep dive into what moved it
- Quarterly: Validate NSM still predicts success

</metric_process>

<output_format>

## Recommendation
- NSM: [metric name and definition]
- Current: [baseline]
- Target: [goal]
- Why: [2-3 sentence rationale]

## Full Analysis
[All sections from process]

## One-Slide Summary
[NSM, how to move it, why it matters]

</output_format>

<meta_guidance>

Great North Star Metric:
- Measures value delivery, not vanity
- Leading indicator, not lagging
- Whole company can influence it
- Simple to explain and understand
- Has strong correlation to revenue/retention

Avoid:
- Picking revenue as NSM (lagging, not actionable)
- Metrics easily gamed without creating value
- Too complex (multi-variable formulas)
- Only one team can influence it
- Changing it every quarter

Remember: NSM should be stable for years, not months. It's okay to evolve it as business model changes, but picking a new NSM quarterly means you never picked the right one.

</meta_guidance>

</north_star_metric>
```

</details>

---

### Draft an Impact Sizing


**📋 Use Case:** Need to estimate the business impact of a feature to prioritize roadmap or get buy-in

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Assumption-based modeling, sensitivity analysis, showing your work

<details>
<summary>Click to view prompt</summary>

```
<impact_sizing>

<sizing_inputs>
WHAT YOU'RE SIZING:
1. Feature/initiative description (what are you building)
2. What metric will this impact? (conversion, retention, revenue, efficiency)
3. Current baseline (what's the metric today)
4. Your hypothesis about impact (educated guess of effect size)

YOUR CONTEXT:
5. Total addressable users (how many people could use this)
6. Expected adoption rate (what % will actually use it)
7. Time to impact (when do results show up)

DATA YOU HAVE:
8. Usage analytics (current behavior)
9. Customer research (stated need intensity)
10. Comparable features (what similar features did)

UPLOADS (if available):
- Analytics screenshot or export
- Customer feedback mentioning this need
- Competitor data on similar features
</sizing_inputs>

<sizing_framework>

You're a senior PM who knows that most impact sizing is either wildly optimistic ("This will double revenue!") or uselessly vague ("This will improve engagement"). Your job: Build a model that's honest, defensible, and shows your assumptions.

THE REALITY:

Bad impact sizing: "This will increase conversion by 10%"
Good impact sizing: "If 30% of users try it, and it improves their success rate from 40% to 50%, we'll see 1.5% lift in overall conversion. Here's the math and assumptions."

The goal isn't to be perfectly accurate. It's to:
1. Make assumptions explicit
2. Show your reasoning
3. Identify what you're most uncertain about

---

## PART 1: UNDERSTAND THE VALUE CHAIN

### Map How Feature → Metric

The feature:
[What you're building]

Who it affects:
[Specific user segment]

What they'll do differently:
[Behavior change you expect]

How that impacts metric:
[Chain of causation]

Example:
- Feature: One-click checkout
- Affects: Mobile users (40% of traffic)
- Behavior change: Fewer drop-offs at payment step
- Impact chain: Mobile cart → checkout flow → conversion rate → revenue

### Identify Your Assumptions

Every impact model is built on assumptions. Make them explicit.

ASSUMPTION 1: Adoption
- Assumption: [X% of users will use this feature]
- Based on: [Similar feature adoption, customer research, gut feel]
- Confidence: [High/Medium/Low]

ASSUMPTION 2: Effect Size
- Assumption: [Feature will improve [metric] by Y%]
- Based on: [Competitor benchmarks, A/B test results, customer data]
- Confidence: [High/Medium/Low]

ASSUMPTION 3: Time to Impact
- Assumption: [Will take Z weeks to see full effect]
- Based on: [Usage frequency, network effects, adoption curve]
- Confidence: [High/Medium/Low]

The assumption you're most unsure about: [Which one and why]

---

## PART 2: BUILD THE MODEL

### The Basic Formula

Impact = (Total Users) × (Adoption Rate) × (Effect Size) × (Metric Value)

Let's break it down step by step:

STEP 1: Size the Audience

Total users who could benefit: [X users/month]

How we got this number:
- Total MAU: [number]
- Segment this affects: [%]
- Addressable audience: [calculation]

STEP 2: Estimate Adoption

Not everyone will use a new feature.

Adoption scenarios:
- Conservative: [X%] adopt in first 90 days
- Moderate: [Y%] adopt in first 90 days
- Optimistic: [Z%] adopt in first 90 days

Why these numbers:
- Similar features in our product: [X-Y% adoption]
- Industry benchmarks: [Z% typical]
- Our assumption: [Which scenario we believe]

STEP 3: Estimate Effect Size

For users who adopt, how much better do they do?

Current state:
- Baseline metric: [current performance]
- Example: "40% of mobile users complete checkout"

With new feature:
- Expected metric: [new performance]
- Example: "Estimate 50% complete checkout (25% relative lift)"

Why this estimate:
- Competitor data: [Company X reports Y% improvement]
- Our data: [Similar change resulted in Z% improvement]
- Customer research: [% who said this would help significantly]

STEP 4: Calculate ImpactConservative Case:
- Users affected: [X]
- Adoption: [Y%]
- Effect size: [Z% improvement]
- Result: [Impact on metric]

Moderate Case:
- [Same structure with moderate assumptions]
- Result: [Impact on metric]

Optimistic Case:
- [Same structure with optimistic assumptions]
- Result: [Impact on metric]

### Show Your Math (Worked Example)

Feature: Add SSO login for enterprise

Baseline:
- Enterprise segment: 200 customers
- Current activation rate: 60% (120 activate)
- Each activated customer worth $50K/year ARR

Assumptions:
- 70% of enterprise customers will use SSO (140 customers)
- SSO will increase activation from 60% to 75%
- Takes 6 months to fully roll out

Calculation:

Current state:
- 200 customers × 60% activation = 120 activated
- 120 × $50K = $6M ARR from enterprise

With SSO:
- SSO customers: 200 × 70% = 140
- SSO activation: 140 × 75% = 105 activated via SSO
- Non-SSO customers: 60 (still 60% activate) = 36 activated
- Total activated: 105 + 36 = 141 activated

New ARR:
- 141 × $50K = $7.05M ARR
- Incremental impact: +$1.05M ARRSensitivity check:
- If only 50% adopt SSO: +$600K ARR
- If only 80% adopt SSO: +$1.2M ARR

---

## PART 3: VALIDATE YOUR ASSUMPTIONS

### The Sanity Checks

Smell test questions:1. Is this too good to be true?
- If you're projecting >20% improvement to a major metric, you better have strong evidence
- Big wins are rare; most features move metrics 1-5%

2. Have you accounted for cannibalization?
- Will new feature pull users from existing successful flows?
- Are you double-counting benefits?

3. What about adoption curve?
- Impact isn't instant; how long to full adoption?
- Have you accounted for ramp time?

4. What could make you wrong?
- List 3 ways your model breaks
- What's the worst case scenario?

### Identify Uncertainty

What you're confident about:
- [Assumption with strong data]

What you're guessing about:
- [Assumption with weak data]

How to de-risk:
- [What experiment or analysis would increase confidence]

Example:
- Confident: "40% of users are on mobile" (we have analytics)
- Guessing: "One-click checkout will reduce drop-off by 20%" (no data)
- De-risk: Run fake door test showing one-click option, measure click rate

---

## PART 4: TRANSLATE TO BUSINESS IMPACT

### From Metric to Money

Most features impact intermediate metrics. Translate to business outcomes.

If you're improving conversion:

Current:
- 10,000 visitors/month
- 5% convert = 500 customers
- $100 average order = $50K revenue/month

With feature (+1.5% absolute conversion):
- 10,000 visitors
- 6.5% convert = 650 customers
- +150 customers × $100 = +$15K/month = +$180K/yearIf you're improving retention:

Current:
- 1000 customers
- 5% monthly churn = 50 leave each month
- $50/month ARPU
- Annual churned revenue = 50 × 12 × $50 = $30K lost

With feature (-1% absolute churn):
- 4% monthly churn = 40 leave
- Annual churned revenue = $24K
- Saved $6K/year in churn

### Cost-Benefit

Investment required:
- Engineering: [X weeks]
- Design: [Y weeks]
- PM/QA: [Z weeks]
- Total cost: [loaded cost ~$150-250/hr for eng]

Expected return:
- Conservative: [$ impact]
- Moderate: [$ impact]
- Optimistic: [$ impact]

Payback period:
- Investment / Monthly impact = [X months to break even]

The decision:
[Is this worth building based on ROI?]

---

## THE OUTPUT

### Impact Sizing Summary (One Page)

Feature: [What we're building]

Target Metric: [What improves]

Expected Impact:
- Conservative: [X% improvement / $Y value]
- Moderate: [X% improvement / $Y value]
- Optimistic: [X% improvement / $Y value]

Key Assumptions:
1. [Assumption 1 with confidence level]
2. [Assumption 2 with confidence level]
3. [Assumption 3 with confidence level]

Investment: [Cost]
Payback Period: [Months]

Recommendation: [Build / Don't Build / Validate Assumptions First]

### Detailed Model

[All calculations from above with clear assumptions]

### Assumption Testing Plan

To increase confidence, we should:
1. [Experiment or analysis to validate key assumption]
2. [Next experiment]

</sizing_framework>

<quality_check>

Are your assumptions realistic?
- [ ] Not assuming 100% adoption
- [ ] Effect sizes are in line with similar features
- [ ] You've accounted for ramp time

Can someone challenge your model?
- [ ] All assumptions are explicit
- [ ] Math is shown step-by-step
- [ ] You've identified what you're uncertain about

Is it actionable?
- [ ] Clear enough to inform prioritization
- [ ] Identifies what would change your mind
- [ ] Conservative enough to be believable

</quality_check>

<meta_wisdom>

On impact sizing:

Most PMs make one of two mistakes:

Mistake 1: Wildly optimistic
"This will 10x our conversion rate!"
(No it won't. It'll move it 2-5% if you're lucky.)

Mistake 2: Refuse to estimate
"We can't know the impact until we ship."
(True, but educated guesses beat no guesses.)

The right approach:
Make an estimate. Show your assumptions. Update as you learn.

The key principle:

Impact sizing isn't about being right.
It's about being honest about uncertainty.

Good model: "If 30% adopt and it works, we'll see $500K lift. But adoption could be 10-50%, so real range is $150K-$1M."

Bad model: "This will generate $847,293 in year one."

On assumptions:

The most dangerous assumptions are the ones you don't write down.

Because if you don't write them, you can't test them.
And if you can't test them, you'll believe them even when they're wrong.

Remember:

All models are wrong. Some are useful.

Your job isn't to predict the future perfectly.
It's to make the best decision you can with imperfect information.

Show your work. State your assumptions. Update your beliefs when reality hits.

</meta_wisdom>

</impact_sizing>
```

</details>

---

### Write SQL Query

**📋 Use Case:** Need to analyze product data but don't write SQL daily

**🛠️ Recommended Tools:** Claude, ChatGPT, Cursor (for code)

**💡 Technique:** Schema understanding, query building step-by-step, explaining logic

<details>
<summary>Click to view prompt</summary>

```
<sql_query_writer>

<query_inputs>
WHAT DO YOU WANT TO KNOW:
[Describe in plain English what you're trying to find out]

YOUR DATABASE:
[Paste table names and columns, or just describe what tables you have]

Optional - if you have it:
- Sample data
- Database type (Postgres, MySQL, BigQuery, etc.)
- Specific date ranges or filters
</query_inputs>

<query_framework>

You write SQL queries for PMs who know enough to be dangerous but not enough to be confident.

YOUR PROCESS:

1. Understand the question
- Restate what they're asking in your own words
- Identify what data points are needed

2. Check if you have enough info
- Do you know the table names?
- Do you know the relevant column names?
- Do you know how tables relate?

If NO: Ask specific questions:
- "What table has user signup data?"
- "What's the column name for [X]?"
- "How do I join users to events?"

3. Write the query
- Start with simple SELECT
- Add filters
- Add aggregations if needed
- Add comments explaining each part

4. Explain what it does
- Plain English explanation
- What each column means
- How to interpret results

THE OUTPUT:
```sql
-- [Plain English: What this query finds]
SELECT
[columns]
FROM [table]
WHERE [filters]
GROUP BY [if needed]
ORDER BY [if needed]
LIMIT 100; -- Start with limit while testing




**What this returns:**
- Column 1: [What this means]
- Column 2: [What this means]

**To run it:**
1. [Any setup needed]
2. [How to verify it worked]

**If you need to modify it:**
- To change date range: [modify this line]
- To add filter: [add this WHERE clause]

</query_framework>

<meta_guidance>

**Keep it simple:**
- One query that answers their question
- Comments explaining logic
- Plain English explanation of results

**If they need complex analysis:**
- Break into multiple simple queries
- Explain how to combine results

**Common patterns:**
- Counting things: COUNT(DISTINCT user_id)
- Percentages: 100.0 * X / Y
- Time periods: DATE_TRUNC('day', timestamp)
- Cohorts: GROUP BY DATE_TRUNC('week', signup_date)

</meta_guidance>

</sql_query_writer>
```

</details>

---

### Edit Feature Results Writeup

**📋 Use Case:** Shipped feature, need to share results with stakeholders/team

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Data storytelling, outcome-focused narrative, executive communication

<details>
<summary>Click to view prompt</summary>

```
<feature_results_writeup>

<writeup_inputs>
PASTE YOUR DRAFT:
[Your current version of the results writeup]

FEATURE CONTEXT:
1. What did you ship? (feature description)
2. What was the goal? (metric you were trying to move)
3. When did it launch? (dates)
4. Who was it for? (segment, % of users)

THE RESULTS:
5. Key metrics (before/after, with numbers)
6. What worked better than expected?
7. What worked worse than expected?
8. Unexpected findings or surprises

AUDIENCE:
9. Who's reading this? (team, execs, company-wide, external)
10. What do they care about? (business outcomes, learnings, what's next)
11. How technical are they? (understand p-values vs. need simple explanation)

OPTIONAL UPLOADS:
- Charts or graphs
- Raw data or analytics screenshots
- Customer quotes or feedback
- PRD or original hypothesis
</writeup_inputs>

<writeup_framework>

You're an executive communications coach who knows that most feature writeups are either:
1. Buried leads (results on page 3)
2. Data dumps (50 metrics, no story)
3. Victory laps (ignoring what didn't work)

Your job: Turn data into narrative that drives decisions.

THE REALITY:

Bad writeup: "We shipped X. Here are 20 metrics. Questions?"
Good writeup: "We shipped X to improve Y. It worked—here's the impact and what we learned."

The best writeups:
- Lead with the outcome
- Tell a story
- Are honest about what didn't work
- Point to what's next

---

## PART 1: STRUCTURE CHECK

### The Formula for Results Writeups

1. TL;DR (3 sentences)
- What we shipped
- What happened (the result)
- What it means (so what)

2. Context (optional, 2-3 sentences)
- Why we built this
- What we expected

3. Results (the meat)
- Key metrics with before/after
- What worked
- What didn't work

4. Insights (what we learned)
- Non-obvious patterns
- Surprises
- User behavior changes

5. What's Next
- Decision made based on results
- Follow-up work
- Open questions

Does your draft follow this structure?
[Yes/No, what's missing]

### Lead With The Punchline

Current opening:
[Your first paragraph]

Does it answer: "So what happened?"
[Yes/No]

Rewritten opening (if needed):
[Lead with the outcome first, context second]

Example transformations:

❌ "We launched the new onboarding flow on March 1st after three months of design and development. The goal was to improve activation. We made several changes including..."

✅ "New onboarding flow increased activation by 23%. 30% more users completed their first project in the first week, driving 15% more paid conversions."

---

## PART 2: SHARPEN THE NARRATIVE

### From Data Dump to Story

What's the headline?
[One sentence: The most important finding]

Supporting evidence:
1. [Data point that supports headline]
2. [Data point that supports headline]
3. [Data point that supports headline]

The "but":
[What didn't work as expected, presented honestly]

Example structure:

"SSO integration drove significant enterprise adoption (headline).

- 78% of enterprise customers activated SSO within 30 days
- Those using SSO had 40% higher retention
- Average deal size for SSO customers: $85K vs $50K baseline

However, activation took longer than expected (6 days vs. 2 day target), primarily due to IT configuration complexity."

### Make Numbers Meaningful

Instead of raw numbers, provide context:

❌ "Conversion rate is now 8.5%"
✅ "Conversion rate improved from 7% to 8.5% (+21% relative increase)"

❌ "We have 142 new signups"
✅ "Signups increased 40% week-over-week, our biggest jump in 6 months"

Your key metrics, rewritten:Metric 1:
- Raw: [Number]
- With context: [Number with comparison/benchmark]

Metric 2:
- Raw: [Number]
- With context: [Number with comparison/benchmark]

### Add The Human Element

Include qualitative signals:Customer quotes:
"[Actual quote showing impact]" - [Customer type]

Support ticket changes:
- Before: [Type of complaint]
- After: [New pattern or reduction]

Sales feedback:
"[What sales team is saying]"

Usage patterns:
[Behavioral observation that tells a story]

Example:
"One enterprise customer told us: 'SSO cut our onboarding time from 3 weeks to 3 days.' Support tickets about login issues dropped 60%. Sales team reports it's now their most requested feature in demos."

---

## PART 3: BE HONEST ABOUT WHAT DIDN'T WORK

### The "However" Section

Most PMs skip this. Don't.

Great writeups acknowledge:
- Metrics that didn't move
- Unexpected negative impacts
- Things that broke
- Assumptions that were wrong

What didn't work as expected:Issue 1:
- What: [Metric or outcome that disappointed]
- Why: [Your hypothesis about cause]
- What we're doing: [How you're addressing it]

Example:
"Mobile adoption was lower than expected (40% vs 65% target). Analysis shows this feature requires desktop workflows that don't translate to mobile. We're designing a mobile-specific version for Q3."

### Acknowledge Uncertainty

Things you're still not sure about:Question 1: [What you don't know yet]
- Why it matters: [Impact of not knowing]
- How we'll learn: [Plan to get answer]

Example:
"We don't yet know if this feature drives long-term retention or just short-term engagement bump. We'll check 90-day retention in June."

---

## PART 4: INSIGHTS AND LEARNINGS

### Beyond The Obvious

Surface-level: "Users liked the new feature"
Insight: "Power users adopted 3x faster than casual users, suggesting this serves advanced use cases better than basic workflows"

Your insights:INSIGHT 1: [Pattern you didn't expect]
- What you observed: [Specific behavior or data]
- Why it matters: [Strategic implication]
- What this means for roadmap: [Decision it informs]

Example:
"Insight: SMB customers using SSO had 2x higher expansion rate vs enterprise.

This surprised us—we built SSO for enterprise, but SMBs with technical founders adopted it heavily and then expanded to larger plans.

Roadmap impact: We'll prioritize SMB-friendly features alongside enterprise ones."

### Segmentation Insights

How different users responded:Segment A: [Behavior and outcome]
Segment B: [Different behavior and outcome]

Why this difference matters:
[What you'll do differently based on this]

Example:
"Segment: Mobile-first users rarely completed setup (20% completion) vs desktop users (75% completion).

Why: Setup requires uploading files, which is clunky on mobile.

Action: Building mobile app for post-setup usage, but keeping setup desktop-only."

---

## PART 5: WHAT'S NEXT

### Decision Point

Based on these results:Decision made:
- [ ] We're doubling down (expand to more users, iterate)
- [ ] We're pivoting (change approach based on learnings)
- [ ] We're cutting losses (results don't justify further investment)
- [ ] We're pausing to learn more (need more data)

Rationale:
[Why this decision, based on results]

### Follow-Up Work

Immediate next steps:Week 1-2:
- [ ] [Action item] - Owner: [Name]
- [ ] [Action item] - Owner: [Name]

Next quarter:
- [ ] [Bigger initiative]
- [ ] [Bigger initiative]

### Open Questions for Future

Things we want to learn:
1. [Question we'll track over time]
2. [Hypothesis to test next]
3. [Metric to monitor]

---

## THE OUTPUT

### Edited Writeup (Ready to Share)

Subject: [Feature Name] Results

---

TL;DR
[3 sentence summary: what we shipped, what happened, what it means]

---

What We Expected
[Brief context on hypothesis and goal]

---

📊 ResultsKey Metrics:
| Metric | Before | After | Change |
|--------|--------|-------|--------|
| [Metric 1] | [#] | [#] | [+X%] |
| [Metric 2] | [#] | [#] | [+X%] |

What Worked:
- [Win 1 with data]
- [Win 2 with data]

What Didn't:
- [Issue with honesty about cause]

---

💡 Key Insights

1. [Non-obvious learning with data]
2. [Unexpected pattern with implication]
3. [Segmentation finding with action]

---

🎯 What's NextDecision: [What we're doing based on results]

Next Steps:
- [Action item with owner and date]
- [Action item with owner and date]

---

### Alternative Versions

Version for Execs (Shorter):
[Just TL;DR, key numbers, decision, ask]

Version for Team (More detail):
[Include technical details, edge cases, customer feedback]

Version for Company (Celebration):
[Focus on wins, learnings, team effort]

</writeup_framework>

<quality_check>

Does it lead with results?
- [ ] First paragraph answers "what happened"
- [ ] No burying the lead with context

Is it honest?
- [ ] Acknowledges what didn't work
- [ ] Doesn't spin bad results as good
- [ ] Clear about uncertainty

Is it actionable?
- [ ] Clear decision made
- [ ] Specific next steps with owners
- [ ] Reader knows what happens next

Is it readable?
- [ ] Scannable (bullets, headers, tables)
- [ ] Numbers have context
- [ ] Not overly technical

</quality_check>

<meta_wisdom>

On results writeups:

Your job isn't to make the feature look good.
It's to help the team learn and make the next decision.

Honest writeups build trust.
Spin writeups destroy credibility.

The hard truth:

Most features don't work as well as you hoped.

That's not failure. That's product development.

The failure is pretending it worked great when it didn't.

On leading with results:

Executives don't care about your process.
They care about outcomes.

"We launched X" is process.
"X increased revenue by Y%" is outcome.

Lead with outcome.

On negative results:

"This didn't work" is valuable information.

It tells you:
- What not to build next
- Where your assumptions were wrong
- What to test differently

Negative results deserve writeups too.

Remember:

The writeup isn't the end.
It's the input to the next decision.

Make it easy for someone to read this and know what to do next.

</meta_wisdom>

</feature_results_writeup>
```

</details>

---

### Debug Low Adoption/Metrics


**📋 Use Case:** Feature shipped but no one's using it, or key metric isn't moving

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Diagnostic frameworks, hypothesis generation, funnel analysis

<details>
<summary>Click to view prompt</summary>

```
<debug_metrics>

<diagnostic_inputs>
WHAT'S THE PROBLEM:
- [ ] Feature launched but low adoption
- [ ] Metric isn't moving (which one: [specify])
- [ ] Usage dropped (what changed)
- [ ] Conversion rate down
- [ ] Other: [describe]

THE DATA:
- Baseline: [What was normal]
- Current: [What it is now]
- When it changed: [Timeline]
- Who it affects: [All users, segment, platform]

WHAT YOU SHIPPED:
[If this is about a feature - what was it, when did it launch]

CONTEXT:
- What was the goal: [What you expected to happen]
- Current theories: [Your hunches about what's wrong]
</diagnostic_inputs>

<debugging_framework>

You're a product diagnostician who debugs why features/metrics aren't working. Your job: systematic investigation, not guessing.

---

## DIAGNOSTIC FRAMEWORK

### Step 1: Clarify the Problem

The symptom:
[What you observed]

Is this a real problem?
- Sample size sufficient? (Not just 10 users)
- Time window sufficient? (Not just 1 day)
- Measurement correct? (Tracking actually works)

Severity:
- How far from goal? [X% gap]
- Impact on business? [Revenue, churn, growth]
- Getting worse or stable? [Trend]

---

### Step 2: The Five Why's

Why is adoption low / metric not moving?Why #1:
[First-level answer]

Why #2:
[Go deeper - why that?]

Why #3:
[Go deeper - why that?]

Why #4:
[Go deeper - why that?]

Why #5:
[Root cause]

Example:

Why is feature adoption low?
→ Users aren't discovering it

Why aren't they discovering it?
→ It's buried in settings menu

Why is it in settings?
→ We thought it was an "advanced" feature

Why did we think that?
→ We assumed only power users would want it

Root cause: Wrong assumption about who needs this.

---

### Step 3: Hypothesis Generation

Possible causes:AWARENESS: Do users know it exists?
- [ ] Feature isn't visible in UI
- [ ] No announcement/education
- [ ] Hidden behind other steps
- [ ] Poor naming/labeling

UNDERSTANDING: Do users know what it does?
- [ ] Unclear value proposition
- [ ] Confusing description
- [ ] No examples/use cases shown
- [ ] Assumes too much knowledge

MOTIVATION: Do users care?
- [ ] Solving wrong problem
- [ ] Not painful enough to act on
- [ ] Timing is wrong
- [ ] Wrong user segment

ABILITY: Can users actually use it?
- [ ] Too complicated
- [ ] Technical barriers (bugs, performance)
- [ ] Missing prerequisites
- [ ] Broken on certain platforms

Which hypothesis is most likely:
[Your strongest hunch based on data]

---

### Step 4: Investigation Plan

To test [hypothesis], check:Data to pull:
- [ ] [Specific metric or funnel]
- [ ] [Segmentation to look at]
- [ ] [Comparison to check]

Users to talk to:
- [ ] Users who tried it (why'd they stop?)
- [ ] Users who never tried it (why not?)
- [ ] Power users (what's their workaround?)

Quick tests:
- [ ] [Small experiment to validate theory]

---

### Step 5: Funnel Analysis

Break down the user journey:Step 1: Awareness
- How many users see/hear about feature?
- [X%] of total users

→ Drop-off: [Y%] never proceed

Step 2: Interest
- How many click/explore?
- [Z%] of aware users

→ Drop-off: [Y%] bounce

Step 3: Trial
- How many try to use it?
- [W%] of interested users

→ Drop-off: [Y%] give up

Step 4: Adoption
- How many successfully use it?
- [V%] of trial users

Biggest drop-off is at:
[Which step loses most users]

This tells us:
[What that drop-off reveals about the problem]

---

### Step 6: Diagnosis

Root cause:
[What you believe is actually wrong]

Evidence:
- [Data point supporting this]
- [User feedback supporting this]
- [Observation supporting this]

Confidence level:
- [ ] High (70%+ sure)
- [ ] Medium (40-70% sure)
- [ ] Low (<40% sure) - need more data

---

### Step 7: Recommended Actions

Immediate fixes (this week):
- [ ] [Quick win that might help]
- [ ] [Another quick win]

Short-term (this month):
- [ ] [Bigger fix or test]
- [ ] [Another approach]

If that doesn't work:
- [ ] [Backup plan]

What we're measuring:
[Metric that will tell us if fix worked]

</debugging_framework>

<common_issues>

### Issue: "Users aren't discovering the feature"

Diagnostics:
- Where is it in UI? (Primary nav, settings, hidden submenu?)
- Did we announce it? (Email, in-app notification, changelog?)
- What % of users scroll past it without noticing?

Common root causes:
- Buried in UI hierarchy
- Looks like existing feature (not differentiated)
- No onboarding tooltip or callout
- Launched quietly

Fixes:
- Surface it more prominently
- Add onboarding highlight
- In-app announcement
- Email to users who'd benefit

---

### Issue: "Users try it once and never return"

Diagnostics:
- What happens on first use? (Success rate)
- What do they do after? (Bounce, continue elsewhere?)
- Error rates or performance issues?

Common root causes:
- First experience is bad (buggy, slow, confusing)
- Value isn't immediate (takes too long to see benefit)
- No habit formation (not integrated into workflow)

Fixes:
- Improve first-time experience
- Show value faster
- Add reminders or triggers to return
- Make it part of existing workflow

---

### Issue: "Only certain segments adopt"

Diagnostics:
- Which segments DO adopt?
- What's different about them?
- Why doesn't it work for others?

Common root causes:
- Built for wrong segment
- Requires prerequisites other segments lack
- Solves problem only one segment has

Fixes:
- Explicitly target the segment that cares
- Build version for other segments
- Accept narrow adoption if right segment

---

### Issue: "Metric moved in wrong direction"

Diagnostics:
- What are second-order effects?
- Did we break something else?
- Did we make something worse to improve this?

Common root causes:
- Optimization for wrong metric
- Trade-off we didn't anticipate
- Changed user behavior unexpectedly

Fixes:
- Look at related metrics
- Talk to users about what changed
- Consider rollback if harm > good

</common_issues>

<meta_guidance>

Debugging principles:Data + Intuition
Don't just look at data.
Don't just trust gut.
Combine both.

Talk to users
The fastest way to debug:
Find 5 users who didn't adopt and ask why.

Check the obvious first
- Is tracking broken?
- Is feature actually live?
- Did announcement go out?

Most "mysterious" problems have simple explanations.

Remember:

Low adoption ≠ bad feature

Sometimes:
- You built for wrong segment
- You haven't marketed it yet
- Users need time to discover

Don't panic and redesign until you understand WHY.

</meta_guidance>

</debug_metrics>
```

</details>

---

### Cohort Analysis

**📋 Use Case:** Understand retention and behavior patterns by signup cohort

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects, NotebookLM

**💡 Technique:** Data interpretation, pattern recognition, actionable insight extraction

<details>
<summary>Click to view prompt</summary>

```
<cohort_analysis>

<cohort_inputs>
YOUR DATA:
[Paste cohort data, or describe what you have access to]

Examples:
- Retention by week/month
- Feature adoption by cohort
- Revenue by cohort
- Engagement metrics over time

CONTEXT:
- What changed: [Product changes, marketing shifts]
- Time period: [Date range you're analyzing]
- Cohort definition: [Signup week, month, channel, etc.]

WHAT YOU WANT TO UNDERSTAND:
- [ ] Retention trends
- [ ] Feature adoption
- [ ] Revenue/LTV patterns
- [ ] Product improvements impact
- [ ] Segment differences
</cohort_inputs>

<analysis_framework>

You analyze cohorts to find patterns others miss. Your job: turn retention tables into insights that drive decisions.

THE PROCESS:1. Understand the data
What are you looking at?

2. Spot the patterns
What's changing over time?

3. Form hypotheses
Why are you seeing these patterns?

4. Recommend actions
What should you do based on this?

---

## COHORT ANALYSIS

### What You're Looking At

Cohort definition: [How users are grouped]
Metric being tracked: [Retention, revenue, engagement, etc.]
Time periods: [Week 0, Week 1, Week 2... or Month 0, Month 1...]
Total cohorts analyzed: [How many cohorts]

---

### Key Patterns

PATTERN 1: [Name the trend]What you see:
[Describe the pattern in the data]

Example: "Recent cohorts (Jan-Mar) retain 20% better at Week 4 than older cohorts (Oct-Dec)"

Why this matters:
[Business implication]

Possible causes:
- [Hypothesis 1]
- [Hypothesis 2]
- [Hypothesis 3]

---

PATTERN 2: [Another trend]

[Same structure]

---

### Cohort Comparison

Best performing cohorts:
- [Cohort]: [Metric] at [timeframe]
- What was different: [Context about this period]

Worst performing cohorts:
- [Cohort]: [Metric] at [timeframe]
- What was different: [Context about this period]

The gap:
[Quantify difference and what it means]

---

### Time-Based Insights

Week 0-1 (Activation):
[What happens in first week]
- Drop-off rate: [%]
- Key pattern: [What you notice]

Week 2-4 (Early retention):
[What happens after initial usage]
- Retention stabilizes at: [%]
- Key pattern: [What you notice]

Week 5+ (Mature retention):
[Long-term patterns]
- Retention curve flattens at: [%]
- Key pattern: [What you notice]

Critical drop-off point:
[Where most loss happens and why it matters]

---

### Hypotheses About What's Working

Hypothesis 1:
[Your theory about why performance changed]

Evidence:
[Data points supporting this]

How to validate:
[What you'd need to check]

---

Hypothesis 2:
[Another theory]

[Same structure]

---

### Segment Insights (If Applicable)

By acquisition channel:
- [Channel]: [Performance]
- [Channel]: [Performance]
- Insight: [What this tells you]

By user type:
- [Segment]: [Performance]
- [Segment]: [Performance]
- Insight: [What this tells you]

By product tier:
- [Tier]: [Performance]
- [Tier]: [Performance]
- Insight: [What this tells you]

---

### Red Flags / Warning Signs

⚠️ [Issue]:
[What's concerning and why]

⚠️ [Issue]:
[Another concern]

---

### What to Do Next

IMMEDIATE (This week):
- [ ] [Action based on finding]
- [ ] [Another action]

SHORT-TERM (This month):
- [ ] [Deeper investigation or experiment]
- [ ] [Product change to test]

MONITORING:
- Track: [Specific metric]
- For cohorts: [Which ones]
- Decision point: [What would trigger action]

</analysis_framework>

<cohort_patterns>

### Common Cohort Patterns & What They Mean

IMPROVING OVER TIME
Newer cohorts retain better than older cohorts

Likely causes:
- Product improvements working
- Better onboarding
- Better customer targeting
- Learning from past cohorts

What to do:
- Document what changed
- Double down on improvements
- Extract playbook for consistency

---

DECLINING OVER TIME
Newer cohorts retain worse than older cohorts

Likely causes:
- Product changes made it worse
- Lower quality customer acquisition
- Market saturation (getting worse-fit customers)
- Competitive pressure increased

What to do:
- Identify when decline started
- What changed at that time?
- Talk to churning customers
- Consider reverting changes

---

PLATEAU PATTERN
All cohorts flatten to same retention rate

What this means:
You've found your natural retention floor

Likely causes:
- Core value is strong
- But missing something for next level
- Product-market fit for subset

What to do:
- Identify what users who stay have in common
- Focus on activating more users to that level
- Improve experience for retained users

---

STEEP DROP-OFF EARLY
Big loss in first week/month, then stable

Likely causes:
- Onboarding isn't working
- Activation isn't happening
- Wrong customers signing up
- Value not obvious quickly

What to do:
- Focus on Week 0-1 experience
- Time-to-value too long
- Improve activation flow
- Better customer qualification

---

STEADY DECLINE (No flatten)
Cohorts keep losing users over time

Likely causes:
- No habit formation
- Competitors are better
- Product doesn't deliver sustained value
- Pricing issue (value < cost)

What to do:
- Deep customer interviews
- Understand why people leave
- Fundamental product or PMF issue

---

SEASONAL PATTERN
Certain cohorts perform differently by time of year

Likely causes:
- Business use case (B2B)
- Consumer behavior (fitness, tax, etc.)
- Budget cycles
- Marketing channel mix changes

What to do:
- Plan for seasonality
- Adjust acquisition strategy
- Build features for off-season retention

</cohort_patterns>

<meta_guidance>

Cohort analysis principles:Compare cohorts, not absolute numbers
"January users retain at 60%" means nothing without context
"January cohort retains 10% better than December" is insight

Look for inflection points
When did performance change?
What happened at that time?

Segment cohorts
Don't just look at all users
Break down by channel, feature, tier

Tie to product changes
Map cohorts to your release calendar
See cause and effect

Focus on early retention
Week 1 retention predicts Week 12
Fix activation before growth

Know your retention curve
Where does it flatten?
That's your loyal user base

Remember:

Cohort analysis isn't about having perfect data.
It's about finding patterns that suggest where to dig deeper.

One clear insight > 10 vague observations.

</meta_guidance>

</cohort_analysis>
```

</details>

---

### A/B Test Design


**📋 Use Case:** Need to design experiment to test feature/change before full rollout

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Hypothesis formation, sample size calculation, metric selection

<details>
<summary>Click to view prompt</summary>

```
<ab_test_design>

<test_inputs>
WHAT YOU WANT TO TEST:
[Describe the change - new feature, UI change, algo tweak, etc.]

WHY YOU'RE TESTING IT:
- Hypothesis: [What you believe will happen]
- Expected impact: [Metric you think will improve]
- Risk: [What could go wrong if you ship to everyone]

YOUR PRODUCT CONTEXT:
- Daily/monthly active users: [Volume]
- Current baseline metric: [The metric you're trying to move]
- Existing conversion/engagement rate: [If relevant]
- How users are assigned: [Session, user ID, random]

CONSTRAINTS:
- Timeline: [How long can you run test]
- Traffic: [Can you split 50/50 or need different allocation]
- Technical: [Any limitations on what you can test]
</test_inputs>

<test_framework>

You design A/B tests that produce reliable results. Follow this analysis:

**STEP 1: Form a clear hypothesis**

Bad hypothesis: "New design will be better"
Good hypothesis: "Adding social proof to checkout will increase conversion rate from 5% to 6%"

**Hypothesis format:**
If we [change]
Then [metric] will [improve by X%]
Because [reasoning based on user behavior]


**Check:**
- Is it specific? (Not "improve," but "increase by X%")
- Is it measurable? (Clear metric)
- Is it testable? (Can you prove/disprove)
- Is the expected change realistic? (6% → 7% yes, 6% → 60% no)

**STEP 2: Choose primary metric carefully**

Your primary metric should be:
- **North Star adjacent:** Tied to what actually matters for business
- **Measurable quickly:** Can detect change in reasonable timeframe
- **Sensitive enough:** Will move if change works
- **Stable enough:** Not too noisy day-to-day

**Bad primary metrics:**
- Page views (vanity, doesn't show value)
- Time on site (could mean confused, not engaged)
- Clicks on button (metric hacking, doesn't show outcome)

**Good primary metrics:**
- Conversion rate (shows real outcome)
- Revenue per user (business impact)
- Feature adoption rate (engagement)
- Retention day 7 (long-term value)

**STEP 3: Define guardrail metrics**

These are metrics that should NOT get worse:

**Must not break:**
- Page load time
- Error rates
- User satisfaction (NPS)
- Core flows (login, checkout, etc.)

**Format:**
Primary metric: [Conversion rate]
Goal: Increase by [X%]
Guardrail metrics:
• Page load time: Must stay <2s
• Error rate: Must stay <1%
• Cart abandonment: Must not increase


**STEP 4: Calculate sample size**

You need enough users to detect the change:

**Required inputs:**
- Baseline rate: [Current metric value]
- Minimum detectable effect: [Smallest change you care about]
- Statistical power: [Usually 80%]
- Significance level: [Usually 95%]

**Rule of thumb calculations:**

For **conversion rate** changes:
- To detect 10% relative lift (5% → 5.5%): ~10,000 users per variant
- To detect 20% relative lift (5% → 6%): ~2,500 users per variant
- To detect 5% relative lift (5% → 5.25%): ~40,000 users per variant

For **engagement metrics** (sessions, clicks):
- Generally need less volume
- But more noise, so longer runtime

**Calculator formula:**
n = 2 × (Zα + Zβ)² × p × (1-p) / (MDE)²
Where:
• Zα = 1.96 (for 95% confidence)
• Zβ = 0.84 (for 80% power)
• p = baseline rate
• MDE = minimum detectable effect


**Then determine runtime:**
Days needed = Sample size needed / (Daily traffic × % allocated to test)


**STEP 5: Design variant carefully**

**Control (A):**
- Current experience
- No changes
- Baseline measurement

**Treatment (B):**
- ONE clear change
- Everything else identical
- Change is measurable

**Common mistakes:**
- Testing multiple changes at once (can't tell what caused effect)
- Making change too subtle (won't detect difference)
- Making change too different (not realistic to ship)

**STEP 6: Plan rollout & assignment**

**User assignment:**
- **By user ID:** Same user always sees same variant (better for logged-in products)
- **By session:** Each session could be different (okay for anonymous products)
- **By device:** Mobile vs desktop

**Traffic allocation:**
- **50/50:** Standard, maximum power
- **90/10:** If risky change, minimize exposure
- **33/33/33:** Testing 2 variants against control

**Rollout plan:**
- Start with 10% of traffic (canary)
- Monitor for 24 hours
- If stable, ramp to 50%
- If still good, full test

**STEP 7: Define decision criteria upfront**

**Ship if:**
- [ ] Primary metric improves by [X%] with 95% confidence
- [ ] Guardrails stay stable
- [ ] No major bugs reported
- [ ] Qualitative feedback is positive

**Don't ship if:**
- [ ] Primary metric neutral or negative
- [ ] Any guardrail breaks
- [ ] Major bugs or user complaints
- [ ] Confidence level <95%

**Inconclusive if:**
- [ ] Small positive movement but not statistically significant
- [ ] Then: Run longer OR redesign test

**STEP 8: Plan instrumentation**

**Events to track:**
test_exposure:
user_id: [ID]
variant: [A or B]
timestamp: [When]
[primary_metric_event]:
user_id: [ID]
variant: [A or B]
value: [Metric value]
timestamp: [When]


**Check before launch:**
- [ ] Events firing correctly
- [ ] Variant assignment is random
- [ ] No overlap with other tests
- [ ] Can filter by variant in analytics

</test_framework>

---

## A/B TEST DESIGN DOC

**Test Name:** [Descriptive name]
**Owner:** [Your name]
**Status:** [Draft / Ready to launch / Running / Complete]

---

### Hypothesis

**If we** [specific change]  
**Then** [primary metric] will [increase/decrease by X%]  
**Because** [reasoning about user behavior]

**Example:**
"If we add customer testimonials to the pricing page, then free-to-paid conversion will increase from 12% to 14% because social proof reduces purchase anxiety."

---

### The Change

**Control (A) - Current experience:**
[Description or screenshot]

**Treatment (B) - New experience:**
[Description or screenshot]

**What's different:**
- [Specific change 1]
- [Specific change 2]

**What stays the same:**
[Everything else]

---

### Metrics

**PRIMARY METRIC (Decision maker):**

**Metric:** [Name]  
**Current baseline:** [X%]  
**Target:** [Y%]  
**Minimum detectable effect:** [Z%]

**Why this metric:**
[Why this is the right thing to measure]

---

**GUARDRAIL METRICS (Must not break):**

| Metric | Current | Must stay above/below |
|--------|---------|----------------------|
| [Metric 1] | [Value] | [Threshold] |
| [Metric 2] | [Value] | [Threshold] |
| [Metric 3] | [Value] | [Threshold] |

**Why these guardrails:**
[What you're protecting against]

---

**SECONDARY METRICS (Understand impact):**
- [Metric 1]: [What we'll learn]
- [Metric 2]: [What we'll learn]

---

### Sample Size & Timeline

**Sample size needed per variant:** [X users]

**Calculation:**
- Baseline rate: [%]
- Target lift: [%]
- Statistical power: 80%
- Significance level: 95%

**Daily traffic:** [Y users/day]  
**Traffic allocation:** [Z% to test]  
**Users per day in test:** [Y × Z%]

**Days needed:** [X users ÷ (Y × Z%)] = [W days]

**Proposed timeline:**
- Start: [Date]
- End: [Date]
- Duration: [W days]

**If we need results faster:**
[Options: increase traffic %, accept lower power, larger MDE]

---

### Traffic Allocation

**Split:**
- Control (A): [50%]
- Treatment (B): [50%]

**Assignment method:**
- [ ] By user ID (consistent experience)
- [ ] By session (can vary per session)
- [ ] Other: [Specify]

**Rollout plan:**
- Day 1: Launch to [10%] of traffic
- Day 2: If stable, ramp to [50%]
- Day 3+: Full test at [50/50]

**Monitoring triggers:**
- Error rate >2% → pause test
- Crash rate up >50% → kill test
- Angry user feedback → investigate

---

### Decision Criteria

**SHIP TO 100% IF:**
- ✅ Primary metric improves by ≥[X%] with p<0.05
- ✅ All guardrails stable (within [Y%] of baseline)
- ✅ No major bugs or user complaints
- ✅ Test ran for full [W days]

**DON'T SHIP IF:**
- ❌ Primary metric flat or negative
- ❌ Any guardrail degrades >[Y%]
- ❌ Significant bugs or complaints
- ❌ Low confidence (p>0.05)

**INCONCLUSIVE IF:**
- ⚠️ Small positive movement but p>0.05
- **Then:** Run [X more days] OR redesign test

**No cherry-picking results:** Wait for full duration, don't stop early because it's winning.

---

### Instrumentation

**Events to implement:**

**Test exposure:**
experiment_viewed:
user_id: string
experiment_name: "test_name"
variant: "A" or "B"
timestamp: datetime


**Primary metric event:**
[event_name]:
user_id: string
variant: "A" or "B"
[metric_value]: number
timestamp: datetime


**Pre-launch checklist:**
- [ ] Events fire on staging
- [ ] Variant assignment is random (check logs)
- [ ] Can filter analytics by variant
- [ ] Guardrail metrics tracked
- [ ] No conflicts with other running tests

---

### Risks & Mitigation

**RISK 1: [Potential problem]**
- **Likelihood:** [High/Med/Low]
- **Impact:** [High/Med/Low]
- **Mitigation:** [What we'll do]
- **Kill switch:** [How to disable quickly]

**Example:**
"Risk: New checkout flow confuses users, increases abandonment  
Likelihood: Medium  
Impact: High (revenue loss)  
Mitigation: Monitor abandonment hourly, qualitative feedback survey  
Kill switch: Feature flag to revert to control"

---

**RISK 2: [Another risk]**
[Same format]

---

### User Experience Considerations

**Switching variants:**
- What happens if user assigned variant A yesterday sees variant B today?
- Plan: [Consistent assignment by user ID]

**Partial exposure:**
- What if user only sees variant on mobile, not desktop?
- Plan: [Accept, assignment is per-device]

**Existing users vs new users:**
- Does this change affect both equally?
- Plan: [Segment analysis by user age]

---

### Analysis Plan

**Primary analysis:**
- Compare [primary metric] between A and B
- Statistical test: [Two-sample t-test / Chi-square]
- Confidence level: 95%

**Segmentation to check:**
- [ ] New vs returning users
- [ ] Mobile vs desktop
- [ ] By geography
- [ ] By user cohort

**Questions to answer:**
1. Did primary metric move?
2. Did any guardrails break?
3. Are there segment differences?
4. Is qualitative feedback consistent with data?

**Dashboard:** [Link to live results]

---

### Rollback Plan

**If we need to kill test:**

**Trigger conditions:**
- [Specific condition 1]
- [Specific condition 2]

**How to rollback:**
1. [Step 1: Turn off feature flag]
2. [Step 2: Verify users see control]
3. [Step 3: Monitor for recovery]

**Communication:**
- Internal: [Slack #team-channel]
- Users: [If needed, what to say]

**Owner on-call:** [Name, contact]

---

### Launch Checklist

**BEFORE LAUNCH:**
- [ ] Hypothesis documented
- [ ] Metrics instrumented and tested
- [ ] Sample size calculated
- [ ] Decision criteria agreed
- [ ] Design/eng review complete
- [ ] QA tested both variants
- [ ] Feature flag configured
- [ ] Rollback plan documented
- [ ] Stakeholders aligned

**AT LAUNCH:**
- [ ] Start at 10% traffic
- [ ] Check events firing
- [ ] Check variant assignment random
- [ ] Monitor for first 2 hours
- [ ] Ramp to full traffic if stable

**DURING TEST:**
- [ ] Daily metrics check
- [ ] Weekly stakeholder update
- [ ] User feedback review
- [ ] Guardrail monitoring

**AT CONCLUSION:**
- [ ] Full statistical analysis
- [ ] Segment breakdowns
- [ ] Qualitative synthesis
- [ ] Decision made and documented
- [ ] Results shared with team

---

### Success Criteria Review

**Expected outcome:**
[What you think will happen]

**Best case:**
[If way better than expected]

**Worst case:**
[If it hurts metrics]

**Most likely:**
[Realistic expectation]

**We'll consider this test successful if:**
[Even if we don't ship, what will we learn?]

</ab_test_design>
```

</details>

---

### Experiment Readout

**📋 Use Case:** A/B test finished, need to analyze results and make ship/no-ship decision

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Statistical interpretation, segment analysis, decision framing

<details>
<summary>Click to view prompt</summary>

```
<experiment_readout>

<experiment_inputs>
PASTE YOUR DATA:
[Raw results - control vs treatment metrics, or describe what you have]

THE TEST:
- What you tested: [Feature/change]
- Hypothesis: [What you expected]
- Primary metric: [What you measured]
- Duration: [How long]
- Sample size: [Users per variant]

YOUR DECISION CRITERIA:
[What was agreed upfront - ship if X, don't ship if Y]
</experiment_inputs>

<readout_framework>

You analyze experiments to make data-driven decisions. Your process:

**STEP 1: Validate the experiment**

**Before analyzing results, check:**
- Did test run for planned duration?
- Was sample size sufficient?
- Was traffic split as expected (50/50)?
- Any implementation bugs?
- Any external factors (holidays, outages, campaigns)?

**Red flags that invalidate results:**
- Imbalanced traffic split
- Test stopped early because "it was winning"
- Major bug discovered in variant
- External event during test (site down, viral moment, etc.)

**If experiment is invalid → don't ship, re-run test**

**STEP 2: Analyze primary metric**

**The question:**
Did treatment move primary metric vs control?

**Statistical test:**
- Difference: [X%]
- P-value: [Number]
- Confidence interval: [Range]
- Statistical significance: [Yes if p<0.05]

**Practical significance:**
- Is difference big enough to matter?
- Does it meet your MDE (minimum detectable effect)?
- Business impact: [Calculate actual value]

**Common pitfall:**
"Statistically significant" ≠ "big enough to care about"
A 0.1% improvement might be significant but not worth the complexity.

**STEP 3: Check guardrail metrics**

**Did anything break?**

For each guardrail metric:
- Did it stay stable? (within ±X%)
- Did it improve? (bonus)
- Did it degrade? (concern)

**If guardrails broke:**
Even if primary metric improved, might not ship if:
- User experience degraded
- Revenue decreased
- Key flow broke
- NPS dropped

**STEP 4: Segment analysis**

**Did it work for everyone or just some users?**

Segment by:
- New vs returning users
- Mobile vs desktop
- Geography
- User cohort
- Product tier

**Patterns to look for:**
- Works great for segment A, hurts segment B
- Only works for new users (or only returning)
- Platform-specific (desktop yes, mobile no)

**If segmented results:**
Consider shipping to only winning segments.

**STEP 5: Look for surprises**

**Secondary metrics:**
Did anything unexpected move?

**Qualitative feedback:**
- User comments
- Support tickets
- Sales feedback
- Social sentiment

**Sometimes data says "ship" but users say "this is confusing"**
→ Investigate the disconnect

**STEP 6: Calculate business impact**

**If you ship to 100%:**

**Impact calculation:**
[Metric lift %] × [baseline volume] × [value per conversion]
= [Annual impact]


**Example:**
5% conversion lift × 10K users/mo × $100 LTV
= 500 more conversions/mo × $100
= $50K/mo = $600K/year

**Compare to:**
- Cost to build/maintain
- Opportunity cost (what else could team build)

**STEP 7: Make recommendation**

**Framework:**

**Ship if:**
- Primary metric improved (statistically + practically significant)
- Guardrails stable
- Positive or neutral qualitative feedback
- Business impact > cost

**Don't ship if:**
- Primary metric flat or negative
- Guardrails broke
- Negative qualitative feedback
- Not worth the complexity

**Iterate if:**
- Results promising but mixed
- Some segments won, some lost
- Qualitative concerns despite data win

**Re-test if:**
- Results inconclusive (not enough data)
- External factors muddied results
- Implementation issues

Now analyze the provided experiment data and make a clear recommendation.

</readout_framework>

---

## Example Experiment Readout

*(Structure will vary based on the experiment, but here's a typical flow)*

### Decision Summary

**Recommendation:** [SHIP / DON'T SHIP / ITERATE / RE-TEST]

**One-line rationale:**
[Primary metric moved X%, guardrails stable, qualitative positive - ship it]

**If shipping:**
- To whom: [100% / specific segments / gradual rollout]
- When: [Timeline]
- With what: [Any changes based on learnings]

---

### Experiment Overview

**Tested:** [Description]  
**Hypothesis:** [Expected outcome]  
**Duration:** [Dates]  
**Sample size:** [N users per variant]  
**Traffic split:** [Actual split achieved]

**Test validity:** ✅ Valid / ⚠️ Concerns / ❌ Invalid
[Note any issues]

---

### Primary Metric Results

**Metric:** [Name]

**Control:** [X%]  
**Treatment:** [Y%]  
**Lift:** [+Z%] (absolute: [A percentage points])

**Statistical significance:** [Yes/No]  
**P-value:** [Number]  
**Confidence interval:** [Range]

**Practical significance:**
[Is this big enough to matter? Business impact calculation]

**Interpretation:**
[What this means in plain language]

---

### Guardrail Metrics

| Metric | Control | Treatment | Change | Status |
|--------|---------|-----------|--------|--------|
| [Metric 1] | [X] | [Y] | [±Z%] | [✅/⚠️/❌] |
| [Metric 2] | [A] | [B] | [±C%] | [Status] |

**Issues:** [Any guardrails that broke]

---

### Segment Analysis

**By [segment type]:**

[Show results for key segments - might be table, might be bullet points, adapt to data]

**Key finding:**
[Did it work better for some segments?]

**Implication:**
[Should we ship to all users or just certain segments?]

---

### Unexpected Findings

**What surprised us:**
[Things that moved unexpectedly]

**Qualitative signals:**
[User feedback, support tickets, sales comments]

**Consistency check:**
[Do data and qualitative align or conflict?]

---

### Business Impact

**If we ship to 100%:**

[Calculate actual impact in revenue, users, or other business metric]

**ROI:**
[Impact vs cost to build/maintain]

---

### Recommendation Details

**Why [ship/don't ship]:**
[Detailed reasoning]

**Confidence level:** [High/Medium/Low]

**Risks:**
[What could still go wrong]

**Next steps:**
[Specific actions]

</experiment_readout>
```

</details>

---

### Define Success Metrics for Feature

**📋 Use Case:** About to build feature, need to define how you'll measure success

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Metric selection, target setting, measurement planning

<details>
<summary>Click to view prompt</summary>

```
<success_metrics>

<feature_inputs>
WHAT YOU'RE BUILDING:
[Feature description]

WHY YOU'RE BUILDING IT:
- Problem it solves: [User pain]
- Expected benefit: [What improves]
- Strategic goal: [Company objective it supports]

WHO IT'S FOR:
[Target users]

CURRENT STATE:
[Relevant baseline metrics if you have them]
</feature_inputs>

<metrics_framework>

You define metrics that actually measure success. Your process:

STEP 1: Start with the "why"Don't start with "what can we measure"
Start with "what does success look like?"

Success definition:
- For users: [What gets better for them]
- For business: [What improves for company]

Example:
Feature: "Auto-save"
Success for users: Never lose work
Success for business: Fewer frustrated users, less support

STEP 2: Choose metric typeInput metrics (leading indicators):
Measure usage/engagement
- % of users who try feature
- Frequency of use
- Feature adoption rate

Pro: Can measure quickly
Con: Doesn't prove value

Output metrics (lagging indicators):
Measure actual outcomes
- Task completion time (decreased)
- Error rate (decreased)
- User retention (increased)
- Revenue (increased)

Pro: Proves actual value
Con: Takes time to measure

Best practice: Track bothSTEP 3: Define primary metricYour ONE metric that matters mostGood primary metrics:
- Directly tied to value delivered
- Measurable within reasonable timeframe
- Sensitive (will move if feature works)
- Directional (clear if good or bad)

Bad primary metrics:
- Vanity (looks good but means nothing)
- Gamed easily (can fake success)
- Delayed too long (can't learn)

STEP 4: Define guardrail metricsWhat should NOT get worse:Common guardrails:
- Performance (load time)
- Reliability (error rates)
- Core flows (don't break key workflows)
- User satisfaction (NPS)

STEP 5: Set realistic targetsTarget framework:Baseline: [Current state]
Target: [What you're aiming for]
Timeline: [When you'll measure]

How to set targets:
- Look at past feature performance
- Industry benchmarks if available
- Directional improvement (any increase is good)
- Stretch but achievable

Avoid:
- Pulled from thin air
- Overly ambitious (sets up for failure)
- Too conservative (not worth building)

STEP 6: Plan measurementHow you'll track:
- What events to instrument
- Where to track them
- Dashboard to monitor
- Review cadence

When you'll know:
- Early signal (1 week)
- Clear signal (1 month)
- Long-term impact (3 months)

Now define metrics for the specific feature described, adapted to its context and goals.

</metrics_framework>

---

## Example Metrics Definition

(Adapt structure based on feature type)

### Feature Success Criteria

Feature: [Name]Goal: [What this achieves]Launch date: [When]

---

### Success Definition

For users:
[What gets better for them - specific and measurable]

For business:
[What improves for company - tied to goals]

We'll know it's working if:
[Concrete observable outcomes]

---

### Primary Metric

Metric: [Name and definition]

Why this metric:
[Why this is the right thing to measure]

Baseline: [Current state]Target: [Goal]Timeline: [When measured]

Calculation:
[How it's measured - formula if needed]

---

### Secondary Metrics

Metric 1: [Name]
- Current: [Baseline]
- Target: [Goal]
- Why tracking: [What this tells us]

Metric 2: [Name]
[Same structure]

---

### Guardrail Metrics

| Metric | Baseline | Must stay above/below | Why it matters |
|--------|----------|----------------------|----------------|
| [Metric 1] | [X] | [Threshold] | [Reason] |
| [Metric 2] | [Y] | [Threshold] | [Reason] |

---

### Measurement Plan

Events to track:
[Specific events and what they capture]

Dashboard: [Where monitored]

Review cadence:
- Week 1: [What we check]
- Month 1: [Assessment]
- Quarter 1: [Long-term view]

Decision criteria:
- Ship to 100% if: [Conditions]
- Iterate if: [Conditions]
- Rollback if: [Conditions]

---

### Learning Goals

Beyond metrics, we want to learn:
[Qualitative questions to answer]

How we'll learn:
[Surveys, interviews, analytics, etc.]

</success_metrics>
```

</details>

---

### Analytics Instrumentation Spec


**📋 Use Case:** Need to tell eng what events to track for new feature

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Event specification, property definition, tracking completeness

<details>
<summary>Click to view prompt</summary>

```
<analytics_instrumentation>

<instrumentation_inputs>
WHAT YOU'RE INSTRUMENTING:
[Feature or flow]

WHY YOU NEED TRACKING:
[What questions you're trying to answer]

YOUR ANALYTICS SETUP:
- Tool: [Segment, Amplitude, Mixpanel, custom, etc.]
- Current naming convention: [If you have one]
- Who implements: [Eng team]
</instrumentation_inputs>

<instrumentation_framework>

You write instrumentation specs that engineers can implement. Your process:

STEP 1: Map the user flowList every step:
1. User does [action]
2. System responds [how]
3. User sees [what]
4. User does [next action]

For each step, ask:
- Do we need to know this happened?
- What properties matter?
- How will we analyze this?

STEP 2: Define eventsEvent naming convention:Pattern: [object]_[action] or [action]_[object]Examples:
- button_clicked or click_button
- form_submitted
- page_viewed
- feature_enabledBe consistent with existing events.Event types:Interaction events:
User does something (click, type, submit)

System events:
System does something (email_sent, job_completed)

Page/screen events:
User navigates (page_viewed, screen_opened)

STEP 3: Define propertiesFor each event, specify:Required properties:
- Always included
- Needed for analysis

Optional properties:
- Sometimes included
- Contextual info

Property naming:
- snake_case or camelCase (pick one)
- Descriptive names
- Consistent across events

Common properties:
- user_id
- timestamp (usually automatic)
- session_id
- device_type
- platform

STEP 4: Specify data types

For each property:
- String: "value"
- Number: 123
- Boolean: true/false
- Array: ["item1", "item2"]
- Object: {nested: "data"}

STEP 5: Document expected valuesFor enums/categories:
List all possible values

Example:button_location: "header" | "sidebar" | "footer" | "modal"For numbers:
Expected range or format

STEP 6: Show implementation examplePseudo-code helps engineers:javascript analytics.track('feature_enabled', {   feature_name: 'auto_save',   user_id: user.id,   plan_type: user.plan,   enabled_by: 'user' // or 'default' }); STEP 7: Explain analysis planWhy each event matters:
"We'll use feature_enabled to calculate adoption rate by plan type"

This helps engineers understand priority and context.

Now create an instrumentation spec for the described feature.

</instrumentation_framework>

---

## Example Instrumentation Spec

(Structure adapts to the feature complexity)

### Instrumentation Spec: [Feature Name]

Owner: [Your name]Engineer: [@Name]Target: [Sprint/date]Analytics tool: [Tool name]

---

### Overview

What we're tracking:
[Feature/flow description]

Why we need this data:
[Questions we're answering]

Analysis plan:
[How we'll use this data]

---

### Events to Implement

EVENT 1: [event_name]When to fire:
[Specific trigger - "When user clicks 'Save' button"]

Required properties:javascript {   user_id: string,          // Unique user identifier   feature_name: string,     // "auto_save"   action_type: string,      // "manual" | "automatic"   file_size: number,        // Size in KB   file_type: string         // "document" | "spreadsheet" | "presentation" } Optional properties:javascript {   time_since_last_save: number,  // Seconds   changes_count: number          // Number of edits since last save } Example:javascript analytics.track('file_saved', {   user_id: '12345',   feature_name: 'auto_save',   action_type: 'automatic',   file_size: 245,   file_type: 'document',   time_since_last_save: 30,   changes_count: 5 }); 

---

EVENT 2: [another_event]

[Same structure]

---

[Continue for all events]

---

### Property Definitions

Shared properties (all events):

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| user_id | string | Unique user ID | "usr_123" |
| session_id | string | Session identifier | "sess_456" |
| timestamp | datetime | Event time (auto) | ISO 8601 |
| platform | string | "web"\|"mobile"\|"api" | "web" |

Feature-specific properties:

[Define properties unique to this feature]

---

### Implementation Notes

Where to implement:
[Specific files/components]

Testing:
[How to verify events fire correctly]

Rollout:
[Any phasing or feature flags]

---

### Validation Checklist

Before shipping:
- [ ] All events firing in dev
- [ ] Properties have correct data types
- [ ] Can see events in analytics tool
- [ ] Dashboard built (if needed)
- [ ] Documentation updated

</analytics_instrumentation>
```

</details>

---


## Operations

*8 prompts in this category*

### Root Cause Analysis (5 Whys)


**📋 Use Case:** Something broke or failed, need to understand why and fix root cause

**🛠️ Recommended Tools:** Claude, ChatGPT Projects

**💡 Technique:** 5 Whys method, fishbone analysis, systemic thinking

<details>
<summary>Click to view prompt</summary>

```
<root_cause_analysis>

<rca_inputs>
WHAT HAPPENED:
[Describe the incident, bug, failure, or problem]

WHEN:
[Timeline of events]

IMPACT:
- Users affected: [Number or percentage]
- Business impact: [Revenue, churn, reputation]
- Duration: [How long]

IMMEDIATE FIX:
[What you did to stop the bleeding]

CONTEXT:
[Any relevant background or recent changes]
</rca_inputs>

<rca_framework>

You help teams get to root causes, not symptoms. Your job: ask "why" until you find the systemic issue, not just the proximate cause.

---

## ROOT CAUSE ANALYSIS

Incident: [Brief description]
Date: [When it happened]
Severity: [Critical/High/Medium/Low]

---

### The Problem

What happened: [Observable symptom]

Impact:
- [Specific impact metric]
- [Customer effect]
- [Business consequence]

---

### The 5 Whys

Problem Statement:
[Starting problem]

Why #1: Why did this happen?
→ [First-level cause]

Why #2: Why did that happen?
→ [Dig deeper]

Why #3: Why did that happen?
→ [Keep going]

Why #4: Why did that happen?
→ [Almost there]

Why #5: Why did that happen?
→ [Root cause]

Root Cause:
[The systemic issue that, if fixed, prevents recurrence]

---

EXAMPLE:Problem: Users couldn't log in for 2 hours

Why #1: Why couldn't users log in?
→ Authentication service was down

Why #2: Why was auth service down?
→ Database ran out of connections

Why #3: Why did database run out of connections?
→ Connection pool was too small for peak traffic

Why #4: Why was connection pool too small?
→ We never load-tested this service

Why #5: Why didn't we load-test?
→ No testing process for new services before production

Root cause: Missing load testing in deployment process

---

### Contributing Factors

Beyond the primary root cause, what else contributed?Technical factors:
- [Infrastructure, code, architecture]

Process factors:
- [Missing reviews, unclear ownership]

Human factors:
- [Communication gaps, knowledge gaps]

Organizational factors:
- [Incentives, priorities, resources]

---

### Corrective Actions

Immediate (This week):
- [ ] [Fix to prevent immediate recurrence] - Owner: [Name]
- [ ] [Another immediate action] - Owner: [Name]

Short-term (This month):
- [ ] [Process improvement] - Owner: [Name]
- [ ] [System improvement] - Owner: [Name]

Long-term (This quarter):
- [ ] [Systemic fix] - Owner: [Name]

How we'll know it's fixed:
[Metric or signal that shows problem solved]

---

### Lessons Learned

What worked well:
- [Response that went right]
- [System that caught issue]

What we'll do differently:
- [Change to process]
- [Change to system]
- [Change to team practice]

---

### Follow-Up

Review date: [When to check if fixes worked]
Owner: [Who's responsible for follow-through]

</rca_framework>

<rca_patterns>

### Common Root Causes

"We didn't know"
→ Missing monitoring/alerting
→ Fix: Add visibility

"We didn't have time"
→ Technical debt prioritization
→ Fix: Allocate capacity for maintenance

"We didn't think it would happen"
→ Missing risk assessment
→ Fix: Pre-mortems before launches

"We didn't communicate"
→ Unclear ownership or handoffs
→ Fix: RACI matrix, better documentation

"We didn't test"
→ Missing testing process
→ Fix: Add required tests before deploy

"We made a trade-off"
→ Conscious decision that backfired
→ Fix: Document trade-offs, revisit regularly

</rca_patterns>

<meta_guidance>

Root cause analysis principles:Blame the system, not the person
"Sarah deployed bad code" is not root cause
"No code review process" is root cause

Don't stop at first answer
First "why" is usually proximate cause
Keep going until you hit systemic issue

Multiple root causes
Complex failures often have multiple contributing factors
Fix all of them

Focus on prevention
RCA isn't about blame
It's about making sure it doesn't happen again

Document and share
RCAs are learning opportunities
Share widely so others learn too

Remember:
If your root cause is "human error," you haven't dug deep enough.

Systems should prevent human error, not rely on humans being perfect.

</meta_guidance>

</root_cause_analysis>
```

</details>

---

### Launch Checklist

**📋 Use Case:** Make sure you don't forget critical steps before shipping

**🛠️ Recommended Tools:** Claude Projects, Notion AI

**💡 Technique:** Completeness verification, risk mitigation, stakeholder alignment

<details>
<summary>Click to view prompt</summary>

```
<launch_checklist>

<launch_inputs>
WHAT YOU'RE LAUNCHING:
[Feature, product, major change]

LAUNCH TYPE:
- [ ] Beta (limited users)
- [ ] GA (General availability)
- [ ] Rollout (phased)
- [ ] Migration (forcing change)

SCOPE:
- User impact: [How many users, which segments]
- Business impact: [Revenue, reputation risk]
- Technical scope: [How complex]

LAUNCH DATE:
[Target date]

TEAM:
[Who's involved - eng, design, marketing, sales, support]
</launch_inputs>

<checklist_framework>

You create launch checklists that prevent disasters. Your job: think of everything that could go wrong, make sure it's covered.

---

## LAUNCH CHECKLIST

Feature: [Name]
Launch date: [Date]
Owner: [Name]
Type: [Beta/GA/Rollout]

---

### PRODUCT READINESS

✅ Core functionality
- [ ] Feature works end-to-end
- [ ] All acceptance criteria met
- [ ] Edge cases handled
- [ ] Error states tested
- [ ] Performance acceptable (load time, scale)

✅ Quality
- [ ] QA testing complete
- [ ] No critical bugs
- [ ] Known issues documented
- [ ] Regression testing passed (didn't break other features)

✅ User experience
- [ ] Design review approved
- [ ] Copy finalized
- [ ] Mobile responsive
- [ ] Accessibility tested
- [ ] Loading states clear

✅ Technical
- [ ] Code review complete
- [ ] Deployed to staging
- [ ] Database migrations tested
- [ ] API endpoints documented
- [ ] Monitoring/alerting configured
- [ ] Feature flag implemented (if rollout)
- [ ] Rollback plan documented

---

### DOCUMENTATION

✅ Internal docs
- [ ] Technical spec updated
- [ ] Architecture diagram current
- [ ] API documentation complete
- [ ] Runbook for on-call
- [ ] Known limitations documented

✅ User-facing docs
- [ ] Help articles written
- [ ] Video tutorial (if complex)
- [ ] FAQs prepared
- [ ] In-app tooltips/guides
- [ ] Changelog entry drafted

✅ Team materials
- [ ] Sales battlecard updated
- [ ] Demo script prepared
- [ ] Support playbook ready
- [ ] Internal FAQ for team

---

### COMMUNICATION

✅ Internal comms
- [ ] Team announced and aligned
- [ ] Support team trained
- [ ] Sales team briefed
- [ ] Success team prepared
- [ ] Execs informed

✅ External comms
- [ ] Release notes drafted
- [ ] Email announcement ready
- [ ] Social posts prepared
- [ ] Blog post (if major)
- [ ] In-app notification configured

✅ Customer-specific
- [ ] Beta customers notified
- [ ] Key accounts briefed personally
- [ ] Breaking changes communicated early

---

### GO-TO-MARKET

✅ Marketing
- [ ] Landing page updated
- [ ] Pricing page updated (if relevant)
- [ ] Email campaign scheduled
- [ ] Social media planned
- [ ] Press outreach (if newsworthy)

✅ Sales enablement
- [ ] CRM updated
- [ ] Sales deck updated
- [ ] Demo environment ready
- [ ] Objection handling prepared
- [ ] Competitive positioning ready

✅ Analytics
- [ ] Tracking instrumented
- [ ] Success metrics defined
- [ ] Dashboard created
- [ ] Alerts configured
- [ ] A/B test setup (if applicable)

---

### RISK MITIGATION

✅ Rollback plan
- [ ] Feature flag to disable
- [ ] Database rollback tested
- [ ] Customer impact of rollback understood
- [ ] Decision criteria for rollback defined

✅ Support readiness
- [ ] Extra support coverage scheduled
- [ ] Escalation path clear
- [ ] Known issues + workarounds documented
- [ ] Slack channel for launch monitoring

✅ Monitoring
- [ ] Error rates baseline
- [ ] Performance metrics baseline
- [ ] Success metrics tracked
- [ ] On-call schedule confirmed

✅ Contingency
- [ ] What if: feature breaks
- [ ] What if: users confused
- [ ] What if: negative feedback
- [ ] What if: competitors respond

---

### COMPLIANCE & SECURITY

✅ Security
- [ ] Security review complete
- [ ] Penetration testing done (if needed)
- [ ] Data privacy assessed
- [ ] Access controls verified

✅ Legal/Compliance
- [ ] Terms of service updated (if needed)
- [ ] Privacy policy updated (if needed)
- [ ] GDPR compliance checked
- [ ] Legal review (if required)

✅ Business
- [ ] Contracts updated (if pricing change)
- [ ] Billing system ready (if monetized)
- [ ] Finance informed (if revenue impact)

---

### LAUNCH DAY

✅ Pre-launch (Morning of)
- [ ] Final smoke test in production
- [ ] Team synced on plan
- [ ] Support ready
- [ ] Marketing materials queued

✅ During launch
- [ ] Feature enabled / rolled out
- [ ] Monitoring active
- [ ] Announcement sent
- [ ] Team available for issues

✅ Post-launch (First 24hrs)
- [ ] Error rates normal
- [ ] User feedback reviewed
- [ ] Quick fixes deployed (if needed)
- [ ] Team debriefed

---

### POST-LAUNCH (Week 1)

✅ Measure success
- [ ] Success metrics pulled
- [ ] User feedback collected
- [ ] Support tickets analyzed
- [ ] Performance reviewed

✅ Follow-up
- [ ] Results shared with team
- [ ] Quick wins implemented
- [ ] Lessons learned documented
- [ ] Next iteration planned

---

### LAUNCH DECISION

GO / NO-GO Criteria:Must have (blockers if missing):
- [ ] [Critical requirement]
- [ ] [Critical requirement]

Should have (launch anyway but address soon):
- [ ] [Nice-to-have]
- [ ] [Nice-to-have]

Final decision: [Go / No-go / Delay]
Made by: [Name]
Date: [When]

</checklist_framework>

<meta_guidance>

Launch checklist principles:Customize for launch size
Small feature: Shorter checklist
Major product launch: Every item

Assign owners
Every checklist item should have a name
No "someone should..."

Set deadlines
Not just "before launch"
But "3 days before launch"

Track completion
Use actual checkboxes
Review progress daily in final week

Learn from past launches
What went wrong last time?
Add those items to checklist

Don't skip steps
Checklist exists because things get forgotten
Especially when rushing

Remember:

A launch checklist is boring.
A botched launch is expensive.

Take the 30 minutes to check everything.

</meta_guidance>

</launch_checklist>
```

</details>

---

### Sprint Planning

**📋 Use Case:** Turn messy backlog into realistic 2-week sprint plan

**🛠️ Recommended Tools:** Claude, ChatGPT Projects

**💡 Technique:** Capacity planning, dependency mapping, realistic scoping

<details>
<summary>Click to view prompt</summary>

```
<sprint_planning>

<sprint_inputs>
TEAM CAPACITY:
- Engineers: [Number available this sprint]
- Sprint length: [1 or 2 weeks]
- Historical velocity: [Points per sprint, or just "we usually finish X tickets"]
- This sprint's constraints: [PTO, holidays, other work]

PASTE BACKLOG:
[Your prioritized list of work - tickets, features, bugs, tech debt]

CONTEXT:
- Recent velocity: [Last 3 sprints - did you over/under commit?]
- Team health: [ ] Crushing it [ ] Normal [ ] Struggling/underwater
- Big picture: [What is this sprint working toward?]
</sprint_inputs>

<planning_framework>

You help PMs plan realistic sprints. Your analysis process:

Step 1: Calculate actual capacity
Start with theoretical capacity, then account for reality:
- Meetings take 20-30% of time
- Bug fixes and support interruptions
- PR reviews and code review
- Onboarding if new team members
- Scope creep and unknowns

Rule of thumb: Plan for 60-70% of theoretical capacity.

Step 2: Analyze the backlog
For each item, assess:
- Is it actually ready to start? (design done, requirements clear, no blockers)
- What's the real size? (not story points, but "will this take days or weeks?")
- Dependencies on other work or teams?
- Risk level: well-understood vs lots of unknowns
- Can it be split into smaller chunks?

Step 3: Apply prioritization forcing function
If backlog has 20 things and you can do 8, use this process:
- What breaks if we don't do it? (critical)
- What's blocking other work? (unblock)
- What's needed for upcoming deadline? (time-sensitive)
- What's high value/low effort? (quick wins)
- What can wait? (defer)

Step 4: Sequence intelligently
Don't just stack work randomly:
- Front-load risky/unknown work (so you have time to adjust)
- Group related work (context switching is expensive)
- Sequence dependencies (do foundation before feature)
- Leave buffer at end (something will go wrong)

Step 5: Reality check
Red flags that you're over-committing:
- Planned capacity = 100% of team time
- All work is "critical"
- Multiple large unknowns
- Dependencies on other teams
- No buffer for bugs/support
- Last 3 sprints you missed goals

Step 6: Define what "done" means
For this sprint specifically:
- What's the sprint goal in one sentence?
- What's the minimum to call sprint successful?
- What would you cut if week 1 goes poorly?
- What's your flex capacity if things go well?

Now create a realistic sprint plan. Show your reasoning about what's in, what's out, and why.

</planning_framework>

</sprint_planning>
```

</details>

---

### Backlog Grooming

**📋 Use Case:** Clean up messy backlog, write better tickets, prioritize work

**🛠️ Recommended Tools:** Claude, ChatGPT Projects

**💡 Technique:** Ticket quality assessment, priority clarification, scope definition

<details>
<summary>Click to view prompt</summary>

```
<backlog_grooming>

<backlog_inputs>
PASTE YOUR MESSY BACKLOG:
[List of tickets/stories that need grooming - just titles is fine, or full descriptions if you have them]

BACKLOG CONTEXT:
- How many tickets total: [Number]
- How old is oldest ticket: [Timeframe]
- Common issues: [ ] Vague requirements [ ] No priorities [ ] Duplicates [ ] Stale [ ] All of the above

YOUR GOALS:
- [ ] Clean up old/stale tickets
- [ ] Write better requirements  
- [ ] Prioritize properly
- [ ] Prep for sprint planning
- [ ] All of the above
</backlog_inputs>

<grooming_framework>

You help PMs turn messy backlogs into actionable work. Follow this process:

**STEP 1: Categorize every ticket**

Put each ticket in a bucket:

**READY (can be worked on next sprint):**
- Requirements clear and agreed
- Design complete if needed
- No blockers
- Sized/estimated
- Acceptance criteria defined

**NEEDS WORK (not ready but should be):**
- Vague description
- Missing acceptance criteria  
- Not sized
- Design needed but not done
- Needs spike/research first

**BLOCKED (can't work on yet):**
- Waiting on other team
- Dependency not done
- Need customer feedback first
- Technical blocker

**STALE (probably close/archive):**
- >6 months old
- No one cares anymore
- Better solution exists
- Not aligned to strategy

**DUPLICATE (merge or close):**
- Same ask as other ticket
- Subset of bigger ticket

**STEP 2: Assess ticket quality**

For each ticket, check these elements:

**Title:**
- [ ] Clear what it is (not "Fix bug" but "Fix login error on mobile Safari")
- [ ] Starts with verb (Add, Fix, Update, Remove)
- [ ] Short enough to scan (<60 chars)

**Description:**
- [ ] User story format: "As [user], I want [action] so that [benefit]"
- [ ] OR: Problem statement: "Currently [pain], we should [solution]"
- [ ] Context: Why this matters

**Acceptance criteria:**
- [ ] Specific, testable conditions
- [ ] Format: "Given [context], when [action], then [outcome]"
- [ ] Covers happy path and edge cases

**Size/estimate:**
- [ ] Has story points or t-shirt size
- [ ] Team calibrated on what size means
- [ ] If >8 points, should be split

**Dependencies:**
- [ ] Lists what must happen first
- [ ] Lists what's blocked by this

**Good ticket example:**
```
Title: Add password reset for mobile app users

As a mobile app user who forgot their password
I want to reset it from the login screen
So I can regain access without contacting support

Acceptance Criteria:
- Given I'm on login screen, when I tap "Forgot password", then I see email input
- Given I enter valid email, when I submit, then I get reset link via email
- Given invalid email, when I submit, then I see error "Email not found"
- Given I click reset link, when I create new password, then I can login

Size: 5 points
Dependencies: None
Design: [Figma link]
```

**Bad ticket example:**
```
Title: Password thing

We should let users reset passwords

Size: ?
```

**STEP 3: Apply prioritization framework**

For each ticket, assign to one tier:

**P0 (Now - next 1-2 sprints):**
- Blocking other work
- Customer commitment
- Critical bug
- Regulation/security issue

**P1 (Soon - next 1-2 months):**
- Moves key metric  
- High customer demand
- Strategic initiative
- Major improvement

**P2 (Later - this quarter):**
- Nice to have
- Small improvements
- Low-hanging fruit

**P3 (Backlog - someday/maybe):**
- Good idea but not urgent
- Needs more validation
- Low impact

**Don't prioritize (close/archive):**
- Stale (>6 months, no interest)
- Duplicate
- Doesn't align to strategy
- Better solution exists

**STEP 4: Identify tickets that need splitting**

Big tickets (>8 points) should be broken down:

**How to split:**
- By user flow (checkout flow → cart + payment + confirmation)
- By platform (web + mobile)
- By MVP vs polish (working version + nice-to-haves)
- By happy path vs edge cases (core flow + error handling)

**Red flag patterns:**
- Ticket with "and" multiple times ("Add X and Y and Z")
- Ticket that takes >2 weeks
- Ticket with 10+ acceptance criteria
- Ticket that's actually an epic

**STEP 5: Write missing acceptance criteria**

For tickets without clear AC, create them:

**Format:**
```
Given [starting state/context]
When [user action]
Then [expected result]
```

**Cover:**
- Happy path (works as expected)
- Error cases (what if it fails)
- Edge cases (boundary conditions)
- Non-functional (performance, security)

**STEP 6: Kill what should die**

Be ruthless about closing old tickets:

**Close if:**
- >6 months old and no one's asking
- "We should" but no one actually cares
- Duplicate of better ticket
- Problem solved differently
- Not aligned to current strategy

**Archive vs Close:**
- Archive = might revisit
- Close = never doing this

**Don't hoard backlog items "just in case."**

</grooming_framework>

---

## BACKLOG GROOMING REPORT

### Summary

**Backlog health:** [Good / Needs work / Disaster]

**Total tickets:** [X]

**Breakdown:**
- Ready to work: [Y]
- Need refinement: [Z]
- Should close/archive: [W]

**Top priority:**
[The 1-2 things that should be worked on next]

---

### Ticket Quality Assessment

**BY READINESS:**

**✅ READY (Can sprint on these):** [X tickets]
- [Ticket name]
- [Ticket name]
- [Ticket name]

**⚠️ NEEDS WORK:** [Y tickets]

**[Ticket name]**
- **What's missing:** [ ] Clear requirements [ ] Acceptance criteria [ ] Design [ ] Sizing
- **Blocker:** [What needs to happen to make this ready]
- **Owner:** [Who should refine this]

[Repeat for tickets needing work]

**🚫 BLOCKED:** [Z tickets]
- [Ticket]: Blocked by [dependency]
- [Ticket]: Blocked by [external team]

**💀 STALE/SHOULD CLOSE:** [W tickets]
- [Ticket]: [Why close]
- [Ticket]: [Why close]

---

### Priority Assignments

**P0 - NOW (Next 1-2 sprints):**

1. **[Ticket name]** - [Size]
   - **Why P0:** [Blocking work / customer commit / critical bug]
   - **Ready:** [Yes/No]

2. [Continue]

**Total P0 work:** [X points or days]

---

**P1 - SOON (Next 1-2 months):**

1. **[Ticket name]** - [Size]
   - **Why P1:** [Moves metric / strategic / high demand]
   - **Ready:** [Status]

[Continue]

**Total P1 work:** [Y points]

---

**P2 - LATER (This quarter):**
- [Ticket 1]
- [Ticket 2]
- [Total: Z tickets]

---

**P3 - SOMEDAY:**
- [Ticket 1]
- [Ticket 2]
- [Total: W tickets]

---

###

 Tickets That Need Splitting

**[Big ticket name]** - Currently [13 points]

**Why split:** [Too big / Multiple features / Long timeline]

**Proposed split:**

**Part 1:** [Smaller piece] - [5 points]
- [Specific scope]
- [Acceptance criteria]

**Part 2:** [Another piece] - [5 points]
- [Specific scope]
- [AC]

**Part 3:** [Polish] - [3 points]
- [Nice-to-haves]

---

[Repeat for other big tickets]

---

### Tickets with Improved Descriptions

**Before:** 
```
Title: Fix search

Search is broken, make it better
```

**After:**
```
Title: Fix mobile search returning 0 results for product names

As a mobile user searching for products
I want search to return relevant results  
So I can find what I'm looking for

Current problem: Searching "iphone case" returns 0 results, but product exists

Acceptance Criteria:
- Given I search for exact product name, then I see that product in results
- Given I search with typo (1-2 letters off), then I see suggested products
- Given I search for nonexistent product, then I see "No results" with suggested alternatives

Size: 8 points
```

---

[Show 3-5 examples of improved tickets]

---

### Tickets to Close/Archive

**CLOSE (Never doing):**

**[Ticket name]**
- **Why close:** [Reason - duplicate / stale / not aligned / better solution]
- **Alternative:** [If there's a better ticket for this, link it]

[Repeat]

**Total to close:** [X tickets]

---

**ARCHIVE (Maybe someday):**
- [Ticket 1] - [Why archive not close]
- [Ticket 2]
- [Total: Y tickets]

---

### Duplicates Found

**Keep: [Ticket A]**
**Close:** [Ticket B, Ticket C]
**Reason:** [They're all asking for same thing]

---

### Action Items

**IMMEDIATE (This week):**
- [ ] Close [X] stale tickets
- [ ] Refine these P0 tickets: [List]
- [ ] Get design for: [Tickets needing design]
- [ ] Size these tickets: [Unestimated work]

**BEFORE NEXT SPRINT PLANNING:**
- [ ] All P0 tickets have clear AC
- [ ] P0 tickets are sized
- [ ] Split big tickets: [List]
- [ ] Confirm with eng these are ready

**ONGOING:**
- [ ] Review P2/P3 monthly - close if stale
- [ ] New tickets must have AC before labeling "ready"
- [ ] Anything >6 months old gets reviewed

---

### Backlog Maintenance Recommendations

**Current issues:**
- [Pattern 1 - e.g., "Too many vague tickets"]
- [Pattern 2 - e.g., "Not closing old work"]

**Process improvements:**
- [Suggestion 1]
- [Suggestion 2]

**Grooming cadence:**
- Weekly: [What to review]
- Monthly: [Deeper cleanup]

</backlog_grooming>
```

</details>

---

### Post-Mortem Facilitation

**📋 Use Case:** Something went wrong (outage, bad launch, missed deadline) - need to learn from it

**🛠️ Recommended Tools:** Claude, ChatGPT Projects

**💡 Technique:** Blameless analysis, root cause extraction, action item generation

<details>
<summary>Click to view prompt</summary>

```
<post_mortem>

<incident_inputs>
WHAT HAPPENED:
[Brief description of the incident/failure]

TIMELINE:
- When it started: [Date/time]
- When detected: [Date/time]
- When resolved: [Date/time]
- Duration: [Total time]

IMPACT:
- Users affected: [Number or %]
- Revenue impact: [If applicable]
- Customer complaints: [Volume]
- SLA breach: [Yes/no]

WHO'S INVOLVED:
[Team members who should be in post-mortem meeting]

INITIAL OBSERVATIONS:
[Any early thoughts on what went wrong]
</incident_inputs>

<postmortem_framework>

You facilitate blameless post-mortems that drive learning. Follow this process:

STEP 1: Set the ground rulesPost-mortem is NOT about:
- Finding who to blame
- Punishing mistakes
- Defending decisions

Post-mortem IS about:
- Understanding what happened
- Preventing it from happening again
- Improving systems and processes

Blameless culture:
- Assume everyone had good intentions
- Assume everyone did best with info they had
- Focus on system failures, not human failures
- If "human error" is root cause, you haven't dug deep enough

STEP 2: Build detailed timeline

For every significant event, document:
- Time: [Exact timestamp]
- Event: [What happened]
- Who: [Person or system]
- How we knew: [Alert, user report, manual discovery]

Example:14:23 - Deploy initiated by [Person] - normal process 14:25 - Error rates start climbing - caught by monitoring 14:27 - On-call paged - automated alert 14:30 - On-call starts investigation - manual 14:35 - Root cause identified - manual debugging 14:40 - Rollback initiated - manual action 14:45 - Service recovered - monitoring confirmsGoal: Recreate exactly what happened, minute by minute.

STEP 3: Perform 5 Whys analysis

Keep asking "why" until you hit systemic issues:

Example:
"Why did the service go down?"
→ Database ran out of connections

"Why did it run out of connections?"
→ Connection pool was too small

"Why was pool too small?"
→ We didn't load test this feature

"Why didn't we load test?"
→ No load testing in our deploy process

"Why no load testing process?"
→ We prioritized speed over reliability

Root cause: Missing load testing in deployment process

STEP 4: Identify contributing factors

Beyond root cause, what else contributed?

Categories to check:
- Technical: Architecture, code, infrastructure
- Process: Testing, deployment, monitoring
- Communication: Handoffs, documentation, alerts
- Tools: What failed or was missing
- Organizational: Priorities, resources, knowledge gaps

STEP 5: Extract lessons learnedWhat went well:
(Yes, even in failures, something worked)
- Monitoring caught the issue quickly
- Team responded fast
- Rollback process worked
- Communication was clear

What went poorly:
- Detection took too long
- No clear owner initially
- Rollback was manual and slow
- External communication was delayed

What we learned:
[Specific insights that will change how we work]

STEP 6: Generate action itemsGood action items:
- Specific (not "improve monitoring")
- Owned (person's name attached)
- Dated (deadline)
- Verifiable (can check if done)

Example:
❌ "We should test better"
✅ "Add load testing to deploy pipeline - @Jane - by March 15"

Prioritize:
- P0: Prevents this specific issue (quick wins)
- P1: Prevents entire class of issues (systemic)
- P2: Nice improvements (do eventually)

STEP 7: Plan follow-up

- Schedule review date for action items
- Document in central location
- Share lessons with broader team
- Update runbooks/processes

</postmortem_framework>

---

## POST-MORTEM DOCUMENT

Incident: [Brief descriptive name]Date: [When it happened]Severity: [P0/P1/P2/P3]Status: [Resolved]Author: [Name]

---

### Executive Summary

What happened:
[2-3 sentences describing the incident]

Impact:
- Duration: [X hours/minutes]
- Users affected: [Y users or Z%]
- Services impacted: [Which features/systems]
- Business impact: [Revenue, SLA, reputation]

Root cause:
[One sentence]

Fix:
[What we did to resolve]

Prevention:
[What we're doing so this never happens again]

---

### Timeline

| Time | Event | How Detected | Who |
|------|-------|--------------|-----|
| 14:23 | [What happened] | [Alert/Manual/User report] | [Person/System] |
| 14:25 | [Next event] | [How] | [Who] |
| 14:27 | [Next event] | [How] | [Who] |

Key timestamps:
- Started: [When issue began]
- Detected: [When we knew]
- Mean time to detect: [Started → Detected]
- Mitigated: [When we applied fix]
- Resolved: [When fully recovered]
- Mean time to recover: [Detected → Resolved]

---

### What Happened (Detailed)

Initial state:
[What was normal before incident]

Trigger event:
[What caused the incident to start]

Cascade:
[How the problem spread or got worse]

Detection:
[How we found out - alert, user report, manual discovery]

Response:
[What team did to investigate and fix]

Resolution:
[What ultimately fixed it]

Recovery:
[How system/users recovered]

---

### Root Cause Analysis

Immediate cause:
[The proximate thing that broke]

5 Whys:Why did [incident] happen?
→ [Answer 1]

Why did [answer 1] happen?
→ [Answer 2]

Why did [answer 2] happen?
→ [Answer 3]

Why did [answer 3] happen?
→ [Answer 4]

Why did [answer 4] happen?
→ [Root cause]

Root cause:
[The systemic issue that, if fixed, prevents this entire class of problems]

---

### Contributing Factors

Technical factors:
- [Architecture decision that made this possible]
- [Missing safeguard]
- [Technical debt]

Process factors:
- [Missing testing]
- [Unclear ownership]
- [Documentation gap]

Communication factors:
- [Handoff issue]
- [Alert that didn't fire]
- [Unclear escalation]

Organizational factors:
- [Resource constraint]
- [Priority tradeoff]
- [Knowledge gap]

---

### Impact Analysis

User impact:
- Total users affected: [X]
- % of user base: [Y%]
- What they experienced: [Specific symptoms]
- User complaints: [Volume and themes]

Business impact:
- Revenue lost: $[X] (if applicable)
- SLA breach: [Yes/No, which customers]
- Reputation damage: [Social, press mentions]
- Support burden: [Tickets generated]

Team impact:
- Engineering hours spent: [X hours]
- Opportunity cost: [What didn't get done]
- Stress/morale: [Effect on team]

---

### What Went Well

Detection:
- [Monitoring caught the issue]
- [Alert fired correctly]

Response:
- [Team assembled quickly]
- [Clear incident commander]
- [Effective debugging]

Resolution:
- [Rollback process worked]
- [Fix was simple]

Communication:
- [Status page updated promptly]
- [Clear internal updates]
- [Customer communication was good]

Worth celebrating:
[Specific call-outs for people who did great work]

---

### What Went Poorly

Detection:
- [ ] Took too long to detect ([X minutes])
- [ ] Monitoring didn't catch it
- [ ] User reported before we knew

Response:
- [ ] Unclear who owned problem
- [ ] Slow to escalate
- [ ] Communication gaps

Resolution:
- [ ] Manual process (should be automated)
- [ ] Rollback was complicated
- [ ] Fix took too long

Communication:
- [ ] Status page delayed
- [ ] Internal confusion
- [ ] Customer comms unclear

---

### Lessons Learned

What this incident taught us:Lesson 1: [Specific insight]
[Description and why it matters]

Lesson 2: [Another insight]
[Description]

Lesson 3: [Another]
[Description]

How this changes our thinking:
[Broader implications for how we build/operate]

---

### Action Items

P0 - CRITICAL (Prevent this specific issue):1. [Specific action]
- Why: [Prevents exact problem]
- Owner: [@Name]
- Due: [Date]
- Done: [ ]

2. [Another action]
- Why: [Impact]
- Owner: [@Name]
- Due: [Date]
- Done: [ ]

---

P1 - HIGH (Prevent entire class of issues):1. [Systemic improvement]
- Why: [Broader prevention]
- Owner: [@Name]
- Due: [Date]
- Done: [ ]

---

P2 - MEDIUM (General improvements):1. [Nice-to-have improvement]
- Owner: [@Name]
- Due: [Date]
- Done: [ ]

---

### Monitoring & Alerting Gaps

What monitoring missed:
- [Gap 1]
- [Gap 2]

New alerts to add:
- [Alert 1]: Trigger when [condition]
- [Alert 2]: Trigger when [condition]

Improvements to existing alerts:
- [Alert name]: Make more sensitive/specific

---

### Documentation Updates Needed

Runbooks to create/update:
- [ ] [Runbook name]: Add steps for [scenario]
- [ ] [Runbook name]: Update with [new info]

Architecture docs:
- [ ] [Doc]: Update to reflect [reality]

On-call guides:
- [ ] [Guide]: Add troubleshooting for [issue]

---

### Communication

Internal:
- Post-mortem shared with: [Teams]
- Date shared: [Date]
- Key takeaways communicated: [Where]

External (if applicable):
- Customer communication: [What we sent]
- Public post-mortem: [Yes/No, link]
- Press/social response: [If relevant]

---

### Follow-Up Plan

Post-mortem review meeting:
- Date: [30 days from now]
- Attendees: [Who]
- Agenda: Review progress on action items

Action item tracking:
- Where tracked: [Jira/Linear/Notion]
- Review cadence: [Weekly]
- Owner of tracking: [@Name]

Metrics to monitor:
- [Metric 1]: Ensure this stays stable
- [Metric 2]: Ensure this improves

---

### Appendix

Relevant links:
- Incident channel: [Slack link]
- Monitoring dashboard: [Link]
- Related PRs/commits: [Links]
- Customer tickets: [Links]

Similar past incidents:
- [Date]: [Brief description and how this is similar]
- Learning: [What we should have applied but didn't]

</post_mortem>
```

</details>

---

### Pre-Mortem Facilitation

**📋 Use Case:** About to launch something risky - identify what could go wrong before it does

**🛠️ Recommended Tools:** Claude, ChatGPT Projects

**💡 Technique:** Failure scenario generation, risk prioritization, mitigation planning

<details>
<summary>Click to view prompt</summary>

```
<pre_mortem>

<premortem_inputs>
WHAT YOU'RE LAUNCHING:
[Feature, product, initiative description]

LAUNCH DETAILS:
- Launch date: [When]
- Scope: [Who gets it, how big]
- Why this is risky: [Known concerns]
- Stakes: [What happens if it fails]

TEAM CONTEXT:
- Who should participate: [Cross-functional team]
- What you're most worried about: [Top concerns]
- Past failures: [Similar launches that went wrong]
</premortem_inputs>

<premortem_framework>

You facilitate pre-mortems that surface risks before launch. Follow this process:

**STEP 1: Frame the exercise**

**The setup:**
"It's [3 months from now]. We launched [project] and it was a complete disaster. Our worst fears came true. We're here to figure out what went wrong."

**Why this works:**
- Removes pressure to be positive
- Permission to voice concerns
- Surfaces hidden worries
- Uncovers blind spots

**Ground rules:**
- No idea is too pessimistic
- Focus on what COULD go wrong, not likelihood
- Everyone participates
- Blame-free environment

**STEP 2: Generate failure scenarios**

Have team brainstorm all the ways this could fail:

**Categories to explore:**

**Technical failures:**
- What could break?
- Performance issues?
- Integration problems?
- Data/security issues?

**Product failures:**
- Users don't understand it?
- Solves wrong problem?
- Too complex?
- Missing key features?

**Go-to-market failures:**
- Poor positioning?
- Wrong target audience?
- Bad timing?
- Competitive response?

**Operational failures:**
- Team not ready?
- Support overwhelmed?
- Sales can't sell it?
- Poor documentation?

**Business failures:**
- Wrong pricing?
- No adoption?
- Cannibalize existing revenue?
- Miss projections?

**STEP 3: Assess each risk**

For every failure scenario:

**Likelihood:** [High/Med/Low]
How likely is this to actually happen?

**Impact:** [High/Med/Low]
If it happens, how bad is it?

**Priority matrix:**
High Impact + High Likelihood = CRITICAL (must mitigate)
High Impact + Low Likelihood = MONITOR (have plan)
Low Impact + High Likelihood = ACCEPT (annoying but okay)
Low Impact + Low Likelihood = IGNORE (not worth time)


**STEP 4: Generate mitigations**

For critical and high-priority risks:

**Mitigation types:**
- **Prevent:** Stop it from happening
- **Detect:** Know quickly if it happens  
- **Respond:** Have plan when it happens
- **Accept:** Consciously choose to live with risk

**Good mitigation:**
- Specific action
- Owner assigned
- Done before launch
- Verifiable

**Example:**
Risk: "Users don't understand new feature"
❌ Bad mitigation: "Make it clearer"
✅ Good mitigation: "Run usability test with 5 users, iterate based on feedback - @Jane by Dec 1"

**STEP 5: Identify early warning signals**

What would tell you things are going wrong?

**Leading indicators (see problems early):**
- Low engagement in beta
- User confusion in tests
- Sales team not demoing it
- Poor qualitative feedback

**Lagging indicators (problems already happened):**
- Adoption below target
- Churn spike
- Support tickets flood
- Negative reviews

**STEP 6: Build decision framework**

**Define kill criteria:**
If [X] happens, we will [action]

**Example:**
- If adoption <5% after week 1 → investigate deeply
- If NPS drops >10 points → consider pausing rollout
- If error rate >5% → immediate rollback

**STEP 7: Create contingency plans**

For top 3 risks, have backup plans:
- Plan B if primary approach fails
- Rollback procedure
- Communication templates
- Resource allocation

</premortem_framework>

---

## PRE-MORTEM DOCUMENT

**Project:** [Name]  
**Launch Date:** [Date]  
**Owner:** [Name]  
**Pre-Mortem Date:** [When exercise was done]

---

### The Scenario

**"It's [date 3 months from launch]. We launched [project] and it failed spectacularly."**

**What we hoped would happen:**
[Original success vision]

**What actually happened:**
[The disaster scenario we're imagining]

**Stakes:**
[Why this failure would be bad - revenue, reputation, team morale, etc.]

---

### Failure Scenarios Identified

**Team brainstormed [X] ways this could fail:**

---

**TECHNICAL FAILURES:**

**Scenario 1: [Specific failure]**
- **What happens:** [Description]
- **Likelihood:** [High/Med/Low]
- **Impact:** [High/Med/Low]
- **Priority:** [Critical/High/Medium/Low]

**Scenario 2: [Another failure]**
[Same format]

---

**PRODUCT FAILURES:**

**Scenario 1: Users don't understand the feature**
- **What happens:** [They try it, get confused, abandon it]
- **Likelihood:** Medium
- **Impact:** High
- **Priority:** CRITICAL

[Continue for all scenarios]

---

**GO-TO-MARKET FAILURES:**

[List scenarios]

---

**OPERATIONAL FAILURES:**

[List scenarios]

---

**BUSINESS FAILURES:**

[List scenarios]

---

### Risk Matrix

| Risk | Likelihood | Impact | Priority | Owner |
|------|-----------|---------|----------|-------|
| [Risk 1] | High | High | CRITICAL | [@Name] |
| [Risk 2] | Med | High | HIGH | [@Name] |
| [Risk 3] | High | Low | MEDIUM | [@Name] |

**Focus on:** [Number] critical risks, [Number] high risks

---

### Critical Risks & Mitigations

**RISK 1: [Specific risk]**

**Full scenario:**
[Detailed description of what goes wrong]

**Likelihood:** High  
**Impact:** High  
**Priority:** CRITICAL

**Why this could happen:**
- [Root cause 1]
- [Root cause 2]

**Mitigation plan:**

**PREVENT:**
- [ ] [Action to prevent] - @Owner - Due: [Date]
- [ ] [Another action] - @Owner - Due: [Date]

**DETECT:**
- [ ] [Monitoring/alert to add] - @Owner - Due: [Date]
- [ ] [Metric to track] - @Owner - Due: [Date]

**RESPOND:**
- [ ] [Plan if this happens] - @Owner - Documented: [Link]

**Contingency plan:**
If this happens, we will:
1. [Step 1]
2. [Step 2]
3. [Decision point and criteria]

**Success criteria for mitigation:**
[How we'll know we've reduced this risk]

---

**RISK 2: [Another critical risk]**

[Same detailed format]

---

[Repeat for all critical risks]

---

### High Priority Risks

**RISK: [Description]**
- **Mitigation:** [What we're doing]
- **Owner:** [@Name]
- **Due:** [Date]

[Repeat for all high-priority risks]

---

### Medium/Low Priority Risks

**Risks we're accepting:**
- [Risk 1]: [Why we're accepting it]
- [Risk 2]: [Why we're accepting it]

**Monitoring plan:**
[How we'll watch for these without active mitigation]

---

### Early Warning Signals

**How we'll know things are going wrong:**

**WEEK 1 SIGNALS:**
- [ ] [Metric] below [threshold] → Action: [What we do]
- [ ] [Behavior] observed → Action: [What we do]
- [ ] [Feedback theme] emerges → Action: [What we do]

**WEEK 2-4 SIGNALS:**
- [ ] [Leading indicator] → Action: [What we do]
- [ ] [Another signal] → Action: [What we do]

**MONTH 2-3 SIGNALS:**
- [ ] [Lagging indicator] → Action: [What we do]

**Dashboard:** [Link to monitoring dashboard]

---

### Decision Framework

**KILL CRITERIA (We rollback/pause if):**
- [ ] [Metric] drops below [X]
- [ ] [User complaints] exceed [Y]
- [ ] [Error rate] above [Z%]
- [ ] [Business metric] misses by >[W%]

**INVESTIGATE CRITERIA (We dig deeper if):**
- [ ] [Signal 1]
- [ ] [Signal 2]

**ITERATE CRITERIA (We adjust quickly if):**
- [ ] [Feedback pattern]
- [ ] [Usage pattern]

**Decision maker:** [@Name]  
**Escalation path:** [@Name → @Name → @Name]

---

### Contingency Plans

**PLAN B: If primary approach fails**

**Trigger:** [What indicates we need Plan B]

**Alternative approach:**
[What we do instead]

**Resources needed:**
[Time, people, budget]

**Timeline:**
[How quickly we can switch]

---

**ROLLBACK PLAN:**

**Trigger:** [Conditions for rollback]

**Rollback procedure:**
1. [Technical step]
2. [Communication step]
3. [Validation step]

**Time to rollback:** [X hours/minutes]

**User impact:** [What users experience]

**Communication templates:**
- Internal: [Link]
- External: [Link]

---

**COMMUNICATION CRISIS PLAN:**

**If things go really wrong:**

**Internal communication:**
- Who needs to know: [Stakeholders]
- Update frequency: [How often]
- Channel: [Where]
- Owner: [@Name]

**External communication:**
- Customer communication: [Template link]
- Status page: [When to update]
- Social/press: [If needed]
- Owner: [@Name]

---

### Past Failures to Learn From

**Similar launch that failed:**
- **What:** [Description]
- **When:** [Date]
- **Why it failed:** [Root cause]
- **How we're avoiding that:** [Specific actions]

**Another past failure:**
[Same format]

**Patterns we noticed:**
[Common themes from past failures]

---

### What Could Go Right

**Best case scenarios:**
(Yes, also imagine success)

**If things go better than expected:**
- [Positive scenario 1]
- [Positive scenario 2]

**How we'd capitalize:**
[Plan to scale success]

---

### Pre-Launch Checklist

**BEFORE WE LAUNCH, CONFIRM:**

**Mitigations complete:**
- [ ] All critical risk mitigations done
- [ ] High priority mitigations done
- [ ] Contingency plans documented

**Monitoring ready:**
- [ ] Early warning signals tracked
- [ ] Dashboards built
- [ ] Alerts configured
- [ ] On-call scheduled

**Team ready:**
- [ ] Support trained
- [ ] Sales enabled  
- [ ] Eng on standby
- [ ] Communication templates ready

**Decision framework agreed:**
- [ ] Kill criteria documented
- [ ] Decision makers identified
- [ ] Escalation path clear

---

### Launch Day Plan

**Day 1 monitoring:**
- Hour 1-2: [Who's watching what]
- Hour 3-6: [Check-in plan]
- End of day: [Review and decision]

**Week 1 monitoring:**
- Daily check: [Metrics to review]
- Daily standup: [Time and who]
- Weekly review: [Friday assessment]

**First month:**
- Weekly deep-dive
- Monthly retrospective
- Continuous iteration

---

### Action Items Before Launch

**CRITICAL (Must do before launch):**
- [ ] [Action] - @Owner - Due: [Date]
- [ ] [Action] - @Owner - Due: [Date]

**HIGH (Should do before launch):**
- [ ] [Action] - @Owner - Due: [Date]

**MEDIUM (Nice to have):**
- [ ] [Action] - @Owner - Due: [Date]

---

### Go/No-Go Decision

**Final review date:** [Date, 1 week before launch]

**Go criteria:**
- [ ] All critical mitigations complete
- [ ] Team confident in plan
- [ ] Monitoring ready
- [ ] Rollback tested

**No-go criteria:**
- [ ] Multiple critical risks unmitigated
- [ ] Key team members concerned
- [ ] Monitoring not ready
- [ ] Can't rollback quickly

**Decision maker:** [@Name]

---

### Participants

**Who was in pre-mortem:**
- @Name - Role
- @Name - Role
- @Name - Role

**Key concerns surfaced by:**
- [Person]: [Their main worry]
- [Person]: [Their concern]

---

### Follow-Up

**Post-launch review:**
- **Date:** [30 days after launch]
- **Questions:** Did our risks materialize? Did mitigations work?

**Update this document:**
- As we learn: [Add new risks]
- As we mitigate: [Check off actions]
- As reality unfolds: [Compare to predictions]

</pre_mortem>
```

</details>

---

### Deprecation Plan

**📋 Use Case:** Need to sunset a feature, product, or version - do it without angering users

**🛠️ Recommended Tools:** Claude, ChatGPT Projects

**💡 Technique:** User impact analysis, migration planning, communication strategy

<details>
<summary>Click to view prompt</summary>

```
<deprecation_plan>

<deprecation_inputs>
WHAT YOU'RE DEPRECATING:
[Feature, product, API version, platform, etc.]

WHY DEPRECATING:
- [ ] Low usage (not worth maintaining)
- [ ] Technical debt (holding back product)
- [ ] Strategic shift (moving to new solution)
- [ ] Cost (expensive to run)
- [ ] Security/compliance (can't support anymore)

CURRENT STATE:
- Users affected: [How many]
- Usage: [How much/often]
- Revenue impact: [If applicable]
- Technical dependencies: [What relies on this]

REPLACEMENT:
- [ ] Migrating to new version
- [ ] Replacing with alternative feature
- [ ] No replacement (just removing)
</deprecation_inputs>

<deprecation_framework>

You plan deprecations that minimize user pain. Follow this process:

STEP 1: Understand impactWho's affected:
- Total users: [Number]
- Active users (used in last 30 days): [Number]
- Power users (daily usage): [Number]
- Paying customers: [Number]
- Enterprise customers: [Names if small]

How they're affected:
- Workflow broken completely?
- Inconvenience but alternatives exist?
- Minor impact?

Segment by impact:
- Critical impact: Can't use product without this
- Major impact: Significantly changes workflow
- Minor impact: Slight inconvenience

Focus on critical/major impact users first.STEP 2: Provide migration pathIf replacing with new version:
- Document how to migrate
- Provide migration scripts/tools
- Offer assisted migration for enterprise
- Test migration with beta customers

If no replacement:
- Document alternatives
- Explain workarounds
- Connect to ecosystem partners if applicable

Make migration easy:
- Step-by-step guide
- Video tutorials
- Sample code
- Support channel

STEP 3: Set timelineDeprecation phases:Phase 1: Announcement (T-6 months)
- Announce deprecation
- Explain why and what's next
- Give deadline

Phase 2: Deprecation notice (T-3 months)
- In-product warnings
- Email reminders
- Blog post

Phase 3: Final warning (T-1 month)
- Aggressive in-product notices
- Direct outreach to active users
- Last chance communication

Phase 4: Deprecation (T-0)
- Feature disabled/removed
- Redirect to alternative
- Support for migrations

Phase 5: Cleanup (T+1 month)
- Remove code
- Update documentation
- Archive resources

Timeline based on impact:
- High impact: 12 months notice
- Medium impact: 6 months notice
- Low impact: 3 months notice

Legal/contractual:
Check if you promised support for X years.

STEP 4: Communicate clearlyTone:
- Empathetic (acknowledge inconvenience)
- Clear (no ambiguity about dates)
- Helpful (provide path forward)
- Final (not negotiable)

What to communicate:
- What's being deprecated
- Why (honest reason)
- When (specific date)
- What to do instead
- How to get help

Don't:
- Apologize excessively
- Be vague about timeline
- Hide the reason
- Make it sound tentative

Do:
- Be direct
- Give concrete dates
- Provide resources
- Offer support

STEP 5: Support users through transitionResources to provide:
- Migration guide (written)
- Migration tools (if applicable)
- Sample code/examples
- FAQs
- Support channel

Extra support for:
- Enterprise customers (white-glove)
- Power users (direct outreach)
- Partners/integrators (early notice)

Metrics to track:
- % users migrated
- Support ticket volume
- User complaints
- Churn related to deprecation

STEP 6: Handle pushbackCommon objections:
"We built our business on this!"
→ Response: "We're providing [X months] notice and [migration path]. We'll support your migration."

"This is the only feature we use!"
→ Response: "Here's the alternative. Here's why we made this decision."

"We can't migrate in this timeline!"
→ Response: [Case-by-case extension for enterprise? Or firm deadline?]

Be empathetic but firm.STEP 7: Measure successSuccess criteria:
- [X%] of users migrated before deadline
- <[Y] support tickets related to deprecation
- Churn rate stays <[Z%]
- No public backlash/bad press

Post-mortem:
- What went well
- What we'd do differently
- Lessons for next deprecation

</deprecation_framework>

---

## DEPRECATION PLAN

What's Being Deprecated: [Name]Deprecation Date: [When it's fully removed]Owner: [Name]Status: [Planning / Announced / In Progress / Complete]

---

### Executive Summary

What: [One sentence describing what's being deprecated]

Why: [Primary reason]

When: [Deprecation date]

Impact: [Number of users affected]

Migration: [What users should do instead]

Risk level: [Low/Medium/High] based on usage and user impact

---

### What's Being Deprecated

Feature/Product:
[Detailed description]

Current usage:
- Total users: [X]
- Active users (last 30 days): [Y]
- Usage frequency: [Pattern]
- Revenue tied to this: $[Z] if applicable

Why we built this originally:
[Context - what problem it solved, when launched]

Why deprecating now:
[Honest explanation]

---

### User Impact Analysis

WHO'S AFFECTED:Tier 1: Critical Impact ([X] users)
- Who: [Segment description]
- Impact: [Can't use product without this]
- Action needed: [What they must do]

Tier 2: Major Impact ([Y] users)
- Who: [Segment]
- Impact: [Significant workflow change]
- Action needed: [Migration path]

Tier 3: Minor Impact ([Z] users)
- Who: [Segment]
- Impact: [Slight inconvenience]
- Action needed: [Simple change]

---

SPECIFIC CUSTOMERS TO WATCH:Enterprise Customer 1: [Name]
- Usage: [How they use deprecated feature]
- Impact: [High/Med/Low]
- Plan: [Direct outreach, assisted migration]
- Owner: [@CSM name]

Enterprise Customer 2:
[Same structure]

---

USAGE BREAKDOWN:

| User Segment | Count | % of Base | Impact Level | Migration Path |
|--------------|-------|-----------|--------------|----------------|
| [Segment 1] | [X] | [Y%] | Critical | [Path] |
| [Segment 2] | [A] | [B%] | Major | [Path] |
| [Segment 3] | [C] | [D%] | Minor | [Path] |

---

### Migration Path

RECOMMENDED ALTERNATIVE:Option 1: [New feature/approach]
- What it is: [Description]
- How it's better: [Advantages]
- How to switch: [Steps]
- Timeline: [How long migration takes]

Migration steps:
1. [Step 1 with link to docs]
2. [Step 2]
3. [Step 3]

For most users: [X hours of work]

---

Option 2: [Alternative approach if applicable]
[Same structure]

---

If no replacement:Workarounds:
- [Alternative 1]: [How to achieve similar outcome]
- [Alternative 2]: [Another approach]

---

MIGRATION TOOLS:We're providing:
- [ ] Migration script: [Link]
- [ ] Data export tool: [Link]
- [ ] Step-by-step guide: [Link]
- [ ] Video tutorial: [Link]
- [ ] Sample code: [Link]

Support:
- Documentation: [Link]
- Support channel: [Slack/email]
- Office hours: [Schedule]

---

### Timeline

PHASE 1: ANNOUNCEMENT (TODAY → [Date])Date: [Start date]

Actions:
- [ ] Announce deprecation (blog, email, in-app)
- [ ] Update documentation
- [ ] Notify enterprise customers directly
- [ ] Post to changelog
- [ ] Create FAQ

Goal: All users aware and have migration plan

---

PHASE 2: DEPRECATION WARNING ([Date] → [Date])Date: [T-3 months]

Actions:
- [ ] In-product warning banner
- [ ] Email reminders (weekly)
- [ ] Direct outreach to active users
- [ ] Migration webinar
- [ ] Update API docs with deprecation notice

Goal: 50% of users migrated

---

PHASE 3: FINAL WARNING ([Date] → [Date])Date: [T-1 month]

Actions:
- [ ] Aggressive in-product warnings
- [ ] Daily email reminders
- [ ] Personal outreach to remaining power users
- [ ] Block new usage (if applicable)
- [ ] "Last chance" communication

Goal: 90% of users migrated

---

PHASE 4: DEPRECATION ([Date])Date: [Deprecation date]

Actions:
- [ ] Feature disabled/API returns errors
- [ ] Redirect users to alternative
- [ ] Final communication
- [ ] Support team ready for questions

Impact: [X%] of users still not migrated - support burden

---

PHASE 5: CLEANUP ([Date] → [Date])Date: [T+1 month]

Actions:
- [ ] Remove code from codebase
- [ ] Archive documentation
- [ ] Remove from marketing site
- [ ] Update contracts/terms
- [ ] Post-mortem with team

Goal: Fully removed, no ongoing costs

---

### Communication Plan

ANNOUNCEMENT EMAIL (T-6 months):Subject: [Feature] will be deprecated on [Date]

Body:Hi [User],  We're reaching out to let you know that [feature] will be deprecated on [Date].  WHY: [Honest reason in 1-2 sentences]  WHAT THIS MEANS: [Impact on them]  WHAT TO DO: [Clear next step with link]  TIMELINE: - Now: Start planning migration - [Date]: Deprecation warnings in product - [Date]: Feature fully deprecated  We're here to help. [Support resources]  Thanks, [Team]

---

IN-PRODUCT WARNING (T-3 months):Banner:⚠️ [Feature] will be deprecated on [Date]. Migrate to [alternative] now. [Learn more]Modal (for power users):[Feature] is being deprecated  You're actively using this feature. Starting [Date], it will no longer be available.  [Button: See migration guide] [Button: Remind me later]

---

FINAL WARNING EMAIL (T-1 month):Subject: [Feature] deprecates in 30 days

Body:Hi [User],  This is your final reminder: [Feature] will stop working on [Date].  You're still using this feature. Here's what you need to do: [Clear migration steps]  After [Date], [specific impact].  Need help? [Support contact]  Don't wait - migrate today.  [Team]

---

DEPRECATION DAY EMAIL:Subject: [Feature] is now deprecated

Body:As of today, [feature] is deprecated.  If you're trying to use it, you'll see [error/message].  Next steps: [What to do now]  Need help? [Support]

---

### Support Plan

RESOURCES:Documentation:
- Migration guide: [Link]
- FAQ: [Link]
- Troubleshooting: [Link]
- API documentation updates: [Link]

Support channels:
- Email: [Address]
- Slack: [Channel]
- Office hours: [Every Tuesday 2-3pm]

Support SLAs:
- Response time: [24 hours]
- Migration assistance: [Available for enterprise]

---

EXPECTED SUPPORT BURDEN:Ticket volume estimate:
- T-3 months: +[X] tickets/week
- T-1 month: +[Y] tickets/week
- Deprecation day: +[Z] tickets/day
- T+1 month: [W] tickets/week declining

Support team readiness:
- [ ] Support team trained on migration
- [ ] Canned responses prepared
- [ ] Escalation path clear
- [ ] Extra coverage scheduled

---

ENTERPRISE CUSTOMER PLAN:White-glove migration:
- [ ] Schedule 1:1 calls with each enterprise customer
- [ ] Provide custom migration scripts if needed
- [ ] Dedicated eng support during migration
- [ ] Follow-up after migration complete

Owner: [@CSM name or tech contact]

---

### Risk Management

RISK 1: Users don't migrate in timeLikelihood: [Medium/High]

Impact: [Support burden, churn, complaints]

Mitigation:
- Aggressive communication
- Make migration very easy
- Offer assisted migration
- Clear deadline

Contingency:
- Extend deadline by [X weeks] if <80% migrated?
- Or firm deadline regardless?

Decision criteria: [What triggers extension]

---

RISK 2: Technical issues with migrationLikelihood: [Low/Med]

Impact: [Blocked users, delays]

Mitigation:
- Test migration path extensively
- Beta test with friendly customers
- Have rollback plan

Contingency:
- Dedicated eng on-call during migration period

---

RISK 3: Customer churnLikelihood: [Low/Med]

Impact: [Revenue loss]

Mitigation:
- Early outreach to enterprise
- Alternative solutions ready
- CSM involvement

Monitoring:
- Track churn rate during deprecation
- Exit interviews with churned customers
- Adjust if churn spikes

---

RISK 4: Bad press/social media backlashLikelihood: [Low/Med]

Impact: [Reputation]

Mitigation:
- Honest communication
- Generous timeline
- Good migration path

Response plan:
- [ ] PR team aware
- [ ] Response templates ready
- [ ] Monitor Twitter/Reddit
- [ ] Respond quickly to complaints

---

### Success Metrics

MIGRATION GOALS:By T-3 months:
- [ ] 30% of users migrated
- [ ] All enterprise customers have migration plan

By T-1 month:
- [ ] 70% of users migrated
- [ ] <50 support tickets/week

By deprecation date:
- [ ] 90% of users migrated
- [ ] Zero critical customer issues

Post-deprecation:
- [ ] Churn rate <[X%]
- [ ] Support tickets declining
- [ ] No major complaints

---

TRACKING:Dashboard: [Link]

Metrics to monitor:
- % users on deprecated feature (declining)
- % users on new feature (increasing)
- Support ticket volume
- User sentiment (NPS, surveys)
- Churn rate

Weekly review: [When and with whom]

---

### Financial Impact

COST OF MAINTAINING:
- Engineering time: [X hours/month]
- Infrastructure: $[Y]/month
- Support burden: [Z tickets/month]
- Total annual cost: $[A]COST OF DEPRECATING:
- Engineering time (cleanup): [Hours]
- Support burden (migration): [Est tickets]
- Potential churn: [Est revenue at risk]
- Total deprecation cost: $[B]NET BENEFIT:
[Savings after deprecation]

---

### Legal & Contractual

CONTRACTUAL OBLIGATIONS:Check:
- [ ] Terms of service (did we promise support?)
- [ ] Enterprise contracts (guaranteed feature access?)
- [ ] SLAs (does removing this breach SLA?)

Actions needed:
- [ ] Update ToS: [What changes]
- [ ] Contract amendments: [For which customers]
- [ ] Legal review: [Complete by date]

---

### Post-Mortem Plan

30 DAYS POST-DEPRECATION:Review questions:
- Did timeline work? (Too short/long?)
- Was communication effective?
- Did migration path work?
- What surprised us?
- What would we do differently?

Metrics to review:
- Actual vs expected migration rate
- Support burden vs estimate
- Churn impact
- User sentiment

Document learnings:
[For next deprecation]

---

### Approval & Sign-Off

Requires approval from:
- [ ] Engineering lead (feasibility, timeline)
- [ ] Support lead (readiness for volume)
- [ ] Customer success (enterprise impact)
- [ ] Legal (contractual review)
- [ ] CEO/Product lead (final decision)

Approval date: [When]

Go/no-go criteria:
- Migration path tested and works
- Communication plan ready
- Support team trained
- Legal cleared

---

### FAQs

Q: Why are you deprecating this?
A: [Clear, honest answer]

Q: Can I keep using it?
A: No. After [date], it will no longer work.

Q: What should I use instead?
A: [Alternative with link]

Q: How long will migration take?
A: [Realistic estimate]

Q: Will you extend the deadline?
A: [Firm answer]

Q: What if I can't migrate in time?
A: [Options: support, workaround, or "feature will stop working"]

Q: Can I export my data?
A: [Yes/no and how]

</deprecation_plan>
```

</details>

---

### Influence Without Authority


**📋 Use Case:** Get things done when you don't have direct control

**🛠️ Recommended Tools:** Claude, ChatGPT Projects

**💡 Technique:** Persuasion framing, stakeholder mapping, alignment tactics

<details>
<summary>Click to view prompt</summary>

```
<influence_without_authority>

<influence_inputs>
WHAT YOU NEED:
[Specific outcome you're trying to drive]

WHO NEEDS TO ACT:
[Person/team you need help from]

WHAT THEY CONTROL:
[Resources, decisions, effort they own]

YOUR RELATIONSHIP:
- Reporting structure: [Peer, different org, etc.]
- History: [Have you worked together before?]
- Current dynamic: [Good/neutral/strained]

THEIR PRIORITIES:
[What they care about, if you know]

YOUR LEVERAGE:
[What you can offer or bring to the table]
</influence_inputs>

<influence_framework>

You get people to act when you have no formal authority over them. Your process:

STEP 1: Map the influence landscapeWho's the real decision maker?Don't assume title = power.Look for:
- Who actually has resources/headcount?
- Who does the senior leader ask for advice?
- Who controls the process/timeline?
- Who has veto power?

Map stakeholders:
- Primary: Who must say yes
- Secondary: Who influences primary
- Blockers: Who could derail it
- Supporters: Who's already on your side

STEP 2: Understand their motivationsWhat do they care about?Common motivations:
- Career advancement (visibility, promotions)
- Team success (OKRs, metrics, headcount)
- Ease/efficiency (less work, fewer meetings)
- Innovation/impact (building cool things)
- Relationships (looking good to their boss)
- Risk avoidance (not getting blamed)

For each stakeholder, identify:
- What's their win?
- What's their fear?
- What's their constraint?

STEP 3: Frame in their termsStop saying: "I need you to..."
Start saying: "Here's how this helps you..."

Translation examples:Your goal: Get eng to build feature faster
Their goal: Hit sprint commitments, manage tech debt
Your frame: "This unblocks [eng priority] and helps us validate [tech approach]"

Your goal: Get marketing to prioritize your launch
Their goal: Hit lead gen targets
Your frame: "This campaign should drive [X] MQLs based on similar launches"

Your goal: Get design resources
Their goal: Avoid rework, showcase portfolio pieces
Your frame: "This lets us nail the UX from the start. Could be a great portfolio piece."

STEP 4: Build reciprocityInfluence is a bank account.Deposits:
- Make them look good to their boss
- Make their job easier
- Give them credit publicly
- Help them hit their OKRs
- Share information they need
- Be low-maintenance

Withdrawals:
- Ask for urgent help
- Change requirements mid-flight
- Create extra work
- Make them miss their goals

Before you ask for something big, make deposits.STEP 5: Choose your influence tacticDifferent situations need different approaches:TACTIC 1: Logic & Data
Best for: Analytical stakeholders, technical decisions

"Here's the data that shows [your case]"

TACTIC 2: Coalition Building
Best for: Big organizational shifts, contentious decisions

"[Name], [Name], and [Name] are all on board"

TACTIC 3: Pilot/Experiment
Best for: Risk-averse stakeholders, uncertain outcomes

"Let's try it with one team and measure results"

TACTIC 4: Escalation (nuclear option)
Best for: Deadlocked situations, last resort

"I'm going to [mutual boss] to decide"

TACTIC 5: Make It Easy
Best for: Busy stakeholders, low-priority requests

"I've done 90% of the work, just need [small thing]"

TACTIC 6: Social Proof
Best for: Competitive teams, trendy initiatives

"[Competitor/Industry leader] is doing this"

STEP 6: Structure your askThe influence pitch:1. Context (30 seconds)
"Here's what's happening and why it matters"

2. The ask (15 seconds)
"Specifically, I need [concrete request]"

3. What's in it for them (30 seconds)
"Here's how this helps you achieve [their goal]"

4. Make it easy (15 seconds)
"I've already [done prep work], you just need to [small step]"

5. Timeline (15 seconds)
"Can we decide by [date]? If yes, here's what happens next."

STEP 7: Handle objectionsCommon objections and responses:"We don't have capacity"
→ "What if I [reduce scope / push timeline / find resources]?"

"That's not a priority for us"
→ "I understand. What would make it a priority?" (Then tie to that)

"We tried that before and it didn't work"
→ "Tell me what happened. Here's what's different now: [X]"

"I need approval from [person]"
→ "Want me to draft the proposal for them? Or should we meet with them together?"

"It's too risky"
→ "Agreed. What if we [de-risk strategy]?"

STEP 8: Build ongoing relationshipsInfluence is long-term.Relationship maintenance:
- Regular 1:1s (even informal coffee chats)
- Share credit loudly
- Help them win, even when you don't benefit
- Keep them informed (no surprises)
- Ask for their input early
- Celebrate their successes

Be the PM other teams WANT to work with.

Now create an influence strategy for the described situation.

</influence_framework>

---

## Example Influence Strategies

(Adapt based on stakeholder and situation)

---

### Strategy 1: Getting Engineering Resources

Situation: Need eng team to prioritize your feature over their roadmap

Stakeholder: Engineering Manager (peer)

Their motivation:
- Hit sprint commitments
- Keep team happy (not overloaded)
- Deliver on tech debt promises

Your approach:1. Make it strategically aligned:
"This feature directly impacts [company OKR] which affects [eng leader's] goals"

2. Reduce scope to be practical:
"What if we build the MVP first - [X days] instead of [Y days]"

3. Offer to help:
"I'll write the specs, do the user testing, and handle the launch. You focus on building."

4. Create urgency (if legit):
"[Customer] needs this by [date] for [their important thing]. If we miss it, we risk [business impact]."

5. Make them the hero:
"When this works, I'm going to highlight your team's execution in the exec meeting."

The ask (in meeting):

"Hey [Name], quick question. We have an opportunity to [business outcome] but it requires [specific eng work]. I know you're slammed, so I did some thinking:

What if we:
- Scope it to just [MVP version] → [X days instead of Y]
- Schedule it for [sprint window that works for them]
- I handle all the PM work around it

This helps us hit [your OKR] AND [their OKR]. Plus it could be a great [technical win they care about].

Would that work? If not, what would make it feasible?"

---

### Strategy 2: Influencing Up (Getting Executive Approval)

Situation: Need executive to approve budget/headcount/strategy

Stakeholder: VP or C-level (your skip-level or higher)

Their motivation:
- Company-level results
- Board perception
- Resource efficiency
- Strategic wins

Your approach:1. Lead with business impact:
Subject: [Specific $ or metric outcome] Opportunity

"TL;DR: We can drive [$X revenue / Y% increase in metric] by [action]. Needs [resource] by [date]."

2. Show you've done the work:
"I've validated this with [data sources], pressure-tested with [stakeholders], and have [team] ready to execute."

3. Present trade-offs clearly:
"We can do this OR [alternative]. Here's the comparison:
- [This approach]: [pros/cons]
- [Alternative]: [pros/cons]
My recommendation: [X] because [strategic reason]"

4. Make the ask easy:
"I need a yes/no by [date]. If yes, here's the 30/60/90 day plan."

The pitch (in meeting):

"I'd like 15 minutes to walk you through an opportunity I think we should pursue.

Context: [What's happening in market/business]

Opportunity: We can [outcome] if we [action]

Why this matters:
- [Metric impact]
- [Strategic alignment]
- [Competitive advantage]

What I need: [Specific ask]

Trade-off: We're choosing this over [alternative] because [reason]

What happens next: [Clear plan]

My ask: Decision by [date]

Questions?"

---

### Strategy 3: Cross-Functional Alignment

Situation: Need Sales, Marketing, and CS aligned on launch

Stakeholders: Multiple team leaders (peers)

Their motivations:
- Sales: Hit quota, avoid customer complaints
- Marketing: Lead gen, campaign success
- CS: Not overwhelmed with support, happy customers

Your approach:1. Find the shared goal:
"We all want [successful launch that hits revenue goals without overwhelming CS]"

2. Show you've thought about their concerns:

To Sales: "I've built enablement so reps can demo in [X] minutes"
To Marketing: "Here's the campaign brief with assets you need"
To CS: "We're launching to [limited segment] first to manage support load"

3. Make it collaborative:
"I need your input on [specific decisions]. What am I missing?"

4. Build coalition:
Get sales leader on board first → use that to convince marketing → create momentum

The alignment meeting:

"Thanks for making time. I want to align on [launch] so we hit our goals without chaos.

Shared goal: [Revenue/adoption target]

Launch plan: [One-pager with timeline]

What I need from each team:
- Sales: [Specific asks]
- Marketing: [Specific asks]
- CS: [Specific asks]

What I'm providing:
- [Enablement materials]
- [Support resources]
- [Weekly sync meetings]

Concerns I've heard:
- [Concern A]: Here's how we're addressing: [Solution]
- [Concern B]: Here's mitigation: [Plan]

Open questions:
- [Question for sales]
- [Question for marketing]
- [Question for CS]

Let's go through these and make sure we're set up to win."

---

### Strategy 4: Influencing a Blocker

Situation: Someone is blocking your project

Stakeholder: Legal, Security, Another PM (has veto power)

Their motivation:
- Risk avoidance
- Protecting their domain
- Not looking bad

Your approach:1. Understand the real objection:
Schedule 1:1: "Help me understand your concerns"
Listen for: Real risk vs. politics vs. NIH syndrome

2. Collaborate on solution:
"Let's solve this together. What if we [address concern]?"

3. Bring them into the process:
"Can you review this approach? I want to make sure we're handling [their concern] properly."

4. Give them credit:
"[Blocker's name] helped us think through [concern] so we could move forward safely."

5. If still blocked, escalate thoughtfully:
"I'd like to get [mutual boss] to help us decide between [your approach] and [their concern]."

The conversation:

"Hey [Name], I know you have concerns about [project]. I'd love to understand them better so we can address them.

Walk me through what worries you about this?"

[Listen actively]

"That makes sense. Let me think out loud about how we could handle that:
- [Option A]: [How it addresses concern]
- [Option B]: [Alternative]

What would make you comfortable moving forward?"

[Collaborate on solution]

"Awesome. Can I document this and share it back with you? And I'd love to credit you in the project plan for helping us think through [concern]."

---

### Key Principles Across All Influence Situations

1. Do your homework
Know their goals, constraints, and fears

2. Frame in their terms
What's their win?

3. Make it easy
Reduce friction, do the work

4. Build relationships before you need them
Deposits before withdrawals

5. Show, don't tell
Data, examples, proof

6. Create coalitions
"[Other stakeholders] are already on board"

7. Offer options
Never "my way or nothing"

8. Be low-maintenance
Don't create extra work

9. Share credit
Make them look good

10. Play long game
You'll work together again

</influence_without_authority>
```

</details>

---


## GTM

*7 prompts in this category*

### Create Sales Battlecard


**📋 Use Case:** Sales needs competitive positioning and objection handling

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Competitive differentiation, objection pre-emption, value messaging

<details>
<summary>Click to view prompt</summary>

```
<sales_battlecard>

<battlecard_inputs>
YOUR PRODUCT:
[What you sell and core value prop]

COMPETITOR:
[Which competitor this is for]

YOUR RESEARCH:
- Competitor's strengths: [What they do well]
- Competitor's weaknesses: [Where they fall short]
- How customers compare you: [What you hear in sales calls]
- Win/loss data: [When you win vs lose against them]

COMMON OBJECTIONS:
[What prospects say when considering competitor]

YOUR DIFFERENTIATORS:
[What makes you better/different]
</battlecard_inputs>

<battlecard_framework>

You create battlecards that help sales win competitive deals. Your job: arm sales with positioning, not just feature comparisons.

---

## SALES BATTLECARD

Competitor: [Name]
Last updated: [Date]

---

### Quick Reference

When to use this:
[Buying scenario where this competitor comes up]

Their position: [How they market themselves]
Your position: [How you differentiate]

Win themes:
[Top 3 reasons you beat them]
1. [Theme with proof point]
2. [Theme with proof point]
3. [Theme with proof point]

---

### Competitive Overview

Who they are:
[Brief description]

Their ideal customer:
[Who they're best for]

What they're good at:
[Honest assessment of strengths]

Where they struggle:
[Weaknesses you can exploit]

---

### Head-to-Head Comparison

| Factor | Us | Them | Talk Track |
|--------|----|----|------------|
| [Key differentiator] | ✅ [Our strength] | ❌ [Their gap] | [What to say] |
| [Another factor] | [Status] | [Status] | [What to say] |

---

### Messaging & Positioning

If they say: "We're considering [Competitor]"

You say: "Great, they're a solid choice for [use case]. The main difference customers tell us: we're [differentiation], while they're [positioning]. For [your ICP], that means [benefit]."

Example:
"Great, Competitor X is solid for basic analytics. The difference: we're built for real-time decision-making, while they're batch processing. For ops teams that need to react in minutes not hours, that's critical."

---

### Objection Handling

OBJECTION: "Competitor is cheaper"

Response:
"You're right, they're less expensive upfront. What we've found: customers save more long-term because [reason]. [Customer name] switched from them and saved $X by [specific benefit]."

Evidence: [ROI data or case study]

---

OBJECTION: "Competitor has feature X"

Response:
"They do have that feature. The trade-off customers mention: [downside of their approach]. We built [your approach] instead because [reason]. For [your ICP], that means [benefit]."

---

OBJECTION: "Competitor has been around longer"

Response:
"True, they've got tenure. What we hear from customers who switched: they're built on older technology. We started fresh with [modern approach], which means [specific advantage]."

---

### Trap Questions (Ask These)

Questions that expose their weaknesses:

Question 1: "How does [their product] handle [edge case they struggle with]?"
- Why this works: [Exposes gap]
- Follow-up: [How you handle it better]

Question 2: "What happens when [scenario where they fail]?"
- Why this works: [Reveals limitation]
- Follow-up: [Your advantage]

Question 3: "Can you [thing they can't do]?"
- Why this works: [Shows missing capability]
- Follow-up: [How you solve it]

---

### Proof Points

Customer wins:
- "[Customer name] switched from them and [result]"
- "[Customer name] chose us over them for [reason]"

Data points:
- [X]% faster than them at [task]
- [Y]% of their customers mention [pain point]
- [Z]% of evaluators choose us when [criteria]

Reviews/validation:
- G2 rating: [Yours vs theirs]
- Analyst positioning: [How you compare]
- Customer quotes: "[Quote comparing you]"

---

### When You'll Lose to Them

Be honest about when they're better choice:They win if customer:
- [Scenario where they're better fit]
- [Another scenario]

If that's the case:
- [How to reframe] or
- [Gracefully walk away - not every deal is worth chasing]

---

### Discovery Questions

Ask these to position yourself:

1. "What's most important: [your strength] or [their strength]?"
- If your strength: You're well-positioned
- If their strength: You'll need different angle

2. "How quickly do you need [thing they're slow at]?"
- Reveals if your speed advantage matters

3. "Who on your team will use this daily?"
- Helps identify if your UX advantage matters

---

### Resources

Case studies: [Link to customers who switched from them]
Product comparison: [Link to detailed comparison]
Demo script: [Link to demo that highlights differentiation]
ROI calculator: [Link to tool showing cost comparison]

---

### Red Flags

Signs you might lose:

- [ ] They've already deployed competitor (switching cost high)
- [ ] Buying criteria favor their strengths
- [ ] Budget-driven decision (not value-driven)
- [ ] Existing relationship with their parent company

If you see these:
[Strategy to overcome or decision to walk]

</battlecard_framework>

<meta_guidance>

Battlecard principles:Be honest
Don't trash competitors
Acknowledge what they do well
Makes you credible

Focus on fit, not features
"Better for X, worse for Y"
Not "we're better at everything"

Arm sales, don't overwhelm
One page ideal
Quick reference, not encyclopedia

Update regularly
Competitors change
Monthly review minimum

Include proof
Don't just claim superiority
Show evidence (customers, data, reviews)

Practice objection handling
Sales should rehearse responses
Not read them for first time in meeting

Remember:
Best battlecard helps sales disqualify bad-fit prospects
Not every deal is winnable
Knowing when to walk is valuable

</meta_guidance>

</sales_battlecard>
```

</details>

---

### Cold Outreach Email

**📋 Use Case:** Need to reach out to potential customer, partner, or user for research/feedback

**🛠️ Recommended Tools:** Claude, ChatGPT Projects

**💡 Technique:** Value-first messaging, personalization at scale, clear CTA

<details>
<summary>Click to view prompt</summary>

```
<cold_outreach>

<outreach_inputs>
WHO YOU'RE REACHING OUT TO:
- Type: [ ] Potential customer [ ] Research participant [ ] Partner [ ] Influencer [ ] Other
- What you know about them: [Role, company, relevant context]
- How you found them: [Referral, LinkedIn, product usage, etc.]

YOUR ASK:
- [ ] Schedule a call
- [ ] Get feedback
- [ ] Demo product
- [ ] Partnership discussion
- [ ] Join beta/pilot
- [ ] Other: [specify]

YOUR CONTEXT:
- Why them specifically: [What makes them relevant]
- What you offer in return: [Value for them]
- Timeline: [How urgent]
</outreach_inputs>

<outreach_framework>

You write cold emails that get responses. Your job: be brief, relevant, and valuable—not salesy.

THE FORMULA:Subject Line (Make them open)
- Personal + Specific
- Curiosity without clickbait
- Under 50 characters

Line 1 (Why you're reaching out to THEM specifically)
- Show you did homework
- Relevant observation
- Genuine compliment (not generic)

Lines 2-3 (What's in it for them)
- Value you provide
- What they get, not what you want
- Make it concrete

Line 4 (The ask)
- Single, clear CTA
- Low friction
- Specific time/format

Line 5 (Make it easy to say yes)
- Remove barriers
- Offer optionality
- Graceful exit

---

## YOUR EMAIL

Subject: [Compelling, specific, personal]

Hi [Name],

[Opening line showing you know who they are and why you're reaching out to them specifically]

[What's in it for them - value proposition in 1-2 sentences]

[The ask - clear and low-friction]

[Make it easy - remove objections, offer flexibility]

[Your name]
[Title/Context]

---

## ALTERNATIVE VERSIONS

Shorter (3 sentences):
[Ultra-brief version]

With social proof:
[Version mentioning relevant customer/mutual connection]

Research angle:
[Version positioning as learning, not selling]

</outreach_framework>

<outreach_patterns>

### Pattern 1: Customer Research

Subject: Quick question about [their workflow/pain point]

Hi [Name],

Saw you're leading [team] at [company]. We're talking to [role] leaders about how they handle [specific challenge].

Would you have 20 minutes to share what's working (or not) for your team? Not selling anything—genuinely trying to understand the problem before we build.

[Calendar link] or just reply with a better time.

Thanks,
[You]

---

### Pattern 2: Beta/Pilot Invitation

Subject: Early access to [product] for [their company]

Hi [Name],

[Mutual connection] mentioned you're dealing with [pain point]. We just built [solution] and looking for 10 companies to pilot it.

What you get: Free access for 3 months + we'll customize it for your workflow. We get feedback.

Interested? Here's a 2-min demo: [link]

No pressure—happy to explain more if timing's not right.

[You]

---

### Pattern 3: Partnership Discussion

Subject: [Your company] + [Their company]?

Hi [Name],

We both serve [audience]. You're great at [their strength], we're focused on [your strength].

Quick idea: [Specific partnership concept, e.g., integration, co-marketing, referral]. Seems like a win-win for [shared customer].

Worth 15 minutes to explore? [Calendar link]

[You]

---

### Pattern 4: Product Demo (Warm Lead)

Subject: [Feature] for [Their Company]

Hi [Name],

Noticed you've been [signal of interest—e.g., checking our pricing page, reading blog].

[Customer in their industry] is using [product] for [use case]. Seems similar to what [their company] does.

Want to see it in action? 15-min demo: [calendar link]

Or I can send you a sandbox to try yourself—just let me know.

[You]

---

### Pattern 5: Re-engage Dormant User

Subject: Miss you!

Hi [Name],

You signed up [X months] ago but haven't been active lately.

Curious: Was it [potential reason 1] or [potential reason 2]? We've shipped [new feature] that might change things.

Worth another look? Or should I stop bothering you? (Totally fine either way!)

[You]

</outreach_patterns>

<meta_guidance>

Cold email principles:Shorter is better
5 sentences max
If you can't fit value prop in subject line + 3 sentences, it's not clear

Personalization beats templates
One detail about them > generic spray-and-pray
"I saw you posted about X" works

Lead with value
Not "I want to tell you about..."
But "You might want to know about..."

Single CTA
Don't give 5 options
One clear next step

Remove friction
Calendar link > "let me know times"
Specific ask > vague "let's chat"

Give them an out
"No worries if not" makes them more likely to respond

Follow up (but not annoyingly)
Day 1: Send
Day 4: Bump (if no response)
Day 8: Final follow-up
Then stop

Remember:
Your email is interrupting their day.
Make it worth their time.

80% of cold emails are terrible because they're about YOU.
Good cold emails are about THEM.

</meta_guidance>

</cold_outreach>
```

</details>

---

### Write Blog Post

**📋 Use Case:** Need to write thought leadership, product launch, or educational content

**🛠️ Recommended Tools:**  Claude Projects, ChatGPT Projects

**💡 Technique:** SEO-aware structure, narrative arc, audience engagement

<details>
<summary>Click to view prompt</summary>

```
<blog_post_writer>

<post_inputs>
TOPIC:
[What you're writing about]

PURPOSE:
- [ ] Announce product/feature
- [ ] Thought leadership/opinion
- [ ] Educational/how-to
- [ ] Company update
- [ ] Customer story

AUDIENCE:
- Who's reading: [Customers, prospects, industry, general]
- What they care about: [Their interests/pain points]
- Technical level: [Non-technical, somewhat technical, very technical]

YOUR ANGLE:
- What's your unique take: [Your POV or insight]
- Why should they care: [Hook/relevance]

TARGET LENGTH:
- [ ] Short (500-800 words)
- [ ] Medium (800-1500 words)
- [ ] Long (1500-3000 words)

SEO KEYWORDS (optional):
[Terms you want to rank for]
</post_inputs>

<post_framework>

You write blog posts that people actually read. Your job: hook them, teach them something, leave them satisfied.

THE STRUCTURE:HEADLINE (Make them click)
- Promise specific benefit
- Use numbers or "how to"
- Under 60 characters for SEO

INTRO (Hook in 3 sentences)
- Sentence 1: Relatable problem or surprising fact
- Sentence 2: Why this matters now
- Sentence 3: What they'll learn

BODY (Deliver on promise)
- Break into scannable sections
- Use subheadings every 2-3 paragraphs
- Examples, not just theory
- Actionable takeaways

CONCLUSION (Stick the landing)
- Recap key points
- Clear next step
- Call to action (if appropriate)

---

## YOUR BLOG POST

Headline: [Compelling title with benefit]

Subheading (optional): [Clarify or expand on headline]

---

### [Opening hook]

[3-4 sentences that grab attention and set up the problem/topic]

### [First Main Point]

[Content with examples]

Key takeaway: [Actionable insight]

### [Second Main Point]

[Content with examples]

Key takeaway: [Actionable insight]

### [Third Main Point if needed]

[Content]

### Conclusion

[Tie it together, give them the "so what"]

What to do next:
[Clear CTA or next step]

---

## SEO OPTIMIZATION

Meta description (155 characters):
[Summary with keyword]

Suggested images:
- [Hero image concept]
- [Diagram/screenshot for section X]

Internal links:
- [Related post 1]
- [Related post 2]

</post_framework>

<post_templates>

### Template 1: Product Launch Post

Headline: Introducing [Feature]: [Benefit in 3-5 words]

Intro:
We heard you. [Pain point] has been your #1 request for [time period]. Today we're launching [feature] to make [outcome] possible.

Body:
- What it does: [Simple explanation]
- Why we built it: [Problem it solves]
- How it works: [Step-by-step with screenshots]
- Who it's for: [Use cases]
- What's next: [Future plans]

Conclusion:
Try it today. [Link]. We'd love your feedback.

---

### Template 2: How-To Post

Headline: How to [Achieve Outcome] in [Timeframe]

Intro:
[Pain point]. We've helped [X customers] do [outcome]. Here's exactly how.

Body:Step 1: [Action]
[What to do and why]

Step 2: [Action]
[What to do and why]

Step 3: [Action]
[What to do and why]

Common mistakes:
- [Mistake and how to avoid]

Conclusion:
[Summary checklist]
Start with [first step]. You'll see [result] within [timeframe].

---

### Template 3: Thought Leadership

Headline: [Contrarian Take] About [Topic]

Intro:
Everyone says [conventional wisdom]. They're wrong. Here's why.

Body:The problem with conventional thinking:
[What's broken about current approach]

What we learned:
[Your experience/data]

A better way:
[Your alternative approach with evidence]

What this means for you:
[Practical application]

Conclusion:
[Call to rethink + invitation to discuss]

---

### Template 4: Customer Story

Headline: How [Customer] [Achieved Result] with [Product]

Intro:
[Customer] had a problem: [specific challenge]. Here's how they solved it.

Body:The challenge:
[What wasn't working]

What they tried:
[Previous failed attempts]

The solution:
[How they used your product]

The results:
[Specific metrics and outcomes]

What they learned:
[Customer quote and advice]

Conclusion:
Want similar results? [CTA]

</post_templates>

<meta_guidance>

Blog post principles:Write like you talk
Conversational > formal
Short sentences > long ones
Active voice > passive

Show, don't tell
Examples > abstractions
Screenshots > descriptions
Data > claims

Make it scannable
- Subheadings every 2-3 paragraphs
- Bullet points for lists
- Bold key points
- White space is your friend

Hook early
First 3 sentences determine if they read more
Don't bury the lead

End strong
Recap + next step
Don't just trail off

SEO basics:
- Keyword in headline
- Keyword in first paragraph
- Use keyword naturally 3-5 times
- Alt text on images
- Meta description

Remember:
People skim before reading.
Make skimming satisfying.

If they only read subheadings, they should get the gist.

</meta_guidance>

</blog_post_writer>
```

</details>

---

### Create Social Media Posts

**📋 Use Case:** Need to announce feature, share content, or engage audience on social

**🛠️ Recommended Tools:**  Claude Projects, ChatGPT Projects

**💡 Technique:** Platform-specific formatting, hook optimization, CTA clarity

<details>
<summary>Click to view prompt</summary>

```
<social_media_posts>

<social_inputs>
WHAT YOU'RE POSTING ABOUT:
[Feature launch, blog post, milestone, thought, engagement]

PLATFORMS:
- [ ] LinkedIn (professional)
- [ ] Twitter/X (brief, punchy)
- [ ] Product Hunt (launch-focused)
- [ ] Company blog promo
- [ ] Other: [specify]

TONE:
- [ ] Professional/thoughtful
- [ ] Excited/celebratory
- [ ] Educational/helpful
- [ ] Casual/conversational

YOUR GOAL:
- [ ] Drive clicks/traffic
- [ ] Engagement/discussion
- [ ] Awareness/reach
- [ ] Conversions/signups

CONTEXT:
[Brief description of what you're promoting/discussing]
</social_inputs>

<social_framework>

You write social posts that stop the scroll. Your job: hook in first line, deliver value, make sharing easy.

PLATFORM RULES:LinkedIn:
- First 2 lines matter (preview)
- Longer form OK (1-3 paragraphs)
- Professional tone, but human
- Questions drive engagement

Twitter/X:
- First 8 words are the hook
- Thread for depth (1 idea per tweet)
- Visual > text only
- Hashtags sparingly (1-2 max)

Product Hunt:
- Clear value prop first line
- Feature bullets
- Social proof
- Direct CTA

---

## YOUR POSTS

### LinkedIn Post

[First line hook - shows up in preview]
[Rest of content - 2-3 short paragraphs]

[CTA or question for engagement]

---

### Twitter/X Post

[Tweet 1 - Hook]

[Tweet 2 - Expand if needed]

[Tweet 3 - Payoff/CTA]

---

### Short Version (All Platforms)

[One sentence hook + link]

</social_framework>

<social_patterns>

### Pattern 1: Feature Announcement

LinkedIn:
We just shipped something our customers have been asking for.

[Feature name] is now live. Here's what it does:
→ [Benefit 1]
→ [Benefit 2]
→ [Benefit 3]

Built because [customer story or pain point].

Try it: [link]

---

Twitter/X:
New: [Feature name] 🎉

Now you can [concrete action] in [timeframe/way].

[Customer/team] has been asking for this for months. It's here.

[Link]

---

### Pattern 2: Thought Leadership

LinkedIn:
Hot take: [Contrarian opinion]

Everyone's focused on [common approach]. But [your insight about what actually matters].

Here's what I've learned from [experience/data]:

[3 bullet points]

What am I missing? [Genuine question to drive comments]

---

Twitter/X:
Unpopular opinion: [Statement]

[Thread explaining why]

1/ [Setup the problem]

2/ [Your experience]

3/ [The insight]

4/ [What this means]

Disagree? Tell me why.

---

### Pattern 3: Educational/How-To

LinkedIn:
[Persona] often struggle with [problem].

Here's a simple framework I use:

1. [Step] - [Why it matters]
2. [Step] - [Why it matters]
3. [Step] - [Why it matters]

Learned this from [source/experience].

Full guide: [link]

---

Twitter/X:
A thread on [topic] everyone should know:

[1-2 sentence hook explaining why this matters]

👇

[Then thread with one insight per tweet]

---

### Pattern 4: Milestone/Celebration

LinkedIn:
Small milestone: [achievement] 🎉

What makes this meaningful: [why it matters beyond the number]

Thanks to [team/customers] who made this possible.

What's next: [future focus]

---

Twitter/X:
We hit [milestone]!

Thank you to everyone who [action - used, supported, built, etc.]

Next up: [what's coming]

[GIF or image]

---

### Pattern 5: Content Promotion

LinkedIn:
Wrote about [topic] after [recent experience/observation].

Key points:
- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]

Full post: [link]

Worth your time if you [target reader situation].

---

Twitter/X:
📝 New post: [Title]

TL;DR:
- [Point]
- [Point]
- [Point]

[Link]

</social_patterns>

<meta_guidance>

Social media principles:First line = everything
Hook in 8 words or lose them
Don't waste it on preamble

Visual > text
Image, GIF, or video outperforms text-only
Screenshots with annotations work well

Shorter > longer
Exception: LinkedIn stories
But even there, break into short paragraphs

One idea per post
Don't cram 5 things into one post
Multiple posts > one overwhelming post

CTA or question
End with clear action or invitation to engage
"What do you think?" drives comments

Timing matters
LinkedIn: Weekday mornings
Twitter: Throughout day
Test what works for your audience

Authenticity > polish
Typo-free important
But overly corporate = ignored

Remember:

Social is conversation, not broadcast.
Write like you're talking to one person, not a crowd.

Test, learn, iterate. Every audience is different.

</meta_guidance>

</social_media_posts>
```

</details>

---

### Landing Page Copy


**📋 Use Case:** Need copy for product page, feature page, or landing page

**🛠️ Recommended Tools:** Claude, ChatGPT Projects

**💡 Technique:** Benefit-driven copywriting, objection handling, conversion optimization

<details>
<summary>Click to view prompt</summary>

```
<landing_page_copy>

<page_inputs>
WHAT'S THE PAGE FOR:
- [ ] Product homepage
- [ ] Feature page
- [ ] Pricing page
- [ ] Landing page (ads, campaign)
- [ ] Signup/conversion page

TARGET AUDIENCE:
[Who's landing here and what they care about]

YOUR OFFER:
[What you're selling/promoting]

UNIQUE VALUE:
[Why choose you vs alternatives]

GOAL:
- [ ] Signups
- [ ] Demo requests
- [ ] Sales calls
- [ ] Downloads
- [ ] Awareness/education

OBJECTIONS TO HANDLE:
[Common hesitations or concerns]
</page_inputs>

<copy_framework>

You write landing page copy that converts. Your job: hook → explain → prove → convert.

THE STRUCTURE:Above the fold:
- Headline (value prop in 5-10 words)
- Subheadline (expand on benefit)
- Visual (product screenshot or hero image)
- Primary CTA (clear, action-oriented)

The Problem (Build tension):
- What pain exists today
- Cost of not solving

The Solution (Your product):
- How it works (simply)
- Key features as benefits
- Why it's different

Proof (Build trust):
- Social proof (logos, testimonials, stats)
- Case studies or results
- Trust signals (security, certifications)

How It Works (Reduce friction):
- 3-step process
- Show don't tell

Pricing (Be clear):
- Transparent pricing if possible
- Show value, not just cost

Final CTA (Convert):
- Repeat primary CTA
- Handle last objections
- Low-risk trial or guarantee

---

## YOUR LANDING PAGE COPY

### Hero Section

Headline:
[Value proposition - what outcome do you deliver?]

Subheadline:
[Expand - who is this for, what makes it unique?]

CTA Button: [Action-oriented text]

---

### The Problem

[Pain point headline]

[2-3 sentences about the current painful state]

Sound familiar?

---

### The Solution

[Product name]: [Benefit-driven description]

[How it works in simple terms]

Key Benefits:

✓ [Benefit 1]: [Specific outcome]
✓ [Benefit 2]: [Specific outcome]
✓ [Benefit 3]: [Specific outcome]

---

### Social Proof

Trusted by [number] [type of companies]

[Customer logos]

> "[Testimonial quote about specific result]"
> — [Name, Title, Company]

---

### How It Works

Get started in 3 steps:1. [Action]
[Brief description - make it sound easy]

2. [Action]
[Brief description]

3. [Action]
[Brief description - emphasize speed to value]

---

### Features → Benefits

[Feature name]
[What it is and why it matters to user]

[Feature name]
[Benefit-focused description]

---

### Objection Handling

"Is it secure?"
[How you handle security with specifics]

"Will it work for my team?"
[Who it's built for, flexibility]

"What if it doesn't work out?"
[Trial, guarantee, easy cancellation]

---

### Final CTA

Ready to [outcome]?

[CTA Button: Action text]

No credit card required • 14-day free trial • Cancel anytime

</copy_framework>

<copy_patterns>

### Pattern 1: Problem-Agitate-Solve

Headline: Stop [painful activity]. Start [desired outcome].

Problem:
You're spending [X hours/week] on [manual task]. Your team is frustrated. Results are inconsistent.

Agitate:
Meanwhile, your competitors are [moving faster/winning deals/scaling]. Every day you wait costs you [specific cost].

Solve:
[Product] automates [task], so you can [benefit]. [Social proof]. Get started in 5 minutes.

---

### Pattern 2: Before/After

Headline: From [Current State] to [Desired State] in [Timeframe]

Before: [Paint picture of current pain]
- [Pain point]
- [Pain point]
- [Pain point]

After: [Show transformed state]
- [Benefit]
- [Benefit]
- [Benefit]

How: [Product name] gives you [key capabilities]

---

### Pattern 3: The Promise

Headline: [Specific Outcome] Without [Common Objection]

Example: "Scale your sales without hiring 10 reps"

The Promise:
We help [target audience] achieve [outcome] without [typical cost/hassle].

How we deliver:
[3 key differentiators]

Proof:
[Customer results]

---

### Pattern 4: The Comparison

Headline: Like [Familiar Thing] but [Key Difference]

Example: "Like Salesforce but actually easy to use"

What you know:
[Familiar solution] works but [pain points]

What's different:
We took the best parts ([strengths]) and fixed what's broken ([innovations]).

Result:
[Customer testimonial showing the difference]

</copy_patterns>

<meta_guidance>

Landing page copy principles:Headline is 80% of success
5 seconds to hook them
Clear benefit > clever wordplay

Features tell, benefits sell
Not: "Real-time dashboard"
But: "Know what's working before your morning coffee"

Show don't tell
Screenshots > descriptions
Videos > screenshots
Demos > videos

Social proof everywhere
Logos above the fold
Testimonials throughout
Stats that prove value

Remove friction
"No credit card required"
"14-day free trial"
"Cancel anytime"

One clear CTA
Don't give 5 options
One primary action
Repeat it 2-3 times

Mobile-first
Most traffic is mobile
Headline must work on small screen

Remember:

People skim landing pages.
Make skimming get them 80% of the message.

Then the full read converts them.

</meta_guidance>

</landing_page_copy>
```

</details>

---

### Email Campaign

**📋 Use Case:** Need email sequence for feature adoption, onboarding, or nurture

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Sequence design, engagement triggers, conversion paths

<details>
<summary>Click to view prompt</summary>

```
<email_campaign>

<campaign_inputs>
CAMPAIGN TYPE:
- [ ] Onboarding (new users)
- [ ] Feature adoption (drive usage)
- [ ] Re-engagement (dormant users)
- [ ] Nurture (leads/trials)
- [ ] Announcement (all users)

AUDIENCE:
[Who's receiving this - segment, behavior, stage]

GOAL:
[What action you want them to take]

SEQUENCE:
- [ ] One-off email
- [ ] 3-email sequence
- [ ] 5-email sequence
- [ ] Ongoing drip

YOUR PRODUCT CONTEXT:
[Brief description of product/feature]
</campaign_inputs>

<campaign_framework>

You design email campaigns that drive action. Your job: guide users through a journey, not spam their inbox.

SEQUENCE STRUCTURE:Email 1: Welcome/Introduce
- What they signed up for
- Quick win / first value
- Clear next step

Email 2: Education
- How to get more value
- Common use cases
- Success stories

Email 3: Social proof
- How others use it
- Results/testimonials
- Address objections

Email 4: Urgency/Scarcity (if applicable)
- Time-limited offer
- What they're missing
- Easy action

Email 5: Last chance (if applicable)
- Final reminder
- Easy out (unsubscribe)
- Alternative path

TIMING:
- Day 1: Email 1
- Day 3: Email 2
- Day 7: Email 3
- Day 14: Email 4 (if no action)
- Day 21: Email 5 (if no action)

---

## YOUR EMAIL SEQUENCE

### Email 1: [Name/Purpose]

Subject: [Compelling subject line]

Preview text: [First line visible in inbox]

---

Hi [Name],

[Opening - acknowledge their action/situation]

[Main message - value or education in 2-3 short paragraphs]

[CTA - single clear action]

[Closing - set expectations for next communication]

[Signature]

---

### Email 2: [Name/Purpose]

[Same structure]

---

[Continue pattern for each email in sequence]

</campaign_framework>

<campaign_patterns>

### Pattern 1: Onboarding Sequence (New Users)

EMAIL 1 - Day 1: Welcome

Subject: Welcome to [Product]! Here's how to start

Hi [Name],

Thanks for signing up! You're now part of [X] teams using [Product] to [outcome].

Here's the fastest way to get value:

Step 1: [Action - link]
Step 2: [Action - link]
Step 3: [Action - link]

Most users see results within [timeframe]. Need help? Reply to this email—I'm here.

[Your name]

---

EMAIL 2 - Day 3: Quick Win

Subject: [Name], try this quick win

Hi [Name],

Quick question: Have you tried [specific feature] yet?

It's the fastest way to [benefit]. Here's how:

[1-2-3 steps with screenshots]

[Customer] used this and [specific result].

Try it now: [CTA button]

---

EMAIL 3 - Day 7: Value Expansion

Subject: Getting the most out of [Product]

Hi [Name],

You've been using [Product] for a week. Here are 3 ways to get even more value:

1. [Feature]: [Use case and benefit]
2. [Feature]: [Use case and benefit]
3. [Feature]: [Use case and benefit]

Which sounds most useful? Just reply and I'll send you a guide.

---

### Pattern 2: Feature Adoption (Existing Users)

EMAIL 1 - Announcement

Subject: New: [Feature] is here

Hi [Name],

You asked, we built it. [Feature] is now live.

What it does: [One sentence]

Why it matters for you: [Specific benefit for their use case]

How to use it: [Link to guide]

[CTA: Try it now]

---

EMAIL 2 - Education

Subject: 3 ways to use [Feature]

Hi [Name],

Saw you haven't tried [Feature] yet. Here are 3 ways teams are using it:

Use case 1: [Description + result]
Use case 2: [Description + result]
Use case 3: [Description + result]

Which fits your workflow? [CTA]

---

EMAIL 3 - Social Proof

Subject: How [Customer] uses [Feature]

Hi [Name],

[Customer], similar to your team, had [problem].

They used [Feature] to [solution]. Result: [specific metric].

> "[Testimonial]" — [Name, Title]

Want similar results? [CTA]

---

### Pattern 3: Re-engagement (Dormant Users)

EMAIL 1 - We Miss You

Subject: [Name], is everything OK?

Hi [Name],

Noticed you haven't logged in since [date]. Everything alright?

A lot has changed:
- [New feature]
- [Improvement]
- [New capability]

Worth another look? [CTA]

Or should I stop emailing? (Totally fine—just let me know)

---

EMAIL 2 - What Changed

Subject: What's new since you've been away

Hi [Name],

Quick update on what you've missed:

[3 bullets of biggest changes with links]

If something here sounds interesting, give it another try: [CTA]

Not interested? [Unsubscribe link - make it easy]

---

EMAIL 3 - Final Goodbye

Subject: Last email from me

Hi [Name],

This is my last email. Figured you've moved on and that's totally OK.

If I'm wrong and you want to give [Product] another shot, door's always open: [CTA]

Otherwise, thanks for giving us a try. Best of luck with [their goal].

[Signature]

---

### Pattern 4: Trial Nurture (Convert to Paid)

EMAIL 1 - Day 1: Welcome

[Same as onboarding]

---

EMAIL 2 - Day 5: Quick Value

Subject: Are you seeing results yet?

Hi [Name],

You're 5 days into your trial. Quick question: Are you seeing the value you expected?

Most successful trials follow this path:
- Week 1: [Milestone]
- Week 2: [Milestone]

You're on track if you've [specific action]. Need help? Reply here.

---

EMAIL 3 - Day 10: Social Proof

Subject: How [similar customer] uses [Product]

[Customer story with results]

You have 4 days left in trial. Ready to keep going? [CTA to upgrade]

---

EMAIL 4 - Day 12: Urgency

Subject: [Name], 2 days left in your trial

Hi [Name],

Your trial ends in 2 days. Don't lose:
- [Data/setup you'll lose]
- [Feature access]
- [Your work]

Continue with [plan]: [CTA]

Questions? Let's talk: [Calendar link]

---

EMAIL 5 - Day 14: Last Chance

Subject: Last call - trial ends today

Hi [Name],

Your trial ends at midnight. Two options:

1. Upgrade now: Keep everything [CTA]
2. Need more time? Reply and I'll extend you

Don't want to continue? No problem—we'll delete your data in 30 days.

</campaign_patterns>

<meta_guidance>

Email campaign principles:One email = one goal
Don't put 5 CTAs in one email
One clear action per email

Subject line > body
40% open rate difference between good/bad subject
Spend time on subjects

Preview text matters
First sentence shows in inbox
Make it count

Personal > corporate
From a person, not "Team@company"
Reply-able email address

Short > long
Ideal: 3-4 short paragraphs
Exception: Story-driven emails

Timing matters
Don't email daily (annoying)
Don't wait 2 weeks (forgotten)
3-7 day gaps work well

Unsubscribe is OK
Make it easy
Better than spam complaints

Test everything
Subject lines
Send times
CTAs
Copy

Remember:

Email is permission-based.
Don't abuse the privilege.

If you wouldn't want this email, don't send it.

</meta_guidance>

</email_campaign>
```

</details>

---

### Demo Script

**📋 Use Case:** Need structured script for product demo or sales presentation

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Discovery-first approach, value-oriented flow, objection anticipation

<details>
<summary>Click to view prompt</summary>

```
<demo_script>

<demo_inputs>
DEMO TYPE:
- [ ] First call (introductory)
- [ ] Deep dive (technical)
- [ ] Executive (high-level)
- [ ] Hands-on (let them drive)

AUDIENCE:
- Roles: [Who's attending]
- Industry: [Their vertical if relevant]
- Company size: [Impacts what you show]
- Known pain points: [What you learned in discovery]

YOUR PRODUCT:
[Brief description]

DEMO LENGTH:
- [ ] 15 minutes
- [ ] 30 minutes
- [ ] 60 minutes

GOAL:
- [ ] Next meeting
- [ ] Trial signup
- [ ] Close deal
- [ ] Technical validation
</demo_inputs>

<demo_framework>

You write demo scripts that sell outcomes, not features. Your job: show how the product solves THEIR problem, not catalog everything it does.

THE FLOW:1. Opening (2-3 min)
- Confirm agenda
- Recap their situation
- Set expectations

2. Discovery/Confirmation (5 min)
- Validate what you learned
- Uncover new info
- Get them talking

3. The Demo (Main chunk)
- Show value first
- Walk through their workflow
- Handle objections as they arise

4. Closing (5 min)
- Recap value
- Answer questions
- Clear next steps

---

## YOUR DEMO SCRIPT

### Pre-Demo Prep

Before the call, know:
- [ ] Their role and goals
- [ ] Pain points (from discovery or research)
- [ ] Decision criteria
- [ ] Timeline and urgency
- [ ] Who else is involved

Setup checklist:
- [ ] Demo environment ready
- [ ] Relevant data loaded
- [ ] Screen sharing tested
- [ ] Backup plan if tech fails

---

### Opening (First 3 minutes)

"Thanks for joining. Before I show you anything, I want to make sure I use your time well."Confirm agenda:
"Here's what I thought we'd cover today:
- Quick intro to [product]
- Walk through how it solves [their problem]
- Answer your questions
- Discuss next steps

Does that work? Anything else you want to see?"

Recap their situation:
"From our last conversation, sounds like you're dealing with [problem]. Did I get that right? Anything change since we talked?"

Set expectations:
"I'm going to show you [specific workflows], not every feature. If you want to see something specific, just interrupt me."

---

### Discovery Questions (Next 5 minutes)

Don't skip this. Even if you've talked before.

"Before I jump in, a few quick questions:"

Current state:
- "Walk me through how you handle [problem] today."
- "What's working? What's not?"
- "How much time does this take?"

Decision criteria:
- "What would make this a win for you?"
- "What would make you choose us vs [alternative]?"
- "Who else needs to sign off on this?"

Urgency:
- "What's driving the timeline?"
- "What happens if you don't solve this?"

[Take notes. Use their words in the demo.]

---

### The Demo (Main content)

Rule: Show outcomes, not features.Structure:Part 1: The "Wow" Moment (Show value fast)

"Let me show you the end result first, then I'll walk you through how it works."

[Show the outcome they want - dashboard, report, result]

"This is what [their goal] looks like when you're using [product]. Notice [specific thing that addresses their pain]."

[Pause for reaction. Let them respond.]

---

Part 2: Their Workflow

"Now let me show you how you'd actually use this. I'll walk through [their specific use case]."

Step 1: [Their process step]

[Show how product handles this]

"Today you're doing [their current method]. With us, you'd [easier way]. Saves you [time/effort]."

Step 2: [Next step]

[Continue pattern - always connecting to their workflow]

Step 3: [Outcome]

"And here's where you end up: [result they wanted]."

---

Part 3: Handle Objections ProactivelyAddress concerns before they ask:

"A question we often get: [common objection]"

"Here's how we handle that: [answer with demo]"

Common objections to address:
- Integration with their tech stack
- Learning curve / ease of use
- Scalability
- Security / compliance

---

Part 4: The Differentiator

"One thing that makes us different: [unique capability]"

[Show the feature competitors don't have]

"[Customer name] uses this for [use case]. They told us [specific result]."

---

### Handling Questions (Throughout)

When they ask questions:

"Great question. Let me show you."

[Demo the answer, don't just tell]

If you don't know:

"I don't know off the top of my head. Let me find out and get back to you by [specific time]."

[Write it down visibly so they see you captured it]

---

### Closing (Last 5 minutes)

Recap value:

"So to recap what you saw:
- [Benefit 1 in their words]
- [Benefit 2 in their words]
- [Benefit 3 in their words]"

Check understanding:

"Does this solve [the problem they mentioned]?"

[Wait for confirmation]

Address concerns:

"What questions do you have?"

[Answer thoroughly]

"Any concerns about moving forward?"

[Surface objections now, not later]

---

### Next Steps (Always get commitment)

If they're ready:

"Great. Next step: [specific action]"
- "I'll send trial access today"
- "Let's get contract over to you"
- "I'll schedule technical deep-dive"

If they need more:

"What do you need to see to move forward?"

[Get specific answer]

"OK, let's schedule [that thing] for [specific date]."

If it's not a fit:

"Sounds like [their situation] might be better served by [alternative]. Here's why..."

[Be honest. Don't waste their time or yours.]

---

### Follow-Up (Within 24 hours)

Email template:

Subject: [Their Company] demo - next steps

Hi [Name],

Thanks for your time today. Here's what we covered:
- [Key point 1]
- [Key point 2]

Next steps:
- [ ] [Action you're taking] - [By when]
- [ ] [Action they're taking] - [By when]

Questions from the call:
- [Question]: [Answer or "Getting answer by [date]"]

Resources:
- [Link to relevant case study]
- [Link to documentation]

Let's connect [specific day] to [next step].

[Your name]

</demo_framework>

<demo_patterns>

### Pattern 1: Executive Demo (High-level)

Focus: Business outcomes, not features
Length: 15-20 minutes max
Tone: Strategic

Script:

"I'll keep this high-level. Three things:

1. The problem: [Business impact of their pain]
2. The solution: [How you solve it]
3. The result: [ROI they can expect]

Then happy to dive deeper on anything."

[Show dashboard/summary view only]
[Use customer metrics and stories]
[No feature demos unless asked]

---

### Pattern 2: Technical Demo (Deep dive)

Focus: How it works, not why
Length: 45-60 minutes
Tone: Detailed

Script:

"I'll show you the full architecture and answer technical questions."

[Walk through:]
- Data flow
- Integration points
- Security model
- API capabilities
- Customization options

[Have technical docs ready]
[Screen share IDE or backend if needed]

---

### Pattern 3: Competitive Displacement

Focus: Why switch from competitor
Length: 30 minutes
Tone: Consultative

Script:

"You're using [Competitor]. Let me show you what's different."

[Head-to-head comparison:]
- "Here's how you do [task] with them..."
- "Here's how you'd do it with us..."
- "Notice: [specific advantage]"

[Use trap questions]
[Show migration path]
[Address switching costs]

</demo_patterns>

<meta_guidance>

Demo script principles:Discovery > Demo
Don't demo until you know their pain
5 minutes of discovery saves 20 minutes of irrelevant demo

Their workflow > feature tour
Show how it fits their day
Not every feature you have

Outcomes > features
"You'll save 10 hours/week"
Not "We have automation"

Questions = engagement
Pause and ask
"Does this make sense?"
"Is this what you expected?"

Silence is OK
Let them react
Don't fill every gap

Handle objections early
Don't let them fester
Address concerns as they arise

Always get next step
Never end with "I'll follow up"
Get specific commitment

Remember:

Best demos are conversations, not presentations.

If you're talking 90% of the time, you're doing it wrong.

</meta_guidance>

</demo_script>
```

</details>

---


## Career

*5 prompts in this category*

### Customize Resume to Job


**📋 Use Case:** Need to tailor your resume to specific job posting to get past ATS and recruiter screen

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Keyword optimization, relevance matching, impact highlighting

<details>
<summary>Click to view prompt</summary>

```
<customize_resume>

<resume_inputs>
PASTE YOUR CURRENT RESUME:
[Copy-paste your full resume]

PASTE THE JOB DESCRIPTION:
[Copy-paste the full job posting]

YOUR SITUATION:
- [ ] Perfect fit (just need to highlight right things)
- [ ] Mostly qualified (need to emphasize relevant experience)
- [ ] Stretch role (need to make connections clear)
- [ ] Career pivot (need to translate experience)

CONSTRAINTS:
- Keep it: [ ] 1 page [ ] 2 pages
- Don't lie or exaggerate
- Keep core facts the same
</resume_inputs>

<resume_framework>

You tailor resumes to get interviews. Your job: make their experience obviously relevant to this specific job.

THE REALITY:
- Recruiters spend 7 seconds on your resume
- ATS scans for keywords from job description
- They're looking for reasons to say no

YOUR GOAL:
Make it impossible to say no.

---

## TAILORED RESUME

### Analysis: Job Requirements vs Your Experience

What they want (from JD):Must-haves:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

Nice-to-haves:
- [Skill/experience]
- [Skill/experience]

Keywords they're scanning for:
[List 10-15 key terms from JD]

---

What you have:Strong matches: ✅
- [Your experience that directly matches]
- [Another strong match]

Partial matches: ⚠️
- [Experience that's related but not exact]
- [How to frame it]

Gaps: ❌
- [What they want that you don't have]
- [How to mitigate or ignore]

---

### Your Tailored Resume

[YOUR NAME]
[Contact info - keep same]

---

SUMMARY (Optional - use if career pivot or needs context)

[2-3 sentences that directly connect your background to this role]

Example:
"Product Manager with 5 years building B2B SaaS tools for [their industry]. Led cross-functional teams to ship [relevant outcome]. Experienced in [their tech stack/methodology]."

Your summary:
[Tailored to this job]

---

EXPERIENCE[Company Name] | [Your Title] | [Dates]

BEFORE (Generic):
- "Led product development for mobile app"
- "Worked with engineering team"
- "Increased user engagement"

AFTER (Tailored):[Rewritten to match their language and priorities]

- [Bullet highlighting most relevant achievement using THEIR keywords]
- [Bullet that speaks to their must-have requirement]
- [Bullet showing impact with metrics]
- [Bullet demonstrating skill they mentioned]

Formula for each bullet:
[Action verb] + [What you did] + [Impact with numbers] + [Keywords from JD]

---

[Previous Role]

[Same treatment - rewrite bullets to emphasize relevance]

---

SKILLSBEFORE (Kitchen sink):
Python, Java, SQL, Excel, Figma, Photoshop, Jira, Public speaking...

AFTER (Targeted):Technical: [List skills from JD that you have, in THEIR order of importance]
Tools: [Their specific tools/platforms mentioned]
Methodologies: [Their frameworks - Agile, Scrum, etc. if they mentioned]

---

EDUCATION
[Keep same unless relevant to emphasize]

---

### Specific Changes Made

Keywords added:
- Replaced "[your term]" with "[their term]" (e.g., "customer" → "client")
- Added "[keyword from JD]" to 3 bullets
- Emphasized "[their priority]" throughout

Achievements reframed:
- Highlighted [X] which matches their requirement for [Y]
- Moved [relevant experience] higher
- De-emphasized [less relevant stuff]

Gaps addressed:
- [How you handled missing requirement]
- [What you emphasized instead]

---

### Resume Checklist

✅ ATS-friendly:
- [ ] Includes exact keywords from JD (not synonyms)
- [ ] Simple formatting (no tables, text boxes, images)
- [ ] Standard section headers (Experience, Skills, Education)
- [ ] Saved as .docx or .pdf (check job posting preference)

✅ Recruiter-friendly:
- [ ] Relevant experience in top 1/3 of page
- [ ] Numbers/metrics in bullets
- [ ] No generic statements ("team player," "fast learner")
- [ ] Clear job titles and companies

✅ Honest:
- [ ] Didn't add skills you don't have
- [ ] Didn't inflate titles or dates
- [ ] Can back up every claim in interview

---

### Cover Letter Hook (Bonus)

First paragraph that connects your experience to their needs:

"I'm reaching out about the [Job Title] role. In my current role at [Company], I [specific achievement that matches their top requirement]. I noticed you're looking for someone to [their key challenge], which is exactly what I did when I [your relevant experience]."

</resume_framework>

<resume_patterns>

### Pattern 1: Direct Match (Lucky you)

Job wants: "5 years PM experience in B2B SaaS"
You have: Exactly that

Strategy:
- Lead with strongest matches
- Use their exact language
- Add metrics to prove impact
- Don't bury the lead

---

### Pattern 2: Translatable Experience

Job wants: "Product Manager"
You have: "Project Manager" or "Business Analyst"

Strategy:
- Emphasize product decisions you made
- Highlight cross-functional leadership
- Show user/customer focus
- De-emphasize execution-only work

Example transformation:
BEFORE: "Managed project timeline and resources"
AFTER: "Led product roadmap prioritization based on user research, working with engineering and design to ship features that increased engagement 30%"

---

### Pattern 3: Industry Pivot

Job wants: Healthcare experience
You have: Fintech experience

Strategy:
- Focus on transferable skills (PM skills, not domain)
- Emphasize similar problems (compliance, security, etc.)
- Show quick learning ability
- Research their space and reference it

Add to summary:
"While my experience is in fintech, I've successfully navigated [similar challenge they face], and am excited to apply [transferable skill] to healthcare."

---

### Pattern 4: Level Up

Job wants: Senior PM
You have: PM experience (but not "senior")

Strategy:
- Emphasize leadership and strategy
- Show scope of impact
- Highlight mentoring/influencing
- Frame achievements at higher level

Reframe bullets:
BEFORE: "Shipped feature X"
AFTER: "Defined product strategy for [area], leading team of 3 PMs to deliver [outcome]"

</resume_patterns>

<meta_guidance>

Resume tailoring principles:It's not lying, it's framing:
- Same facts, different emphasis
- Highlight what matters to them
- De-emphasize what doesn't

Use their language:
- They say "clients" → you say "clients" (not "customers")
- They say "Agile" → mention Agile (not just "iterative")
- They say "growth" → emphasize growth metrics

Metrics matter:
- "Increased engagement" = vague
- "Increased engagement 40% in 6 months" = concrete
- Even rough estimates better than nothing

Don't keyword stuff:
- Yes: Naturally work in relevant terms
- No: "Python Python Python experienced Python developer"

One resume per job:
- Generic resume gets generic results
- Takes 20 minutes to tailor
- 3x better response rate

Remember:
Goal is to get the interview.
Once you're in the room, your skills speak for themselves.

The resume just has to get you in the room.

</meta_guidance>

</customize_resume>
```

</details>

---

### Create Work Product for Job Application

**📋 Use Case:** Need to show your thinking for job application or take-home assignment

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Strategic analysis, clear communication, professional presentation

<details>
<summary>Click to view prompt</summary>

```
<pm_work_sample>

<sample_inputs>
WHAT'S THIS FOR:
- [ ] Job application (proactive)
- [ ] Take-home assignment (they requested)
- [ ] Portfolio piece
- [ ] Interview presentation

THE PROMPT (if they gave one):
[Paste their assignment/question]

OR choose your own:
- [ ] Product strategy for [their product]
- [ ] Feature analysis/recommendation
- [ ] Market opportunity assessment
- [ ] Competitive analysis
- [ ] Roadmap recommendation

YOUR EXPERIENCE TO DRAW FROM:
[Brief description of relevant projects you've worked on]

WHAT YOU KNOW ABOUT THEIR COMPANY:
[Product, market, recent news, challenges]
</sample_inputs>

<sample_framework>

You create work samples that show how you think. Your job: demonstrate PM skills in 2 pages of clear, actionable insights.

---

## WORK SAMPLE STRUCTURE

### The 2-Pager Formula

Page 1: The thinking
- Problem/Opportunity
- Analysis
- Recommendation

Page 2: The details
- How it works
- Why it matters
- Next steps

Goal: Show you can think strategically AND get into details

---

### TEMPLATE: PRODUCT STRATEGY

Title: [Product Strategy for X]

---

THE OPPORTUNITYCurrent state:
[What's true today - market, product, users]

The gap:
[What's missing or could be better]

Why now:
[Timing, urgency, market window]

Impact if we act:
[Quantify the opportunity - revenue, users, market share]

---

ANALYSISWhat I looked at:
- [Data source or research method 1]
- [Data source or research method 2]
- [Data source or research method 3]

Key insights:Insight 1: [Finding]
[Evidence supporting this]
→ Implication: [What this means for strategy]

Insight 2: [Finding]
[Evidence]
→ Implication: [Strategic meaning]

Insight 3: [Finding]
[Evidence]
→ Implication: [Strategic meaning]

---

RECOMMENDATIONI recommend: [Clear, specific strategy]Why this approach:
1. [Reason tied to insight]
2. [Another reason]
3. [Third reason]

Expected impact:
- [Metric 1]: [X → Y in Z timeframe]
- [Metric 2]: [Impact]
- [Metric 3]: [Impact]

---

HOW IT WORKS (Page 2)Phase 1: [Timeframe - e.g., Months 1-3]Focus: [What to build/do]

Key deliverables:
- [Specific output]
- [Specific output]

Success looks like:
[Metric or outcome]

---

Phase 2: [Timeframe]
[Same structure]

---

Phase 3: [Timeframe]
[Same structure]

---

RISKS & MITIGATIONSRisk 1: [What could go wrong]
- Likelihood: High/Med/Low
- Impact: High/Med/Low
- Mitigation: [How to address]

Risk 2: [Another risk + mitigation]

---

WHAT I'D NEED TO VALIDATEOpen questions:
1. [Question I'd answer through research]
2. [Question I'd validate with customers]
3. [Question I'd test with prototype]

How I'd validate:
[Brief description of research plan]

---

NEXT STEPSImmediate:
- [Action in week 1]

Short-term:
- [Action in month 1]

Long-term:
- [Action in quarter 1]

---

### TEMPLATE: FEATURE RECOMMENDATION

Title: [Feature] for [Product]

---

THE PROBLEMWho has this problem:
[Specific user segment]

What they're struggling with:
[Specific pain point, not generic]

How they solve it today:
[Current workaround or competitor solution]

Cost of not solving:
- For users: [Time, money, frustration]
- For business: [Churn, revenue, NPS]

---

THE SOLUTIONI recommend building: [Specific feature]How it works:
1. [User action]
2. [System response]
3. [Outcome]

Why users will love it:
- [Benefit 1 in user language]
- [Benefit 2]
- [Benefit 3]

Why this, not alternatives:
- Considered: [Alternative A] → Rejected because [reason]
- Considered: [Alternative B] → Rejected because [reason]
- This approach: [Why it's best]

---

SUPPORTING EVIDENCEUser research:
"[Quote from user interview]"
- [X] customers mentioned this pain in [timeframe]

Competitive landscape:
- [Competitor A]: Has this, but [weakness]
- [Competitor B]: Doesn't have this
- Gap: [Opportunity for differentiation]

Data:
- [Metric showing problem scope]
- [Usage data supporting need]

---

IMPLEMENTATION (Page 2)MVP Scope:
✅ Include:
- [Core functionality]
- [Must-have element]

❌ Exclude (future phases):
- [Nice-to-have]
- [Complex addition]

Technical considerations:
[Any obvious implementation notes, if you know them]

Estimated effort:
[If you know engineering velocity: Small/Medium/Large]
[If not: "Would estimate with eng team"]

---

SUCCESS METRICSPrimary metric:
[The one number that shows success]
- Current: [Baseline]
- Target: [Goal] by [timeframe]

Secondary metrics:
- [Supporting metric]
- [Another metric]

How we'll measure:
[Tracking plan]

---

ROLLOUT PLANPhase 1: Beta
- Who: [Small user group]
- Goal: Validate usage and quality
- Timeline: [2-4 weeks]

Phase 2: General availability
- Who: [All users]
- Support: [Documentation, onboarding needed]
- Timeline: [Date]

---

RISKS

[Same structure as strategy template]

</sample_framework>

<quality_checks>

### What Makes a Strong Work Sample

✅ Shows strategic thinking:
- Not just "add feature X"
- But "here's why it matters and what we'll learn"

✅ Demonstrates research:
- Cites specific sources
- References data or users
- Shows you did homework

✅ Makes clear recommendations:
- Not wishy-washy "could do A or B"
- Specific: "I recommend X because Y"

✅ Addresses trade-offs:
- Acknowledges alternatives
- Explains why you'd prioritize this

✅ Is skimmable:
- Clear headers
- Bullets over paragraphs
- Bold key points
- Visual (simple chart/diagram) if helpful

✅ Shows PM judgment:
- Prioritization
- User empathy
- Business sense
- Realistic about constraints

---

### What Makes a Weak Work Sample

❌ Too generic:
- Could apply to any product
- No specific insights about this company

❌ No evidence:
- Just opinions
- No data, research, or user input

❌ Feature list:
- Just describes what to build
- Doesn't explain why or how to prioritize

❌ Too long:
- More than 2-3 pages
- Buries the lead
- No clear structure

❌ Unrealistic:
- Ignores obvious constraints
- Suggests massive undertaking as "quick win"

</quality_checks>

<meta_guidance>

Real talk about work samples:Time investment:
- Take-home assignment: They expect 2-4 hours
- Proactive sample: Spend 3-5 hours max
- Diminishing returns after that

Use your real experience:
- Draw on projects you've actually done
- Reframe for their context
- Your real insights > generic frameworks

Show don't tell:
- Don't say "I'm strategic"
- Show strategic thinking in the work
- Let quality speak for itself

Less is more:
- 2 great pages > 5 mediocre pages
- Every sentence should add value
- Cut anything generic

Make it skimmable:
- Hiring manager has 10 minutes
- They'll skim before deep read
- Make skimming satisfying

The gut check questions:

1. Does this show how I think?
2. Is this specific to this company?
3. Would I be proud to discuss this in interview?
4. Does it demonstrate PM skills (not just analysis)?

Remember:

Work sample gets you to next round.
It doesn't have to be perfect.
It has to be good enough to make them want to talk to you.

Ship it and move on.

</meta_guidance>

</pm_work_sample>
```

</details>

---

### Draft Referral Request Email

**📋 Use Case:** Need referral for job but don't want to be awkward or pushy

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Relationship-appropriate tone, clear ask, low friction

<details>
<summary>Click to view prompt</summary>

```
<referral_email>

<referral_inputs>
WHO YOU'RE ASKING:
- Name: [Their name]
- Your relationship: [How you know them]
- [ ] Close friend/former colleague
- [ ] Acquaintance/met a few times
- [ ] LinkedIn connection only
- [ ] Cold reach (alumni, mutual connection)

THE JOB:
- Company: [Company name]
- Role: [Job title]
- Why you want it: [Brief reason]
- How you found it: [Job posting, their post, etc.]

WHAT YOU KNOW ABOUT THEM:
- Their role at company: [Current position]
- How long there: [Tenure]
- Your connection: [What you have in common]

YOUR CONSTRAINT:
- [ ] Need referral ASAP (deadline)
- [ ] Just exploring
- [ ] Already applied, need boost
</referral_inputs>

<email_framework>

You write referral requests that respect relationships and make it easy to say yes. Your job: clear ask, low friction, graceful out.

---

## REFERRAL EMAIL TEMPLATES

### Template 1: Former Colleague (Warm)

Subject: Quick favor - [Company] PM role

---

Hi [Name],

Hope you're doing well! Saw you're at [Company] now - congrats, seems like a great fit.

I'm looking at the [Role Title] position on your team and would love to throw my hat in the ring. I know you're busy, but would you be comfortable giving me a referral?

Quick context: [1-2 sentences about why you're interested and why you're qualified]

Happy to send my resume and any other info that would help. Totally understand if now's not a good time - no pressure either way!

Let me know,
[Your name]

---

### Template 2: Acquaintance (Need to Reconnect)

Subject: [Mutual connection/Context] - reaching out

---

Hi [Name],

Hope this isn't too out of the blue - we [met at X / worked together on Y / connected through Z]. I've been following your work at [Company] and impressed with [specific thing about their product or their work].

I'm exploring PM roles and saw an opening for [Role] at [Company]. Given your experience there, would you have 15 minutes to chat about the team and role? I'd also love to ask if you'd be open to referring me if it seems like a good fit.

No worries at all if you're swamped - I know these asks can be a lot.

Thanks for considering,
[Your name]

---

### Template 3: LinkedIn Connection (Weaker Tie)

Subject: [Company] PM role - asking for advice

---

Hi [Name],

We're connected on LinkedIn through [mutual connection / same school / same interest], and I've been following your journey at [Company].

I'm considering applying for the [Role] position and was hoping to get your perspective on the team and role before I apply. Would you have 15-20 minutes for a quick call?

If it seems like a good fit after we chat, I'd be grateful for any help with a referral - but totally understand if that's not possible.

Either way, would love to learn from your experience at [Company].

Best,
[Your name]

---

### Template 4: Cold Reach (Alumni/Shared Background)

Subject: Fellow [School/Background] alum - [Company] PM role

---

Hi [Name],

I'm reaching out as a fellow [School] alum (found you through [source]). I saw you're a PM at [Company] and wanted to reach out about the [Role] opening.

Quick background: [1-2 sentences about your experience and why you're interested in this specific role]

I know this is a cold email, but I'd really appreciate any insights into the team and role. If you think I'd be a good fit and you're comfortable with it, I'd be grateful for a referral.

Totally understand if you prefer not to - I know you don't know me. Either way, thanks for considering.

[Your name]

[LinkedIn profile link]
[Resume attached or link]

---

## EMAIL COMPONENTS

### The Subject Line

Good subjects:
- "Quick favor - [Company] PM role"
- "[Mutual connection] suggested I reach out"
- "Fellow [background] - exploring [Company]"

Bad subjects:
- "Help!" (vague)
- "Referral please" (demanding)
- "Opportunity at [Company]" (sounds like spam)

---

### The Opening

If you know them well:
"Hope you're doing well! [Personal touch about them or shared memory]"

If acquaintance:
"Hope this isn't too out of the blue - we [context of how you met]"

If cold:
"I'm reaching out as a [shared background] - found you through [source]"

---

### The Ask

Make it clear and low-friction:Good asks:
- "Would you be comfortable giving me a referral?"
- "Would you be open to referring me if you think I'd be a good fit?"
- "Could I get 15 minutes to learn about the role and potentially ask for a referral?"

Bad asks:
- "Can you help me get a job?" (too vague)
- "Will you refer me?" (too demanding)
- "Let me know ASAP" (too pushy)

---

### Why You're Qualified

Keep it to 1-2 sentences:Good:
"I'm a PM with 3 years at [company], focused on [relevant area]. I've shipped [relevant accomplishment] which seems aligned with this role."

Bad:
"I have 5 years experience doing various things..." (too vague)
[Full resume in email] (too much)

---

### The Graceful Out

Always include:
"Totally understand if now's not a good time - no pressure either way."
"No worries at all if you're swamped."
"Either way, appreciate you considering it."

Why this matters:
- Removes pressure
- Makes them more likely to help
- Maintains relationship if they say no

---

### Call-to-Action

If warm:
"Let me know if you need my resume or any other info!"

If cold:
"Happy to send my resume or set up a quick call - whatever works best for you."

Keep it open-ended, let them choose next step

---

## FOLLOW-UP STRATEGY

### If they say yes:

Immediate response:

"Thank you so much! Really appreciate it.

Here's my info:
- Resume: [attach or link]
- LinkedIn: [link]
- Job posting: [link]

Let me know if you need anything else. Thanks again!"

---

### If they say "let's chat first":

Response:

"Absolutely! Here are some times that work for me:
- [Option 1]
- [Option 2]
- [Option 3]

Or feel free to send a calendar link if that's easier."

---

### If they don't respond:

Wait 1 week, then:

"Hi [Name],

Just bumping this up in case it got buried. Totally understand if you're busy or prefer not to - no worries at all!

[Your name]"

One follow-up max. Then let it go.

---

### If they say no:

Response:

"Totally understand - thanks for considering it!

If you have any other advice about [Company] or the PM role there, I'd still love to hear it. But no pressure either way.

Thanks again,
[Your name]"

Maintain relationship, don't burn bridge

</email_framework>

<meta_guidance>

Real talk about referrals:Referrals work:
- 5-10x higher chance of interview
- Worth the awkwardness
- Most people want to help

Relationship matters:
- Close friend: Direct ask, informal
- Acquaintance: Coffee first, referral second
- Cold: Very low expectations, focus on learning

Make it easy for them:
- Clear subject line
- Brief email (<150 words)
- Specific ask
- All info ready (resume, link)
- Easy to say no

Don't:
- Send without context
- Ask multiple people at same company
- Be pushy about timeline
- Follow up more than once
- Take rejection personally

Timing:
- Ask before you apply (referral works better)
- Give them 2-3 days to respond
- One follow-up after 1 week
- Then move on

Remember:

Most people say yes.
But some will say no.
That's okay.

One good referral > ten perfect emails.

Send it and move on.

</meta_guidance>

</referral_email>
```

</details>

---

### Generate Interview Practice Questions

**📋 Use Case:** Interview coming up, need to practice likely questions based on your background

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:** Pattern matching, question prediction, answer frameworks

<details>
<summary>Click to view prompt</summary>

```
<interview_prep>

<prep_inputs>
PASTE YOUR RESUME:
[Copy-paste your resume]

PASTE THE JOB DESCRIPTION:
[Copy-paste the full JD]

WHAT YOU KNOW ABOUT INTERVIEW:
- Interview type: [ ] Phone screen [ ] Hiring manager [ ] Panel [ ] Final round
- Who's interviewing you: [Names/roles if you know]
- Interview focus: [ ] General fit [ ] Technical/execution [ ] Strategic [ ] Behavioral
- Duration: [Time length]
- Any other context: [Company stage, known priorities, etc.]

YOUR CONCERNS:
- [ ] Gap in resume to explain
- [ ] Career transition story
- [ ] Specific weak area (analytics, technical, etc.)
- [ ] Less experience than required
- [ ] Other: [What you're worried about]
</prep_inputs>

<prep_framework>

You generate practice questions they'll likely ask. Your job: realistic questions based on actual interview patterns, plus guidance on how to answer.

---

## YOUR INTERVIEW PREP

### Questions They'll Definitely Ask

These come up in 90%+ of PM interviews:

---

Q1: "Walk me through your background / Tell me about yourself"Why they ask:
Icebreaker, see how you tell your story

What they're evaluating:
- Can you be concise?
- Is there a narrative arc?
- Why PM, why now, why here?

Your answer structure:

"I'm a PM with [X years] focused on [area]. Currently at [Company] where I [key accomplishment].

Before that, I was at [Previous] where I [relevant experience].

I got into PM because [brief why PM story].

I'm excited about [Company] because [specific reason related to role]."

Keep it to 90 seconds max.Your draft:
[Write your 90-second version here]

---

Q2: "Why do you want to work here / Why are you interested in this role?"Why they ask:
Checking if you actually care or just spray-and-pray

What they're evaluating:
- Did you do homework?
- Genuine interest or just need a job?
- Understand what we do?

Bad answer:
"Great company, good culture, want to grow"

Good answer:
"Three reasons: [Specific thing about product], [Specific thing about market/mission], [Specific thing about role that aligns with your experience]"

Your draft:
[Write your specific answer]

---

Q3: "Tell me about a product you shipped"Why they ask:
Can you execute? Do you understand PM fundamentals?

What they're evaluating:
- Full lifecycle understanding
- Metrics-driven
- Cross-functional collaboration
- Problem-solving

Answer framework (STAR):Situation: [Context - what problem, why important]

Task: [What you needed to do]

Action: [What you actually did - be specific]
- Discovery: [How you validated problem]
- Execution: [How you prioritized, worked with eng/design]
- Measurement: [How you tracked success]

Result: [Outcome with metrics - X → Y, improved by Z%]

Your story:
[Pick your best product story and draft the STAR]

---

Q4: "Tell me about a time you had to say no"Why they ask:
Can you prioritize? Do you just say yes to everything?

What they're evaluating:
- Judgment
- Stakeholder management
- Data-driven decisions

Answer framework:Situation: [Stakeholder wanted X]

Why you said no: [Data, strategy, resources - the real reason]

How you communicated it: [What you actually said]

Alternative offered: [What you did instead, if anything]

Outcome: [What happened - did they understand? Did it work out?]

Your story:
[Draft your example]

---

### Questions Based on Your Resume

These are specific to your background:

---

Q5: About [Specific project from your resume]

"I see you [project]. Can you walk me through that?"

They want to know:
- What was your actual role (vs team's work)
- How you made decisions
- What you learned

Prepare:
- The problem you were solving
- How you approached it
- What you'd do differently now

---

Q6: About [Gap or transition in your resume]

"I notice you [gap / switched from X to Y / left Company after short time]. Can you tell me about that?"

They're checking:
- Any red flags?
- Valid reasons?
- What did you learn?

Your answer:
[Be honest, brief, forward-looking]

"[Honest reason]. What I learned: [Takeaway]. Since then, [What you've done]."

---

Q7: About [Skill they need that you might lack]

"This role requires [X]. I see you've done [related Y]. How would you approach [X]?"

They're testing:
- Self-awareness
- Learning agility
- Transferable skills

Your answer:
"I haven't done [X] specifically, but I have experience with [related Y]. Here's how I'd approach [X]: [Show your thinking]. I'm a fast learner - for example, [story of learning something quickly]."

---

### Questions Based on the Job

These are specific to what they need:

---

Q8: [Their main problem]

Based on JD, they're struggling with: [Problem]

Likely question:
"How would you approach [their problem]?"

or

"What's your experience with [their challenge]?"

Your answer structure:
1. Show you understand the problem
2. Share relevant experience
3. Outline how you'd approach it here

Your draft:
[Prepare your answer]

---

Q9: [Their product/strategy]

"What do you think of our product?"

or

"If you were CEO, what would you prioritize?"

They're checking:
- Did you use the product?
- Do you have product sense?
- Can you think strategically?

Your answer:
[Prepare 2-3 specific observations/suggestions]

---

Q10: [Their key metric]

"How would you improve [metric they care about]?"

Your answer:
- Clarify the baseline
- Hypothesize why it's at current level
- Suggest 2-3 approaches to test
- Explain how you'd prioritize

---

### Behavioral Questions (Most Common)

Q11: "Tell me about a time you failed"Framework:
- What happened (own it)
- What you learned
- What you do differently now

---

Q12: "Tell me about a conflict with a teammate"Framework:
- The disagreement (be specific)
- How you resolved it (show maturity)
- Outcome (focus on learning/growth)

---

Q13: "How do you prioritize?"Framework:
- Your framework (RICE, impact/effort, etc.)
- Example of using it
- Trade-offs you consider

---

Q14: "How do you work with engineers?"Framework:
- Your philosophy (respect, collaboration, not just task giver)
- Specific example
- What you've learned about what works

---

Q15: "Tell me about a time you influenced without authority"Framework:
- Context (why you had no authority)
- Your approach (data, storytelling, building coalition)
- Outcome

---

### Questions to Test Product Sense

Q16: "How would you improve [popular product]?"Framework:
1. Clarify: Who's the user? What goal?
2. Problem: What's broken or missing?
3. Solution: 2-3 options
4. Prioritize: Which and why
5. Measure: How you'd know it worked

---

Q17: "Design [product] for [user]"Framework:
1. Clarify constraints
2. User needs (what job to be done?)
3. Key features (prioritize 3)
4. How it works (simple flow)
5. Success metrics

---

Q18: "Should we build [feature]?"Framework:
1. Ask clarifying questions (who wants it, why, alternatives)
2. Framework (pros/cons, impact/effort)
3. Recommendation (yes/no with reasoning)
4. How to validate (experiment plan)

---

### Analytical/Technical Questions

Q19: "How would you measure success of [feature]?"Framework:
- North star metric
- Supporting metrics
- Guardrail metrics (what might go wrong)

---

Q20: "Estimate [market size / users / revenue]"Framework:
- Clarify question
- Break down (top-down or bottom-up)
- Show your math
- State assumptions
- Sanity check

---

Q21: "Diagnose why [metric] dropped"Framework:
1. Clarify (how much, when, which segment)
2. Hypotheses (5+ possible causes)
3. How to investigate (what data to check)
4. Prioritize hypotheses
5. Recommend solution

---

### Strategy Questions

Q22: "Where should [product] be in 3 years?"Framework:
- Market trends
- User needs evolution
- Competitive landscape
- Your vision (specific, ambitious, achievable)

---

Q23: "Should we enter [market / build new product]?"Framework:
- Size the opportunity
- Assess fit (why us, why now)
- Risks
- Recommendation

---

### Questions You Should Ask Them

About the role:
- "What does success look like in first 90 days?"
- "What's the biggest challenge this role will tackle?"
- "Why is this role open / what happened to last person?"

About the team:
- "How does PM team work with eng/design?"
- "How are decisions made?"
- "What's the team's biggest strength and biggest opportunity?"

About the company:
- "What keeps you up at night about the business?"
- "What's your biggest competitive threat?"
- "What would make this role obsolete in 2 years?"

---

### Questions Based on Your Specific Concerns

IF: Gap in resumeThey might ask:
"What have you been doing for the past [timeframe]?"

Your answer:
[Honest, brief reason + what you learned/did + why you're ready now]

---

IF: Career transition (not PM before)They might ask:
"Why transition to PM now?"

Your answer:
- What you loved about previous role that's PM-adjacent
- What you've done to learn PM (courses, side projects, books)
- Why this specific PM role is perfect entry point

---

IF: Less experience than requiredThey might ask:
"This role says [X years], you have [Y years]. Why should we consider you?"

Your answer:
- Quality of experience (accomplished more in less time)
- Relevant depth (you've done exactly what they need)
- Learning velocity (show you close gaps fast)

</prep_framework>

<meta_guidance>

Interview prep reality:You won't remember scripted answers:
- Don't memorize word-for-word
- Know your stories and frameworks
- Be conversational

Practice out loud:
- Record yourself
- Practice with friend
- Time yourself (most answers should be 2-3 minutes)

Have 5-6 solid stories:
- Product you shipped
- Conflict you resolved
- Time you failed
- Time you influenced
- Data-driven decision
- Customer insight

Use these stories across multiple questions:
Same story can answer "conflict," "influence," "data-driven," etc.

The 90-second rule:
Most answers should be 90 seconds to 2 minutes
Exception: Product deep-dives can go 3-5 minutes

Ask clarifying questions:
"That's a great question. Can I ask - are you more interested in [X] or [Y] aspect?"
Shows PM thinking, buys you time

Remember:

Interview is conversation, not interrogation.

They want you to succeed.
They're rooting for you.

If you get stuck, it's okay to say:
"Let me think about that for a second..."

Be human. Be honest. Show your thinking.

</meta_guidance>

</interview_prep>
```

</details>

---

### Review Interview Transcript

**📋 Use Case:** Just finished interview (or mock), need feedback on what you said

**🛠️ Recommended Tools:** Claude Projects, ChatGPT Projects

**💡 Technique:**  competency assessment, answer quality evaluation

<details>
<summary>Click to view prompt</summary>

```
<review_pm_interview>

<transcript_inputs>
PASTE WHAT HAPPENED:
[Interview transcript or your detailed notes of Q&A]

THE ROLE:
- Company: [Name]
- Stage: [ ] Early startup [ ] Growth [ ] Late stage/enterprise
- Product type: [B2B/B2C, what they build]
- What they're hiring for: [From JD - what problems PM will solve]

YOUR ANSWERS TO KEY QUESTIONS:
[Paste or describe your responses to their main questions]
</transcript_inputs>

<analysis_framework>

You're a PM interview coach analyzing performance. Follow this thinking process:

STEP 1: Identify what PM competency each question tested

For each question, determine:
- Product sense (understanding users, problems, solutions)
- Execution (shipping, working with eng, metrics)
- Strategy (vision, prioritization, market thinking)
- Leadership (influence, conflict, stakeholder management)
- Technical (understanding systems, APIs, tradeoffs)
- Analytical (metrics, data, estimation)

STEP 2: Evaluate answer quality against PM standards

For each answer, assess:
- Structure: Did they use a framework (STAR, CIRCLES, etc.)?
- Specificity: Concrete examples with names, numbers, dates?
- User focus: Did they talk about users or just features?
- Metrics: Did they quantify impact (X → Y, improved by Z%)?
- Tradeoffs: Did they acknowledge what you're NOT doing?
- Business connection: Linked to company goals/revenue?
- Realism: Understood constraints, didn't over-promise?

STEP 3: Check for PM failure modes

Common ways PMs fail interviews:
- Feature factory: Lists features, no strategy/why
- No metrics: Builds things, never measures success
- User-blind: Talks about technology, not problems
- Can't prioritize: Everything is P0, no tradeoffs
- Too vague: "Worked with stakeholders" (doing what?)
- Blame culture: "Eng was slow, design was bad"
- Lack of ownership: "Team did X" not "I did X"

Mark which failure modes appeared in this interview.

STEP 4: Grade core PM competencies

Score A/B/C/D on:
- Product sense (do they get users?)
- Strategic thinking (see big picture?)
- Execution ability (can they ship?)
- Communication (clear and structured?)
- Metrics fluency (data-driven?)
- Stakeholder management (influence?)

STEP 5: Identify the gap pattern

Is the main issue:
- Inexperience showing: Right thinking, no stories
- Wrong role fit: Not PM thinking (too IC or too high-level)
- Poor preparation: Good PM, bad interview skills
- Communication: Good work, can't articulate it
- Red flags: Concerning behaviors (blaming, defensive)

STEP 6: Build specific improvement plan

Based on gaps, prescribe:
- Which 5-6 stories to prepare (with STAR structure)
- Which PM frameworks to learn (RICE, Jobs-to-be-done, etc.)
- How to reframe weak answers
- Practice exercises (mock interviews, case studies)
- Knowledge gaps to fill (metrics, technical, strategy)

</analysis_framework>

---

## INTERVIEW PERFORMANCE REPORT

### Overall Assessment

Performance Grade: [A/B/C/D]One-line summary:
[Did they demonstrate PM competency? Pass/borderline/fail?]

Main strengths:
- [What they did well]
- [Another strength]

Main gaps:
- [Critical issue 1]
- [Critical issue 2]

Likely outcome: [Advance / Maybe / Probably not]

---

### PM Competency Scorecard

| Competency | Grade | Evidence |
|------------|-------|----------|
| Product Sense | [A/B/C/D] | [Why this grade] |
| Strategic Thinking | [A/B/C/D] | [Why] |
| Execution Ability | [A/B/C/D] | [Why] |
| Communication | [A/B/C/D] | [Why] |
| Metrics/Analytical | [A/B/C/D] | [Why] |
| Stakeholder Mgmt | [A/B/C/D] | [Why] |

Overall: [Pass/Borderline/Fail]

---

### Question-by-Question Analysis

Q1: "[The question]"Competency tested: [What this question was assessing]

Your answer summary:
[What you said in 2-3 sentences]

What worked:
✅ [Specific good thing - e.g., "Used STAR format"]
✅ [Another strength]

What didn't work:
❌ [Specific issue - e.g., "No metrics mentioned"]
❌ [Another problem]

PM failure modes present:
- [ ] Feature factory thinking
- [ ] No metrics
- [ ] User-blind
- [ ] Can't prioritize
- [ ] Too vague
- [ ] Blame culture

Score: [A/B/C/D]How a strong PM would answer this:

[Rewritten answer showing proper structure]

"Situation: [Context in 1 sentence]
Task: [What needed to happen]
Action: [What you did - specific steps]
- Talked to 10 customers, found [insight]
- Prioritized using [framework] because [reason]
- Worked with eng on [specific approach]
Result: [Metric] went from X → Y in Z timeframe, leading to [business impact]"

Why this is better:
- Specific metrics (X → Y)
- Shows PM process (discovery → decision → ship)
- User-focused
- Demonstrates judgment

---

[Repeat for each major question]

---

### Critical Patterns

STRENGTH PATTERN:
[What you consistently did well across answers]

Example: "You always included metrics and showed data-driven thinking. Every answer had concrete numbers."

---

WEAKNESS PATTERN:
[What you consistently struggled with]

Example: "You never mentioned users. Every answer was about features and technology, not problems being solved."

---

PM FAILURE MODES DETECTED:❌ Feature Factory Thinking:
- [Example from interview]
- Impact: Makes you seem tactical, not strategic

❌ No Metrics:
- [Example]
- Impact: Can't prove you create value

❌ [Other failure mode]:
- [Example]
- [Impact]

---

### Red Flags Raised

Concerns interviewer may have:

🚩 [Concern 1]:
- What triggered it: [Specific moment]
- Why it's a problem: [Perception created]
- How to address: [What to do differently]

🚩 [Concern 2]:
[Same structure]

---

### Strongest Moments

Best answers:1. [Question]
- Why it was strong: [Specific, structured, showed PM skills]
- What made it work: [Framework used, metrics included, etc.]

2. [Question]
- Why: [Clear thinking, good judgment, etc.]

Use these as your template.

---

### Weakest Moments

Answers that hurt you:1. [Question]
- Why it was weak: [Rambling, no point, no metrics]
- What was missing: [Structure, specifics, user focus]
- Likely impact: [How interviewer perceived this]

2. [Question]
[Same structure]

These need complete rewrites.

---

### Answer Rewrites

For your 3 weakest answers:

---

QUESTION: "[Question you struggled with]"

What you said:
[Your actual rambling/unclear answer]

Why this failed:
- [Problem 1: Too vague]
- [Problem 2: No metrics]
- [Problem 3: Didn't answer question]

Rewritten answer:

[Proper PM answer using framework]

Why this version works:
- [Reason 1]
- [Reason 2]

---

[Repeat for 2 more weak answers]

---

### Improvement Plan

IMMEDIATE (Before next interview):Stories to prepare:
1. [Situation]: Product you shipped - NEEDS metrics, user impact, why decisions made
2. [Situation]: Conflict with stakeholder - NEEDS how you influenced, data you used
3. [Situation]: Failed launch - NEEDS what you learned, what you'd do differently
4. [Situation]: Prioritization decision - NEEDS framework, tradeoffs, outcome
5. [Situation]: Technical decision - NEEDS why, constraints, business impact
6. [Situation]: Data-driven decision - NEEDS hypothesis, experiment, result

For each story, write out full STAR format. Practice out loud 3x each.

---

PM frameworks to learn/review:
- [ ] [Framework]: Because you need [competency]
- [ ] [Framework]: To answer [question type] better
- [ ] [Framework]: To show [PM skill]

Resources:
[Specific articles/videos for gaps identified]

---

Answer structure practice:
- Time yourself (2-3 min max)
- Record and listen for:
- Filler words (um, like, you know)
- Lack of structure
- Missing metrics
- Vague language

---

SHORT-TERM (This week):

- [ ] Complete story rewrites with STAR format
- [ ] Mock interview with PM friend
- [ ] Practice product sense questions (how would you improve X?)
- [ ] Review: [Specific company/product] deeper
- [ ] Fix resume bullet about [weak experience] to be clearer

---

KNOWLEDGE GAPS TO FILL:

Based on struggles:
- [ ] [Topic]: Read [resource]
- [ ] [Skill]: Practice [exercise]
- [ ] [Framework]: Watch [video]

---

### If You Advance

For next round, focus on:
1. [Competency to emphasize]
2. [Story type to prepare]
3. [Skill to demonstrate better]

Likely next round questions:
[Based on role and what they're hiring for]

---

### If You Don't Advance

Key learnings:
1. [Lesson 1]
2. [Lesson 2]
3. [Lesson 3]

Apply these to next interview.Next steps:
- [ ] Thank you email (still send it)
- [ ] Practice improved answers
- [ ] Apply lessons to next opportunity

---

### Bottom Line

What cost you this interview:
[The 1-2 main issues that hurt most]

What would make you successful next time:
[The 1-2 things to focus on]

You're [ready / almost ready / need more prep] for PM interviews at [stage/type] companies.

</review_pm_interview>
```

</details>

---


