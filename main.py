from src.scraper import PremierLeagueScraper
from src.processor import DataProcessor
from src.database import DatabaseManager

def main():
    URL = "https://theanalyst.com/competition/premier-league/stats"
    
    scraper = PremierLeagueScraper(URL)
    raw_df = scraper.get_raw_data()
    
    processor = DataProcessor()
    cleaned_df = processor.clean_data(raw_df)
    final_df = processor.add_clusters(cleaned_df)
    
    print("Step 3: Saving to SQLite (Master Storage)...")
    db_manager = DatabaseManager()
    db_manager.save_data(final_df)
    
    print("Step 4: Exporting cleaned CSV for Power BI...")
    csv_path = "data/premier_league_cleaned.csv"
    final_df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    
    print(f"Pipeline completed! Cleaned data available at {csv_path}")

if __name__ == "__main__":
    main()