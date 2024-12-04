import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class NumPyPandasBasics:
    """
    Этот класс содержит обучающие примеры использования библиотек NumPy, Pandas и Matplotlib.
    Примеры ориентированы на новичков и показывают практическое применение.
    """

    def __init__(self):
        print("Привет! Сегодня мы изучим библиотеки NumPy, Pandas и Matplotlib.")
        print("Эти инструменты помогут нам работать с числами, таблицами и графиками!")
        print("Мы также разберем примеры из реальной жизни, чтобы все было понятно и полезно.")

    def numpy_example(self):
        """
        Пример использования библиотеки NumPy с простыми объяснениями и реальными примерами.
        """
        print("\n=== NumPy: Быстрая работа с числами ===")

        # Пример из реальной жизни: Ежедневные температуры
        print("\nПредставьте, что у нас есть температуры (в °C) за неделю: 20, 22, 19, 21, 23, 24, 20.")
        temperatures = np.array([20, 22, 19, 21, 23, 24, 20])
        print("Температуры на неделе:", temperatures)

        # Найдем среднюю температуру за неделю
        print("\nМы можем найти среднюю температуру за неделю.")
        average_temp = np.mean(temperatures)
        print(f"Средняя температура: {average_temp:.2f} °C")
        #! :.2f ДЛЯ округления до сотой доли (два числа после запятой)

        # Добавим к каждому дню 5°C (например, глобальное потепление через 10 лет)
        print("\nЧто если через 10 лет температура увеличится на 5°C каждый день?")
        future_temperatures = temperatures + 5
        print("Температуры через 10 лет:", future_temperatures)

        # Пример: Нахождение самой высокой температуры
        print("\nТеперь найдем самую высокую температуру за неделю.")
        max_temp = np.max(temperatures)
        print(f"Максимальная температура за неделю: {max_temp} °C")

        print(type(temperatures))

    def pandas_example(self):
        """
        Пример использования библиотеки Pandas с реальными сценариями.
        """
        print("\n=== Pandas: Работа с таблицами ===")

        # Пример из реальной жизни: Таблица продаж
        print("\nПредставьте, что вы работаете в магазине. Вот таблица продаж за 3 дня:")
        data = {
            "Дата": ["2024-12-01", "2024-12-02", "2024-12-03"],
            "Товар": ["Хлеб", "Молоко", "Сыр"],
            "Продажи": [10, 6000, 1000]
        }
        sales_df = pd.DataFrame(data)
        print(sales_df)

        # Пример: Сумма всех продаж
        print("\nСколько всего товаров продали за 3 дня?")
        total_sales = sales_df["Продажи"].sum()
        print(f"Всего продано: {total_sales} товаров")

        #* Пример: Увеличение продаж на 10%
        print("\nЧто если продажи увеличатся на 10%?")
        sales_df["Продажи после увеличения"] = sales_df["Продажи"] * 1.10
        print("Обновленная таблица с увеличенными продажами:")
        print(sales_df)

        # Пример: Фильтрация — только товары с продажами больше 25
        print("\nКакие товары продавались больше 25 раз?")
        filtered_sales = sales_df[sales_df["Продажи"] > 25]
        filtered_by_goods = sales_df[sales_df["Товар"] == 'Сыр']
        # print(filtered_by_goods)
        # print(filtered_sales)
        # print(filtered_sales.iloc[1])
        # print(filtered_sales['Товар'])

        sorted_dataframe = sales_df.sort_values(by='Продажи', ascending=True)
        print(sorted_dataframe)

        print(
            sorted_dataframe.reset_index(drop=True)
        )

    def matplotlib_example(self):
        """
        Пример использования библиотеки Matplotlib с реальным примером.
        """
        print("\n=== Matplotlib: Построение графиков ===")

        # Пример из реальной жизни: График температуры
        print("\nДопустим, мы записали температуры за 7 дней и хотим их визуализировать.")
        days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
        temperatures = [20, 22, 19, 21, 23, 24, 20]

        print("Рисуем график температур...")
        plt.plot(days, temperatures, marker="x", label="Температура (°C) for a week", color="blue")
        plt.title("Температура за неделю")
        plt.xlabel("Дни недели")
        plt.ylabel("Температура (°C)")
        plt.legend()
        plt.grid()
        plt.show()


# --- Основная программа ---
#! Зачем нужна 100-строка? ЧТОБЫ ФАЙЛ, при импорте, не запускался (объекты, методы, функции не запускались сразу)
#! Всё что ниже 100-строки будет запускаться, только если мы сами напрямую это сделаем (запустим файл)
if __name__ == "__main__":
    tutorial = NumPyPandasBasics()
    # tutorial.numpy_example()
    tutorial.pandas_example()
    # tutorial.matplotlib_example()
