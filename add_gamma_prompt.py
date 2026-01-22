import json
import re

# Read the original prompts data
with open('prompts-data-original.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the JSON data
json_match = re.search(r'window\.promptsData = (.*);', content, re.DOTALL)
if json_match:
    prompts_data = json.loads(json_match.group(1))
else:
    print("Error: Could not parse JSON from file")
    exit(1)

# Find the new Gamma prompt from the markdown
with open('BC-Prompt-Library.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Extract the Gamma prompt
gamma_match = re.search(
    r'### Executive Presentation Builder \(Gamma\)\n\n\*\*📋 Use Case:\*\* ([^\n]+)\n\n\*\*🛠️ Recommended Tools:\*\* ([^\n]+)\n\n\*\*💡 Technique:\*\* ([^\n]+).*?<details>.*?```\n(.*?)\n```.*?</details>',
    md_content,
    re.DOTALL
)

if gamma_match:
    gamma_prompt = {
        'name': 'Executive Presentation Builder (Gamma)',
        'category': 'Productivity',
        'useCase': gamma_match.group(1).strip(),
        'tools': gamma_match.group(2).strip(),
        'technique': gamma_match.group(3).strip(),
        'prompt': gamma_match.group(4).strip()
    }

    # Check if it already exists
    exists = any(p['name'] == gamma_prompt['name'] for p in prompts_data)

    if not exists:
        prompts_data.append(gamma_prompt)
        print(f"[OK] Added new Gamma prompt. Total: {len(prompts_data)} prompts")
    else:
        print(f"[INFO] Gamma prompt already exists. Total: {len(prompts_data)} prompts")
else:
    print("[ERROR] Could not find Gamma prompt in markdown")
    exit(1)

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
