import sqlite3
import pandas as pd

# 1. 샘플 데이터베이스 생성 및 가상 테이블 구축
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT,
    age INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
"""
)

cursor.execute(
    """
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT,
    price REAL NOT NULL,
    stock_quantity INTEGER
)
"""
)

# 샘플 데이터 삽입
cursor.execute(
    "INSERT INTO users VALUES (1, 'Alice', 'alice@email.com', 28, '2026-01-10')"
)
cursor.execute("INSERT INTO users VALUES (2, 'Bob', NULL, 34, '2026-02-15')")
cursor.execute(
    "INSERT INTO products VALUES (101, '수분 크림', '스킨케어', 25000.0, 50)"
)
cursor.execute(
    "INSERT INTO products VALUES (102, '선크림', '스킨케어', 18000.0, NULL)"
)
conn.commit()


# 2. 카탈로그 분석 클래스 정의
class DatabaseCatalogAnalyzer:

    def __init__(self, connection):
        self.conn = connection

    def get_table_list(self):
        """데이터베이스 내 전체 테이블 목록 조회"""
        query = (
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT"
            " LIKE 'sqlite_%';"
        )
        return pd.read_sql_query(query, self.conn)["name"].tolist()

    def analyze_schema_catalog(self):
        """전체 테이블의 스키마 구조 분석 (컬럼명, 데이터 타입, PK 여부 등)"""
        catalog_schema = []
        tables = self.get_table_list()

        for table in tables:
            info_df = pd.read_sql_query(f"PRAGMA table_info('{table}');", self.conn)
            for _, row in info_df.iterrows():
                catalog_schema.append(
                    {
                        "table_name": table,
                        "column_name": row["name"],
                        "data_type": row["type"],
                        "not_null": bool(row["notnull"]),
                        "is_primary_key": bool(row["pk"]),
                    }
                )

        return pd.DataFrame(catalog_schema)

    def analyze_data_quality(self):
        """테이블별 데이터 건수 및 결측치 현황 분석"""
        quality_report = []
        tables = self.get_table_list()

        for table in tables:
            df = pd.read_sql_query(f"SELECT * FROM {table}", self.conn)
            total_rows = len(df)

            for col in df.columns:
                null_count = df[col].isnull().sum()
                null_ratio = (null_count / total_rows) * 100 if total_rows > 0 else 0
                quality_report.append(
                    {
                        "table_name": table,
                        "column_name": col,
                        "total_rows": total_rows,
                        "null_count": null_count,
                        "null_ratio(%)": round(null_ratio, 2),
                    }
                )

        return pd.DataFrame(quality_report)


# 3. 분석 실행 및 결과 출력
analyzer = DatabaseCatalogAnalyzer(conn)

print("=== 1. 스키마 카탈로그 분석 ===")
df_schema = analyzer.analyze_schema_catalog()
print(df_schema.to_string(index=False))

print("\n=== 2. 데이터 품질 카탈로그 분석 ===")
df_quality = analyzer.analyze_data_quality()
print(df_quality.to_string(index=False))

# 연결 종료
conn.close()