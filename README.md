<a name="readme-top"></a>

<div align="center">
  <h1><b>Income Prediction Challenge for Azubian</b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [Project Description ](#Sepsi-Insights)
  - [🛠 Built with ](#-built-with-)
    - [Tech Stack ](#tech-stack-)
  - [Key Insights ](#key-features-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [👥 Authors ](#-authors-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🙏 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

# Income prediction for Azubian <a name="about-project"></a>

**Income Prediction Challenge for Azubian** Income inequality, characterized by the uneven distribution of income within a population, is a growing concern in developing nations worldwide. The rapid advancement of AI and automation could exacerbate this issue if not addressed. This challenge aims to develop a machine learning model that predicts whether an individual earns above or below a certain income threshold. By leveraging such models, we can potentially reduce costs and enhance the accuracy of monitoring critical population indicators, such as income levels, between census years. This information is crucial for policymakers to better manage and mitigate income inequality on a global scale.


### Data Dictionary

| Column Name                         | Attribute/Target | Data Type | Description                                                                                 |
|-------------------------------------|------------------|-----------|---------------------------------------------------------------------------------------------|
| **ID**                              | N/A              | Integer    | Unique identifier for each record.                                                          |
| **age**                             | Attribute        | Integer    | Age of the individual in years.                                                             |
| **gender**                          | Attribute        | String     | Gender of the individual (e.g., male, female).                                              |
| **education**                       | Attribute        | String     | Highest level of education attained by the individual.                                      |
| **class**                           | Attribute        | String     | Socioeconomic class of the individual.                                                      |
| **education_institute**             | Attribute        | String     | Type of educational institute attended.                                                     |
| **marital_status**                  | Attribute        | String     | Marital status of the individual (e.g., single, married, divorced).                         |
| **race**                            | Attribute        | String     | Race of the individual.                                                                     |
| **is_hispanic**                     | Attribute        | Boolean    | Indicates whether the individual is of Hispanic origin.                                     |
| **employment_commitment**           | Attribute        | String     | Level of commitment to employment (e.g., full-time, part-time).                             |
| **unemployment_reason**             | Attribute        | String     | Reason for unemployment (e.g., laid off, seeking work).                                     |
| **employment_stat**                 | Attribute        | String     | Current employment status of the individual.                                                |
| **wage_per_hour**                   | Attribute        | Float      | Hourly wage of the individual.                                                              |
| **is_labor_union**                  | Attribute        | Boolean    | Indicates whether the individual is a member of a labor union.                              |
| **working_week_per_year**           | Attribute        | Integer    | Number of weeks worked per year.                                                            |
| **industry_code**                   | Attribute        | Integer    | Code representing the industry of employment.                                               |
| **industry_code_main**              | Attribute        | String     | Main industry code classification.                                                          |
| **occupation_code**                 | Attribute        | Integer    | Code representing the occupation.                                                           |
| **occupation_code_main**            | Attribute        | String     | Main occupation code classification.                                                        |
| **total_employed**                  | Attribute        | Integer    | Total number of individuals employed.                                                       |
| **household_stat**                  | Attribute        | String     | Household status of the individual.                                                         |
| **household_summary**               | Attribute        | String     | Summary of the household composition.                                                       |
| **under_18_family**                 | Attribute        | Integer    | Number of family members under 18 years old.                                                |
| **veterans_admin_questionnaire**    | Attribute        | Boolean    | Indicates if the individual has completed the Veterans Administration questionnaire.        |
| **vet_benefit**                     | Attribute        | Boolean    | Indicates whether the individual receives veteran benefits.                                 |
| **tax_status**                      | Attribute        | String     | Tax filing status of the individual.                                                        |
| **gains**                           | Attribute        | Float      | Total gains (e.g., capital gains).                                                          |
| **losses**                          | Attribute        | Float      | Total losses (e.g., capital losses).                                                        |
| **stocks_status**                   | Attribute        | String     | Status of stock ownership (e.g., own stocks, do not own stocks).                            |
| **citizenship**                     | Attribute        | String     | Citizenship status of the individual.                                                       |
| **mig_year**                        | Attribute        | Integer    | Year of migration to the current country.                                                   |
| **country_of_birth_own**            | Attribute        | String     | Country of birth of the individual.                                                         |
| **country_of_birth_father**         | Attribute        | String     | Country of birth of the individual's father.                                                |
| **country_of_birth_mother**         | Attribute        | String     | Country of birth of the individual's mother.                                                |
| **migration_code_change_in_msa**    | Attribute        | String     | Migration code indicating change within a Metropolitan Statistical Area (MSA).              |
| **migration_prev_sunbelt**          | Attribute        | Boolean    | Indicates whether the individual previously lived in the Sunbelt region.                    |
| **migration_code_move_within_reg**  | Attribute        | String     | Migration code indicating movement within a region.                                         |
| **migration_code_change_in_reg**    | Attribute        | String     | Migration code indicating change within a region.                                           |
| **residence_1_year_ago**            | Attribute        | String     | Type of residence 1 year ago (e.g., same house, different house).                           |
| **old_residence_reg**               | Attribute        | String     | Region of previous residence.                                                               |
| **old_residence_state**             | Attribute        | String     | State of previous residence.                                                                |
| **importance_of_record**            | Attribute        | String     | Importance or priority of the record.                                                       |
| **income_above_limit**              | Target           | Boolean    | Indicates whether the individual's income is above a certain limit.                         |



## 🛠 Built With <a name="Technologies Used"></a>
Income Prediction Challenge for Azubian was done following the CRISP-DM process. It also involved a variety of technologies, programming languages, and libraries to process, analyze, and visualize the data. The following tools were utilized:
1. _Python_: Python programming language was the backbone of the project, used for data processing, analysis, and visualization tasks.

2. _Pandas_ and NumPy: Pandas and NumPy libraries were essential for data manipulation and numerical computations.

3. _Matplotlib and Seaborn_: Matplotlib and Seaborn were employed for data visualization, creating insightful charts and graphs to represent the findings.

4. _Visual Studio Code and Jupyter Notebooks_: Jupyter Notebooks within the Visual Studio IDE provided an interactive environment for running code, visualizing data, and documenting the analysis process.

5. _Scikit-learn_: Scikit-learn's library SimpleImputer was utilized for imputing null values in the amount column.

6. _Streamlit_: Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver interactive data apps – in only a few lines of code.

7. _FastAPI_: is a web framework first released in 2018 for building HTTP-based service APIs in Python. It is used for building APIs with Python 3.8+ based on standard Python-type hints. FastAPI is based on Pydantic and uses type hints to validate, serialize and deserialize data.

8. _Docker_: Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. The service has both free and premium tiers. The software that hosts the containers is called Docker Engine.

9. _Optuna_: Optuna is an automatic hyperparameter optimization software framework, particularly designed for machine learning.

10. _GitHub_: GitHub served as the version control system for the project, enabling collaboration and tracking changes in the codebase.
    These technologies played a crucial role in the successful implementation of the project, providing the necessary tools to analyze and derive insights from the Indian Startup Ecosystem funding datasets.

<details>
  <summary>Data Sources</summary>
  <p>The dataset provided for this project was provided by Zindi for their learning competition dubbed 'Income Prediction Challenge For Azubian'. It includes various citizens and non-citizens demographic attributes and their corresponding incomes collected from a random population. There are ~200 000 individuals in train and ~100 000 individuals in the test file. The dataset is subject to strict usage restrictions and can only be used for the purpose of this assignment. The data directory consists of both the training and testing data.</p>
</details>


<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>


<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Success Criteria <a name="key-features"></a>
- Accuracy: The model's should obtain an accuracy of 75% or higher.
- Precision and Recall:The final model should maintain both Precision and Recall scores of 0.75 or above.
- F1 Score: The final model should attain an F1 score of 0.75 to 0.85 or higher according to state-of-the-art SOTA models
Area Under the Receiver Operating Characteristic Curve (AUC-ROC): According to the state-of-the-art SOTA models for income prediction should achieve AUC-ROC scores in the range of 0.80 to 0.90 or higher.

## Key Insights <a name="key-Insights"></a>
The distilled recommendations are as follows:
1. .


 
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python


### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone https://github.com/Azubi-Team-Selenium/Income_prediction_for_Azubian.git
```

Change into the cloned repository

```sh
  cd Income_prediction_for_Azubian
  
```

Create a virtual environment

```sh

python -m venv env

```

Activate the virtual environment

```sh
    env/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```

## Running The Docker Images from Dockerhub

To run the Docker images on your local machine, follow these steps.

### Prerequisites

In order to run this project, you need:

- Python installed on your machine

### Steps

1. **Install Docker**

   If you haven't already installed Docker, you can download and install it from the [official Docker website](https://www.docker.com/get-started). Follow the installation instructions specific to your operating system.

2. **Pull the Docker Images**

   Open your terminal or command prompt and pull the required Docker images from Dockerhub using the following commands:

   ``` sh
   docker pull 
   docker pull 
   ```

  ``` sh
   docker run -d --name mycontainer -p
   docker run -d --name mycontainer -p 
   ```
### Streamlit frontend application

[client](https://income-iq-frontend-latest-2.onrender.com)


<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Bright Kwarteng Senior Adu**

- GitHub: [GitHub Profile](https://github.com/adubrightkwartengsnr)
- LinkedIn: [LinkedIn Profile](www.linkedin.com/in/bright-adu-kwarteng-snr)

🕵🏽‍♀️ **Success Makafui Kwawu**

- GitHub: [GitHub Profile](https://github.com/Makafui-Kwawu)
- LinkedIn: [LinkedIn Profile](www.linkedin.com/in/smkwawu/)

🕵🏽‍♀️ **Florence Josephina Laryea**

- GitHub: [GitHub Profile](https://github.com/FloJoLaryea)
- LinkedIn: [LinkedIn Profile](www.linkedin.com/in/flojolaryea)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


  
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

We would like to express my sincere gratitude to our instructors Racheal Appiah-Kubi and Glen Anum for their exceptional guidance, unwavering support, and invaluable mentorship throughout the course of this project. Their expertise, dedication, and commitment to our learning journey have been instrumental in shaping our understanding and skills in data analysis.

We would also like to extend a special thank you to Solomon Nyamson for his valuable advice and insights shared during the development of this project. His experiences and expertise in similar projects have been a source of inspiration and guidance, enriching our project with practical knowledge.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>





