markdown1 = """
| Column Name                       | Attribute/Target | Data Type | Description                                                         |
|-----------------------------------|------------------|-----------|---------------------------------------------------------------------|
| ID                                | N/A              | Integer   | Unique identifier for each record.                                  |
| age                               | Attribute        | Integer   | Age of the individual in years.                                     |
| gender                            | Attribute        | String    | Gender of the individual (e.g., male, female).                      |
| education                         | Attribute        | String    | Highest level of education attained by the individual.              |
| class                             | Attribute        | String    | Socioeconomic class of the individual.                              |
| education_institute               | Attribute        | String    | Type of educational institute attended.                             |
| marital_status                    | Attribute        | String    | Marital status of the individual (e.g., single, married, divorced). |
| race                              | Attribute        | String    | Race of the individual.                                             |
| is_hispanic                       | Attribute        | Boolean   | Indicates whether the individual is of Hispanic origin.             |
| employment_commitment             | Attribute        | String    | Level of commitment to employment (e.g., full-time, part-time).     |
| unemployment_reason               | Attribute        | String    | Reason for unemployment (e.g., laid off, seeking work).             |
| employment_stat                   | Attribute        | String    | Current employment status of the individual.                        |
| wage_per_hour                     | Attribute        | Float     | Hourly wage of the individual.                                      |
| is_labor_union                    | Attribute        | Boolean   | Indicates whether the individual is a member of a labor union.      |
| working_week_per_year             | Attribute        | Integer   | Number of weeks worked per year.                                    |
| industry_code                     | Attribute        | Integer   | Code representing the industry of employment.                       |
| industry_code_main                | Attribute        | String    | Main industry code classification.                                  |
| occupation_code                   | Attribute        | Integer   | Code representing the occupation.                                   |
| occupation_code_main              | Attribute        | String    | Main occupation code classification.                                |
| total_employed                    | Attribute        | Integer   | Total number of individuals employed.                               |
| household_stat                    | Attribute        | String    | Household status of the individual.                                 |
| household_summary                 | Attribute        | String    | Summary of the household composition.                               |
| under_18_family                   | Attribute        | Integer   | Number of family members under 18 years old.                        |
| importance_of_record              | Attribute        | String    | Importance or priority of the record.                               |
| income_above_limit                | Target           | Boolean   | Indicates whether the individual's income is above a certain limit. |
"""


markdown2 = """ 
                | Column Name                       | Attribute/Target | Data Type | Description                                                         |
                |-----------------------------------|------------------|-----------|---------------------------------------------------------------------|
                | veterans_admin_questionnaire      | Attribute        | Boolean   | Indicates if the individual has completed the Veterans Administration questionnaire. |
                | vet_benefit                       | Attribute        | Boolean   | Indicates whether the individual receives veteran benefits.         |
                | tax_status                        | Attribute        | String    | Tax filing status of the individual.                                |
                | gains                             | Attribute        | Float     | Total gains (e.g., capital gains).                                  |
                | losses                            | Attribute        | Float     | Total losses (e.g., capital losses).                                |
                | stocks_status                     | Attribute        | String    | Status of stock ownership (e.g., own stocks, do not own stocks).    |
                | citizenship                       | Attribute        | String    | Citizenship status of the individual.                               |
                | mig_year                          | Attribute        | Integer   | Year of migration to the current country.                           |
                | country_of_birth_own              | Attribute        | String    | Country of birth of the individual.                                 |
                | country_of_birth_father           | Attribute        | String    | Country of birth of the individual's father.                        |
                | country_of_birth_mother           | Attribute        | String    | Country of birth of the individual's mother.                        |
                | migration_code_change_in_msa      | Attribute        | String    | Migration code indicating change within a Metropolitan Statistical Area (MSA). |
                | migration_prev_sunbelt            | Attribute        | Boolean   | Indicates whether the individual previously lived in the Sunbelt region. |
                | migration_code_move_within_reg    | Attribute        | String    | Migration code indicating movement within a region.                 |
                | migration_code_change_in_reg      | Attribute        | String    | Migration code indicating change within a region.                   |
                | residence_1_year_ago              | Attribute        | String    | Type of residence 1 year ago (e.g., same house, different house).   |
                | old_residence_reg                 | Attribute        | String    | Region of previous residence.                                       |
                | old_residence_state               | Attribute        | String    | State of previous residence.                                        |
                
                """