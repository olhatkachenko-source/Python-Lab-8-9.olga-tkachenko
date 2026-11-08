import pandas as pd
import numpy as np

# Налаштування відображення pandas (щоб таблиця не обрізалася)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# ЗАВАНТАЖЕННЯ ДАНИХ ТА ДОПОВНЕННЯ НАБОРУ 
try:
    df = pd.read_csv('lab5.csv')
    print("Файл 'lab5.csv' успішно завантажено!\n")
except FileNotFoundError:
    print("Помилка: Файл 'lab5.csv' не знайдено у директорії.")
    exit()

# Доповнюємо набір даних показниками
np.random.seed(42)
df['GDP_per_capita'] = np.linspace(1500, 3500, len(df)) + np.random.normal(0, 50, len(df))
df['Population'] = np.linspace(51.5, 43.7, len(df)) * 1e6

# Сортуємо за роком у хронологічному порядку
df = df.sort_values('Year').reset_index(drop=True)


# БАЗОВИЙ АНАЛІЗ ДАНИХ (ВИВІД DATAFRAME)
print("--- 1. Повний вміст DataFrame ---")
print(df.to_string())  # Використовуємо .to_string(), щоб гарантовано вивести всю таблицю

print("\n" + "="*50 + "\n")
print("--- 2. Перші 3 рядки DataFrame (df.head(3)) ---")
print(df.head(3).to_string())

print("\n" + "="*50 + "\n")
print("--- 3. Типи даних у кожному стовпці (df.dtypes) ---")
print(df.dtypes)

print("\n" + "="*50 + "\n")
print("--- 4. Кількість рядків і стовпців (df.shape) ---")
print(df.shape)

print("\n" + "="*50 + "\n")
print("--- 5. Описова статистика для числових даних (df.describe()) ---")
print(df.describe().to_string())


# ПОПЕРЕДНЄ ОБРОБЛЕННЯ ДАНИХ 
df['Life_GDP_Index'] = df['Life Expectancy (years)'] / df['GDP_per_capita'] * 1000
df['Decade'] = df['Year'].apply(lambda y: f"{(y // 10) * 10}-х років")

filtered_df = df[df['Life Expectancy (years)'] > 70]
print("\n" + "="*50 + "\n")
print(f"--- Результат фільтрації (тривалість життя > 70 років, всього: {len(filtered_df)}) ---")
print(filtered_df.to_string())

sorted_df = df.sort_values(by='GDP_per_capita', ascending=False)
print("\n" + "="*50 + "\n")
print("--- Результат сортування за ВВП (Топ-3) ---")
print(sorted_df.head(3).to_string())


# АНАЛІЗ ДАНИХ ЗА ДОПОМОГОЮ ГРУПУВАННЯ 
grouped_df = df.groupby('Decade')['Life Expectancy (years)'].mean().reset_index()
print("\n" + "="*50 + "\n")
print("--- Результат групування (середня тривалість життя за десятиліттями) ---")
print(grouped_df.to_string())

unique_years_count = df['Year'].nunique()
print(f"\nКількість унікальних років у наборі даних: {unique_years_count}")


# ЗБЕРЕЖЕННЯ РЕЗУЛЬТАТІВ АНАЛІЗУ 
output_filename = 'analyzed_lab8_data.csv'
df.to_csv(output_filename, index=False, encoding='utf-8')
print(f"\nРезультати опрацювання та аналізу успішно збережено у новий файл '{output_filename}'.")
