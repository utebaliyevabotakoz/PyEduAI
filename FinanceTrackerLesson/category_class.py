class Category:
    def __init__(self, name):
        # name: название категории (например, "Еда", "Развлечения")
        self.name = name

    # Метод для строкового представления категории
    def __str__(self):
        return self.name
