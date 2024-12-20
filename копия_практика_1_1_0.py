# -*- coding: utf-8 -*-
"""Copy of Практика 1.1.0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aDBxGwLcFG1IuhYNXXi2YElblGsMX-lD

**ФИО:**
"""

Сбродов Илья Андреевич

"""# Задание 1

**Описание:** Создайте иерархию классов для разных типов сотрудников в компании. Реализуйте родительский класс Employee и дочерние классы Manager и Developer. Каждый класс должен иметь метод для расчета зарплаты на основе различных критериев класса.


Отрабатываемый принцип: Наследование
"""

class Employee:
    salary = 15000


    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.salary = self.salary

    def salary_calculation(self, days_working):
        self.salary = self.salary * int(round(days_working / 15, 1))

    def get_salary(self):
        return f"Зарплата обычного работника {self.first_name} {self.second_name}: {self.salary} рублей"


class Manager(Employee):
    salary = 20000


    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)

    def salary_calculation(self, days_working):
        self.salary = self.salary * int(round(days_working / 15, 1))

    def get_salary(self):
        return f"Зарплата менеджера {self.first_name} {self.second_name}: {self.salary} рублей"

class Developer(Employee):
    salary = 30000


    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)

    def salary_calculation(self, days_working):
        self.salary = self.salary * int(round(days_working / 15, 1))

    def get_salary(self):
        return f"Зарплата разработчика {self.first_name} {self.second_name}: {self.salary} рублей"

employee1 = Employee("Андрей", "Вовкин", "м")
manager1 = Manager("Данила", "Деткин", "м")
developer1 = Developer("Кирилл", "Вишневский", "м")

print(f'{employee1.first_name} работал 25 дней')
employee1.salary_calculation(25)
print(employee1.get_salary())

print(f'{manager1.first_name} работал всего 25 дней')
manager1.salary_calculation(25)
print(manager1.get_salary())

print(f'{developer1.first_name} работал всего 25 дней')
developer1.salary_calculation(25)
print(developer1.get_salary())

"""# Задание 2

**Описание:** Создайте иерархию классов для различных типов транспортных средств (Необходим один родительский класс и 3 дочерних). Реализуйте метод, который позволяет каждому транспортному средству возвращать собственное описание (Метод в каждом классе должен иметь одинаковое название). Продемонстрируйте вызов данного метода для каждого транспортного средства.


Отрабатываемый принцип: Полиморфизм
"""

class Transport:

    def __init__(self, weight, number_of_seats, car_brand):
        self.weight = weight
        self.number_of_seats = number_of_seats
        self.car_brand = car_brand

    def call(self):
        return (f'!Описание транспортного средства:\n'
                f'Вес: {self.weight} килограмм\n'
                f'Количество посадочных мест: {self.number_of_seats}\n'
                f'Марка транспортного средства: {self.car_brand}')


class Passenger(Transport):

    def __init__(self, weight, number_of_seats, car_brand):
        super().__init__(weight, number_of_seats, car_brand)


    def call(self):
        return (f'!Описание транспортного средства:\n'
                f'Вид: Легковой\n'
                f'Вес: {self.weight} килограмм\n'
                f'Количество посадочных мест: {self.number_of_seats}\n'
                f'Марка транспортного средства: {self.car_brand}')


class Truck(Transport):

    def __init__(self, weight, number_of_seats, car_brand):
        super().__init__(weight, number_of_seats, car_brand)


    def call(self):
        return (f'!Описание транспортного средства:\n'
                f'Вид: Грузовик\n'
                f'Вес: {self.weight} килограмм\n'
                f'Количество посадочных мест: {self.number_of_seats}\n'
                f'Марка транспортного средства: {self.car_brand}')


class Bus(Transport):

    def __init__(self, weight, number_of_seats, car_brand):
        super().__init__(weight, number_of_seats, car_brand)


    def call(self):
        return (f'!Описание транспортного средства:\n'
                f'Вид: Автобус\n'
                f'Вес: {self.weight} килограмм\n'
                f'Количество посадочных мест: {self.number_of_seats}\n'
                f'Марка транспортного средства: {self.car_brand}')

