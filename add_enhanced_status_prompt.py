"""Add Enhanced Weekly Status Update prompt to the BC Prompt Library.

Replaces the old "Roadmap: Confluence Status Update Summary" with the enhanced
version that also updates roadmap.json + kpis.json on GitHub.

Usage: python add_enhanced_status_prompt.py
"""
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

# The enhanced prompt
enhanced_prompt = {
    'name': 'Enhanced Weekly Status Update',
    'category': 'Productivity',
    'useCase': 'Weekly status workflow: collect KPIs + epic changes, update roadmap.json + kpis.json on GitHub, publish Confluence status page with 10-workstream summary',
    'tools': 'Claude, Atlassian MCP, GitHub MCP',
    'technique': 'Structured input collection with chat pre-fill, triple-output generation (GitHub data + Confluence narrative), workstream-aligned status tracking',
    'prompt': """<enhanced_weekly_status>

<mcp_config>
Atlassian MCP:
  CLOUD_ID: 597e34b6-1435-49c1-9de4-413ffd885120
  SPACE_ID: 65703
  PARENT_PAGE_ID: 753666

GitHub MCP:
  REPO: bcali/roadmap-dashboard
  DATA_FILES: data/roadmap.json, data/kpis.json
</mcp_config>

<system_context>
You are managing the weekly status workflow for Operation Money Tree — Minor Hotels' payment modernization program. 10 active workstreams, 49 epics, $10.71M total opportunity.

WORKSTREAMS:
| # | ID | Name | Business Case |
|---|-----|------|--------------|
| 1 | ORCH-001 | Orchestration | $2.23M per 1% auth rate |
| 2 | SCALE-001 | Hotel Onboarding & Scale | Enables all value |
| 3 | OPERA-001 | Opera Cloud Integration | $56K + $1.84M enabled |
| 4 | FRAUD-001 | Fraud & Decisioning | $258K annual savings |
| 5 | MIT-001 | Merchant-Initiated Transactions | $824K / $4M GBV at risk |
| 6 | DS-001 | D$ Online Redemption | $608K ($121K Ph1 + $487K Ph2) |
| 7 | AVC-001 | AVC Onboarding | $550K / $80M volume |
| 8 | LAQ-001 | Local Acquiring | $1.84M / $84.7M volume |
| 9 | FX-001 | FX / MCC | $4.27M total |
| 10 | APM-001 | Alternative Payment Methods | Conversion uplift |

DEPENDENCY CHAINS:
- SCALE-001 -> Everything
- MIT-070 -> DS-040 (D$ refundable) + FX-060 (MCC refundable)
- FX-030 -> Full LAQ value (external dep: Digital/Web team)

PROPERTIES TARGET: 585
</system_context>

<instructions>

### STEP 1: COLLECT STRUCTURED INPUT

First, call recent_chats(n=20, after=[7 days ago]) and conversation_search for terms like "completed", "signed", "live", "blocked", "shipped" to pre-fill what you can.

Then prompt user with this template (pre-filled where possible):

```
WEEKLY STATUS INPUT

Auth rate: ___% (from CKO/Juspay dashboard)
Hotels on stack: ___ (total count)
Local acquiring markets live: ___ (count)

Epics completed this week: [comma-separated IDs, e.g., FRAUD-010, LAQ-010]
Epics started this week: [comma-separated IDs, e.g., SCALE-030]
Epics blocked: [ID + reason, or "none"]

Key wins (1-3 bullets):
-

Key risks (1-3 bullets):
-

Asks (who/what/when):
-

Context: [travel, PTO, major events, or "none"]
```

Wait for user confirmation/edits before proceeding.

### STEP 2: FETCH PREVIOUS STATUS

1. Search Confluence: ancestor = 753666 order by created desc (limit 1)
2. Fetch that child page with getConfluencePage (contentFormat: markdown)
3. Extract previous status color, "NEXT / UPCOMING" items, carry-forward blockers

### STEP 3: UPDATE roadmap.json ON GITHUB

1. Fetch data/roadmap.json from GitHub (github:get_file_contents, owner: bcali, repo: roadmap-dashboard)
2. For each epic user marked completed: set status to "Complete"
3. For each epic user marked started: set status to "In Progress"
4. For each epic user marked blocked: set status to "Blocked"
5. Push updated file (github:create_or_update_file) with commit: "chore: /status W[XX] - update epic statuses"
6. Compute roadmap_metrics:
   - total_workstreams: count level-1 entries
   - total_epics: count level-2 entries
   - completed_epics: count level-2 with status "Complete"
   - in_progress_epics: count level-2 with status "In Progress"
   - not_started_epics: count level-2 with status "Not Started"
   - blocked_epics: count level-2 with status "Blocked"
   - completion_pct: round(completed / total * 100)

### STEP 4: UPDATE kpis.json ON GITHUB

1. Fetch data/kpis.json from GitHub
2. Append new entry to history array:
   {
     "week": "2026-W[XX]",
     "date": "[YYYY-MM-DD]",
     "metrics": {
       "payment_success_rate": [user input],
       "avg_cost_per_transaction": [user input or carry forward],
       "pct_hotels_on_stack": [hotel_count / 585 * 100],
       "local_acquiring_markets": [user input],
       "business_case_value_realized": [carry forward or user input]
     },
     "roadmap_metrics": { [computed from Step 3] },
     "notes": "[1-sentence summary]"
   }
3. Push with commit: "chore: /status W[XX] - update KPIs"

### STEP 5: GENERATE CONFLUENCE STATUS PAGE

Determine status color:
- GREEN: No blockers, >=80% planned items complete, auth rate stable/improving
- YELLOW: Active blockers being worked, 50-80% complete, timeline pressure
- RED: Critical blockers >2 weeks, <50% complete, missed deadlines

Page structure:

## Weekly Status Update: Payments Modernization

**STATUS: [emoji] [COLOR]** - [One sentence headline]

### KPIs
| Metric | Value | Target | Trend |
|--------|-------|--------|-------|
| Auth Rate | X% | 82%+ | arrow |
| Hotels on Stack | X / 585 | 50 by Q2 | arrow |
| Local Acquiring Markets | X / 6 | 6 by Q2 | arrow |
| Epics Complete | X / 49 | - | arrow |

### Last Week Planned vs Completed
[Table from previous NEXT section with status indicators]

### Wins / Progress
[Grouped by workstream ID]

### Workstream Status Summary
| # | Workstream | Status | This Week | Business Case |
[10 rows, one per workstream, with RAG and 1-line summary]

### Next Week
[Priority table with owner and workstream ID]

### Risks / Blockers
[With severity, impact, mitigation, carry-forward age]

### Asks
[What / Who / By When table]

### STEP 6: PUBLISH TO CONFLUENCE

1. Create child page under 753666 with title "Status Update [M/D/YYYY]"
2. Update parent page 753666 - add row at TOP of index table
3. Return link to user

### STEP 7: OUTPUT

Return:
- Confluence link
- GitHub commits (roadmap.json + kpis.json)
- Stats: planned items completed, epics complete, carried-forward blockers
- Flags: recurring blockers, missed items, or "None"

### ERROR HANDLING
- GitHub push fails: output JSON diffs in chat for manual commit
- Confluence fails: output full page in chat for manual post
- No chats found: skip pre-fill, prompt for manual input
- No previous status: skip comparison, proceed with generation

</instructions>

</enhanced_weekly_status>"""
}

