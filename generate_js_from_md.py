import re
import json

# Read the markdown file
with open('BC-Prompt-Library.md', 'r', encoding='utf-8') as f:
    content = f.read()

prompts_data = []

# Find all category sections (## Category Name)
category_pattern = r'^## ([^\n]+)\n\n\*(\d+) prompts in this category\*'
categories = list(re.finditer(category_pattern, content, re.MULTILINE))

for i, category_match in enumerate(categories):
    category_name = category_match.group(1).strip()
    category_start = category_match.end()

    # Find the end of this category (start of next category or end of file)
    if i + 1 < len(categories):
        category_end = categories[i + 1].start()
    else:
        category_end = len(content)

    category_content = content[category_start:category_end]

    # Find all ### headers (prompts)
    prompt_headers = list(re.finditer(r'\n###\s+([^\n]+)', category_content))

    for j, prompt_match in enumerate(prompt_headers):
        prompt_name = prompt_match.group(1).strip()
        prompt_start = prompt_match.end()

        # Find end of this prompt (next ### or end of category)
        if j + 1 < len(prompt_headers):
            prompt_end = prompt_headers[j + 1].start()
        else:
            prompt_end = len(category_content)

        prompt_content_section = category_content[prompt_start:prompt_end]

        # Extract metadata
        use_case_match = re.search(r'\*\*📋 Use Case:\*\* ([^\n]+)', prompt_content_section)
        tools_match = re.search(r'\*\*🛠️ Recommended Tools:\*\* ([^\n]+)', prompt_content_section)
        technique_match = re.search(r'\*\*💡 Technique:\*\* ([^\n]+)', prompt_content_section)

        use_case = use_case_match.group(1).strip() if use_case_match else ''
        tools = tools_match.group(1).strip() if tools_match else ''
        technique = technique_match.group(1).strip() if technique_match else ''

        # Extract prompt content from code blocks inside <details>
        details_match = re.search(r'<details>.*?```\n(.*?)\n```.*?</details>', prompt_content_section, re.DOTALL)
        if details_match:
            prompt_text = details_match.group(1).strip()
        else:
            prompt_text = ''

        # Only add if we have the essential fields
        if prompt_name and prompt_text and use_case:
            prompts_data.append({
                'name': prompt_name,
                'category': category_name,
                'prompt': prompt_text,
                'technique': technique,
                'tools': tools,
                'useCase': use_case
            })

# Create JavaScript file
js_content = f"// Auto-generated from BC-Prompt-Library.md\n"
js_content += f"window.promptsData = {json.dumps(prompts_data, indent=2, ensure_ascii=False)};\n"

# Write to file
with open('prompts-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"[OK] Generated prompts-data.js with {len(prompts_data)} prompts")

# Show count per category
category_counts = {}
for p in prompts_data:
    cat = p['category']
    category_counts[cat] = category_counts.get(cat, 0) + 1

print("\nPrompts per category:")
for cat in sorted(category_counts.keys()):
    print(f"  {cat}: {category_counts[cat]}")
