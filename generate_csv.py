# Импорт бибилотек | Import libraries
import pandas as pd
import random
import datetime


# Создание случайных данных | Generating Random Data
firstTime = datetime.datetime.today()
timestamps = [firstTime + datetime.timedelta(seconds=i) for i in range(200)]
sensor1Values = [random.uniform(0, 100) for _ in range(200)]
sensor2Values = [random.uniform(0, 100) for _ in range(200)]

# Создание DataFrame | Creating a DataFrame
data = {'Timestamp': timestamps, 'Sensor1': sensor1Values, 'Sensor2': sensor2Values}
dataframe = pd.DataFrame(data)

# Сохранение в CSV файл | Saving to CSV file
dataframe.to_csv('temperature_data3.csv', index=False)

print("Файл 'temperature_data.csv' сгенерирован.")
