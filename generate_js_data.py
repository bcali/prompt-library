import pandas as pd
import json

# Read Excel
df = pd.read_excel('BC Prompt Library.xlsx')

# Convert to list of dictionaries
prompts_data = []
for _, row in df.iterrows():
    prompts_data.append({
        'name': str(row.get('Name', 'Untitled')),
        'category': str(row.get('Category', '')),
        'prompt': str(row.get('Prompt', '')),
        'technique': str(row.get('Prompting Technique', '')),
        'tools': str(row.get('Recommended Tools', '')),
        'useCase': str(row.get('Use Case', ''))
    })

# Create JavaScript file
js_content = f"// Auto-generated from BC Prompt Library.xlsx\n"
js_content += f"window.promptsData = {json.dumps(prompts_data, indent=2, ensure_ascii=False)};\n"

# Write to file
with open('prompts-data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"✅ Generated prompts-data.js with {len(prompts_data)} prompts")

