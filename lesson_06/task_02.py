# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.


class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def get_full_profit(self, weight=25, thickness=5):
        return f'{self._lenght} м * {self._width} м * {weight} кг * {thickness} см =' \
               f' {(self._lenght * self._width * weight * thickness) / 1000} т'

road_1 = Road(5000, 20)
print(road_1.get_full_profit())