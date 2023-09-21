class Heater:
    """
    >>> machine1 = Heater('radiator kitchen', temperature=20)
    >>> machine2 = Heater('radiator living', minimum=15, temperature=18)
    >>> machine3 = Heater('radiator bathroom', temperature=22, minimum=18, maximum=28)
    >>> print(machine1)
    radiator kitchen: current temperature: 20.0; allowed min: 0.0; allowed max: 100.0
    >>> machine2
    Heater('radiator living', 18.0, 15.0, 100.0)
    >>> machine2.change_temperature(8)
    >>> machine2.temperature()
    26.0
    >>> machine3.change_temperature(-5)
    >>> machine3
    Heater('radiator bathroom', 18.0, 18.0, 28.0)
    """
    def __init__(self, words, temperature=10.0, minimum=0.0, maximum=100.0): #these are 'attributes' or 'properties'
        self.words = words
        self.tem = float(temperature)
        self.min = float(minimum)
        self.max = float(maximum)

    def __str__(self): # attributes / print(something) 했을 때 나오는 값
        return f'{self.words}: current temperature: {self.tem}; allowed min: {self.min}; allowed max: {self.max}'

    def __repr__(self): # attributes / 그냥 something 치면 나오는 값
        return f"Heater('{self.words}', {self.tem}, {self.min}, {self.max})"

    def change_temperature(self, number): # mathod
        self.tem = self.tem + number
        if self.tem > self.max:
            self.tem = self.max
        elif self.tem < self.min:
            self.tem = self.min
        else:
            self.tem = self.tem

    def temperature(self): # mathod
        return self.tem

