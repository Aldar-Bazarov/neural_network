from datetime import datetime
import pandas as pd
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

date_string = input('Введите дату формата DD_MM_YYYY: ')
date_format = "%d_%m_%Y"

target_data = datetime.strptime(date_string, date_format).date()

def check_date(date):
    try:
        cell_date = datetime.strptime(date, "%d %B %Y").date()
        return cell_date == target_data
    except:
        return False

file_path = './data.xlsx'

df_exchange_rates = pd.read_excel(file_path, sheet_name='Курсы валют')

filtered_rows = df_exchange_rates[df_exchange_rates['День'].apply(check_date)]

if not filtered_rows.empty:
    dollar_rate = float(filtered_rows.iloc[:, 1].iloc[0])
    euro_rate = float(filtered_rows.iloc[:, 2].iloc[0])
else:
    print("Не найдено данных с введённой вами датой")  
    exit() 

df_electricity = pd.read_excel(file_path, sheet_name='Цены на ЭЭ')

min_interval = float(input('Введите нижнее значение интервала цены в рублях: ')) / dollar_rate
max_interval = float(input('Введите верхнее значение интервала цены в рублях: ')) / dollar_rate

dollar_cost_column_name = 'Цена $ сша на электроэнергию за кВт. для бизнеса 2023 году'
ruble_cost_column_name = 'Цена ₽ россия на электроэнергию за кВт. для бизнеса 2023 году'
euro_cost_column_name = 'Цена € евро на электроэнергию за кВт. для бизнеса 2023 году'

filtered_df_electricity = df_electricity[df_electricity[dollar_cost_column_name].astype(float).between(min_interval, max_interval)]

if not filtered_df_electricity.empty:
    filtered_df_electricity = filtered_df_electricity.copy()
    filtered_df_electricity[ruble_cost_column_name] = round(filtered_df_electricity[dollar_cost_column_name].astype(float) * dollar_rate, 3)
    filtered_df_electricity[euro_cost_column_name] = round(filtered_df_electricity[dollar_cost_column_name].astype(float) * dollar_rate / euro_rate, 3)
else:
    print("Нет строк, удовлетворяющих условию.")
    exit()

output_file_path = 'Electro_{}.xlsx'.format(date_string)

with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
    filtered_df_electricity.to_excel(writer, sheet_name='Цены на ЭЭ', index=False)
    df_exchange_rates.to_excel(writer, sheet_name='Курсы валют', index=False)

print("Новый файл создан успешно.")