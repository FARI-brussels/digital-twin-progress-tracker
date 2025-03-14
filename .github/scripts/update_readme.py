import pandas as pd
import matplotlib.pyplot as plt
import os

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
markdown_table = data.to_markdown(index=False)

# Create README content
readme_content = f"""# Data Resources Dashboard

## Implementation Status

![Implementation Status](assets/implementation_chart.svg)

**{implemented_count} out of {len(data)} resources implemented ({implementation_percentage}%)**

## Available Data Resources

{markdown_table}

---

*This dashboard is automatically generated based on data.csv*
"""

# Write to README.md
with open('README.md', 'w') as f:
    f.write(readme_content)

print("README.md updated successfully!")