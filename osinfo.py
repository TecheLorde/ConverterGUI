"""Detects operating system and displays appropriate GUI"""
import platform
# import pandas


class OsInfo:
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
