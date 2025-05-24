# Data Science Salaries Analysis and Dashboard

## Description
This project aims to analyze salary data for professions in the field of Data Science, visualize the results of the analysis, and present an interactive dashboard using Streamlit. The dashboard allows users to explore various salary-related insights based on factors such as remote work ratio, experience level, company location, and more.

## Feature
1. **Data Analysis**
   - Analyze the relationship between work experience and salary.
   - Calculate average salaries based on remote work ratio, company size, job type, and company location.
   - Identify key patterns in the data, such as factors that significantly influence salaries.

2. **Data Visualization**
   - Create various visualizations such as line plots, bar plots, and box plots to illustrate the analysis results.
   - Provide visual representations that are easy for users to understand.

3. **Interactive Dashboard**
   - Develop dashboards using Streamlit to present analysis results and visualizations.
   - This dashboard has been deployed so it can be accessed online.

## Installation
### Prerequisite
Make sure you have Python 3.8 or later and a virtual environment enabled.

1. Clone repository:
   ```bash
   git clone https://github.com/Adittt17/data_science_salaries.git
   ```
2. Go to the project directory:
   ```bash
   cd dashboard.py
   ```
3. Activate virtual environment:
   ```bash
   source myenv/bin/activate  # Mac/Linux
   myenv\Scripts\activate   # Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Locally
1. Run the dashboard with the following command:
   ```bash
   streamlit run dashboard.py
   ```
2. The dashboard will be available in your browser at `http://localhost:8501`.

## Access Deployed Dashboard
The dashboard has been deployed and can be accessed via the following link.:
[**Data Science Salaries Dashboard**](https://adit-data-science-salaries.streamlit.app/)

## Main Visualization
1. **Average Salary Based on Remote Ratio**:
   - Shows that onsite jobs have the highest average salary, followed by fully remote jobs, and hybrid in last place.

2. **Salary Distribution by Year**:
   - Compare salary distributions across years to identify upward or downward trends.

3. **Highest Paying Jobs**:
   - Showing 10 professions in the field of Data Science with the highest average salary.

4. **Relationship between Experience and Salary**:
   - Visualization of the direct relationship between experience level (junior, mid-level, senior) and average salary.

## Contribution
We welcome contributions! If you have an idea or would like to add a new feature, please follow these steps::
1. Fork this repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Adding new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin new_feature
   ```
5. Submit a pull request.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this project provided you acknowledge the original copyright notice.
