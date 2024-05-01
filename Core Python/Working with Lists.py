
lucky_numbers = [4, 8, 15, 23, 42]
friends = ["Nicat", "Nihat", "Fuad", "Mozart", "Kamal"]    # inside list there can be numbers, booleans and etc.

print(friends)
print(friends[0])   # prints 1st element
print(friends[-1])  # prints 1st element from end
print(friends[1:])  # prints all elements after 2nd
print(friends[1:3]) # prints all between 2nd and 3rd (take 2nd, till 3rd)

# updating list element:
friends[4] = "Mustafa"
print(friends)


# LIST FUNCTIONS
friends.extend(lucky_numbers)
print(friends)  # will give friends list with lucky_numbers
friends.append("Osman") # add item edn of the list
friends.insert(1, "Kevin")  # will add Kevin to the 1 index
friends.remove("Osman") # will remove Osman from list
friends.clear() # will celar list
friends.pop()   #removes the last element from list
print(friends.index("Nicat"))   # willgive the index of the item, if there's not, will give error
friends.count("Jim")    # how many Jims are there
friends.sort()  # will sort as alphabetic order (ascending)
lucky_numbers.reverse() # reverse the order of the list
friends = friends.copy() # will basically copy previous list