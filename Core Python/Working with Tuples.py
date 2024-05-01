
# Tuple is a container and stores different values.
# Very similar of list. But there are key differences

coordinates = (4, 5)
# TUPLES ARE IMMUTABLE. they cannot be changed or modified. we cannot change ANYTHING inside tuple
print(coordinates[0])
coordinates[1] = 10   # TypeError: 'tuple' object does not support item assignment. bcs they are immutable

# People use tuples for datas that never change, such as coordinates
