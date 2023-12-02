#MAC Address Changer
This Python script allows you to change the MAC (Media Access Control) address of a network interface on a Linux system. Changing the MAC address can be useful for various purposes, such as enhancing privacy or security. The script utilizes the ifconfig command to manipulate the network interface.

##Prerequisites
This script is designed for Linux systems.
Ensure that Python is installed on your machine.
Usage
Open a terminal.

Navigate to the directory containing the script.

Run the script with root privileges:

##bash
Copy code
sudo ./mac_changer.py -i <interface> -m <new_mac_address>
Replace <interface> with the name of your network interface (e.g., eth0, wlan0) and <new_mac_address> with the desired MAC address.

##Options
-i, --interface: Specify the network interface whose MAC address you want to change.
-m, --mac: Set the new MAC address.
Example
bash

sudo ./mac_changer.py -i wlan0 -m 00:11:22:33:44:55
Script Details
getArguments Function
Parses command-line arguments using the optparse module.
Requires the user to specify the network interface (-i) and the new MAC address (-m).
changeMac Function
Disables the specified network interface.
Changes the MAC address of the interface.
Enables the network interface.
getCurrentMac Function
Retrieves the current MAC address of the specified network interface using the ifconfig command.
Example
bash

$ ./mac_changer.py -i wlan0 -m 00:11:22:33:44:55
The current MAC is: 11:22:33:44:55:66
[+] MAC address was changed to 00:11:22:33:44:55
Note
Ensure that you have the necessary permissions to modify network interfaces (use sudo).
The script may not work on all Linux distributions or network interface types.
Disclaimer
This script is provided as-is and without any warranty. Use it responsibly and only on networks that you have permission to modify. Changing MAC addresses may violate the terms of service of some networks.

Author
Ethan Robinson

License
This project is licensed under the MIT License.