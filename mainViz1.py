from data_loader import DataLoader
import pandas as pd

# Инициализация и загрузка данных
loader = DataLoader()
loader.load_from_csv("season-2324.csv")  # Предполагается, что файл существует

if loader.data is not None:
    # Пример 1: Гистограмма голов домашней команды
    loader.add_histogram(
        column="FTHG",
        figure_name="home_goals_hist",
        bins=20,
        color='green',
        title="Распределение голов домашней команды",
        save_path="home_goals_hist.png"
    )

    # Пример 2: Диаграмма рассеяния голов домашних и гостевых команд
    loader.add_scatter_plot(
        x_column="FTHG",
        y_column="FTAG",
        figure_name="goals_scatter",
        color='purple',
        s=30,
        title="Голы домашних vs гостевых команд",
        save_path="goals_scatter.png"
    )

    # Пример 3: Линейный график (дополнительный пример)
    loader.add_line_plot(
        x_column="Date",  # Предполагается, что столбец с датами существует
        y_column="TotalGoals",
        figure_name="goals_trend",
        color='orange',
        marker='s',
        linestyle='--',
        title="Динамика голов по датам",
        save_path="goals_trend.svg"
    )

else:
    print("Данные не загружены.")