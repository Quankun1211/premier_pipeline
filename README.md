# 🏆 Premier League Data Pipeline & Analytics System

[![Weekly Scraping Job](https://github.com/Quankun1211/premier_pipeline/actions/workflows/scrape_weekly.yml/badge.svg)](https://github.com/Quankun1211/premier_pipeline/actions)

## 📌 Project Overview
An automated **End-to-End Data Pipeline** designed to crawl Premier League player statistics, perform data cleaning, execute Machine Learning clustering, and generate interactive visual reports. The system is engineered to operate **100% autonomously** on a weekly schedule using GitHub Actions.

## 🏗 System Architecture
The system follows a modern data engineering architecture:
1. **Data Ingestion**: Utilizes **Selenium (Headless mode)** to scrape raw data from high-fidelity sports sources (The Analyst).
2. **Data Transformation (ETL)**: Implements data cleaning, logic standardization, and **K-Means Clustering** for player categorization.
3. **Storage**: Maintains a **SQLite Database** for master data (historical tracking) and exports optimized **Cleaned CSV** files for reporting.
4. **Orchestration**: Leverages **GitHub Actions** to coordinate the periodic execution of the entire workflow.
5. **Visualization**: An interactive **Power BI Dashboard** for advanced performance analysis (Goals vs. xG, Efficiency).

---

## 🛠 Tech Stack
- **Language**: Python (Pandas, Scikit-learn, Selenium).
- **Database**: SQLite.
- **CI/CD & Automation**: GitHub Actions.
- **Visualization**: Power BI (DAX, Advanced Analytics).
- **Environment**: Chrome WebDriver (Headless).

---

## 📊 Key Features & Analytics
- **K-Means Clustering**: Automatically segments players into three distinct groups: *Clinical Finishers*, *Efficient Scorers*, and *Potential Talents*.
- **Advanced Metrics**: Calculates sophisticated indicators such as `Goals per 90`, `xG Efficiency`, and `Shot Accuracy`.
- **Historical Tracking**: Features a `player_stats_history` table in SQLite to monitor player form fluctuations over the season.
- **Automated Workflow**: Scheduled to trigger at 00:00 UTC every Monday, ensuring fresh data for the start of each week.

---

## 🚀 Installation & Usage

1. **Clone the project:**
   ```bash
   git clone [https://github.com/Quankun1211/premier_pipeline.git](https://github.com/Quankun1211/premier_pipeline.git)
   cd premier_pipeline
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Run Locally:**
   ```bash
   python main.py

---

## 📈 Dashboard Preview

<p align="center">
  <img src="./image/image.png" alt="Premier League Dashboard" width="800">
</p>
