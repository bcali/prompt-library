"""Update the Confluence Status Update prompt in BC Prompt Library with MCP-integrated v2.

Usage: python add_confluence_v2_prompt.py
"""
import json
import re

with open('prompts-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_match = re.search(r'window\.promptsData = (.*);', content, re.DOTALL)
if json_match:
    prompts_data = json.loads(json_match.group(1))
else:
    print("Error: Could not parse JSON from file")
    exit(1)

updated_prompt = {
    'name': 'Roadmap: Confluence Status Update Summary',
    'category': 'Productivity',
    'useCase': 'Pull weekly status updates from Confluence via Atlassian MCP, index all entries, and transform into structured roadmap input with execution scorecard, vendor tracking, risk register, and multi-week comparison',
    'tools': 'Claude, Atlassian MCP',
    'technique': 'MCP-driven page fetching (index page -> child pages), structured section parsing with workstream ID mapping, carry-forward detection, and cross-week trend analysis',
    'prompt': (
        '<confluence_status_summary>\n\n'
        '<mcp_config>\n'
        'You have access to the Atlassian MCP server. Use these coordinates:\n\n'
        'CLOUD_ID: emeapayments.atlassian.net\n'
        'INDEX_PAGE_ID: 753666\n'
        'SPACE_KEY: ~5c9c53b9266e576700accb2e\n\n'
        'STEP 1: Fetch the index page (ID: 753666) using getConfluencePage with contentFormat "markdown".\n'
        'This returns a table with columns: Date | Update | TL;DR\n'
        'Each date cell contains a link to a child page with the full status update.\n\n'
        'STEP 2: Parse the index table. Identify the most recent entry (top row).\n'
        'Extract the child page ID from the link URL (the number in /pages/XXXXXXXX/).\n\n'
        'STEP 3: Fetch that child page using getConfluencePage with contentFormat "markdown".\n'
        'This is the full weekly status update.\n\n'
        'If a specific week is requested, find the matching date row in the index table instead of defaulting to the most recent.\n'
        '</mcp_config>\n\n'
        '<inputs>\n'
        'WEEK: [YYYY-WXX, e.g., 2026-W08 — or "LATEST" to auto-detect]\n\n'
        'OPTIONAL — MULTI-WEEK COMPARISON:\n'
        'If you want trend analysis across multiple weeks, specify:\n'
        'COMPARE_WEEKS: [number of weeks to look back, e.g., 3]\n'
        '</inputs>\n\n'
        '<system_context>\n'
        'You are a program management analyst for the payments modernization program at Minor Hotels.\n\n'
        'ACTIVE ROADMAP INITIATIVES AND EPICS:\n'
        '- PAY-001: Payment Orchestration Platform\n'
        '  - PAY-010: Juspay Integration (checkout, routing, orchestration)\n'
        '  - PAY-020: Multi-PSP Routing (Checkout.com, Airwallex, 2C2P, Worldline)\n'
        '  - PAY-030: Oracle PMS Integration (OWS/OHIP, guarantee codes, Opera Cloud)\n'
        '  - PAY-040: Fraud Prevention (Forter replacement, CKO built-in fraud)\n'
        '  - PAY-050: Settlement & Reconciliation (payouts, finance reports, FX)\n'
        '- LOY-001: Loyalty Payment Integration\n'
        '  - LOY-010: Discovery Dollars (D$ redemption, non-cancellable rates)\n'
        '  - LOY-014: Viridian Automation\n'
        '  - LOY-020: Points Earning\n'
        '- ANA-001: Analytics & Reporting\n'
        '  - ANA-010: Local Analytics Dashboard\n'
        '  - ANA-020: Executive Reporting\n\n'
        'KEY VENDORS: Juspay, Oracle (OWS/OHIP/Opera Cloud), Forter, Checkout.com, Airwallex, 2C2P, Worldline, PayPal, Stripe, Viridian\n\n'
        'KPIs:\n'
        '- Payment Success Rate (target: >= 75%)\n'
        '- Avg Cost per Transaction (target: decreasing toward 2.1%)\n'
        '- % Hotels on Payment Stack (target: increasing)\n'
        '</system_context>\n\n'
        '<page_structure>\n'
        'The status update pages follow this consistent structure:\n\n'
        '1. HEADER — "Weekly Status Update: Payments Modernization" + STATUS (Green/Yellow/Red) + summary\n'
        '2. LAST WEEK PLANNED VS COMPLETED — Table: Planned Item | Status (Done/Not Done/Partial) | Notes\n'
        '3. WINS / PROGRESS — Categorized sections: Beta, Business Case, Contracts, Settlement, Integration\n'
        '4. NEXT / UPCOMING — Table: Date/Priority | Item | Owner\n'
        '5. RISKS / BLOCKERS — Each with severity (Critical/High/Medium), description, impact, mitigation\n\n'
        'Preserve exact percentages, dollar amounts, dates, owner names, and severity levels.\n'
        '</page_structure>\n\n'
        '<instructions>\n'
        'After fetching the status update page(s) via MCP, produce:\n\n'
        '# Weekly Status Update - [WEEK]\n\n'
        '## Source (page title, author, date, overall RAG)\n'
        '## KPI Data Points (payment success rate, cost/txn, % hotels, other metrics)\n'
        '## Execution Scorecard (planned vs completed table, completion rate, carry-forwards)\n\n'
        'Per initiative (PAY, LOY, ANA):\n'
        '- Status RAG\n'
        '- What happened this week (mapped to workstream IDs)\n'
        '- What is planned next week (with owners and priority)\n'
        '- Blockers or risks (with severity)\n\n'
        '## Vendor & Contract Status (table: vendor, update, status, financial impact)\n'
        '## Risk Register (table: risk, severity, workstream, status, mitigation)\n'
        '## Week-over-Week Delta (resolved, new risks, carry-forwards 2+ weeks, KPI movement, RAG change)\n'
        '## AI Observations (patterns, risks, opportunities, concerns for the analysis pipeline)\n'
        '</instructions>\n\n'
        '</confluence_status_summary>'
    )
}

# Find and replace the existing prompt
replaced = False
for i, p in enumerate(prompts_data):
    if p['name'] == updated_prompt['name']:
        prompts_data[i] = updated_prompt
        replaced = True
        print(f"[OK] Updated: {updated_prompt['name']}")
        break

if not replaced:
    prompts_data.append(updated_prompt)
    print(f"[OK] Added: {updated_prompt['name']}")

print(f"\nTotal prompts: {len(prompts_data)}")

js_content = f"// Auto-generated from BC Prompt Library\n"
js_content += f"// Total prompts: {len(prompts_data)}\n"
js_content += f"window.promptsData = {json.dumps(prompts_data, indent=2, ensure_ascii=False)};\n"

with open('prompts-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"[OK] Updated prompts-data.js")
