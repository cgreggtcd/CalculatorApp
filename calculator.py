def calculate(input):
    answer = multiply_string(input)
    return int(answer)

def multiply_string(input):
    index_of_mul = input.find("*")

    # If there is no * in the equation
    if index_of_mul == -1:
        return input

    # Find the start of the multiplicand
    start_multiplicand = index_of_mul - 1
    while start_multiplicand > 0 and input[start_multiplicand].isdigit():
        start_multiplicand -= 1
    # Calculate the multiplicand
    multiplicand = int(input[start_multiplicand:index_of_mul])

    # Find the end of the multiplier
    end_multiplier = index_of_mul + 1
    while end_multiplier < len(input) and input[end_multiplier].isdigit():
        end_multiplier += 1
    # Calculate the multiplier
    multiplier = int(input[index_of_mul+1:end_multiplier])

    # Recursively call the method, replacing the part that was calculated with the answer
    return multiply_string(input[:start_multiplicand]
        + str(multiplicand * multiplier) + input[end_multiplier:])
