# import md5 library
import hashlib

# variable to hold the input string
some_string = "ckczppom"

# variable to hold the integer counter
some_number = 0

# variable to stick the string and number together
puzzle_input = some_string + str(some_number)

# loop until the md5 checksum has "00000" as the first 5 characters
while True:
    output = hashlib.md5(puzzle_input.encode('utf-8')).hexdigest()
    if output[:5] == "00000":
        print("Part 1 answer is:", some_number)
        break
    some_number = some_number + 1
    puzzle_input = some_string + str(some_number)

# Part 2 starts here
# initialize the integer counter
some_number = 0

# loop until the md5 checksum has "000000" as the first 6 characters
while True:
    output = hashlib.md5(puzzle_input.encode('utf-8')).hexdigest()
    if output[:6] == "000000":
        print("Part 2 answer is:", some_number)
        break
    some_number = some_number + 1
    puzzle_input = some_string + str(some_number)




