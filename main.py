import pandas as pd
import src.extraction as ext

# Read the data about Gun Violence
incidents = pd.read_csv("data/gun_violence.csv", sep=';')
# Group gun violence incidents by year using a function from src/extraction.py
incidents_group = ext.group_df_incidents_per_year(incidents)
# Export to csv
incidents_group.to_csv("data/gun_violence_groupby.csv")


# Read the data about Firearms Sales
gun_sold = pd.read_csv("data/firearm_sales.csv", sep=';')
# Group firearm sales by year using a function from src/extraction.py
gun_sold_group = ext.group_df_guns_sold_per_year(gun_sold)
# Export to csv
gun_sold_group.to_csv("data/firearm_sales_groupby.csv")