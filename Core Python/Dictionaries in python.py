
# Dictionary is a special structure in Python that allows us to store key/value pairs
# In order to acces value or information, we must refer to its key
# lets create Jan -> January, Mar -> March
monthConversions = {
    "Jan":"January",     # key : value
    "Feb": "February",
    "Mar": "March",      # ALL KEYS MUST BE UNIQUE
    "Apr": "April",
    "May": "May",        # we can use numbers in key values as well
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])      # we refer to the key, and get value we want
print(monthConversions.get("Dec"))  # another way to get value. 
print(monthConversions.get("Abc", "Not a valid key"))  # we get default value in get function

