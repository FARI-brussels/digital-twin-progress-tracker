import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# Create assets directory if it doesn't exist
if not os.path.exists('assets'):
    os.makedirs('assets')

# Read the CSV file
data = pd.read_csv('data.csv')

# Calculate implementation stats
implemented_count = sum(data['implemented'].map(lambda x: str(x).lower() == 'true'))
not_implemented_count = len(data) - implemented_count
implementation_percentage = round((implemented_count / len(data)) * 100, 2)

# Create the pie chart
labels = ['Implemented', 'Not Implemented']
sizes = [implemented_count, not_implemented_count]
colors = ['#4CAF50', '#F44336']  # Green for implemented, red for not implemented
explode = (0.1, 0)  # Explode the first slice (Implemented)

plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title(f'Implementation Status: {implementation_percentage}% Implemented')
plt.savefig('assets/implementation_chart.svg', format='svg', bbox_inches='tight', transparent=True)

# Capitalize column names for better readability in the table
data.columns = [col.capitalize() for col in data.columns]

# Function to convert boolean values to colored text
def format_implemented(value):
    if str(value).lower() == 'true':
        return '✅ Yes'
    elif str(value).lower() == 'false':
        return '❌ No'
    else:
        return value

# Apply formatting
data['Implemented'] = data['Implemented'].apply(format_implemented)

# Sort by priority (if it's numerical)
try:
    data = data.sort_values(by='Priority')
except:
    pass  # Skip sorting if Priority is not numerical

# Convert DataFrame to markdown table
try:
    # Try using to_markdown if tabulate is installed
    markdown_table = data.to_markdown(index=False)
except ImportError:
    # Fallback to manual markdown table creation if tabulate is not available
    headers = data.columns.tolist()
    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join(["---" for _ in headers]) + " |"
    
    rows = []
    for _, row in data.iterrows():
        row_values = [str(val) for val in row.tolist()]
        rows.append("| " + " | ".join(row_values) + " |")
    
    markdown_table = "\n".join([header_line, separator_line] + rows)

# Implementation status content
implementation_status_content = f"""![Implementation Status](assets/implementation_chart.svg)

**{implemented_count} out of {len(data)} resources implemented ({implementation_percentage}%)**
"""

# Read the existing README.md file
try:
    with open('README.md', 'r') as f:
        readme_content = f.read()
except FileNotFoundError:
    # Create a basic README if it doesn't exist
    readme_content = """# Project Dashboard

## Implementation Status

Implementation status will be inserted here.

## Data Sources

Data sources table will be inserted here.
"""

# Update the Implementation Status section
if '## Implementation Status' in readme_content:
    pattern = r'(## Implementation Status\s*\n)[\s\S]*?(?=\n##|\Z)'
    replacement = r'\1' + implementation_status_content
    readme_content = re.sub(pattern, replacement, readme_content)
else:
    # Add Implementation Status section if it doesn't exist
    readme_content += f"\n\n## Implementation Status\n\n{implementation_status_content}"

# Update the Data Sources section
if '## Data Sources' in readme_content:
    pattern = r'(## Data Sources\s*\n)[\s\S]*?(?=\n##|\Z)'
    replacement = r'\1\n' + markdown_table + '\n'
    readme_content = re.sub(pattern, replacement, readme_content)
else:
    # Add Data Sources section if it doesn't exist
    readme_content += f"\n\n## Data Sources\n\n{markdown_table}\n"

# Write the updated content back to README.md
with open('README.md', 'w') as f:
    f.write(readme_content)

print("README.md updated successfully!")