class Vehicle:
    _color_variants: list = ['yellow', 'red', 'green', 'blue', 'purple', 'black']

    def __init__(self, owner, model, engine_power, color):
        self.owner: str = owner
        self.__model: str = model
        self.__engine_power: int = engine_power
        self.__color: str = color
        self._color_variants: list = ['yellow', 'red', 'green', 'blue', 'purple', 'black']

    def get_model(self):
        return print(f'Модель: {self.__model}')

    def get_horsepower(self):
        return print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        return print(f'Цвет: {self.__color}')

    def print_info(self):
        return self.get_model(), self.get_horsepower(), self.get_color(), print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in self._color_variants:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    _passangers_limit = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
