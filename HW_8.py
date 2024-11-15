
class Category:
    def __init__(self, name, description):
        self.name = name  # Ідентифікатор категорії
        self.description = description  # Назва категорії

    def __str__(self):
        return f"Category: {self.name}, Desc: {self.description}"

# Приклад використання
Category_1 = Category("Електроніка", "Електроніка")
print(Category_1)

class Article:
    def __init__(self, author, article_name, date):
        self.author = author
        self.article_name = article_name
        self.date = date

    def __str__(self):
        return f"Author name: {self.author}, Article Name: {self.article_name}, Date of publish: {self.date}"

Article_1 = Article("Петя", "Петя", "2024")
print(Article_1)

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product name: {self.name}, Price: {self.price}, Category: {self.category}"

Product_1 = Product("Laptop",1500,Category_1.name)
print(Product_1)
