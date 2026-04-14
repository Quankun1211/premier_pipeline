import pandas as pd
from sklearn.cluster import KMeans

class DataProcessor:
    @staticmethod
    def clean_data(df):
        df = df.copy()
        
        if "conv %" in df.columns:
            df["conv %"] = df["conv %"].str.replace('%', '', regex=False).astype(float)

        numeric_cols = ['apps', 'mins', 'goals', 'xg', 'goals_vs_xg', 'shots', 'sot', 'xg_per_shot']
        df.columns = [col.strip().replace(' ', '_').replace('%', 'Rate') for col in df.columns]
        
        target_numeric = [col.lower() for col in df.columns if col.lower() in [c.lower().replace(' ', '_') for c in numeric_cols]]
        for col in df.columns:
            if col.lower().replace(' ', '_') in [c.lower() for c in numeric_cols]:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        df = df[df['mins'] >= 90].reset_index(drop=True)
        df = df.fillna(0)

        if 'sot' in df.columns and 'shots' in df.columns:
            invalid_shots = df[df['sot'] > df['shots']]
            if not invalid_shots.empty:
                print(f"Cảnh báo: Có {len(invalid_shots)} dòng dữ liệu sot > shots. Đang hiệu chỉnh...")
                df.loc[df['sot'] > df['shots'], 'sot'] = df['shots']

        df['goals_per_90'] = (df['goals'] / df['mins']) * 90
        df['xg_per_90'] = (df['xg'] / df['mins']) * 90
        df['shots_per_90'] = (df['shots'] / df['mins']) * 90
        
        df['shot_accuracy'] = (df['sot'] / df['shots']).fillna(0)
        
        if 'name' in df.columns:
            df['name'] = df['name'].str.strip()
            
        df.columns = [col.strip().replace(' ', '_').replace('%', 'Rate') for col in df.columns]

        if 'conv_rate' in df.columns:
            df['conv_rate'] = df['conv_rate'] / 100

        print("--- THÔNG TIN CẤU TRÚC BẢNG ---")
        print(df.info())
        return df

    @staticmethod
    def add_clusters(df):
        required_features = ['goals_per_90', 'xg_per_90', 'shot_accuracy']
        if all(col in df.columns for col in required_features):
            features = df[required_features]
            kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
            df['player_segment'] = kmeans.fit_predict(features)
        else:
            print("Lỗi: Thiếu cột dữ liệu để phân cụm.")
        return df