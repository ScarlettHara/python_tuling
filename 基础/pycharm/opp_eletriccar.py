class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive(self):
        print(self.year, self.model, self.make)

    def read_odometer(self):
        print("This car has %s miles on it" % self.odometer_reading)

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This has %s-Kwh battery" % self.battery_size)


if __name__ == '__main__':
    my_tesla = ElectricCar('tesla', 'model s', 2016)

    my_tesla.get_descriptive()
    my_tesla.describe_battery()
