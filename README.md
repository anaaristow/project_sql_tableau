# Project4 - Data Analysis for Firearms Sales and Gun Violence

## SQL - Tableau Project

![Alt text](usa.webp)

In this analysis, two datasets were employed, one sourced from the National Instant Criminal Background Check System (NICS)² database maintained by the FBI, and the other retrieved from Kaggle. The primary objective of this project is to examine and establish correlations between the total of firearms sales and incidents of gun violence.

The analysis involved extraction of data using Python, exploration through SQL queries, and visualization using Tableau.

## Libraries Used
- **Pandas**: Used for data manipulation and analysis.
- **Getpass**: Secure password input without displaying it on the screen.
- **SQLAlchemy (alch)**: A robust toolkit and Object-Relational Mapping (ORM) library for Python, making it easier and more flexible to interact with databases by translating Python code into SQL queries.

## Extraction
Functions were created to extract data, grouping it by state and year. This resulted in two datasets: one containing information about gun violence (columns: state, year, n_killed, n_injured) and another about firearms sales (columns: year, state, totals).

## Exploratory
SQL queries were executed using Python to perform a exploratory phase:

1. States with higher firearm sales and the number of injuries
2. Number of firearms sold and the total number of injuries in a given year
3. Relationship between states with higher ranks in gun sales and gun-related injuries
4. Number of gun incidents (both killed and injured) over the years

## Visualizations and Analysis
A dashboard was created using Tableau to visually represent the analysis objectives.

![Alt text](<Data Analysis for Firearms Sales & Gun Violence _ Tableau Public - Google Chrome 2023-11-20 22-23-47-1.gif>)

### Regression Equation

In the regression analysis, a model was developed to quantify the relationship between total gun sales and injuries. The equation Injuries=0.000863384×Total+16663.19
serves as a mathematical representation of this relationship. To illustrate, consider that for every 10,000 guns sold, an estimated increase of approximately 9 injuries is anticipated.

### R-Squared Value

The R-Squared value, at approximately 35.63%, indicates the proportion of the variability in injuries that can be explained by the total number of guns sold. The remaining 64.37% of the variability is ascribed to other variables not explicitly considered in this analysis.

### P-value

The low p-value obtained from the analysis rejects the null hypothesis, signaling that the number of guns sold significantly impacts the number of injuries. The p-value, often less than 0.0001, provides statistical evidence supporting the relationship observed.

## Conclusion
The analysis revealed significant insights. Despite not finding the expected outcomes, a relationship between total guns sold and injuries was identified using a regression equation.

In conclusion, although the expected results were not found, a meaningful relationship between gun sales and injuries was established. Further investigation into additional variables may contribute to a more comprehensive understanding of the factors influencing gun-related injuries.

# Links
[Tableau Dashboard](https://public.tableau.com/app/profile/ana.cidral/viz/DataAnalysisforFirearmsSalesGunViolence/Story1?publish=yes)

[Gun Violence Data](https://www.kaggle.com/datasets/jameslko/gun-violence-data/code)

[Firearms Sales](https://raw.githubusercontent.com/BuzzFeedNews/nics-firearm-background-checks/master/data/nics-firearm-background-checks.csv)