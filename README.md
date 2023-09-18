# TemperatureGraph
Этот репозиторий содержит инструмент для построения графиков температурных данных на основе CSV файлов.
Инструмент разработан на Python с использованием библиотеки pandas для анализа данных и matplotlib для визуализации.

Основные функции:
Загрузка и анализ данных из CSV файлов с температурными показателями.
Возможность настройки заголовка графика, названия датчика и имени файла.
Отображение данных на графике с разметкой по времени и значениям температуры.
Сохранение полученного графика в формате PNG.

Инструкции по использованию:
Клонируйте репозиторий на свой компьютер.
Установите необходимые зависимости, выполнив pip install -r requirements.txt.
Запустите скрипт main.py, указав обязательный параметр "output_file" - Имя файла для сохранения графика(формат .png), с необязательными параметрами можно ознакомится с помощью команды "python main.py -h".
График будет сохранен в файле PNG в текущей директории.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


This repository contains a tool for plotting temperature data based on CSV files.
The tool is developed in Python using the pandas library for data analysis and matplotlib for visualization.

Main functions:
Load and analyze data from temperature CSV files.
Ability to customize graphics title, sensor name and file name.
Display data on a graph with time and temperature values.
Saving the resulting image in PNG format.

Instructions for use:
Clone the repository to your computer.
Install the required ones depending on it by running pip install -r require.txt.
Run the main.py script, specifying the required parameter "output_file" - the name of the file to save the graphics (.png format), you can familiarize yourself with the optional parameters using the command "python main.py -h".
The graph will be saved as a PNG file in the current directory.
