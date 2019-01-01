class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model

        self.year = year
        """属性的默认值"""
        self.odometer = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = "{0} {1} {2}".format(self.year, self.model, self.year)
        return long_name

    def read_odometer(self):
        print("This car has", str(self.odometer), "miles on it")

    def update_odometer(self, mileage):
        """通过方法更该属性的值"""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back am odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer += miles


if __name__ == '__main__':
    my_new_car = Car('audi', 'a4', '2016')
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()

    my_new_car.update_odometer(22)
    print("\nafter one day")
    my_new_car.read_odometer()

    a = 100
    my_new_car.increment_odometer(a)
    print("\n增加里程"+str(a))
    my_new_car.read_odometer()