from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException
import getpass
import pandas as pd
import os
import csv
import time


with open("ips_OLT_test.txt", "r") as f:
  X = f.read().splitlines()
  for IP in X:
    try:  
      pwd = getpass.getpass('Please enter the password:')
      device = {
      "host":IP,  
      "username":"xyz", #change this as per your requirement 
      "password":"pwd", #change this as per your requirement
      "secret": "abc",
      "device_type":"keymile_nos",
      "session_log": "netmiko.log"
      }
      with ConnectHandler(**device) as c:
        c.enable()
        firmware=c.send_command("show onu firmware version")
        Onuinfo=c.send_command("show onu info")
        print(f'{IP}\n')
        print(f'show onu firmware\n{firmware}')
        print((f"show onu info\n{Onuinfo},\n"))
    
      with open("14July.txt", "a") as f:
        f.write(f"OLT ip address is {IP},\n")
        f.write(f"{firmware},\n")
        f.write(f"show onu info\n{Onuinfo},\n")
        #f.write(f"{Onuinfo},\n")

      print('delay for 5sec')
      time.sleep(5)

    except Exception as e:
        print (f"error",e,IP)      
        with open ("OLTerror.txt","a") as fileerror:
            fileerror.write(f"{IP}\n")