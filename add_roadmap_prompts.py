"""Add 4 roadmap automation prompts to the BC Prompt Library.

Prompts:
1. Roadmap: Outlook Weekly Email Summary
2. Roadmap: Teams Meeting Transcript Summary
3. Roadmap: Confluence Status Update Summary
4. Roadmap: Weekly Aggregation Digest

Usage: python add_roadmap_prompts.py
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

# Define the 4 new prompts
new_prompts = [
    {
        'name': 'Roadmap: Outlook Weekly Email Summary',
        'category': 'Productivity',
        'useCase': 'Transform Microsoft Copilot email summary into structured roadmap input (weekly-emails.md)',
        'tools': 'Claude, Outlook Copilot',
        'technique': 'Structured extraction with priority categorization, workstream ID tagging, and risk signal detection',
        'prompt': '<outlook_email_summary>\n\n<inputs>\nCOPILOT EMAIL SUMMARY:\n[Paste your full Microsoft Copilot email summary here]\n\nWEEK: [YYYY-WXX, e.g., 2026-W07]\n\nADDITIONAL CONTEXT (optional):\n- Any emails Copilot may have missed or you want to highlight\n- Threads you know are critical to the payment roadmap\n</inputs>\n\n<system_context>\nYou are a program management analyst for a payments modernization program at Minor Hotels. Your job is to extract roadmap-relevant information from a weekly email summary.\n\nACTIVE ROADMAP INITIATIVES:\n- PAY: Payment Orchestration Platform (Juspay, Multi-PSP Routing, Oracle PMS, Fraud/Forter, Settlement)\n- LOY: Loyalty Payment Integration (Discovery Dollars, Viridian Automation, Points Earning)\n- ANA: Analytics & Reporting (Local Dashboard, Executive Reporting)\n\nKEY PARTNERS/VENDORS: Juspay, Oracle (OWS/OHIP), Forter, Worldline, 2C2P, Checkout.com, Airwallex, Viridian\n\nKPIs TO WATCH FOR:\n- Payment success rates\n- Transaction costs\n- Hotel onboarding/rollout numbers\n</system_context>\n\n<instructions>\nAnalyze the Copilot email summary and produce a structured markdown file. Focus on:\n\n1. Roadmap relevance - Only include emails related to the payment program\n2. Action extraction - Pull out every commitment, ask, or deadline\n3. Risk signals - Flag anything suggesting timeline risk, scope change, or blocker\n4. Use roadmap IDs - Reference workstream IDs (e.g., PAY-010, LOY-001) when applicable\n\nSkip purely operational emails (HR, facilities, unrelated projects).\n\nOutput format:\n# Weekly Email Summary - [WEEK]\n\n## High Priority\n### Email: [Subject Line]\n**From:** [Name] | **To:** [Name(s)] | **Date:** [Date]\n**Relates to:** [Workstream ID(s) or "General"]\nKey Points: [bullets]\nAction Items: [action - owner - due date]\nRisk Signal: [risk or "None"]\n\n## Standard Priority\n[Same structure]\n\n## FYI / Informational\n[One-liner summaries]\n\n## Week-at-a-Glance\nTotal roadmap-relevant emails, key themes, decisions made, open threads\n</instructions>\n\n</outlook_email_summary>'
    },
    {
        'name': 'Roadmap: Teams Meeting Transcript Summary',
        'category': 'Productivity',
        'useCase': 'Transform Microsoft Teams meeting transcripts into structured roadmap input (weekly-meetings.md)',
        'tools': 'Claude, Microsoft Teams',
        'technique': 'Signal extraction from noisy transcripts with workstream tagging, decision capture, and contradiction detection',
        'prompt': '<teams_meeting_summary>\n\n<inputs>\nMEETING TRANSCRIPTS:\n[Paste one or more Teams meeting transcripts/recaps here. Separate multiple meetings with "---NEW MEETING---"]\n\nWEEK: [YYYY-WXX, e.g., 2026-W07]\n</inputs>\n\n<system_context>\nYou are a program management analyst for a payments modernization program at Minor Hotels.\n\nACTIVE WORKSTREAMS:\n- PAY-010: Juspay Integration | PAY-020: Multi-PSP Routing | PAY-030: Oracle PMS | PAY-040: Fraud/Forter | PAY-050: Settlement\n- LOY-010: D$ Payment Method | LOY-014: Viridian Automation | LOY-020: Points Earning\n- ANA-010: Local Analytics Dashboard | ANA-020: Executive Reporting\n\nKPIs: Payment success rate (>=75%), avg cost per transaction, % hotels on payment stack\n</system_context>\n\n<instructions>\nProcess each meeting transcript into structured roadmap input:\n\n1. Filter for signal - Extract only roadmap-relevant content from noisy transcripts\n2. Map to workstreams - Tag every discussion point with workstream IDs\n3. Capture exact quotes - For critical decisions, include brief direct quotes with speaker attribution\n4. Flag contradictions - If discussions contradict current roadmap data, call it out\n\nFor each meeting output:\n## Meeting: [Name]\n**Date:** [Date] | **Attendees:** [Names]\n**Relates to:** [Workstream IDs]\n\n### Key Discussion Points\n### Decisions Made\n### Status Updates (table: Workstream | Update | Impact)\n### Action Items (checkboxes with owner and due date)\n### Roadmap Impact (timeline changes, new risks, dependencies, scope changes)\n### Notable Quotes\n\nEnd with:\n## Cross-Meeting Themes\n## Decisions Log (table: Decision | Meeting | Who | Workstream)\n</instructions>\n\n</teams_meeting_summary>'
    },
    {
        'name': 'Roadmap: Confluence Status Update Summary',
        'category': 'Productivity',
        'useCase': 'Pull and summarize Confluence status pages into structured roadmap input (weekly-status.md)',
        'tools': 'Claude, Atlassian MCP, Confluence',
        'technique': 'Automated page retrieval via MCP with KPI extraction, RAG status mapping, and roadmap discrepancy detection',
        'prompt': '<confluence_status_summary>\n\n<inputs>\nMODE: [A - Pull from Confluence via MCP / B - Manual paste]\n\nFOR MODE A:\nCONFLUENCE SPACE KEY: [e.g., "PAYMENTS"]\nPAGE TITLE PATTERN: [e.g., "Weekly Status"]\nDATE RANGE: [e.g., "2026-02-10 to 2026-02-14"]\n\nFOR MODE B:\nCONFLUENCE PAGE CONTENT:\n[Paste your Confluence status update page content here]\n\nWEEK: [YYYY-WXX]\n</inputs>\n\n<system_context>\nYou are a program management analyst for a payments modernization program at Minor Hotels.\n\nACTIVE INITIATIVES: PAY-001, LOY-001, ANA-001\nKPIs: Payment Success Rate (>=75%), Avg Cost/Txn (decreasing), % Hotels on Stack (increasing)\n</system_context>\n\n<instructions>\nFor Mode A: Use Atlassian MCP searchConfluenceUsingCql to find pages, then getConfluencePage to fetch content.\n\nProcess the status update into standardized format:\n\n1. Extract KPI data - All metrics, percentages, success rates, cost figures, hotel counts\n2. Map to workstreams - Tag each status item with roadmap IDs\n3. Identify deltas - What changed since last week\n4. Flag concerns - Anything marked red/amber/at-risk\n\nOutput format:\n# Weekly Status Update - [WEEK]\n\n## Source (page title, author, date)\n## KPI Data Points (payment success rate, cost/txn, % hotels)\n\nPer initiative (PAY, LOY, ANA):\n- Overall Status and RAG\n- What happened this week\n- What is planned next week\n- Blockers or risks\n- Key metrics mentioned\n\n## Cross-Cutting Items\n## Confluence vs. Roadmap Discrepancies\n</instructions>\n\n</confluence_status_summary>'
    },
    {
        'name': 'Roadmap: Weekly Aggregation Digest',
        'category': 'Productivity',
        'useCase': 'Aggregate all weekly inputs (emails, meetings, status) into rolling master digest with trend analysis',
        'tools': 'Claude',
        'technique': 'Cross-document synthesis with rolling trend analysis, KPI tracking, and institutional memory building',
        'prompt': '<weekly_aggregation>\n\n<inputs>\nWEEK: [YYYY-WXX]\n\nTHIS WEEK\'S INPUT FILES:\n[Paste contents of emails.md, meetings.md, and status.md]\n\nCURRENT WEEKLY DIGEST (if exists):\n[Paste current inputs/weekly-digest.md or "FIRST RUN"]\n</inputs>\n\n<system_context>\nYou maintain a rolling digest of the Minor Hotels payment modernization program. This compounds week over week as the AI\'s institutional memory.\n\nACTIVE INITIATIVES: PAY-001, LOY-001, ANA-001\nKPIs: Payment Success Rate (>=75%), Avg Cost/Txn (decreasing), % Hotels on Stack (increasing)\n\nThree purposes: Rolling summary, Trend tracking, Context for AI analysis pipeline.\n</system_context>\n\n<instructions>\nProcess all 3 input files and produce:\n\n1. This Week\'s Digest Entry - concise summary (max 30 lines)\n2. Updated Trend Analysis - review full history and update observations\n\nMaster tracker format:\n# Payment Program - Weekly Digest\n\n## Trend Analysis\n- Program Health Trajectory\n- KPI Trends (rolling 5-week table with direction arrows)\n- Recurring Themes\n- Velocity Observations\n- Stakeholder Sentiment\n\n## Weekly Entries (newest first)\n### Week [YYYY-WXX]\nOverall Assessment | RAG Status per initiative\nTable: Initiative | Status | Key Event | Blocker\nDecisions Made (with source)\nAction Items Created\nRisks Identified\nKPI Data Points\nKey Quotes\nSource Documents (count per type)\n\nRULES:\n- NEVER modify previous week entries - only prepend new week\n- Update Trend Analysis based on ALL historical entries\n- Cross-reference all 3 input files and flag contradictions\n- Preserve specific numbers and dates exactly\n- Trend Analysis grows smarter each week\n</instructions>\n\n</weekly_aggregation>'
    }
]

# Add each prompt if it doesn't already exist
added = 0
for prompt in new_prompts:
    exists = any(p['name'] == prompt['name'] for p in prompts_data)
    if not exists:
        prompts_data.append(prompt)
        added += 1
        print(f"[OK] Added: {prompt['name']}")
    else:
        print(f"[SKIP] Already exists: {prompt['name']}")

print(f"\nAdded {added} new prompts. Total: {len(prompts_data)}")

# Write the updated JS data
js_content = f"// Auto-generated from BC Prompt Library\n"
js_content += f"// Total prompts: {len(prompts_data)}\n"
js_content += f"window.promptsData = {json.dumps(prompts_data, indent=2, ensure_ascii=False)};\n"

with open('prompts-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"[OK] Updated prompts-data.js")

# Count per category
category_counts = {}
for p in prompts_data:
    cat = p['category']
    category_counts[cat] = category_counts.get(cat, 0) + 1

print("\nPrompts per category:")
for cat in sorted(category_counts.keys()):
    print(f"  {cat}: {category_counts[cat]}")

# Also append to the markdown file
md_prompts = [
    ('Roadmap: Outlook Weekly Email Summary',
     'Transform Microsoft Copilot email summary into structured roadmap input (weekly-emails.md)',
     'Claude, Outlook Copilot',
     'Structured extraction with priority categorization, workstream ID tagging, and risk signal detection'),
    ('Roadmap: Teams Meeting Transcript Summary',
     'Transform Microsoft Teams meeting transcripts into structured roadmap input (weekly-meetings.md)',
     'Claude, Microsoft Teams',
     'Signal extraction from noisy transcripts with workstream tagging, decision capture, and contradiction detection'),
    ('Roadmap: Confluence Status Update Summary',
     'Pull and summarize Confluence status pages into structured roadmap input (weekly-status.md)',
     'Claude, Atlassian MCP, Confluence',
     'Automated page retrieval via MCP with KPI extraction, RAG status mapping, and roadmap discrepancy detection'),
    ('Roadmap: Weekly Aggregation Digest',
     'Aggregate all weekly inputs (emails, meetings, status) into rolling master digest with trend analysis',
     'Claude',
     'Cross-document synthesis with rolling trend analysis, KPI tracking, and institutional memory building'),
]

md_addition = '\n'
for i, (name, use_case, tools, technique) in enumerate(md_prompts):
    md_addition += f'''\n### {name}\n\n**\U0001f4cb Use Case:** {use_case}\n\n**\U0001f6e0\ufe0f Recommended Tools:** {tools}\n\n**\U0001f4a1 Technique:** {technique}\n\n<details>\n<summary>Click to view prompt</summary>\n\n```\n{new_prompts[i]["prompt"]}\n```\n\n</details>\n\n---\n'''

with open('BC-Prompt-Library.md', 'a', encoding='utf-8') as f:
    f.write(md_addition)

print("[OK] Appended 4 prompts to BC-Prompt-Library.md")
