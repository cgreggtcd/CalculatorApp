def calculate(input):
    answer = multiply_string(input)
    answer = add_string(answer)
    return int(answer)

# This function resolves any sets of two signs: +- -> -, -+ -> -, -- -> +
def resolve_signs(input):
    prevChar = input[0]
    i = 1
    while i < len(input):
        currChar = input[i]
        print("prevChar = {}, currChar = {}".format(prevChar, currChar))

        if (prevChar == "-" and currChar == "+") or (prevChar == "+" and currChar == "-"):
            input = input[:i-1] + "-" + input[i+1:]
            # Then, everything after the second +/- is one to the left
            prevChar = input[i]
            i+=1
            print("New input is {}, new prevChar = {}, new i = {}".format(input, prevChar, i))

        elif prevChar == "-" and currChar == "-":
            input = input[:i-1] + "+" + input[i+1:]
            # Then, everything after the second +/- is one to the left
            prevChar = input[i]
            i+=1
            print("New input is {}, new prevChar = {}, new i = {}".format(input, prevChar, i))

        else:
            i += 1
            prevChar = currChar

    return input

def multiply_string(input):
    index_of_mul = input.find("*")

    # If there is no * in the equation
    if index_of_mul == -1:
        return input

    # Find the start of the multiplicand
    start_multiplicand = index_of_mul - 1
    while start_multiplicand-1 >= 0 and input[start_multiplicand-1].isdigit():
        start_multiplicand -= 1
    if start_multiplicand-1 == 0 and input[start_multiplicand-1] == "-":
        start_multiplicand -= 1
    # Calculate the multiplicand
    multiplicand = int(input[start_multiplicand:index_of_mul])

    # Find the end of the multiplier
    end_multiplier = index_of_mul + 1
    if input[end_multiplier] == "-":
        end_multiplier += 1
    while end_multiplier < len(input) and input[end_multiplier].isdigit():
        end_multiplier += 1
    # Calculate the multiplier
    multiplier = int(input[index_of_mul + 1:end_multiplier])

    # Recursively call the method, replacing the part that was calculated with the answer
    return multiply_string(input[:start_multiplicand]
                           + str(multiplicand * multiplier) + input[end_multiplier:])


def add_string(input):
    # using similar naming convention as the multiplication function
    index_of_add = input.find("+")

    # If no addition operations are found
    if index_of_add == -1:
        return input

    # Find the augend (number to which another is added)
    start_augend = index_of_add - 1
    while start_augend > 0 and input[start_augend].isdigit():
        start_augend -= 1

    # Calculate the start_augend
    augend = int(input[start_augend:index_of_add])

    # Find the end of the addend
    end_addend = index_of_add + 1
    while end_addend < len(input) and input[end_addend].isdigit():
        end_addend += 1

    # Calculate the addend
    addend = int(input[index_of_add + 1:end_addend])

    # Recursively call the method, replacing the calculated part with the answer
    return add_string(input[:start_augend] + str(augend + addend)
                      + input[end_addend:])
