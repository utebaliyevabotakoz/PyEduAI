
class Account:
    def __init__(self):
        # Изначальный баланс равен 0
        self.balance = 0
        # Список для хранения всех транзакций
        self.transactions = []

    # Метод для добавления транзакции в список и обновления баланса
    def add_transaction(self, transaction):
        self.transactions.append(transaction)  # Добавляем транзакцию в список
        self.balance += transaction.amount  # Обновляем баланс на основе суммы транзакции

    # Метод для получения текущего баланса
    def get_balance(self):
        return self.balance

    # Метод для получения всех транзакций
    def get_transactions(self):
        return self.transactions