transport1 = Transport(2700, 5, "BMW")
passenger1 = Passenger(1380 , 5, "Lada")
truck1 = Truck(5000, 5, "MAN")
bus1 = Bus(16600, 43, "Hyundai")
print(transport1.call())
print(passenger1.call())
print(truck1.call())
print(bus1.call())

"""# Задание 3

Онлайн-магазин:
- Создайте модель для онлайн-магазина с классами Product, Order, Customer, и ShoppingCart.
- Product включает информацию о цене, наличии на складе и категории товара.
Order обрабатывает процесс покупки, включая расчет цены с учетом скидок и налогов.
- Customer управляет информацией о пользователе и его истории заказов.
- ShoppingCart позволяет добавлять, удалять и обновлять количество товаров перед оформлением заказа.
"""

class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def checking_for_availability(self, count):
        if self.stock == count:
            return f'Товар {self.name} присутствует на складе в нужном количестве!'
        else:
            return f'Товара {self.name} недостаёт на складе, а именно {self.stock - count}'

    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity

    def info(self):
        return f'Товар: {self.name}, категория: {self.category}, цена: {self.price} руб, в наличии: {self.stock} шт.'


class Customer:
    def __init__(self, name):
        self.name = name
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)

    def call(self):
        return f'Клиент: {self.name}, История заказов: {len(self.order_history)} заказов.'


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.checking_for_availability(quantity):
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
        else:
            print(f"Недостаточное количество товара {product.name} на складе.")

    def remove_product(self, product):
        if product in self.items:
            del self.items[product]

    def update_quantity(self, product, new_quantity):
        if product.checking_for_availability(new_quantity):
            self.items[product] = new_quantity
        else:
            print(f'Недостаточное количество товара {product.name} на складе')

    def clear_cart(self):
        self.items = {}

    def calculate_total(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    def call(self):
        if self.items:
            cart_content1 = []
            for product, quantity in self.items.items():
                cart_content1.append(f"{product.name}: {quantity} шт.")
            cart_content = "\n".join(cart_content1)
            return f"Содержимое корзины:\n{cart_content}"
        else:
            "Корзина пуста."


class Order:
    def __init__(self, customer, shopping_cart, discount=0, tax=0.17):
        self.customer = customer
        self.shopping_cart = shopping_cart
        self.discount = discount
        self.tax = tax

    def calculate_final_price(self):
        subtotal = self.shopping_cart.calculate_total()
        discount_amount = subtotal * (self.discount / 100)
        tax_amount = (subtotal - discount_amount) * self.tax
        final_price = subtotal - discount_amount + tax_amount
        return final_price

    def complete_order(self):
        for product, quantity in self.shopping_cart.items.items():
            product.reduce_stock(quantity)
        self.customer.add_order(self)
        self.shopping_cart.clear_cart()

    def call(self):
        return f"Заказ для {self.customer.name}. Итоговая сумма: {self.calculate_final_price():.2f} руб."

product1 = Product("Ноутбук", 15000, 20, "Электроника")
product2 = Product("Компьютер", 22000, 15, "Электроника")

customer = Customer("Максим Максимов")

cart = ShoppingCart()
cart.add_product(product1, 1)
cart.add_product(product2, 2)

print(cart.call())
print(f"Общая стоимость без скидок и налогов: {cart.calculate_total()} руб")

order = Order(customer, cart, discount=10, tax=0.2)
print(order.call())
order.complete_order()

print(customer.call())

"""# Задание 4

Симулятор космического корабля:
- Создайте симулятор управления космическим кораблем с классами SpaceShip, CrewMember, и Mission.
- SpaceShip имеет атрибуты для управления топливом, состоянием корпуса, и текущей скоростью.
- CrewMember контролирует здоровье, навыки, и роли в команде (например, пилот, инженер).
- Mission определяет цели, ресурсы, и возможные события (например, аварии, встречи с астероидами).
"""

class SpaceShip:
    def __init__(self, fuel, hull_integrity, speed):
        self.fuel = fuel
        self.hull_integrity = hull_integrity
        self.speed = speed

    def travel(self, distance):
        fuel_needed = distance * 0.15
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f"Космический корабль путешествует на расстояние {distance}."
                  f"\nТопливо, которое осталось: {self.fuel}. Топливо, которое потрачено: {fuel_needed}")
        else:
            print("Недостаточно топлива для путешествия >= полёт совершить невозможно(")

    def repair_hull(self, repair_amount):
        if self.hull_integrity < 100:
            self.hull_integrity += repair_amount
            if self.hull_integrity > 100:
                self.hull_integrity = 100
            print(f"Состояние корпуса восстановлено до {self.hull_integrity}.")
        else:
            print("Состояние корпуса в полном порядке.")

    def change_speed(self, new_speed):
        self.speed = new_speed
        print(f"Скорость изменена на {self.speed}.")

