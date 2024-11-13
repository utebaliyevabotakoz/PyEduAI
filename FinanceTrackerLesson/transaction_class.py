import datetime

# Класс Transaction представляет каждую отдельную транзакцию (доход или расход).
class Transaction:
    def __init__(self, amount, category, date=None):
        # amount: сумма транзакции (положительная для дохода, отрицательная для расхода)
        # category: категория транзакции (например, "Еда", "Транспорт")
        # date: дата транзакции, по умолчанию текущая дата, если не указана
        self.amount = amount
        self.category = category
        self.date = date or datetime.date.today()  # Если дата не передана, используется текущая дата

    # Метод для отображения информации о транзакции в удобном виде
    def display(self):
        # Выводим дату, категорию и сумму (с плюсом или минусом в зависимости от типа транзакции)
        return f"{self.date} - {self.category}: {'+' if self.amount >= 0 else '-'}${abs(self.amount)}"
