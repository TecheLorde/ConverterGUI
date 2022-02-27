from guichoice import GuiChoice

gui_c = GuiChoice()
gui_c.identify_os()
try:
    if gui_c.operating_system == "Windows":
        print("Its Bill Gates!")
        gui_c.call_windows_gui()
except RuntimeError:
    print("Something went wrong, contact support")
