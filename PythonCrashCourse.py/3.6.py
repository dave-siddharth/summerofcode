import os
import math

# Initial guest list
guest_list = ["Kinjal", "Mum", "Kinsha"]

# Informing about the guest who can't make it
unable_to_attend = "Mum"
print(f"Unfortunately, {unable_to_attend} can't make it to the dinner.\n")

# Replacing the guest who can't make it with a new guest
new_guest = "Sid"
guest_list[guest_list.index(unable_to_attend)] = new_guest

# Informing that a bigger dinner table is available
print("Good news! I found a bigger dinner table, so now I can invite more guests!\n")

# Adding more guests
guest_list.insert(0, "Kaku")  # Adding to the beginning
guest_list.insert(2, "Kaki")    # Adding to the middle
guest_list.append("Evan")        # Adding to the end

# Printing the new set of invitation messages
for guest in guest_list:
    print(f"Dear {guest},\nYou are cordially invited to dinner. I would be honored to have you join me.\n")
