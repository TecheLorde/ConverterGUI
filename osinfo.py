"""Detects operating system and displays appropriate GUI"""
import platform
from windowsgui import WindowsGUI
from linuxgui import LinuxGUI
from macgui import MacGUI
# import pandas


class GuiChoice:
    def __init__(self):
        self.operating_system = ""
        self.version_number = ""
        self.gui_selection = ""

    def get_os(self):
        self.operating_system = platform.system()
        return self.operating_system

    def get_os_version(self):
        self.version_number = platform.release()
        return self.version_number

    def identify_os(self):
        self.get_os()
        self.get_os_version()
        return self.operating_system, self.version_number

    def call_windows_gui(self):
        self.gui_selection = "Windows"
        win_gui = WindowsGUI()
        win_gui.display_gui()
        return self.gui_selection

    def call_linux_gui(self):
        self.gui_selection = "Linux"
        lin_gui = LinuxGUI()
        lin_gui.display_gui()
        return self.gui_selection

    def call_mac_gui(self):
        self.gui_selection = "Linux"
        mac_gui = MacGUI()
        mac_gui.display_gui()
        return self.gui_selection
