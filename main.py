# Импорт бибилотек | Import libraries
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, SecondLocator

# Создание графика температур | Creating a temperature graph
def CreatingTemperatureGraph(csv_file, sensorName, title, output_file):
    # Загрузка данных из CSV файла в DataFrame Loading data from a CSV file into a DataFrame
    dataframe = pd.read_csv(csv_file, parse_dates=['Timestamp'])

    # Проверка наличия необходимых столбцов | Checking that required columns are present
    if 'Timestamp' not in dataframe or 'Sensor1' not in dataframe or 'Sensor2' not in dataframe:
        print("Ошибка: CSV файл должен содержать столбцы 'Timestamp', 'Sensor1' и 'Sensor2'.")
        return
    dataframe = dataframe.iloc[::5]
    # Построение графика | Graphing
    plt.figure(figsize=(12, 8))
    plt.plot(dataframe['Timestamp'], dataframe['Sensor1'], label=f'{sensorName} 1')
    plt.plot(dataframe['Timestamp'], dataframe['Sensor2'], label=f'{sensorName} 2')
    plt.xlabel('Время')
    plt.ylabel('Температура °C')
    plt.xticks(fontsize=8, rotation=90)
    plt.title(title)
    plt.legend()

    ax = plt.gca()
    ax.xaxis.set_major_locator(SecondLocator(interval=10))  # Интервал в 10 секунд | 10 second interval
    ax.xaxis.set_major_formatter(DateFormatter("%d %H:%M:%S"))

    # Сохранение графика в файл PNG | Saving a graph to a PNG file
    plt.savefig(output_file)
    print(f"График сохранен в {output_file}")


if __name__ == "__main__":
    # Считывание аргументов | Reading Arguments
    parser = argparse.ArgumentParser(description="Построение графика температуры")
    parser.add_argument("output_file", help="Имя файла для сохранения графика (.png)")
    parser.add_argument("--csv_file", default="temperature_data.csv", help="Имя CSV файла с данными")
    parser.add_argument("--sensor", default="Датчик", help="Название условного температурного датчика")
    parser.add_argument("--title", default="Изменение графика температуры", help="Заголовок графика")

    args = parser.parse_args()

    CreatingTemperatureGraph(args.csv_file, args.sensor, args.title, args.output_file)
