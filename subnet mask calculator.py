#If you are anything like me, you may forget the subnet calculations quite often.
#Chances are, you want to save time
#Here is my silly little program I made with Tkinter
import tkinter as tk
from ipaddress import ip_network, ip_interface

def calculate_subnet_details():
    try:
        ip_cidr = entry_ip.get()
        ip_obj = ip_interface(ip_cidr)

        network = ip_obj.network
        broadcast = network.broadcast_address
        num_ips = network.num_addresses

        is_broadcast = ip_obj.ip == broadcast

        label_result.config(text=f"Network Address: {network.network_address}\n"
                                f"Broadcast Address: {broadcast}\n"
                                f"Number of IPs: {num_ips}\n")

    except ValueError as e:
        label_result.config(text="Invalid IP or Subnet. Please try again.")

#This block is what you will want to edit if you would like to change any of the features
#root.resizable(False, False) makes it so that the window is not resizable, I did this because I thought it looked better small
#disable_fullscreen disables fullscreen
#root.attributes("-topmost", 1) tells the window to always stay at the topmost layer, for ease of use when working
root = tk.Tk()
root.resizable(False, False)
def disable_fullscreen(event=None):
    return "break"
root.attributes("-topmost", 1)
root.title("Subnet Calculator")


label_ip = tk.Label(root, text="Enter IP Address (CIDR):")
label_ip.pack()

entry_ip = tk.Entry(root, width=30)
entry_ip.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate_subnet_details)
button_calculate.pack()

label_result = tk.Label(root, text="", justify=tk.LEFT)
label_result.pack()

root.mainloop()
