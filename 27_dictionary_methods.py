myDict = {
    "fast": "In a Quick Manner",
    "Sanyam": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'Sanyam': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "Sanyam": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Sanyam")) # Prints value associated with key "Sanyam"
print(myDict["Sanyam"]) # Prints value associated with key "Sanyam"

# The difference between .get and [] syntax in Dictionaries?
print(myDict.get("Sanyam2")) # Returns None as Sanyam2 is not present in the dictionary
print(myDict["Sanyam2"]) # throws an error as Sanyam2 is not present in the dictionary