class Converter:
    def __init__(self):
        self.first_unit = ""
        self.second_unit = ""
        self.converted_value = 0.0
        self.user_value = 0.0
        self.accuracy = 1

    """Temperature conversion methods"""
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

    """Weight Conversion Methods"""
    def convert_kilogram_to_ounces(self):
        self.converted_value = self.user_value / 0.0283495231
        return self.converted_value

    def convert_kilogram_to_pounds(self):
        self.converted_value = self.user_value / 0.45359237
        return self.converted_value

    def convert_ounces_to_kilograms(self):
        self.converted_value = self.user_value * 0.0283495231
        return self.converted_value

    def convert_ounces_to_pounds(self):
        self.converted_value = self.user_value / 16
        return self.converted_value

    def convert_pounds_to_kilograms(self):
        self.converted_value = self.user_value * 0.45359237
        return self.converted_value

    def convert_pounds_to_ounces(self):
        self.converted_value = self.user_value * 16
        return self.converted_value
    # distance
    # energy

    def convert_atmospheres_to_bars(self):
        self.converted_value = self.user_value * 1.01325
        return self.converted_value

    def convert_atmospheres_to_torr(self):
        self.converted_value = self.user_value * 760
        return self.converted_value

    def convert_atmospheres_to_kilopascals(self):
        self.converted_value = self.user_value * 101.325
        return self.converted_value

    def convert_atmospheres_to_pascals(self):
        self.converted_value = self.user_value * 101325
        return self.converted_value

    def convert_bars_to_atmospheres(self):
        self.converted_value = self.user_value / 1.01325
        return self.converted_value

    def convert_bars_to_torr(self):
        self.converted_value = self.user_value / 0.001333223684
        return self.converted_value

    def convert_bars_to_kilopascals(self):
        self.converted_value = self.user_value * 100
        return self.converted_value

    def convert_bars_to_pascals(self):
        self.converted_value = self.user_value * 100000
        return self.converted_value

    def convert_torr_to_atmospheres(self):
        self.converted_value = self.user_value / 760
        return self.converted_value

    def convert_torr_to_bars(self):
        self.converted_value = self.user_value * 0.001333223684
        return self.converted_value

    def convert_torr_to_kilopascals(self):
        self.converted_value = self.user_value * 0.1333223684
        return self.converted_value

    def convert_torr_to_pascals(self):
        self.converted_value = self.user_value * 133.3223684
        return self.converted_value

    def convert_kilopascals_to_atmospheres(self):
        self.converted_value = self.user_value / 101.325
        return self.converted_value

    def convert_kilopascals_to_bars(self):
        self.converted_value = self.user_value / 100
        return self.converted_value

    def convert_kilopascals_to_torr(self):
        self.converted_value = self.user_value / 0.1333223684
        return self.converted_value

    def convert_kilopascals_to_pascals(self):
        self.converted_value = self.user_value * 1000
        return self.converted_value

    def convert_pascals_to_atmospheres(self):
        self.converted_value = self.user_value / 101325
        return self.converted_value

    def convert_pascals_to_bars(self):
        self.converted_value = self.user_value / 100000
        return self.converted_value

    def convert_pascals_to_torr(self):
        self.converted_value = self.user_value / 133.3223684
        return self.converted_value

    def convert_pascals_to_kilopascals(self):
        self.converted_value = self.user_value / 1000
        return self.converted_value
