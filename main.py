from guichoice import GuiChoice
from tkinter import messagebox
gui_c = GuiChoice()
gui_c.identify_os()
try:
    if gui_c.operating_system == "Windows":
        print("Its Bill Gates!")
        version = gui_c.get_os_version()
        if version == '10' or version == '8.1' or version == '8' or version == '7':
            gui_c.call_windows_gui()
        else:
            messagebox.showerror(title="Incorrect Version", message="The application works on windows 7, 8, 8.1 and 10")
except RuntimeError:
    print("Something went wrong, contact support")
