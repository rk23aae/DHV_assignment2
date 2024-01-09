import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

combined_happiness_data = pd.read_csv("Combined_Data.csv")

#Final
#Final
# Set the style for the plots
sns.set_style("darkgrid")
plt.rcParams.update({'font.size': 12})

# Define the figure for the infographic
fig, axes = plt.subplots(3, 2, figsize=(20, 25), gridspec_kw={'height_ratios': [1, 1, 0.2]})
fig.suptitle('Global Quest for Happiness: A Data-Driven Journey from 2015-2019', fontsize=40, fontweight='bold')
fig.set_facecolor('lightgray')

# Title and Student ID
plt.figtext(0.5, 0.01, "Name: RUCHITABEN SHAILESHBHAI KABARIYA - Student ID: 22062263", ha="center", fontsize=20, fontweight='bold', bbox={"facecolor":"orange", "alpha":0.5, "pad":5})

# Plot 1: Average happiness score by year
avg_happiness_by_year = combined_happiness_data.groupby('Year')['Happiness Score'].mean()
axes[0, 0].plot(avg_happiness_by_year.index, avg_happiness_by_year.values, marker='o', color='b')
axes[0, 0].set_title('Trend of Average Happiness Score by Year', fontsize=16)
axes[0, 0].set_xlabel('Year', fontsize=16)
axes[0, 0].set_ylabel('Average Happiness Score', fontsize=16)
axes[0, 0].tick_params(axis='both', which='major', labelsize=14)  # Increase tick label size

# Plot 2: Top 10 countries with the highest happiness score in the latest year
latest_year = combined_happiness_data['Year'].max()
top_countries_latest_year = combined_happiness_data[combined_happiness_data['Year'] == latest_year].nlargest(10, 'Happiness Score')
sns.barplot(x='Happiness Score', y='Country', data=top_countries_latest_year, ax=axes[0, 1], palette='coolwarm')
axes[0, 1].set_title(f'Top 10 Happiest Countries in {latest_year}', fontsize=16)
axes[0, 1].set_xlabel('Happiness Score', fontsize=16)
axes[0, 1].set_ylabel('Country', fontsize=16)
axes[0, 1].tick_params(axis='both', which='major', labelsize=14)  # Increase tick label size


# Plot 3: Average GDP per Capita and Happiness Score by Year
avg_gdp_happiness_by_year = combined_happiness_data.groupby('Year')[['Happiness Score', 'GDP per Capita']].mean()
axes[1, 0].bar(avg_gdp_happiness_by_year.index - 0.2, avg_gdp_happiness_by_year['Happiness Score'], width=0.4, label='Happiness Score', align='center')
axes[1, 0].bar(avg_gdp_happiness_by_year.index + 0.2, avg_gdp_happiness_by_year['GDP per Capita'], width=0.4, label='GDP per Capita', align='center')
axes[1, 0].set_title('Average Happiness Score and GDP per Capita by Year', fontsize=16)
axes[1, 0].set_xlabel('Year', fontsize=16)
axes[1, 0].set_ylabel('Average Score / GDP per Capita', fontsize=16)
axes[1, 0].legend()
axes[1, 0].tick_params(axis='both', which='major', labelsize=14)  # Increase tick label size

# Plot 4: Generosity Over the Years
sns.boxplot(data=combined_happiness_data, x='Year', y='Generosity', ax=axes[1, 1])
axes[1, 1].set_title('Generosity Over the Years', fontsize=16)
axes[1, 1].set_xlabel('Year', fontsize=16)
axes[1, 1].set_ylabel('Generosity', fontsize=16)
axes[1, 1].tick_params(axis='both', which='major', labelsize=14)  # Increase tick label size


# Enhanced explanations with introduction and conclusion remarks
intro_remark = "Embark on an insightful voyage through the World Happiness Report from 2015-2019, as we uncover the layers of what constitutes happiness across the globe. \nThis journey not only maps the contours of joy and contentment but also delves into the economic and altruistic fibers that intertwine to shape the well-being of societies.\n"
conclusion_remark = "\nIn conclusion, our global quest for happiness reveals a complex tapestry where economic prosperity and generosity play vital roles but are part of a broader picture. As we move forward, it \nbecomes increasingly clear that the pursuit of happiness is multifaceted, with cultural, social, and economic dimensions all weaving into the narrative of what makes a society thrive in joy."
explanations = [
    "1. The average happiness score indicates a notable dip and recovery, suggesting significant global events may influence collective well-being.",
    "2. The top 10 happiest countries consistently showcase strong social and economic foundations, hinting at the crucial role of systemic stability in fostering happiness.",
    "3. The comparison between happiness scores and GDP per capita across the years reflects an intriguing, but not perfect, correlation, \nimplying that while wealth may contribute to happiness, it is not the sole determinant.",
    "4. The generosity trend over the years remains relatively stable, with slight variations, indicating that the spirit of giving is resilient to changing times."
]

axes[2, 0].axis('off')
axes[2, 1].axis('off')

# Explanation text centrally aligned to the figure, below the plots
fig.text(0.03, 0.023, "\n".join([intro_remark] + explanations + [conclusion_remark]), ha='left', va='bottom', fontsize=15)

# Adjust layout for better visualization
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save the figure
plt.savefig("22062263.png", dpi=300)