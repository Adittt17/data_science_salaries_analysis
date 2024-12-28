import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('DataScience_salaries_2024.csv')

# Preprocess dataset
data['work_year'] = data['work_year'].astype(str)

# Dashboard title
st.title('Data Science Salaries Dashboard')
st.header('Assignment Machine Learning Division - GDG')
st.subheader('Adityo Pangestu')
st.markdown("## Exploratory Data Analysis of Salaries")

# Sidebar options
st.sidebar.header("Visualization Options")
options = st.sidebar.multiselect(
    "Select visualizations to display:",
    [
        "Average Salary Over Work Years",
        "Salary Distribution by Work Year",
        "Average Salary by Experience Level",
        "Top Job Titles by Average Salary",
        "Average Salary by Company Size",
        "Average Salary by Employment Type",
        "Average Salary by Company Location",
        "Average Salary by Remote Ratio",
    ],
    default=["Average Salary Over Work Years"]
)

# Helper function to display plots
def plot_to_streamlit(plot_func):
    fig, ax = plt.subplots()
    plot_func(ax)
    st.pyplot(fig)

# 1. Average Salary Over Work Years
if "Average Salary Over Work Years" in options:
    st.subheader("Average Salary Over Work Years")
    work_year_salary_in_usd = data.groupby('work_year')['salary_in_usd'].mean().reset_index()

    def plot_avg_salary_over_years(ax):
        sns.lineplot(x='work_year', y='salary_in_usd', data=work_year_salary_in_usd, ax=ax)
        ax.set_title('Average Salary in USD Over Work Years')
        ax.set_xlabel('Work Year')
        ax.set_ylabel('Average Salary (USD)')

    plot_to_streamlit(plot_avg_salary_over_years)

# 2. Salary Distribution by Work Year
if "Salary Distribution by Work Year" in options:
    st.subheader("Salary Distribution by Work Year")

    def plot_salary_distribution(ax):
        sns.boxplot(x=data['work_year'], y=data['salary_in_usd'], palette="coolwarm", ax=ax)
        ax.set_title('Salary Distribution by Work Year')
        ax.set_xlabel('Work Year')
        ax.set_ylabel('Salary (USD)')

    plot_to_streamlit(plot_salary_distribution)

# 3. Average Salary by Experience Level
if "Average Salary by Experience Level" in options:
    st.subheader("Average Salary by Experience Level")
    experience_salary_avg = data.groupby('experience_level')['salary_in_usd'].mean().sort_values()

    def plot_experience_salary(ax):
        sns.barplot(x=experience_salary_avg.index, y=experience_salary_avg.values, palette="viridis", ax=ax)
        ax.set_title('Average Salary by Experience Level')
        ax.set_xlabel('Experience Level')
        ax.set_ylabel('Average Salary (USD)')

    plot_to_streamlit(plot_experience_salary)

# 4. Top Job Titles by Average Salary
if "Top Job Titles by Average Salary" in options:
    st.subheader("Top Job Titles by Average Salary")
    job_salary_avg = data.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(10)

    def plot_job_titles_salary(ax):
        sns.barplot(x=job_salary_avg.values, y=job_salary_avg.index, palette="plasma", ax=ax)
        ax.set_title('Top Job Titles by Average Salary')
        ax.set_xlabel('Average Salary (USD)')
        ax.set_ylabel('Job Title')

    plot_to_streamlit(plot_job_titles_salary)

# 5. Average Salary by Company Size
if "Average Salary by Company Size" in options:
    st.subheader("Average Salary by Company Size")
    company_size_salary_avg = data.groupby('company_size')['salary_in_usd'].mean()

    def plot_company_size_salary(ax):
        sns.barplot(x=company_size_salary_avg.index, y=company_size_salary_avg.values, palette="magma", ax=ax)
        ax.set_title('Average Salary by Company Size')
        ax.set_xlabel('Company Size')
        ax.set_ylabel('Average Salary (USD)')

    plot_to_streamlit(plot_company_size_salary)

# 6. Average Salary by Employment Type
if "Average Salary by Employment Type" in options:
    st.subheader("Average Salary by Employment Type")
    employment_salary_avg = data.groupby('employment_type')['salary_in_usd'].mean().sort_values()

    def plot_employment_type_salary(ax):
        sns.barplot(x=employment_salary_avg.index, y=employment_salary_avg.values, palette="YlGnBu", ax=ax)
        ax.set_title('Average Salary by Employment Type')
        ax.set_xlabel('Employment Type')
        ax.set_ylabel('Average Salary (USD)')

    plot_to_streamlit(plot_employment_type_salary)

# 7. Average Salary by Company Location
if "Average Salary by Company Location" in options:
    st.subheader("Average Salary by Company Location")
    company_location_salary_avg = data.groupby('company_location')['salary_in_usd'].mean().sort_values()

    def plot_company_location_salary(ax):
        sns.barplot(x=company_location_salary_avg.index, y=company_location_salary_avg.values, palette="YlOrBr", ax=ax)
        ax.set_title('Average Salary by Company Location')
        ax.set_xlabel('Company Location')
        ax.set_ylabel('Average Salary (USD)')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

    plt.figure(figsize=(20, 6))
    plot_to_streamlit(plot_company_location_salary)

# 8. Average Salary by Remote Ratio
if "Average Salary by Remote Ratio" in options:
    st.subheader("Average Salary by Remote Ratio")
    remote_salary_avg = data.groupby('remote_ratio')['salary_in_usd'].mean()

    def plot_remote_ratio_salary(ax):
        sns.lineplot(x=remote_salary_avg.index, y=remote_salary_avg.values, marker="o", ax=ax)
        ax.set_title('Average Salary by Remote Ratio')
        ax.set_xlabel('Remote Ratio')
        ax.set_ylabel('Average Salary (USD)')

    plot_to_streamlit(plot_remote_ratio_salary)
