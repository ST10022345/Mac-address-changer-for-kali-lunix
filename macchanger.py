#!/usr/bin/env python

import subprocess
import optparse
import re


def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-]please specify and interface user --help for more info")
    elif not options.new_mac:
        parser.error("[-]please enter a new mac address use --help for more info")
    return options


def changeMac(interface, new_mac):

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def getCurrentMac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_result:
        return mac_address_result.group(0)
    else:
        print("[-]error,could not get mac address")


options = getArguments()
current_mac = getCurrentMac(options.interface)

print("The current mac is:" + str(current_mac))

changeMac(options.interface, options.new_mac)

current_mac = getCurrentMac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was changed to " + current_mac)
else:
    print("[-] MAC address did not get changed")





