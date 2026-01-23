import json
import re

# Read the current prompts data
with open('prompts-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the JSON data
json_match = re.search(r'window\.promptsData = (.*);', content, re.DOTALL)
if json_match:
    prompts_data = json.loads(json_match.group(1))
else:
    print("Error: Could not parse JSON from file")
    exit(1)

# Create the new Document Critique prompt
document_critique_prompt = {
    'name': 'Product Document Critique',
    'category': 'PM Artifacts',
    'useCase': 'Get detailed, actionable feedback on product documents (PRDs, briefs, charters, one-pagers)',
    'tools': 'Claude Projects, Claude Code',
    'technique': 'Multi-phase diagnostic framework with scoring, stress tests, and surgical line-by-line critique',
    'prompt': '''<document_critique>

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

</document_critique>'''
}

# Check if it already exists
exists = any(p['name'] == document_critique_prompt['name'] for p in prompts_data)

if not exists:
    prompts_data.append(document_critique_prompt)
    print(f"[OK] Added Document Critique prompt. Total: {len(prompts_data)} prompts")
else:
    print(f"[INFO] Document Critique prompt already exists. Total: {len(prompts_data)} prompts")

# Write the updated data
js_content = f"// Auto-generated from BC Prompt Library\n"
js_content += f"// Total prompts: {len(prompts_data)}\n"
js_content += f"window.promptsData = {json.dumps(prompts_data, indent=2, ensure_ascii=False)};\n"

with open('prompts-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"[OK] Generated prompts-data.js with {len(prompts_data)} prompts")

# Count per category
category_counts = {}
for p in prompts_data:
    cat = p['category']
    category_counts[cat] = category_counts.get(cat, 0) + 1

print("\nPrompts per category:")
for cat in sorted(category_counts.keys()):
    print(f"  {cat}: {category_counts[cat]}")
