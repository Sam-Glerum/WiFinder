import sys
import os

class InterfaceSelector():

    def __init__(self):
        pass

    def menu(self):
        self.interface_scanner()
        print("\nSelect the interface to use for scanning networks from the list above")
        choice = input(">")

        self.set_interface_to_monitor_mode(choice)
        input("Press any key to revert")

    def interface_scanner(self):
        print("Available network interfaces:")
        os.system("ls /sys/class/net")

    def set_interface_to_monitor_mode(self, network_interface):
        print("Setting interface {} to monitor mode".format(network_interface))
        os.system("sudo ifconfig {} down")
        os.system("sudo iwconfig {} mode monitor")
        os.system("sudo ifconfig {} up")
        print("Interface {} has been set to monitor mode")

    def set_interface_to_managed_mode(self, network_interface):
        print("Setting interface {} to managed".format(network_interface))
        os.system("sudo ifconfig {} down")
        os.system("sudo iwconfig {} mode managed")
        os.system("sudo ifconfig {} up")
        print("Interface {} has been set to managed mode")