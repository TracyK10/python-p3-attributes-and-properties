#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def get_name(self):
        print("Retrieving name.")
        return self._name 
    
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Setting name to {name}.")
            self._name = name
        else:
            print("Name must be a string between 1 and 25 characters.")
    
    def get_breed(self):
        print("Retrieving breed.")
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            print(f"Setting breed to {breed}.")
            self._breed = breed
        else:
            print("Breed must be in the list of approved breeds.")
    
    def __str__(self):
        return f"Dog(name={self._name}, breed={self._breed})"
    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

# Example of creating a Dog instance and printing it
fido = Dog("Fido", "Beagle")
print(fido)
