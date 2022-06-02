class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, value):
        self.temperature = value

    temp = property(get_temperature, set_temperature)

fish = Celsius(37)

print(fish.temp)

