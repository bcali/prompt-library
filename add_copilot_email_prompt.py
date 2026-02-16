"""Add the Copilot Email Summary prompt to the BC Prompt Library.

Usage: python add_copilot_email_prompt.py
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

new_prompt = {
    'name': 'Copilot: Weekly Email Deep Search',
    'category': 'Productivity',
    'useCase': 'Run in Microsoft 365 Copilot to search ALL Outlook folders (Inbox, Sent, Archive, Deleted, Junk, subfolders) and produce a comprehensive action-oriented email summary',
    'tools': 'Microsoft 365 Copilot (Outlook)',
    'technique': 'Exhaustive multi-folder search with action-based categorization (action required, waiting on others, decisions made, key updates) plus overdue reply detection',
    'prompt': (
        'Search through ALL of my Outlook email folders from the last 7 days — '
        'this includes Inbox, Sent Items, Archive, Deleted Items, Junk, Drafts, '
        'and every subfolder or nested folder I have. Do not limit your search to '
        'just the Inbox. I need a complete picture of my email activity.\n\n'
        'For each email or thread you find, assess whether it relates to any of these topics:\n'
        '- Payments, payment processing, payment gateways, PSP, PCI compliance\n'
        '- Juspay, Oracle PMS (OWS/OHIP), Forter, Worldline, 2C2P, Checkout.com, Airwallex\n'
        '- Hotel technology, property management systems, hotel onboarding or rollout\n'
        '- Loyalty programs, Discovery Dollars, Viridian, points earning\n'
        '- Analytics, reporting, dashboards, data\n'
        '- Any project status updates, timeline changes, go-live dates, or launch plans\n'
        '- Any escalations, blockers, risks, or issues raised\n'
        '- Any decisions requested or made\n'
        '- Budget, contracts, vendor negotiations, procurement\n'
        '- Team changes, resource allocation, hiring for program roles\n\n'
        'Now produce the following structured summary:\n\n'
        '## ACTION REQUIRED — Emails Where I Need To Do Something\n\n'
        'For each email where I am expected to take action, reply, approve, review, or make a decision:\n\n'
        '**Subject:** [full subject line]\n'
        '**From:** [sender name and email] | **Date:** [date sent]\n'
        '**Folder found in:** [which folder this was in]\n'
        '**What\'s needed from me:** [specific action required — be precise]\n'
        '**Deadline:** [if any deadline is mentioned or implied]\n'
        '**Thread summary:** [2-3 sentence summary of the full thread context]\n\n'
        '---\n\n'
        '## WAITING ON OTHERS — Emails Where I\'m Waiting For a Response\n\n'
        'For each email I sent that has not received a reply, or where someone committed to get back to me:\n\n'
        '**Subject:** [full subject line]\n'
        '**Sent to:** [recipient(s)] | **Date I sent/they committed:** [date]\n'
        '**What I\'m waiting for:** [what was asked or promised]\n'
        '**How long overdue:** [if past any stated deadline]\n\n'
        '---\n\n'
        '## DECISIONS MADE — Emails Where Something Was Decided\n\n'
        'For any thread where a decision was reached, approval was given, or direction was set:\n\n'
        '**Subject:** [full subject line]\n'
        '**Decision:** [what was decided]\n'
        '**Decided by:** [who made the call]\n'
        '**Date:** [when]\n'
        '**Impact:** [what this means going forward]\n\n'
        '---\n\n'
        '## KEY UPDATES — Important Information I Should Know\n\n'
        'For significant updates, announcements, or status changes (even if no action from me):\n\n'
        '**Subject:** [full subject line]\n'
        '**From:** [sender] | **Date:** [date]\n'
        '**Summary:** [what happened or changed]\n\n'
        '---\n\n'
        '## WEEK OVERVIEW\n\n'
        '- **Total emails found across all folders:** [count]\n'
        '- **Emails requiring my action:** [count]\n'
        '- **Emails where I\'m waiting on others:** [count]\n'
        '- **Top 3 themes this week:** [bullet points]\n'
        '- **Anything flagged as urgent or escalated:** [list or "None"]\n'
        '- **Emails from people I haven\'t replied to in 3+ days:** [list or "None"]\n\n'
        'Be thorough. I would rather have too much information than miss something important. '
        'If you\'re unsure whether an email is relevant, include it. '
        'Do not summarize folders you skipped — I need you to check every folder.'
    )
}

# Check if it already exists
exists = any(p['name'] == new_prompt['name'] for p in prompts_data)
if exists:
    print(f"[SKIP] Already exists: {new_prompt['name']}")
else:
    prompts_data.append(new_prompt)
    print(f"[OK] Added: {new_prompt['name']}")

print(f"\nTotal prompts: {len(prompts_data)}")

# Write the updated JS data
js_content = f"// Auto-generated from BC Prompt Library\n"
js_content += f"// Total prompts: {len(prompts_data)}\n"
js_content += f"window.promptsData = {json.dumps(prompts_data, indent=2, ensure_ascii=False)};\n"

with open('prompts-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"[OK] Updated prompts-data.js")

# Append to the markdown file
md_addition = f'''

### Copilot: Weekly Email Deep Search

**Use Case:** Run in Microsoft 365 Copilot to search ALL Outlook folders (Inbox, Sent, Archive, Deleted, Junk, subfolders) and produce a comprehensive action-oriented email summary

**Recommended Tools:** Microsoft 365 Copilot (Outlook)

**Technique:** Exhaustive multi-folder search with action-based categorization (action required, waiting on others, decisions made, key updates) plus overdue reply detection

<details>
<summary>Click to view prompt</summary>

```
{new_prompt["prompt"]}
```

</details>

---
'''

with open('BC-Prompt-Library.md', 'a', encoding='utf-8') as f:
    f.write(md_addition)

print("[OK] Appended to BC-Prompt-Library.md")
