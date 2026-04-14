import sqlite3
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path='data/premier_league.db'):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

    def save_data(self, df, table_name='player_stats'):
        conn = sqlite3.connect(self.db_path)
        try:
            # 1. Lưu bảng Snapshot (Ghi đè - Dùng cho truy vấn nhanh hiện tại)
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            
            # 2. Lưu bảng History (Thêm mới - Có gắn timestamp để theo dõi lịch sử)
            df_history = df.copy()
            df_history['scraped_at'] = datetime.now().strftime("%Y-%m-%d")
            df_history.to_sql(f"{table_name}_history", conn, if_exists='append', index=False)
            
            print(f"Successfully saved to DB: {self.db_path}")
        finally:
            conn.close()