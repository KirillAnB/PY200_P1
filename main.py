from typing import Union
class Airplane():
    """Класс создает объект самолет с атрибутами тип самолет(string),колличество двигателей(intger от 1 до 4)
     и запас топлива(integer или float в диапазоне от 1000 до 5000)"""
    def __init__(self,plane_type: str, engines_num: int, fuel_capacity: Union[int, float] ):
        if not isinstance(plane_type, str):
            raise TypeError("Plane stype should be str type")
        self.plane_type = plane_type
        if engines_num not in range(1,5):
            raise ValueError("Engines num should be beetwe 1 and 4")
        self.engines_num = engines_num
        if fuel_capacity not in range(1000,5001):
            raise ValueError("Check fuel capasity")
        self.fuel_capacity = fuel_capacity
    def flying(self):
        pass
    def refuiling(self):
        pass
class Car():
    '''Класс создает оъект автомобиля с атрибутами модель(string), цвет(string) и цена(integer or float)'''
    def __init__(self, model: str, colour: str, price: Union[int, float]):
        avalible_colors = ['red', 'green', 'black']
        if not isinstance(model, str):
            raise TypeError("Check car model")
        self.model = model
        if colour not in avalible_colors:
            raise ValueError(f"Colour should be any of {avalible_colors}")
        self.colour = colour
        if price not in range(1000,100000):
            raise ValueError("Check car price")
        self.price = price
    def eng_start(self):
        pass
    def paint_job(self):
        pass
class Building():
    '''Класс создает обьект дом с атрибутами колличество этажей(integer от 1 до 25), тип стен(string)
     и цена за квадратный метр(integer или float больше 0)'''
    def __init__(self,floors_number: int, walls: str, sq_m_price: Union[int, float] ):
        if floors_number not in range(1,26):
            raise ValueError("Flours value should be in range form 1 to 25")
        self.floors_number = floors_number
        if not isinstance(walls, str):
            raise TypeError('Walls type should be string')
        self.walls = walls
        if sq_m_price < 0:
            raise ValueError("Price should not be negative")
        self.sq_m_price = sq_m_price
    def repair(self):
        pass
    def sale(self):
        pass

if __name__ == "__main__":
    plane1 = Airplane('passenger', 2, 1000)
    car1 = Car('VAZ', 'red', 35000)
    building1 = Building(16, "Bricks", 99000)