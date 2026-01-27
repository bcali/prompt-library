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

# Create the new Email Inbox Triage prompt
inbox_triage_prompt = {
    'name': 'Email Inbox Triage',
    'category': 'Productivity',
    'useCase': 'Quickly identify urgent emails and action items from the last 5 days',
    'tools': 'Gmail, Outlook, Claude integration',
    'technique': 'Structured categorization by urgency, sender importance, and dependency blocking',
    'prompt': '''Scan my inbox from the last 5 days. Create three sections:

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

Format as a table with: Sender | Subject | Days Old | Action Required'''
}

# Check if it already exists
exists = any(p['name'] == inbox_triage_prompt['name'] for p in prompts_data)

if not exists:
    prompts_data.append(inbox_triage_prompt)
    print(f"[OK] Added Email Inbox Triage prompt. Total: {len(prompts_data)} prompts")
else:
    print(f"[INFO] Email Inbox Triage prompt already exists. Total: {len(prompts_data)} prompts")

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
