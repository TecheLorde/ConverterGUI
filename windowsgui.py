import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# from tkinter import font
from converter import Converter

conv = Converter()


class WindowsGUI:
    def __init__(self):
        self.is_on = True
        """The encoding is set to allow future extensions to be compatible, font is kept as default for now"""
        self.uft_encode = "utf-8"
        self.font = ""
        self.root = tk.Tk()
        self.temp_units = ['Celsius', 'Fahrenheit', 'Kelvin']
        self.weight_units = ['Kilograms', 'Ounces']
        self.conversion_choice = ""
        self.conversion_type_choice_labelframe = ttk.Labelframe(self.root, text="Type Choice")
        self.temp_choice_button = ttk.Button(self.conversion_type_choice_labelframe, text="Temperature")
        self.weight_choice_button = ttk.Button(self.conversion_type_choice_labelframe, text="Weight")
        self.distance_choice_button = ttk.Button(self.conversion_type_choice_labelframe, text="Distance")
        self.energy_choice_button = ttk.Button(self.conversion_type_choice_labelframe, text="Energy")
        self.force_choice_button = ttk.Button(self.conversion_type_choice_labelframe, text="Force")
        self.unit_choices_labelframe = ttk.Labelframe(self.root, text="Choose Units")
        self.from_unit = ""
        self.first_unit_label = ttk.Label(self.unit_choices_labelframe, text="First Unit")
        self.first_unit = ttk.Combobox(self.unit_choices_labelframe, values=[])
        self.to_unit = ""
        self.second_unit_label = ttk.Label(self.unit_choices_labelframe, text="Second Unit")
        self.second_unit = ttk.Combobox(self.unit_choices_labelframe, values=[])
        self.starting_accuracy = tk.StringVar()
        self.starting_accuracy.set("1")
        self.accuracy = 1
        self.choose_accuracy_label = ttk.Label(self.unit_choices_labelframe, text="Decimal places")
        self.choose_accuracy = ttk.Spinbox(self.unit_choices_labelframe, increment=1, from_=1, to=6,
                                           textvariable=self.starting_accuracy)
        self.result_label = ttk.Label(self.unit_choices_labelframe, text="The result is..")
        self.result_output = tk.Text(self.unit_choices_labelframe, height=1, width=10)
        self.convert_button = ttk.Button(self.root, text="Convert")
        self.user_value_label = ttk.Label(self.unit_choices_labelframe, text="Enter Value")
        self.reset_button = ttk.Button(self.root, text="Reset")
        self.user_value = ttk.Entry(self.unit_choices_labelframe)
        self.user_value_stored = 0.0
        self.converted_value = 0.0
        self.canvas_window_frame = ttk.Frame(self.root)
        self.logo_canvas = tk.Canvas(self.canvas_window_frame)
        self.logo_img = tk.PhotoImage(file="Documents/placeholdLogo1.png")
        self.s = ttk.Style()

    def convert_button_method(self):
        try:
            self.user_value_stored = float(self.user_value.get())
            self.check_user_inputs()
            if -1000001 < self.user_value_stored < 1000001:
                self.result_output.delete('1.0', 'end')
                if self.from_unit == 'Celsius' and self.to_unit == 'Fahrenheit':
                    conv.user_value = self.user_value_stored
                    self.converted_value = conv.convert_celsius_to_fahrenheit()
                elif self.from_unit == 'Celsius' and self.to_unit == 'Kelvin':
                    conv.user_value = self.user_value_stored
                    self.converted_value = conv.convert_celsius_to_kelvin()
                elif self.from_unit == 'Fahrenheit' and self.to_unit == 'Celsius':
                    conv.user_value = self.user_value_stored
                    self.converted_value = conv.convert_fahrenheit_to_celsius()
                elif self.from_unit == 'Fahrenheit' and self.to_unit == 'Kelvin':
                    conv.user_value = self.user_value_stored
                    self.converted_value = conv.convert_fahrenheit_to_kelvin()
                elif self.from_unit == 'Kelvin' and self.to_unit == 'Celsius':
                    conv.user_value = self.user_value_stored
                    self.converted_value = conv.convert_kelvin_to_celsius()
                elif self.from_unit == 'Kelvin' and self.to_unit == 'Fahrenheit':
                    conv.user_value = self.user_value_stored
                    self.converted_value = conv.convert_kelvin_to_fahrenheit()
                self.converted_value = round(self.converted_value, self.accuracy)
                print(self.converted_value)
                self.remove_error_highlights()
                self.user_output()
        except ValueError:
            self.check_user_inputs()

    def user_output(self):
        self.result_output.insert('1.0', str(self.converted_value))
        return self.converted_value

    def show_temp_options(self):
        self.first_unit.config(values=self.temp_units)
        self.second_unit.config(values=self.temp_units)

    def show_weight_options(self):
        self.first_unit.config(values=self.weight_units)
        self.second_unit.config(values=self.weight_units)

    def set_first_unit(self, event):
        self.from_unit = event.widget.get()
        return self.from_unit

    def set_second_unit(self, event):
        self.to_unit = event.widget.get()
        return self.to_unit

    def get_accuracy(self):
        self.accuracy = int(self.choose_accuracy.get())
        print(self.accuracy)
        return self.accuracy

    def check_user_inputs(self):
        self.user_value.config(foreground="red")
        if -1000000 > self.user_value_stored > 1000000:
            self.user_value.config(foreground="red")
            messagebox.showerror("Error", message="Enter a number", detail="Enter a number from"
                                                                           " -1,000,000 to 1,000,000")
        if self.from_unit == "" or self.to_unit == "":
            messagebox.showerror(title="Error", message="Select conversion units!")

    def remove_error_highlights(self):
        self.user_value.config(foreground="")
        return self.user_value

    def reset_function(self):
        self.get_accuracy()
        self.result_output.delete('1.0', 'end')
        self.first_unit.set('')
        self.second_unit.set('')
        self.user_value_stored = 0.0
        self.user_value.delete(0, 'end')
        return self.result_output

    def style_widgets(self):
        self.root.config(bg='#7fadf7')
        self.s.configure('TLabelframe', background='#7fadf7', borderwidth=5, padding=5)

    def place_gui_elements(self):
        self.conversion_type_choice_labelframe.grid(column=0, row=0)
        self.temp_choice_button.grid(column=0, row=0)
        self.weight_choice_button.grid(column=0, row=1)
        self.distance_choice_button.grid(column=0, row=2)
        self.energy_choice_button.grid(column=0, row=3)
        self.force_choice_button.grid(column=0, row=4)
        self.unit_choices_labelframe.grid(column=1, row=0)
        self.first_unit_label.grid(column=0, row=0)
        self.first_unit.grid(column=1, row=0)
        self.second_unit_label.grid(column=0, row=1)
        self.second_unit.grid(column=1, row=1)
        self.choose_accuracy_label.grid(column=0, row=2)
        self.choose_accuracy.grid(column=1, row=2)
        self.user_value_label.grid(column=0, row=3)
        self.user_value.grid(column=1, row=3)
        self.result_label.grid(column=0, row=4)
        self.result_output.grid(column=1, row=4)
        self.convert_button.grid(column=1, row=3)
        self.reset_button.grid(column=0, row=3)
        self.canvas_window_frame.grid(column=0, row=4, columnspan=2)
        self.logo_canvas.grid(columnspan=2, column=0, row=5)
        self.logo_canvas.create_image(0, 0, anchor='nw', image=self.logo_img)

    def initialise_gui_elements(self):
        self.temp_choice_button.config(command=self.show_temp_options)
        self.weight_choice_button.config(command=self.show_weight_options)
        self.convert_button.config(command=self.convert_button_method)
        self.first_unit.bind("<<ComboboxSelected>>", self.set_first_unit)
        self.second_unit.bind("<<ComboboxSelected>>", self.set_second_unit)
        self.choose_accuracy.config(command=self.get_accuracy)
        self.reset_button.config(command=self.reset_function)

    def display_gui(self):
        self.root.title("Converter Application")
        self.root.geometry('500x500')
        # self.root.state('zoomed')
        self.root.resizable(True, True)
        self.root.columnconfigure(0, weight=1)
        self.style_widgets()
        self.place_gui_elements()
        self.initialise_gui_elements()
        self.root.mainloop()
        self.is_on = False
        return self.is_on
