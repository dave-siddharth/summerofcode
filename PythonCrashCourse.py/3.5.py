import os
import math

# Initial guest list
guest_list = ["Dad", "Mum", "Kinsha"]

# Informing about the guest who can't make it
unable_to_attend = "Mum"
print(f"Unfortunately, {unable_to_attend} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new guest
new_guest = "Sid"
guest_list[guest_list.index(unable_to_attend)] = new_guest

# Print the updated guest list and invitation messages
for guest in guest_list:
    print(f"Dear {guest},\nYou are cordially invited to dinner. I would be honored to have you join me.\n")
