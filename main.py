"""Main"""
from osinfo import OsInfo
from tkinter import messagebox
from gui import GUI
gui = GUI()
os = OsInfo()
os.identify_os()
try:
    if os.operating_system == "Windows":
        version = os.get_os_version()
        if version == '10' or version == '8.1' or version == '8' or version == '7':
            gui.display_gui()
        else:
            messagebox.showerror(title="Incorrect Version", message="The application works on windows 7, 8, 8.1 and 10")
    elif os.operating_system == "Linux":
        gui.display_gui()
    elif os.operating_system == "Macintosh":
        gui.display_gui()
except RuntimeError:
    print("Something went wrong, contact support")
    messagebox.showerror(title="Error", message="Contact Support")
