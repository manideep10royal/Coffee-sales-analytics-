import os
import sys
from datetime import datetime

try:
    import pandas as pd
except ImportError:
    print("Missing required package: pandas")
    print("Install it with: python -m pip install pandas")
    sys.exit(1)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'index (1).csv')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'analysis_outputs')


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date
    df['money'] = pd.to_numeric(df['money'], errors='coerce')
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates()
    df = df[df['datetime'].notna()]
    df = df[df['money'].notna()]
    df['weekday'] = df['datetime'].dt.day_name()
    df['hour'] = df['datetime'].dt.hour
    df['payment_method'] = df['cash_type'].fillna('unknown').str.lower()
    return df


def save_output(df: pd.DataFrame, filename: str) -> str:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)
    df.to_csv(path, index=False)
    return path


def main() -> None:
    print('Loading dataset from', DATA_FILE)
    df = load_data(DATA_FILE)

    print('Original rows:', len(df))
    df = clean_data(df)
    print('Rows after cleaning:', len(df))

    print('\nMissing value summary:')
    print(df.isna().sum())

    print('\nSales summary:')
    print(df['money'].describe())

    totals = {
        'total_transactions': len(df),
        'total_sales': df['money'].sum(),
        'average_sale': df['money'].mean(),
        'min_sale': df['money'].min(),
        'max_sale': df['money'].max(),
    }
    for key, value in totals.items():
        print(f'{key}: {value}')

    top_products = (
        df.groupby('coffee_name')
        .agg(transaction_count=('coffee_name', 'size'), total_sales=('money', 'sum'))
        .sort_values(['total_sales', 'transaction_count'], ascending=False)
        .reset_index()
    )
    print('\nTop products by sales:')
    print(top_products.head(10).to_string(index=False))

    sales_by_weekday = (
        df.groupby('weekday')
        .agg(total_sales=('money', 'sum'), transactions=('money', 'size'))
        .reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        .reset_index()
    )
    print('\nSales by weekday:')
    print(sales_by_weekday.to_string(index=False))

    sales_by_hour = (
        df.groupby('hour')
        .agg(total_sales=('money', 'sum'), transactions=('money', 'size'))
        .reset_index()
        .sort_values('hour')
    )
    print('\nSales by hour:')
    print(sales_by_hour.to_string(index=False))

    payment_summary = (
        df.groupby('payment_method')
        .agg(total_sales=('money', 'sum'), transactions=('money', 'size'))
        .reset_index()
    )
    print('\nPayment method summary:')
    print(payment_summary.to_string(index=False))

    daily_sales = (
        df.groupby('date')
        .agg(total_sales=('money', 'sum'), transactions=('money', 'size'))
        .reset_index()
    )
    print('\nDaily sales sample:')
    print(daily_sales.head(10).to_string(index=False))

    save_output(top_products, 'top_products.csv')
    save_output(sales_by_weekday, 'sales_by_weekday.csv')
    save_output(sales_by_hour, 'sales_by_hour.csv')
    save_output(payment_summary, 'payment_summary.csv')
    save_output(daily_sales, 'daily_sales.csv')

    print(f'\nSaved analysis outputs to {OUTPUT_DIR}')


if __name__ == '__main__':
    main()
