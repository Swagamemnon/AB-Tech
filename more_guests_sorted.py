# create a list of dinner guests
guest_list = ['kanye west', 'barack obama', 'leonardo da Vinci']
# add more guests 
print("Dear Guests, good news! I am now able to invite more VIPs!")
guest_list.insert(0, 'taylor swift')
guest_list.insert(2, 'meryl streep')
guest_list.append('nikki haley')
# sort the list alphabetically
guest_list.sort()
print(guest_list)
# create a new message for guests
print(f"My party couldn't be complete without {guest_list[0].title()}!!!")
print(f"My party couldn't be complete without {guest_list[1].title()}!!!")
print(f"My party couldn't be complete without {guest_list[2].title()}!!!")
print(f"My party couldn't be complete without {guest_list[3].title()}!!!")
print(f"My party couldn't be complete without {guest_list[4].title()}!!!")
print(f"My party couldn't be complete without {guest_list[5].title()}!!!")