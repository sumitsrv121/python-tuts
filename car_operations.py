class Car:
    def __init__(self, company_name, model, engine):
        self.company_name = company_name
        self.model = model
        self.engine = engine

    class Engine:
        def __init__(self, motor, mileage):
            self.motor = motor
            self.mileage = mileage

    def get_car_info(self):
        print(f"Car from {self.company_name} & model {self.model}")
        print(
            f"Engine: {self.engine.mileage} KMs mileage and motor is {self.engine.motor}"
        )


engine1 = Car.Engine("Electric", 18)
car1 = Car("Ford", "Mustang", engine1)


car1.get_car_info()
