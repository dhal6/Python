### file 1
class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

class Admin(User):
    def __init__(self, login, password, admin_field1, admin_field2, admin_field3):
        super().__init__(login, password)
        self.admin_field1 = admin_field1
        self.admin_field2 = admin_field2
        self.admin_field3 = admin_field3

    def admin_action1(self):
        # Реалізувати логіку дії
        pass

    def admin_action2(self):
        # Реалізувати логіку дії
        pass

class Support(User):
    def __init__(self, login, password, support_field1, support_field2, support_field3):
        super().__init__(login, password)
        self.support_field1 = support_field1
        self.support_field2 = support_field2
        self.support_field3 = support_field3

    def support_action1(self):
        # Реалізувати логіку дії
        pass

    def support_action2(self):
        # Реалізувати логіку дії
        pass
########## file 3
class Item:
    def __init__(self, name, description, price):
        self.__name = name
        self.__description = description
        self.__price = price

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if isinstance(new_price, (int, float)) and new_price >= 0:
            self.__price = new_price
        else:
            raise ValueError("Ціна повинна бути числом і більше або дорівнювати нулю.")

    def __str__(self):
        return f"Товар: {self.__name}\nОпис: {self.__description}\nЦіна: {self.__price} грн"

class Blog:
    def __init__(self, title, text):
        self.__title = title
        self.__text = text

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def set_title(self, new_title):
        self.__title = new_title

    def set_text(self, new_text):
        self.__text = new_text

    def __str__(self):
        return f"Заголовок: {self.__title}\nТекст: {self.__text}"
###File 4
class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __str__(self):
        return f"Логін: {self.login}, Пароль: {self.password}"

class User1(User):
    def __init__(self, login, password, user1_field1):
        super().__init__(login, password)
        self.user1_field1 = user1_field1

    def __str__(self):
        return f"{super().__str__()}, user1_field1: {self.user1_field1}"

class User2(User):
    def __init__(self, login, password, user1_field2):
        super().__init__(login, password)
        self.user1_field2 = user1_field2

    def __str__(self):
        return f"{super().__str__()}, user1_field2: {self.user1_field2}"

class User3(User):
    def __init__(self, login, password, user1_field3):
        super().__init__(login, password)
        self.user1_field3 = user1_field3

    def __str__(self):
        return f"{super().__str__()}, user1_field3: {self.user1_field3}"

class User4(User):
    def __init__(self, login, password, user1_field4):
        super().__init__(login, password)
        self.user1_field4 = user1_field4

    def __str__(self):
        return f"{super().__str__()}, user1_field4: {self.user1_field4}"

# Приклад:
user1 = User1(login="user1", password="password1", user1_field1="Field1 Data")
user2 = User2(login="user2", password="password2", user1_field2="Field2 Data")
user3 = User3(login="user3", password="password3", user1_field3="Field3 Data")
user4 = User4(login="user4", password="password4", user1_field4="Field4 Data")
print(user1)
print(user2)
print(user3)
print(user4)
### File 6
class Car:
    def __init__(self, wheels_type="standard", stop_system_type="standard"):
        self.wheel_field1, self.wheel_field2, self.wheel_field3 = self._set_wheel_type(wheels_type)
        self.system_type_field1, self.system_type_field2, self.system_type_field3 = self._set_stop_system_type(
            stop_system_type)

    def _set_wheel_type(self, type):
        if type == "standard":
            return "Standard Wheel 1", "Standard Wheel 2", "Standard Wheel 3"
        elif type == "sport":
            return "Sport Wheel 1", "Sport Wheel 2", "Sport Wheel 3"
        elif type == "off-road":
            return "Off-Road Wheel 1", "Off-Road Wheel 2", "Off-Road Wheel 3"
        else:
            raise ValueError(f"Unknown wheel type: {type}")

    def _set_stop_system_type(self, type):
        if type == "standard":
            return "Standard Brake System 1", "Standard Brake System 2", "Standard Brake System 3"
        elif type == "abs":
            return "ABS Brake System 1", "ABS Brake System 2", "ABS Brake System 3"
        elif type == "ebd":
            return "EBD Brake System 1", "EBD Brake System 2", "EBD Brake System 3"
        else:
            raise ValueError(f"Unknown stop system type: {type}")

    def __str__(self):
        return (f"Колеса: {self.wheel_field1}, {self.wheel_field2}, {self.wheel_field3}\n"
                f"Гальмівна система: {self.system_type_field1}, {self.system_type_field2}, {self.system_type_field3}")

# Приклад:
car1 = Car(wheels_type="sport", stop_system_type="abs")
print(car1)
### File 7
class User:
    def __init__(self, login, password, user_type):
        self.login = login
        self.password = password
        self.user_type = user_type

    def __str__(self):
        return f"User(type: {self.user_type}, login: {self.login}, password: {self.password})"
users = []
choice = input("Виберіть тип користувача (1, 2, 3 або 4): ")
login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if choice in ["1", "2", "3", "4"]:
    user = User(login, password, choice)
    users.append(user)
else:
    print("Невірний вибір. Будь ласка, виберіть 1, 2, 3 або 4.")
for user in users:
    print(user)
### File 8
import copy

class User:
    def __init__(self, login, password):
        self.login = login
        self.__password = password

    def __str__(self):
        return f"User(login: {self.login}, password: {'*' * len(self.__password)})"

# Створення оригінального об'єкта
user1 = User("user1", "password123")

# Створення копії об'єкта
user2 = copy.copy(user1)  # Поверхневе копіювання

# Виведення об'єктів
print("Оригінал:", user1)
print("Поверхнева копія:", user2)

# Зміна даних у копії
user2.login = "user2"
user3.login = "user3"

# Перевірка змін після модифікацій
print("\nПісля змін:")
print("Оригінал:", user1)
print("Поверхнева копія:", user2)
