# 定义伊兰特车类
class YilanteCar(object):

    def move(self):
        print("mone the car")

    def stop(self):
        print("stop the car")


# 定义索纳塔车类
class SuonataCar(object):
    def move(self):
        print("mone the car")

    def stop(self):
        print("stop the car")


# 定义一个生产汽车的工厂
class CarFactory(object):

    def create_car(self, typename):
        if typename == "伊兰特":
            car = YilanteCar()
        elif typename == "索纳塔":
            car = SuonataCar()

        return car


# 定义一个销售汽车的类
class CarStore(object):

    def __init__(self):
        self.car_factory = CarFactory()

    def order(self, typename):
        car = self.car_factory.create_car(typename)
        return car


cs = CarStore()
ylt = cs.order("伊兰特")
ylt.move()
ylt.stop()

snt = cs.order("索纳塔")
snt.move()



