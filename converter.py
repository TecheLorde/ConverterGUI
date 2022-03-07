"""Converts units from on type to another"""


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

    """Distance/Length Conversion Methods"""
    def convert_miles_to_nautical_miles(self):
        self.converted_value = self.user_value / 1.15078
        return self.converted_value

    def convert_miles_to_yards(self):
        self.converted_value = self.user_value * 1760
        return self.converted_value

    def convert_miles_to_feet(self):
        self.converted_value = self.user_value * 5280
        return self.converted_value

    def convert_miles_to_kilometers(self):
        self.converted_value = self.user_value * 1.609344
        return self.converted_value

    def convert_miles_to_hectometers(self):
        self.converted_value = self.user_value * 16.09344
        return self.converted_value

    def convert_miles_to_meters(self):
        self.converted_value = self.user_value * 1609.344
        return self.converted_value

    def convert_miles_to_centimeters(self):
        self.converted_value = self.user_value * 160934.4
        return self.converted_value

    def convert_miles_to_millimeters(self):
        self.converted_value = self.user_value * 1609344
        return self.converted_value

    def convert_miles_to_inches(self):
        self.converted_value = self.user_value * 63360
        return self.converted_value

    def convert_nautical_miles_to_miles(self):
        self.converted_value = self.user_value * 1.15078
        return self.converted_value

    def convert_nautical_miles_to_yards(self):
        self.converted_value = self.user_value * 2025.37183
        return self.converted_value

    def convert_nautical_miles_to_feet(self):
        self.converted_value = self.user_value * 6076.11549
        return self.converted_value

    def convert_nautical_miles_to_kilometers(self):
        self.converted_value = self.user_value * 1.852
        return self.converted_value

    def convert_nautical_miles_to_hectometers(self):
        self.converted_value = self.user_value * 18.52
        return self.converted_value

    def convert_nautical_miles_to_meters(self):
        self.converted_value = self.user_value * 1852
        return self.converted_value

    def convert_nautical_miles_to_centimeters(self):
        self.converted_value = self.user_value * 185200
        return self.converted_value

    def convert_nautical_miles_to_millimeters(self):
        self.converted_value = self.user_value * 1852000
        return self.converted_value

    def convert_nautical_miles_to_inches(self):
        self.converted_value = self.user_value * 72913.3858
        return self.converted_value

    def convert_yards_to_miles(self):
        self.converted_value = self.user_value / 1760
        return self.converted_value

    def convert_yards_to_nautical_miles(self):
        self.converted_value = self.user_value / 2025.37183
        return self.converted_value

    def convert_yards_to_feet(self):
        self.converted_value = self.user_value * 3
        return self.converted_value

    def convert_yards_to_kilometers(self):
        self.converted_value = self.user_value * 0.0009144
        return self.converted_value

    def convert_yards_to_hectometers(self):
        self.converted_value = self.user_value * 0.009144
        return self.converted_value

    def convert_yards_to_meters(self):
        self.converted_value = self.user_value * 0.9144
        return self.converted_value

    def convert_yards_to_centimeters(self):
        self.converted_value = self.user_value * 91.44
        return self.converted_value

    def convert_yards_to_millimeters(self):
        self.converted_value = self.user_value * 914.4
        return self.converted_value

    def convert_yards_to_inches(self):
        self.converted_value = self.user_value * 36
        return self.converted_value

    def convert_feet_to_miles(self):
        self.converted_value = self.user_value / 5280
        return self.converted_value

    def convert_feet_to_nautical_miles(self):
        self.converted_value = self.user_value / 6076.11549
        return self.converted_value

    def convert_feet_to_yards(self):
        self.converted_value = self.user_value / 3
        return self.converted_value

    def convert_feet_to_kilometers(self):
        self.converted_value = self.user_value * 0.0003048
        return self.converted_value

    def convert_feet_to_hectometers(self):
        self.converted_value = self.user_value * 0.003048
        return self.converted_value

    def convert_feet_to_meters(self):
        self.converted_value = self.user_value * 0.3048
        return self.converted_value

    def convert_feet_to_centimeters(self):
        self.converted_value = self.user_value * 30.48
        return self.converted_value

    def convert_feet_to_millimeters(self):
        self.converted_value = self.user_value * 304.8
        return self.converted_value

    def convert_feet_to_inches(self):
        self.converted_value = self.user_value * 12
        return self.converted_value

    def convert_kilometers_to_miles(self):
        self.converted_value = self.user_value / 1.609344
        return self.converted_value

    def convert_kilometers_to_nautical_miles(self):
        self.converted_value = self.user_value / 1.852
        return self.converted_value

    def convert_kilometers_to_yards(self):
        self.converted_value = self.user_value / 0.0009144
        return self.converted_value

    def convert_kilometers_to_feet(self):
        self.converted_value = self.user_value / 0.0003048
        return self.converted_value

    def convert_kilometers_to_hectometers(self):
        self.converted_value = self.user_value * 10
        return self.converted_value

    def convert_kilometers_to_meters(self):
        self.converted_value = self.user_value * 1000
        return self.converted_value

    def convert_kilometers_to_centimeters(self):
        self.converted_value = self.user_value * 100000
        return self.converted_value

    def convert_kilometers_to_millimeters(self):
        self.converted_value = self.user_value * 1000000
        return self.converted_value

    def convert_kilometers_to_inches(self):
        self.converted_value = self.user_value / 0.0000254
        return self.converted_value

    def convert_hectometers_to_miles(self):
        self.converted_value = self.user_value / 16.09344
        return self.converted_value

    def convert_hectometers_to_nautical_miles(self):
        self.converted_value = self.user_value / 18.52
        return self.converted_value

    def convert_hectometers_to_yards(self):
        self.converted_value = self.user_value / 0.009144
        return self.converted_value

    def convert_hectometers_to_feet(self):
        self.converted_value = self.user_value / 0.003048
        return self.converted_value

    def convert_hectometers_to_kilometers(self):
        self.converted_value = self.user_value / 10
        return self.converted_value

    def convert_hectometers_to_meters(self):
        self.converted_value = self.user_value * 100
        return self.converted_value

    def convert_hectometers_to_centimeters(self):
        self.converted_value = self.user_value * 10000
        return self.converted_value

    def convert_hectometers_to_millimeters(self):
        self.converted_value = self.user_value * 100000
        return self.converted_value

    def convert_hectometers_to_inches(self):
        self.converted_value = self.user_value / 0.000254
        return self.converted_value

    def convert_meters_to_miles(self):
        self.converted_value = self.user_value / 1609.344
        return self.converted_value

    def convert_meters_to_nautical_miles(self):
        self.converted_value = self.user_value / 1852
        return self.converted_value

    def convert_meters_to_yards(self):
        self.converted_value = self.user_value / 0.9144
        return self.converted_value

    def convert_meters_to_feet(self):
        self.converted_value = self.user_value / 0.3048
        return self.converted_value

    def convert_meters_to_kilometers(self):
        self.converted_value = self.user_value / 1000
        return self.converted_value

    def convert_meters_to_hectometers(self):
        self.converted_value = self.user_value / 100
        return self.converted_value

    def convert_meters_to_centimeters(self):
        self.converted_value = self.user_value * 100
        return self.converted_value

    def convert_meters_to_millimeters(self):
        self.converted_value = self.user_value * 1000
        return self.converted_value

    def convert_meters_to_inches(self):
        self.converted_value = self.user_value / 0.0254
        return self.converted_value

    def convert_centimeters_to_miles(self):
        self.converted_value = self.user_value / 160934.4
        return self.converted_value

    def convert_centimeters_to_nautical_miles(self):
        self.converted_value = self.user_value / 185200
        return self.converted_value

    def convert_centimeters_to_yards(self):
        self.converted_value = self.user_value / 91.44
        return self.converted_value

    def convert_centimeters_to_feet(self):
        self.converted_value = self.user_value / 30.48
        return self.converted_value

    def convert_centimeters_to_kilometers(self):
        self.converted_value = self.user_value / 100000
        return self.converted_value

    def convert_centimeters_to_hectometers(self):
        self.converted_value = self.user_value / 10000
        return self.converted_value

    def convert_centimeters_to_meters(self):
        self.converted_value = self.user_value / 100
        return self.converted_value

    def convert_centimeters_to_millimeters(self):
        self.converted_value = self.user_value * 10
        return self.converted_value

    def convert_centimeters_to_inches(self):
        self.converted_value = self.user_value / 2.54
        return self.converted_value

    def convert_millimeters_to_miles(self):
        self.converted_value = self.user_value / 1609344
        return self.converted_value

    def convert_millimeters_to_nautical_miles(self):
        self.converted_value = self.user_value / 1852000
        return self.converted_value

    def convert_millimeters_to_yards(self):
        self.converted_value = self.user_value / 914.4
        return self.converted_value

    def convert_millimeters_to_feet(self):
        self.converted_value = self.user_value / 304.8
        return self.converted_value

    def convert_millimeters_to_kilometers(self):
        self.converted_value = self.user_value / 1000000
        return self.converted_value

    def convert_millimeters_to_hectometers(self):
        self.converted_value = self.user_value / 100000
        return self.converted_value

    def convert_millimeters_to_meters(self):
        self.converted_value = self.user_value / 1000
        return self.converted_value

    def convert_millimeters_to_centimeters(self):
        self.converted_value = self.user_value / 10
        return self.converted_value

    def convert_millimeters_to_inches(self):
        self.converted_value = self.user_value / 25.4
        return self.converted_value

    def convert_inches_to_miles(self):
        self.converted_value = self.user_value / 63360
        return self.converted_value

    def convert_inches_to_nautical_miles(self):
        self.converted_value = self.user_value / 72913.3858
        return self.converted_value

    def convert_inches_to_yards(self):
        self.converted_value = self.user_value / 36
        return self.converted_value

    def convert_inches_to_feet(self):
        self.converted_value = self.user_value / 12
        return self.converted_value

    def convert_inches_to_kilometers(self):
        self.converted_value = self.user_value * 0.0000254
        return self.converted_value

    def convert_inches_to_hectometers(self):
        self.converted_value = self.user_value * 0.000254
        return self.converted_value

    def convert_inches_to_meters(self):
        self.converted_value = self.user_value * 0.0254
        return self.converted_value

    def convert_inches_to_centimeters(self):
        self.converted_value = self.user_value * 2.54
        return self.converted_value

    def convert_inches_to_millimeters(self):
        self.converted_value = self.user_value * 25.4
        return self.converted_value

    """Energy Conversion Methods"""
    def convert_terajoules_to_gigajoules(self):
        self.converted_value = self.user_value * 1000
        return self.converted_value

    def convert_terajoules_to_megajoules(self):
        self.converted_value = self.user_value * 1000000
        return self.converted_value

    def convert_terajoules_to_kilojoules(self):
        self.converted_value = self.user_value * 1000000000
        return self.converted_value

    def convert_terajoules_to_joules(self):
        self.converted_value = self.user_value * 1000000000000
        return self.converted_value

    def convert_terajoules_to_kilocalories(self):
        self.converted_value = self.user_value / 0.000000004184
        return self.converted_value

    def convert_terajoules_to_calories(self):
        self.converted_value = self.user_value / 0.000000000004184
        return self.converted_value

    def convert_gigajoules_to_terajoules(self):
        self.converted_value = self.user_value / 1000
        return self.converted_value

    def convert_gigajoules_to_megajoules(self):
        self.converted_value = self.user_value * 1000
        return self.converted_value

    def convert_gigajoules_to_kilojoules(self):
        self.converted_value = self.user_value * 1000000
        return self.converted_value

    def convert_gigajoules_to_joules(self):
        self.converted_value = self.user_value * 1000000000
        return self.converted_value

    def convert_gigajoules_to_kilocalories(self):
        self.converted_value = self.user_value / 0.000004184
        return self.converted_value

    def convert_gigajoules_to_calories(self):
        self.converted_value = self.user_value / 0.000000004184
        return self.converted_value

    def convert_megajoules_to_terajoules(self):
        self.converted_value = self.user_value / 1000000
        return self.converted_value

    def convert_megajoules_to_gigajoules(self):
        self.converted_value = self.user_value / 1000
        return self.converted_value

    def convert_megajoules_to_kilojoules(self):
        self.converted_value = self.user_value * 1000
        return self.converted_value

    def convert_megajoules_to_joules(self):
        self.converted_value = self.user_value * 1000000
        return self.converted_value

    def convert_megajoules_to_kilocalories(self):
        self.converted_value = self.user_value / 0.004184
        return self.converted_value

    def convert_megajoules_to_calories(self):
        self.converted_value = self.user_value / 0.000004184
        return self.converted_value

    def convert_kilojoules_to_terajoules(self):
        self.converted_value = self.user_value / 1000000000
        return self.converted_value

    def convert_kilojoules_to_gigajoules(self):
        self.converted_value = self.user_value / 1000000
        return self.converted_value

    def convert_kilojoules_to_megajoules(self):
        self.converted_value = self.user_value / 1000
        return self.converted_value

    def convert_kilojoules_to_joules(self):
        self.converted_value = self.user_value * 1000
        return self.converted_value

    def convert_kilojoules_to_kilocalories(self):
        self.converted_value = self.user_value / 4.184
        return self.converted_value

    def convert_kilojoules_to_calories(self):
        self.converted_value = self.user_value / 0.004184
        return self.converted_value

    def convert_joules_to_terajoules(self):
        self.converted_value = self.user_value / 1000000000000
        return self.converted_value

    def convert_joules_to_gigajoules(self):
        self.converted_value = self.user_value / 1000000000
        return self.converted_value

    def convert_joules_to_megajoules(self):
        self.converted_value = self.user_value / 1000000
        return self.converted_value

    def convert_joules_to_kilojoules(self):
        self.converted_value = self.user_value / 1000
        return self.converted_value

    def convert_joules_to_kilocalories(self):
        self.converted_value = self.user_value / 4184
        return self.converted_value

    def convert_joules_to_calories(self):
        self.converted_value = self.user_value / 4.184
        return self.converted_value

    def convert_kilocalories_to_terajoules(self):
        self.converted_value = self.user_value * 0.000000004184
        return self.converted_value

    def convert_kilocalories_to_gigajoules(self):
        self.converted_value = self.user_value * 0.000004184
        return self.converted_value

    def convert_kilocalories_to_megajoules(self):
        self.converted_value = self.user_value * 0.004184
        return self.converted_value

    def convert_kilocalories_to_kilojoules(self):
        self.converted_value = self.user_value * 4.184
        return self.converted_value

    def convert_kilocalories_to_joules(self):
        self.converted_value = self.user_value * 4184
        return self.converted_value

    def convert_kilocalories_to_calories(self):
        self.converted_value = self.user_value * 1000
        return self.converted_value

    def convert_calories_to_terajoules(self):
        self.converted_value = self.user_value * 0.000000000004184
        return self.converted_value

    def convert_calories_to_gigajoules(self):
        self.converted_value = self.user_value * 0.000000004184
        return self.converted_value

    def convert_calories_to_megajoules(self):
        self.converted_value = self.user_value * 0.000004184
        return self.converted_value

    def convert_calories_to_kilojoules(self):
        self.converted_value = self.user_value * 0.004184
        return self.converted_value

    def convert_calories_to_joules(self):
        self.converted_value = self.user_value * 4.184
        return self.converted_value

    def convert_calories_to_kilocalories(self):
        self.converted_value = self.user_value / 1000
        return self.converted_value

    """Pressure Conversion Methods"""
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
