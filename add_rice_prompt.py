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

# Create the new RICE prompt
rice_prompt = {
    'name': 'RICE Feature Scoring',
    'category': 'Strategy & Planning',
    'useCase': 'Score and prioritize features using the RICE framework',
    'tools': 'Claude, ChatGPT, or any LLM',
    'technique': 'Structured scoring with explicit rationale for assumptions and risks',
    'prompt': 'RICE Score = (Reach × Impact × Confidence) / Effort\n\nFeature: [NAME]\nReach: [NUMBER] | Impact: [SCORE] | Confidence: [%] | Effort: [WEEKS]\nScore: [CALCULATED]\nRationale: [2-3 sentences on the biggest assumption or risk]'
}

# Check if it already exists
exists = any(p['name'] == rice_prompt['name'] for p in prompts_data)

if not exists:
    prompts_data.append(rice_prompt)
    print(f"[OK] Added new RICE prompt. Total: {len(prompts_data)} prompts")
else:
    print(f"[INFO] RICE prompt already exists. Total: {len(prompts_data)} prompts")

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