class CrewMember:
    def __init__(self, name, health, skills, role):
        self.name = name
        self.health = health
        self.skills = skills
        self.role = role

    def heal(self, heal_amount):
        self.health += heal_amount
        if self.health > 100:
            self.health = 100
        print(f"{self.name} восстановил здоровье до {self.health}.")

    def show_info(self):
        print(f"Член экипажа: {self.name}, Здоровье: {self.health}, Навыки: {self.skills}, Роль: {self.role}")

class Mission:
    def __init__(self, objectives, resources):
        self.objectives = objectives
        self.resources = resources

    def start_mission(self):
        print("Миссия начата!")
        print(f"Цели: {self.objectives}")
        print(f"Доступные ресурсы: {self.resources}")

    def encounter_event(self, event):
        print(f"Событие: {event}")

def main():
    str1 = """Перед вами симулятор космического корабля. Вам будет предложено поиграть в данный симулятор
По умолчанию топливо корабля будет равно 100 ед., состояние корабля - 80 ед., а скорость 12 ед.
Вы выберете, какаую миссию должен будет завершить ваш корабль. Также вы вводите членов экипажа, их по умолчанию 2, пишите их роли, навыки и имена.
Также вы заполните цели и ресурсы, необходимые для полёта.
За вас будет заполнены несколько вещей таких как, дистанция полёта, изменение скорости, на какое-то число, произвольное лечение второго члена и показ информации о первом члене."""
    print(str1)
    spaceship = SpaceShip(fuel=100, hull_integrity=80, speed=12)

    info1 = input("Введите имя, количество здоровья, 2 навыка и роль первого члена экипажа(Обязательно через запятую): ").split(", ")
    #Макс, 100, Лидер, Молодец, Пилот
    crew_member1 = CrewMember(info1[0], int(info1[1]), info1[2:4], info1[4])
    info2 = input("Введите имя, количество здоровья, 2 навыка и роль второго члена экипажа(Обязательно через запятую): ").split(", ")
    #Алекс, 75, проектирование, навигация, инженер
    crew_member2 = CrewMember(info2[0], int(info2[1]), info2[2:4], info2[4])

    objectives1 = input("Введите цели для полёта на своём корабле(Обязательно через запятую): ").split(", ")
    resources1 = input("Введите ресурсы, необходимые для миссии(Обязательно через запятую): ").split(", ")
    mission = Mission(objectives1, resources1)

    mission.start_mission()

    spaceship.travel(50)
    spaceship.change_speed(20)
    crew_member1.show_info()
    crew_member2.heal(10)
    spaceship.repair_hull(15)

    event1 = input("Введите непредвиденное событие, с которым столкнётся ваш корабль: ")
    mission.encounter_event(event1)

main()

"""# Дополнительно:

**Описание:** создайте консольную версию игры крестики-нолики, используя классы
"""

