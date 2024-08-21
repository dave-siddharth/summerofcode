import os 
import math

# List of guests
guest_list = ["Mum", "Dad", "Kinsha"]

for guest in guest_list:
    print(f"Dear {guest},\nYou are invited to my dinner.\n")

def invite_guest(guest):
    return f"Dear {guest},\nPlease join as we will have a lot of food and drinks. It will be a pleasureable time!\n"

for guest in guest_list:
    print(invite_guest(guest))
