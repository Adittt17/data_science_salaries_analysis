import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Page config ---
st.set_page_config(page_title="Data Science Salaries", layout="wide")
sns.set_style("whitegrid")

# --- Load dataset ---
data = pd.read_csv('DataScience_salaries_2024.csv')
data['work_year'] = data['work_year'].astype(str)

# --- Header ---
st.title("💼 Data Science Salaries Dashboard")
st.markdown("##### Data Analyst | By: Adityo Pangestu")
st.markdown("Explore salary insights from the global data science workforce. Use the sidebar to customize your view.")

# --- Insight utama ---
st.info("🔍 **Insight:** Experience level is the most significant factor in determining an individual's salary.")

# --- Sidebar Options ---
st.sidebar.header("📌 Visualization Options")
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

# --- Plot Helper ---
def plot_to_streamlit(plot_func, figsize=(10, 6)):
    fig, ax = plt.subplots(figsize=figsize)
    plot_func(ax)
    st.pyplot(fig)

# === VISUALIZATIONS ===

# 1. Average Salary Over Work Years
if "Average Salary Over Work Years" in options:
    st.subheader("📈 Average Salary Over Work Years")
    avg_salary_by_year = data.groupby('work_year')['salary_in_usd'].mean().reset_index()

    def plot_avg_salary(ax):
        sns.lineplot(data=avg_salary_by_year, x='work_year', y='salary_in_usd', marker='o', ax=ax)
        ax.set_title("Yearly Average Salary (USD)")
        ax.set_xlabel("Work Year")
        ax.set_ylabel("Avg Salary (USD)")

    plot_to_streamlit(plot_avg_salary)
    st.success("""
    🧠 **Insight:**  
    Average salary has increased steadily each year, indicating a positive trend in compensation for data science roles.  
    This could reflect growing demand and competition for talent in the industry.
    """)

# 2. Salary Distribution by Work Year
if "Salary Distribution by Work Year" in options:
    st.subheader("📊 Salary Distribution by Work Year")

    def plot_distribution(ax):
        sns.boxplot(data=data, x='work_year', y='salary_in_usd', palette='coolwarm', ax=ax)
        ax.set_title("Salary Distribution (USD) by Year")
        ax.set_xlabel("Work Year")
        ax.set_ylabel("Salary (USD)")

    plot_to_streamlit(plot_distribution)
    st.info("""
    📌 **Insight:**  
    While the median salary has increased over time, salary variability is also rising — especially in the latest years.  
    This suggests broader salary ranges due to factors like region, company size, or job specialization.
    """)

# 3. Average Salary by Experience Level
if "Average Salary by Experience Level" in options:
    st.subheader("👤 Average Salary by Experience Level")
    experience_salary = data.groupby('experience_level')['salary_in_usd'].mean().sort_values()

    def plot_experience(ax):
        sns.barplot(x=experience_salary.index, y=experience_salary.values, palette='viridis', ax=ax)
        ax.set_title("Avg Salary by Experience Level")
        ax.set_xlabel("Experience Level")
        ax.set_ylabel("Avg Salary (USD)")

    plot_to_streamlit(plot_experience)
    st.success(f"""
    🧠 **Insight:**  
    There is a clear positive correlation between experience level and salary.  
    **Entry-level roles (EN)** earn significantly less than **Senior-level roles (SE)** or **Executive (EX)**.  
    Experience is the strongest predictor of salary range in the dataset.
    """)

# 4. Top Job Titles by Average Salary
if "Top Job Titles by Average Salary" in options:
    st.subheader("🏆 Top Job Titles by Average Salary")
    top_jobs = data.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(10)

    def plot_top_jobs(ax):
        sns.barplot(x=top_jobs.values, y=top_jobs.index, palette="plasma", ax=ax)
        ax.set_title("Top 10 Job Titles by Avg Salary")
        ax.set_xlabel("Avg Salary (USD)")
        ax.set_ylabel("Job Title")

    plot_to_streamlit(plot_top_jobs)
    st.info("""
    🏅 **Insight:**  
    Roles like **Analytics Engineering Manager** and **Data Science Tech Lead** dominate the top salary tier.  
    This shows that specialized or leadership roles drive higher compensation.
    """)

# 5. Average Salary by Company Size
if "Average Salary by Company Size" in options:
    st.subheader("🏢 Average Salary by Company Size")
    size_salary = data.groupby('company_size')['salary_in_usd'].mean()

    def plot_company_size(ax):
        sns.barplot(x=size_salary.index, y=size_salary.values, palette="magma", ax=ax)
        ax.set_title("Avg Salary by Company Size")
        ax.set_xlabel("Company Size")
        ax.set_ylabel("Avg Salary (USD)")

    plot_to_streamlit(plot_company_size)
    st.info("""
    🏭 **Insight:**  
    Mid-size companies tend to offer higher salaries, but Large companies are often competitive too.  
    Startups and small orgs may offer lower base pay but compensate via equity or perks.
    """)

# 6. Average Salary by Employment Type
if "Average Salary by Employment Type" in options:
    st.subheader("📃 Average Salary by Employment Type")
    employment_salary = data.groupby('employment_type')['salary_in_usd'].mean().sort_values()

    def plot_employment_type(ax):
        sns.barplot(x=employment_salary.index, y=employment_salary.values, palette="YlGnBu", ax=ax)
        ax.set_title("Avg Salary by Employment Type")
        ax.set_xlabel("Employment Type")
        ax.set_ylabel("Avg Salary (USD)")

    plot_to_streamlit(plot_employment_type)
    st.info("""
    📄 **Insight:**  
    **Contract and part time roles** may vary in pay, but **full-time positions** consistently provide higher average salaries.  
    Stable employment correlates with better compensation.
    """)

# 7. Average Salary by Company Location
if "Average Salary by Company Location" in options:
    st.subheader("🌍 Average Salary by Company Location")
    location_salary = data.groupby('company_location')['salary_in_usd'].mean().sort_values(ascending=False).head(10)

    def plot_company_location(ax):
        sns.barplot(x=location_salary.values, y=location_salary.index, palette="YlOrBr", ax=ax)
        ax.set_title("Top 10 Company Locations by Avg Salary")
        ax.set_xlabel("Avg Salary (USD)")
        ax.set_ylabel("Company Location")

    plot_to_streamlit(plot_company_location)
    st.info("""
    🌐 **Insight:**    
    Location remains a key factor in salary variation — often due to cost of living and tech maturity.
    """)

# 8. Average Salary by Remote Ratio
if "Average Salary by Remote Ratio" in options:
    st.subheader("🛰️ Average Salary by Remote Ratio")
    remote_salary = data.groupby('remote_ratio')['salary_in_usd'].mean()

    def plot_remote(ax):
        sns.lineplot(x=remote_salary.index, y=remote_salary.values, marker='o', ax=ax)
        ax.set_title("Avg Salary by Remote Work Ratio")
        ax.set_xlabel("Remote Ratio (%)")
        ax.set_ylabel("Avg Salary (USD)")

    plot_to_streamlit(plot_remote)
    st.info("""
    💻 **Insight:**  
    Surprisingly, **fully on-site roles (0% remote)** have the highest average salaries.  
    This may indicate that top-paying companies still value in-person presence for certain strategic or high-impact roles.  
    Remote and hybrid jobs offer flexibility, but may not always come with the highest pay.
    """)


# --- Footer ---
st.markdown("---")
st.caption("Created with by Adityo Pangestu · Dataset: Data Science Salaries 2024")
