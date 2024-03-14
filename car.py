class Car:
    def __init__(self, color, size, model):
        self.color = color
        self.size = size
        self.model = model
        self.speed = 0

    def start_engine(self):
        print("Engine started.")

    def accelerate(self, speed_increase):
        self.speed += speed_increase
        print(f"Car accelerated. Current speed: {self.speed} km/h")

    def brake(self, speed_decrease):
        self.speed -= speed_decrease
        print(f"Car slowed down. Current speed: {self.speed} km/h")

    def honk_horn(self):
        print("Beep! Beep!")

# Example usage
my_car = Car(color="Red", size="small", model="sedan")
my_car.start_engine()
my_car.accelerate(20)
my_car.brake(10)
my_car.honk_horn()

