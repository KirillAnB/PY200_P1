from typing import Union


class Airplane:
    """Класс создает объект самолет с атрибутами тип самолет(string),колличество двигателей(intger от 1 до 4)
     и запас топлива(integer или float в диапазоне от 1000 до 5000)"""

    def __init__(self, plane_type: str, engines_num: int, fuel_capacity: Union[int, float]):
        if not isinstance(plane_type, str):
            raise TypeError("Plane stype should be str type")
        self.plane_type = plane_type
        if engines_num not in range(1, 5):
            raise ValueError("Engines num should be beetwe 1 and 4")
        self.engines_num = engines_num
        if fuel_capacity not in range(1000, 5001):
            raise ValueError("Check fuel capasity")
        self.fuel_capacity = fuel_capacity

    def flying(self):
        pass

    def refuiling(self):
        pass


class Car:
    """Класс создает оъект автомобиля с атрибутами модель(string), цвет(string) и цена(integer or float)"""

    def __init__(self, model: str, colour: str, price: Union[int, float]):
        avalible_colors = ['red', 'green', 'black']
        if not isinstance(model, str):
            raise TypeError("Check car model")
        self.model = model
        if colour not in avalible_colors:
            raise ValueError(f"Colour should be any of {avalible_colors}")
        self.colour = colour
        if price not in range(1000, 100000):
            raise ValueError("Check car price")
        self.price = price

    def eng_start(self):
        pass

    def paint_job(self):
        pass


class Building:
    """Класс создает обьект дом с атрибутами колличество этажей(integer от 1 до 25), тип стен(string)
     и цена за квадратный метр(integer или float больше 0)"""

    def __init__(self, floors_number: int, walls: str, sq_m_price: Union[int, float]):
        if floors_number not in range(1, 26):
            raise ValueError("Flours value should be in range form 1 to 25")
        self.floors_number = floors_number
        if not isinstance(walls, str):
            raise TypeError("Walls type should be string")
        self.walls = walls
        if sq_m_price < 0:
            raise ValueError("Price should not be negative")
        self.sq_m_price = sq_m_price

    def repair(self):
        pass

    def sale(self):
        pass


class PC:
    """Класс создает оъект 'персональный компьютер' с атрибутами тип пк, название модели,скорость цпу и ценой."""

    def __init__(self, pc_type: str, model: str, cpu: int, price: Union[int, float]):
        if pc_type not in ['home pc', 'notebook']:
            raise ValueError("Check pc type")
        self.pc_type = pc_type
        self.model = model
        if not isinstance(cpu, int):
            raise TypeError("CPU value should be integer")
        self.cpu = cpu
        try:
            price = float(price)
            self.price = price
        except:
            raise ValueError("Check pc price")

    def upgrade(self):
        pass

    def service(self):
        pass


class Book:
    """Класс создает обьект книга с атрибутами тип обложки, колличество страниц, цена и возрастное ограничение."""
    cover_types = ['hard', 'soft']

    def __init__(self, cover_type: str, pages: int, price: float, age: int):
        if cover_type not in Book.cover_types:
            raise ValueError(f"Check cover type(should be {Book.cover_types[0]} or {Book.cover_types[1]}")
        self.cover_type = cover_type
        if pages not in range(1, 10000):
            raise ValueError("Check book pages value")
        self.pages = pages
        try:
            price = float(price)
            self.price = price
        except:
            raise ValueError("Check pc price")
        if not isinstance(age, int):
            raise ValueError()
        self.age = age

    def sale(self):
        pass

    def short_cut(self):
        pass


class Coffeemachine:
    """Создает обьект кофе-машина с атрибутами тип аппарата, название модели, цвет и цена."""
    avalible_colors = ['red', 'blue', 'black', 'white']

    def __init__(self, machine_type: str, model: str, color: str, price: Union[int, float]):
        if not isinstance(machine_type, str):
            raise ValueError("Check coffee machine type!")
        self.machine_type = machine_type
        if not isinstance(model, str):
            raise ValueError("Check coffe machibe model")
        self.model = model
        if color not in Coffeemachine.avalible_colors:
            raise ValueError(f"Avalible colors are {Coffeemachine.avalible_colors}")
        self.color = color
        try:
            price = float(price)
            self.price = price
        except:
            raise ValueError("Check pc price")

    def sale(self):
        pass

    def coffee_cooking(self):
        pass


if __name__ == "__main__":
    pass

    # plane1 = Airplane('passenger', 2, 1000)
    # car1 = Car('VAZ', 'red', 35000)
    # building1 = Building(16, "Bricks", 99000)
    # pc1 = PC('home pc',1200,10000,'text')
    # book1 = Book('hard',300,999,18)
    # coffee_machine1 = Coffeemachine('Home', 'Zambony', 'black', 1000)
