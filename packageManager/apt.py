"""
APT

About
apt is a commandline package manager and provides commands for
searching and managing as well as querying information about packages.
It provides the same functionality as the specialized APT tools,
like apt-get and apt-cache, but enables options more suitable for
interactive use by default.
"""

from packageManager.config import *
class apt:
    def __init__(self):
        pass
    def install(self):
        pass
    def uninstall(self):
        pass
    def show(self):
        pass
    def reinstall(self):
        pass
    def full_upgrade(self):
        pass
    def search(self):
        pass
    def list_installed_packages(self):
        return os.system("apt list")