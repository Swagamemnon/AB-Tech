# copying a list using slices
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favorite foods are:')
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# print first three items in my_foods
print("The first three items in the list are:")
print(my_foods[:3])
# print 2 itmes from the middle of the list
print("Two items from the middle of the list are:")
print(my_foods[1:3])
# print the last three items in the list
print("The last three items in the list are:")
print(my_foods[1:])