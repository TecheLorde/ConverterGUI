"""Converts units from on type to another"""


class Converter:
    user_value = 0.0
    converted_value = 0.0

    """Temperature conversion methods"""
    @staticmethod
    def convert_celsius_to_fahrenheit(user_value):
        converted_value = user_value * 9 / 5 + 32
        return converted_value

    @staticmethod
    def convert_celsius_to_kelvin(user_value):
        converted_value = user_value + 273.15
        return converted_value

    @staticmethod
    def convert_fahrenheit_to_celsius(user_value):
        converted_value = (user_value - 32) * 5 / 9
        return converted_value

    @staticmethod
    def convert_fahrenheit_to_kelvin(user_value):
        converted_value = (user_value - 32) * 5 / 9 + 273.15
        return converted_value

    @staticmethod
    def convert_kelvin_to_celsius(user_value):
        converted_value = user_value - 273.15
        return converted_value

    @staticmethod
    def convert_kelvin_to_fahrenheit(user_value):
        converted_value = (user_value - 273.15) * 9/5 + 32
        return converted_value

    """Weight Conversion Methods"""
    @staticmethod
    def convert_kilogram_to_ounces(user_value):
        converted_value = user_value / 0.0283495231
        return converted_value

    @staticmethod
    def convert_kilograms_to_pounds(user_value):
        converted_value = user_value / 0.45359237
        return converted_value

    @staticmethod
    def convert_ounces_to_kilograms(user_value):
        converted_value = user_value * 0.0283495231
        return converted_value

    @staticmethod
    def convert_ounces_to_pounds(user_value):
        converted_value = user_value / 16
        return converted_value

    @staticmethod
    def convert_pounds_to_kilograms(user_value):
        converted_value = user_value * 0.45359237
        return converted_value

    @staticmethod
    def convert_pounds_to_ounces(user_value):
        converted_value = user_value * 16
        return converted_value

    """Distance/Length Conversion Methods"""
    @staticmethod
    def convert_miles_to_nautical_miles(user_value):
        converted_value = user_value / 1.15078
        return converted_value

    @staticmethod
    def convert_miles_to_yards(user_value):
        converted_value = user_value * 1760
        return converted_value

    @staticmethod
    def convert_miles_to_feet(user_value):
        converted_value = user_value * 5280
        return converted_value

    @staticmethod
    def convert_miles_to_kilometers(user_value):
        converted_value = user_value * 1.609344
        return converted_value

    @staticmethod
    def convert_miles_to_hectometers(user_value):
        converted_value = user_value * 16.09344
        return converted_value

    @staticmethod
    def convert_miles_to_meters(user_value):
        converted_value = user_value * 1609.344
        return converted_value

    @staticmethod
    def convert_miles_to_centimeters(user_value):
        converted_value = user_value * 160934.4
        return converted_value

    @staticmethod
    def convert_miles_to_millimeters(user_value):
        converted_value = user_value * 1609344
        return converted_value

    @staticmethod
    def convert_miles_to_inches(user_value):
        converted_value = user_value * 63360
        return converted_value

    @staticmethod
    def convert_nautical_miles_to_miles(user_value):
        converted_value = user_value * 1.15078
        return converted_value

    @staticmethod
    def convert_nautical_miles_to_yards(user_value):
        converted_value = user_value * 2025.37183
        return converted_value

    @staticmethod
    def convert_nautical_miles_to_feet(user_value):
        converted_value = user_value * 6076.11549
        return converted_value

    @staticmethod
    def convert_nautical_miles_to_kilometers(user_value):
        converted_value = user_value * 1.852
        return converted_value

    @staticmethod
    def convert_nautical_miles_to_hectometers(user_value):
        converted_value = user_value * 18.52
        return converted_value

    @staticmethod
    def convert_nautical_miles_to_meters(user_value):
        converted_value = user_value * 1852
        return converted_value

    @staticmethod
    def convert_nautical_miles_to_centimeters(user_value):
        converted_value = user_value * 185200
        return converted_value

    @staticmethod
    def convert_nautical_miles_to_millimeters(user_value):
        converted_value = user_value * 1852000
        return converted_value

    @staticmethod
    def convert_nautical_miles_to_inches(user_value):
        converted_value = user_value * 72913.3858
        return converted_value

    @staticmethod
    def convert_yards_to_miles(user_value):
        converted_value = user_value / 1760
        return converted_value

    @staticmethod
    def convert_yards_to_nautical_miles(user_value):
        converted_value = user_value / 2025.37183
        return converted_value

    @staticmethod
    def convert_yards_to_feet(user_value):
        converted_value = user_value * 3
        return converted_value

    @staticmethod
    def convert_yards_to_kilometers(user_value):
        converted_value = user_value * 0.0009144
        return converted_value

    @staticmethod
    def convert_yards_to_hectometers(user_value):
        converted_value = user_value * 0.009144
        return converted_value

    @staticmethod
    def convert_yards_to_meters(user_value):
        converted_value = user_value * 0.9144
        return converted_value

    @staticmethod
    def convert_yards_to_centimeters(user_value):
        converted_value = user_value * 91.44
        return converted_value

    @staticmethod
    def convert_yards_to_millimeters(user_value):
        converted_value = user_value * 914.4
        return converted_value

    @staticmethod
    def convert_yards_to_inches(user_value):
        converted_value = user_value * 36
        return converted_value

    @staticmethod
    def convert_feet_to_miles(user_value):
        converted_value = user_value / 5280
        return converted_value

    @staticmethod
    def convert_feet_to_nautical_miles(user_value):
        converted_value = user_value / 6076.11549
        return converted_value

    @staticmethod
    def convert_feet_to_yards(user_value):
        converted_value = user_value / 3
        return converted_value

    @staticmethod
    def convert_feet_to_kilometers(user_value):
        converted_value = user_value * 0.0003048
        return converted_value

    @staticmethod
    def convert_feet_to_hectometers(user_value):
        converted_value = user_value * 0.003048
        return converted_value

    @staticmethod
    def convert_feet_to_meters(user_value):
        converted_value = user_value * 0.3048
        return converted_value

    @staticmethod
    def convert_feet_to_centimeters(user_value):
        converted_value = user_value * 30.48
        return converted_value

    @staticmethod
    def convert_feet_to_millimeters(user_value):
        converted_value = user_value * 304.8
        return converted_value

    @staticmethod
    def convert_feet_to_inches(user_value):
        converted_value = user_value * 12
        return converted_value

    @staticmethod
    def convert_kilometers_to_miles(user_value):
        converted_value = user_value / 1.609344
        return converted_value

    @staticmethod
    def convert_kilometers_to_nautical_miles(user_value):
        converted_value = user_value / 1.852
        return converted_value

    @staticmethod
    def convert_kilometers_to_yards(user_value):
        converted_value = user_value / 0.0009144
        return converted_value

    @staticmethod
    def convert_kilometers_to_feet(user_value):
        converted_value = user_value / 0.0003048
        return converted_value

    @staticmethod
    def convert_kilometers_to_hectometers(user_value):
        converted_value = user_value * 10
        return converted_value

    @staticmethod
    def convert_kilometers_to_meters(user_value):
        converted_value = user_value * 1000
        return converted_value

    @staticmethod
    def convert_kilometers_to_centimeters(user_value):
        converted_value = user_value * 100000
        return converted_value

    @staticmethod
    def convert_kilometers_to_millimeters(user_value):
        converted_value = user_value * 1000000
        return converted_value

    @staticmethod
    def convert_kilometers_to_inches(user_value):
        converted_value = user_value / 0.0000254
        return converted_value

    @staticmethod
    def convert_hectometers_to_miles(user_value):
        converted_value = user_value / 16.09344
        return converted_value

    @staticmethod
    def convert_hectometers_to_nautical_miles(user_value):
        converted_value = user_value / 18.52
        return converted_value

    @staticmethod
    def convert_hectometers_to_yards(user_value):
        converted_value = user_value / 0.009144
        return converted_value

    @staticmethod
    def convert_hectometers_to_feet(user_value):
        converted_value = user_value / 0.003048
        return converted_value

    @staticmethod
    def convert_hectometers_to_kilometers(user_value):
        converted_value = user_value / 10
        return converted_value

    @staticmethod
    def convert_hectometers_to_meters(user_value):
        converted_value = user_value * 100
        return converted_value

    @staticmethod
    def convert_hectometers_to_centimeters(user_value):
        converted_value = user_value * 10000
        return converted_value

    @staticmethod
    def convert_hectometers_to_millimeters(user_value):
        converted_value = user_value * 100000
        return converted_value

    @staticmethod
    def convert_hectometers_to_inches(user_value):
        converted_value = user_value / 0.000254
        return converted_value

    @staticmethod
    def convert_meters_to_miles(user_value):
        converted_value = user_value / 1609.344
        return converted_value

    @staticmethod
    def convert_meters_to_nautical_miles(user_value):
        converted_value = user_value / 1852
        return converted_value

    @staticmethod
    def convert_meters_to_yards(user_value):
        converted_value = user_value / 0.9144
        return converted_value

    @staticmethod
    def convert_meters_to_feet(user_value):
        converted_value = user_value / 0.3048
        return converted_value

    @staticmethod
    def convert_meters_to_kilometers(user_value):
        converted_value = user_value / 1000
        return converted_value

    @staticmethod
    def convert_meters_to_hectometers(user_value):
        converted_value = user_value / 100
        return converted_value

    @staticmethod
    def convert_meters_to_centimeters(user_value):
        converted_value = user_value * 100
        return converted_value

    @staticmethod
    def convert_meters_to_millimeters(user_value):
        converted_value = user_value * 1000
        return converted_value

    @staticmethod
    def convert_meters_to_inches(user_value):
        converted_value = user_value / 0.0254
        return converted_value

    @staticmethod
    def convert_centimeters_to_miles(user_value):
        converted_value = user_value / 160934.4
        return converted_value

    @staticmethod
    def convert_centimeters_to_nautical_miles(user_value):
        converted_value = user_value / 185200
        return converted_value

    @staticmethod
    def convert_centimeters_to_yards(user_value):
        converted_value = user_value / 91.44
        return converted_value

    @staticmethod
    def convert_centimeters_to_feet(user_value):
        converted_value = user_value / 30.48
        return converted_value

    @staticmethod
    def convert_centimeters_to_kilometers(user_value):
        converted_value = user_value / 100000
        return converted_value

    @staticmethod
    def convert_centimeters_to_hectometers(user_value):
        converted_value = user_value / 10000
        return converted_value

    @staticmethod
    def convert_centimeters_to_meters(user_value):
        converted_value = user_value / 100
        return converted_value

    @staticmethod
    def convert_centimeters_to_millimeters(user_value):
        converted_value = user_value * 10
        return converted_value

    @staticmethod
    def convert_centimeters_to_inches(user_value):
        converted_value = user_value / 2.54
        return converted_value

    @staticmethod
    def convert_millimeters_to_miles(user_value):
        converted_value = user_value / 1609344
        return converted_value

    @staticmethod
    def convert_millimeters_to_nautical_miles(user_value):
        converted_value = user_value / 1852000
        return converted_value

    @staticmethod
    def convert_millimeters_to_yards(user_value):
        converted_value = user_value / 914.4
        return converted_value

    @staticmethod
    def convert_millimeters_to_feet(user_value):
        converted_value = user_value / 304.8
        return converted_value

    @staticmethod
    def convert_millimeters_to_kilometers(user_value):
        converted_value = user_value / 1000000
        return converted_value

    @staticmethod
    def convert_millimeters_to_hectometers(user_value):
        converted_value = user_value / 100000
        return converted_value

    @staticmethod
    def convert_millimeters_to_meters(user_value):
        converted_value = user_value / 1000
        return converted_value

    @staticmethod
    def convert_millimeters_to_centimeters(user_value):
        converted_value = user_value / 10
        return converted_value

    @staticmethod
    def convert_millimeters_to_inches(user_value):
        converted_value = user_value / 25.4
        return converted_value

    @staticmethod
    def convert_inches_to_miles(user_value):
        converted_value = user_value / 63360
        return converted_value

    @staticmethod
    def convert_inches_to_nautical_miles(user_value):
        converted_value = user_value / 72913.3858
        return converted_value

    @staticmethod
    def convert_inches_to_yards(user_value):
        converted_value = user_value / 36
        return converted_value

    @staticmethod
    def convert_inches_to_feet(user_value):
        converted_value = user_value / 12
        return converted_value

    @staticmethod
    def convert_inches_to_kilometers(user_value):
        converted_value = user_value * 0.0000254
        return converted_value

    @staticmethod
    def convert_inches_to_hectometers(user_value):
        converted_value = user_value * 0.000254
        return converted_value

    @staticmethod
    def convert_inches_to_meters(user_value):
        converted_value = user_value * 0.0254
        return converted_value

    @staticmethod
    def convert_inches_to_centimeters(user_value):
        converted_value = user_value * 2.54
        return converted_value

    @staticmethod
    def convert_inches_to_millimeters(user_value):
        converted_value = user_value * 25.4
        return converted_value

    """Energy Conversion Methods"""

    @staticmethod
    def convert_terajoules_to_gigajoules(user_value):
        converted_value = user_value * 1000
        return converted_value

    @staticmethod
    def convert_terajoules_to_megajoules(user_value):
        converted_value = user_value * 1000000
        return converted_value

    @staticmethod
    def convert_terajoules_to_kilojoules(user_value):
        converted_value = user_value * 1000000000
        return converted_value

    @staticmethod
    def convert_terajoules_to_joules(user_value):
        converted_value = user_value * 1000000000000
        return converted_value

    @staticmethod
    def convert_terajoules_to_kilocalories(user_value):
        converted_value = user_value / 0.000000004184
        return converted_value

    @staticmethod
    def convert_terajoules_to_calories(user_value):
        converted_value = user_value / 0.000000000004184
        return converted_value

    @staticmethod
    def convert_gigajoules_to_terajoules(user_value):
        converted_value = user_value / 1000
        return converted_value

    @staticmethod
    def convert_gigajoules_to_megajoules(user_value):
        converted_value = user_value * 1000
        return converted_value

    @staticmethod
    def convert_gigajoules_to_kilojoules(user_value):
        converted_value = user_value * 1000000
        return converted_value

    @staticmethod
    def convert_gigajoules_to_joules(user_value):
        converted_value = user_value * 1000000000
        return converted_value

    @staticmethod
    def convert_gigajoules_to_kilocalories(user_value):
        converted_value = user_value / 0.000004184
        return converted_value

    @staticmethod
    def convert_gigajoules_to_calories(user_value):
        converted_value = user_value / 0.000000004184
        return converted_value

    @staticmethod
    def convert_megajoules_to_terajoules(user_value):
        converted_value = user_value / 1000000
        return converted_value

    @staticmethod
    def convert_megajoules_to_gigajoules(user_value):
        converted_value = user_value / 1000
        return converted_value

    @staticmethod
    def convert_megajoules_to_kilojoules(user_value):
        converted_value = user_value * 1000
        return converted_value

    @staticmethod
    def convert_megajoules_to_joules(user_value):
        converted_value = user_value * 1000000
        return converted_value

    @staticmethod
    def convert_megajoules_to_kilocalories(user_value):
        converted_value = user_value / 0.004184
        return converted_value

    @staticmethod
    def convert_megajoules_to_calories(user_value):
        converted_value = user_value / 0.000004184
        return converted_value

    @staticmethod
    def convert_kilojoules_to_terajoules(user_value):
        converted_value = user_value / 1000000000
        return converted_value

    @staticmethod
    def convert_kilojoules_to_gigajoules(user_value):
        converted_value = user_value / 1000000
        return converted_value

    @staticmethod
    def convert_kilojoules_to_megajoules(user_value):
        converted_value = user_value / 1000
        return converted_value

    @staticmethod
    def convert_kilojoules_to_joules(user_value):
        converted_value = user_value * 1000
        return converted_value

    @staticmethod
    def convert_kilojoules_to_kilocalories(user_value):
        converted_value = user_value / 4.184
        return converted_value

    @staticmethod
    def convert_kilojoules_to_calories(user_value):
        converted_value = user_value / 0.004184
        return converted_value

    @staticmethod
    def convert_joules_to_terajoules(user_value):
        converted_value = user_value / 1000000000000
        return converted_value

    @staticmethod
    def convert_joules_to_gigajoules(user_value):
        converted_value = user_value / 1000000000
        return converted_value

    @staticmethod
    def convert_joules_to_megajoules(user_value):
        converted_value = user_value / 1000000
        return converted_value

    @staticmethod
    def convert_joules_to_kilojoules(user_value):
        converted_value = user_value / 1000
        return converted_value

    @staticmethod
    def convert_joules_to_kilocalories(user_value):
        converted_value = user_value / 4184
        return converted_value

    @staticmethod
    def convert_joules_to_calories(user_value):
        converted_value = user_value / 4.184
        return converted_value

    @staticmethod
    def convert_kilocalories_to_terajoules(user_value):
        converted_value = user_value * 0.000000004184
        return converted_value

    @staticmethod
    def convert_kilocalories_to_gigajoules(user_value):
        converted_value = user_value * 0.000004184
        return converted_value

    @staticmethod
    def convert_kilocalories_to_megajoules(user_value):
        converted_value = user_value * 0.004184
        return converted_value

    @staticmethod
    def convert_kilocalories_to_kilojoules(user_value):
        converted_value = user_value * 4.184
        return converted_value

    @staticmethod
    def convert_kilocalories_to_joules(user_value):
        converted_value = user_value * 4184
        return converted_value

    @staticmethod
    def convert_kilocalories_to_calories(user_value):
        converted_value = user_value * 1000
        return converted_value

    @staticmethod
    def convert_calories_to_terajoules(user_value):
        converted_value = user_value * 0.000000000004184
        return converted_value

    @staticmethod
    def convert_calories_to_gigajoules(user_value):
        converted_value = user_value * 0.000000004184
        return converted_value

    @staticmethod
    def convert_calories_to_megajoules(user_value):
        converted_value = user_value * 0.000004184
        return converted_value

    @staticmethod
    def convert_calories_to_kilojoules(user_value):
        converted_value = user_value * 0.004184
        return converted_value

    @staticmethod
    def convert_calories_to_joules(user_value):
        converted_value = user_value * 4.184
        return converted_value

    @staticmethod
    def convert_calories_to_kilocalories(user_value):
        converted_value = user_value / 1000
        return converted_value

    """Pressure Conversion Methods"""

    @staticmethod
    def convert_atmospheres_to_bars(user_value):
        converted_value = user_value * 1.01325
        return converted_value

    @staticmethod
    def convert_atmospheres_to_torr(user_value):
        converted_value = user_value * 760
        return converted_value

    @staticmethod
    def convert_atmospheres_to_kilopascals(user_value):
        converted_value = user_value * 101.325
        return converted_value

    @staticmethod
    def convert_atmospheres_to_pascals(user_value):
        converted_value = user_value * 101325
        return converted_value

    @staticmethod
    def convert_bars_to_atmospheres(user_value):
        converted_value = user_value / 1.01325
        return converted_value

    @staticmethod
    def convert_bars_to_torr(user_value):
        converted_value = user_value / 0.001333223684
        return converted_value

    @staticmethod
    def convert_bars_to_kilopascals(user_value):
        converted_value = user_value * 100
        return converted_value

    @staticmethod
    def convert_bars_to_pascals(user_value):
        converted_value = user_value * 100000
        return converted_value

    @staticmethod
    def convert_torr_to_atmospheres(user_value):
        converted_value = user_value / 760
        return converted_value

    @staticmethod
    def convert_torr_to_bars(user_value):
        converted_value = user_value * 0.001333223684
        return converted_value

    @staticmethod
    def convert_torr_to_kilopascals(user_value):
        converted_value = user_value * 0.1333223684
        return converted_value

    @staticmethod
    def convert_torr_to_pascals(user_value):
        converted_value = user_value * 133.3223684
        return converted_value

    @staticmethod
    def convert_kilopascals_to_atmospheres(user_value):
        converted_value = user_value / 101.325
        return converted_value

    @staticmethod
    def convert_kilopascals_to_bars(user_value):
        converted_value = user_value / 100
        return converted_value

    @staticmethod
    def convert_kilopascals_to_torr(user_value):
        converted_value = user_value / 0.1333223684
        return converted_value

    @staticmethod
    def convert_kilopascals_to_pascals(user_value):
        converted_value = user_value * 1000
        return converted_value

    @staticmethod
    def convert_pascals_to_atmospheres(user_value):
        converted_value = user_value / 101325
        return converted_value

    @staticmethod
    def convert_pascals_to_bars(user_value):
        converted_value = user_value / 100000
        return converted_value

    @staticmethod
    def convert_pascals_to_torr(user_value):
        converted_value = user_value / 133.3223684
        return converted_value

    @staticmethod
    def convert_pascals_to_kilopascals(user_value):
        converted_value = user_value / 1000
        return converted_value
