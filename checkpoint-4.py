#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
print ("Exercise 1:")

my_list = [1, 2, 3, 4, 5]
print ("List", my_list)

my_tuple = (6, 7, 8, 9, 10)
print ("Tuple", my_tuple)

my_float = 3.14
print ("Float", my_float)

my_integer = 42
print ("Integer", my_integer)

my_decimal = 3.141592
print ("Decimal", my_decimal)

my_dictionary = {
    "nombre": "Elena",
    "edad": 30, 
    "ciudad": "Vitoria-Gasteiz",
}

print ("Dictionary", my_dictionary)

#Exercise 2: Round your float up.

rounded_float = round(my_float)

print ("Exercise 2:", rounded_float)

#Exercise 3: Get the square root of your float.

square_float = my_float ** 0.5

print ("Exercise 3:", square_float)

#Exercise 4: Select the first element from your dictionary.

first_element = my_dictionary["nombre"]

print ("Exercise 4:", first_element)

#Exercise 5: Select the second element from your tuple.

second_element = my_tuple[1]

print ("Exercise 5:", second_element)

#Exercise 6: Add an element to the end of your list.

new_element = 6
position = len(my_list)
my_list.insert(position, new_element)

print ("Exercise 6:", my_list)

#Exercise 7: Replace the first element in your list.

my_list[0] = 8

print ("Exercise 7:", my_list)

#Exercise 8: Sort your list alphabetically.

my_list.sort()

print ("Exercise 8:", my_list)

#Exercise 9: Use reassignment to add an element to your tuple.

my_tuple += (11,)

print ("Exercise 9:", my_tuple)