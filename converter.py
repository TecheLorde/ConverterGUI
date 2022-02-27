class Converter:
    def __init__(self):
        self.first_unit = ""
        self.second_unit = ""
        self.converted_value = 0.0
        self.user_value = 0.0
        self.accuracy = 1

    def convert_celsius_to_fahrenheit(self):
        self.converted_value = self.user_value * 9 / 5 + 32
        return self.converted_value

    def convert_celsius_to_kelvin(self):
        self.converted_value = self.user_value + 273.15
        return self.converted_value

    def convert_fahrenheit_to_celsius(self):
        self.converted_value = (self.user_value - 32) * 5 / 9
        return self.converted_value

    def convert_fahrenheit_to_kelvin(self):
        self.converted_value = (self.user_value - 32) * 5 / 9 + 273.15
        return self.converted_value

    def convert_kelvin_to_celsius(self):
        self.converted_value = self.user_value - 273.15
        return self.converted_value

    def convert_kelvin_to_fahrenheit(self):
        self.converted_value = (self.user_value - 273.15) * 9/5 + 32
        return self.converted_value
