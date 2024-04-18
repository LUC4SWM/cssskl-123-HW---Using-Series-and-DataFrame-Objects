import pandas as pd

# Task 1:
filename = 'flag.data'
headers = ['name', 'landmass', 'zone', 'area', 'population', 'language', 'religion', 'bars', 'stripes', 'colours',
           'red', 'green', 'blue', 'gold', 'white', 'black', 'orange', 'mainhue', 'circles', 'crosses',
           'saltires', 'quarters', 'sunstars', 'crescent', 'triangle', 'icon', 'animate', 'text', 'topleft', 'botright']

# Read in the data file and label the columns
df_flag = pd.read_csv(filename, names=headers, low_memory=False)

# Task 2:

# Count the number of countries in North America
count_NA = df_flag[df_flag['landmass'] == 1]['landmass'].count()

print('*** Task 2 ***\nNumber in North America: ' + str(count_NA))

# Task 3:
print('\n*** Task 3 ***')

# With explicit looping
landmass_counts = {}  # Dictionary to hold count-values for each landmass
for index, row in df_flag.iterrows():
    landmass_value = row['landmass']
    if landmass_value in landmass_counts:
        landmass_counts[landmass_value] += 1
    else:
        landmass_counts[landmass_value] = 1
print('Using explicit loops:')
for landmass, count in sorted(landmass_counts.items()):
    print(landmass, '  ', count)

# Without explicit looping
print('\nWithout using explicit loops:\n' + str(df_flag.groupby('landmass')['name'].count()))

# Task 4:
print('\n*** Task 4 ***')

print('Population (in millions) for speakers of each language: ')

# Total population of countries that speak each language
grouped_populations_by_language = df_flag.groupby('language')['population'].sum()
print(grouped_populations_by_language.sort_values(ascending=False))

# Filtered population for countries with national populations less than 50 million
filtered_df_flag = df_flag[df_flag['population'] < 50]
grouped_filtered_populations_by_language = filtered_df_flag.groupby('language')['population'].sum()
print('\nFiltered to only include countries with populations under 50 million:\n',
      grouped_filtered_populations_by_language.sort_values(ascending=False))

""" 
    > Q: Any conclusions you can make from the different charts? 
    
    > A: The charts show that languages like 6 (Other 
    Indo-European) and 7 (Chinese) are associated with countries that have larger populations, potentially indicating 
    their widespread use or dominance in populous regions. Filtering for countries with populations under 50 million 
    reveals the population distribution across languages in smaller countries, highlighting the diverse linguistic 
    landscape across different population sizes.
"""


# Task 5:
print('\n*** Task 5 ***')

# Employee data
df_reps = pd.DataFrame({'Rep Name': ['Max', 'Jill', 'Fong', 'Juanita', 'Nya'],
                        'Rep Language': [1, 2, 5, 5, 8]})

# Merge flags dataset with employee dataset
merged_df = pd.merge(df_flag, df_reps, left_on='language', right_on='Rep Language', how='inner')
# Drop unneeded column
merged_df.drop('Rep Language', axis=1, inplace=True)

# Count the total number of representative-countries
repped_country_count = merged_df['Rep Name'].notnull().sum()
print("Total representative-countries: ", repped_country_count)

# Task 6:
print("\n*** Task 6 ***")

# Create a pivot table to show total area of countries for each combination of landmass and language
table = df_flag.pivot_table(values='area', aggfunc='sum', columns='language', index='landmass')
print(table)
"""
    Q: What do the NaN values mean in that table?
    
    A: In the case of this table, the NaN values indicate that there are no countries within the dataset that possess 
    that combination of landmass and language. For example, landmass

"""