# Remove old version if it exists
prompts_data = [p for p in prompts_data if p['name'] != 'Enhanced Weekly Status Update']

# Add the new prompt
prompts_data.append(enhanced_prompt)
print(f"[OK] Added: {enhanced_prompt['name']}")

# Write the updated JS data
js_content = f"// Auto-generated from BC Prompt Library\n"
js_content += f"// Total prompts: {len(prompts_data)}\n"
js_content += f"window.promptsData = {json.dumps(prompts_data, indent=2, ensure_ascii=False)};\n"

with open('prompts-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"[OK] Updated prompts-data.js")
print(f"Total prompts: {len(prompts_data)}")

# Append to markdown file
md_addition = """

### Enhanced Weekly Status Update

**📋 Use Case:** Weekly status workflow: collect KPIs + epic changes, update roadmap.json + kpis.json on GitHub, publish Confluence status page with 10-workstream summary

**🛠️ Recommended Tools:** Claude, Atlassian MCP, GitHub MCP

**💡 Technique:** Structured input collection with chat pre-fill, triple-output generation (GitHub data + Confluence narrative), workstream-aligned status tracking

<details>
<summary>Click to view prompt</summary>

See `add_enhanced_status_prompt.py` for full prompt content.

</details>

---
"""

with open('BC-Prompt-Library.md', 'a', encoding='utf-8') as f:
    f.write(md_addition)

print("[OK] Appended to BC-Prompt-Library.md")
