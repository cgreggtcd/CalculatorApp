def calculate(input):
    input = input.replace("--",'+')
    answer = multiply_string(input)
    answer = add_string(answer)
    answer = subtract_string(answer)
    # replace special string "neg" with '-' once all operation have been calculated
    answer = answer.replace("neg", "-")
    answer = answer.replace('-','', answer.count('-')-1)
    return int(answer)


def multiply_string(input):
    print(input)
    index_of_mul = input.find("*")

    # If there is no * in the equation
    if index_of_mul == -1:
        return input

    # Find the start of the multiplicand
    start_multiplicand = index_of_mul - 1
    while start_multiplicand > 0 and input[start_multiplicand-1].isdigit():
        start_multiplicand -= 1
    # Calculate the multiplicand
    multiplicand = int(input[start_multiplicand:index_of_mul])

    if((found_negative(input[:index_of_mul], multiplicand))==1):
        print(multiplicand)
        multiplicand = -multiplicand
        print(multiplicand)
        #input = input.replace(str(input[start_multiplicand-1]),'')
        #index_of_mul -= 1

    # Find the end of the multiplier
    end_multiplier = index_of_mul + 1

    if(input[end_multiplier]=='-'):
        end_multiplier += 1


    while end_multiplier < len(input) and input[end_multiplier].isdigit():
        end_multiplier += 1
    # Calculate the multiplier
    multiplier = int(input[index_of_mul + 1:end_multiplier])

    result = multiplicand * multiplier

    # Recursively call the method, replacing the part that was calculated with the answer
    if(multiplier < 0 and result < 0):
        return multiply_string(input[:start_multiplicand]
                               + str(result) + input[end_multiplier:])
    else:
        return multiply_string(input[:start_multiplicand]
                           + str(abs(result)) + input[end_multiplier:])


def add_string(input):
    print(input)
    # using similar naming convention as the multiplication function
    index_of_add = input.find("+")

    # If no addition operations are found
    if index_of_add == -1:
        return input

    # Find the augend (number to which another is added)
    start_augend = index_of_add - 1
    while start_augend > 0 and input[start_augend-1].isdigit():
        start_augend -= 1

    # Calculate the start_augend
    augend = int(input[start_augend:index_of_add])

    if((found_negative(input[:index_of_add], augend))==1 ):
        augend = -augend
        #input = input.replace(str(input[start_augend-1]),'')
        #index_of_add -= 1

    # Find the end of the addend
    end_addend = index_of_add + 1
    if (input[end_addend]=='-'):
        end_addend += 1

    while end_addend < len(input) and input[end_addend].isdigit():
        end_addend += 1

    # Calculate the addend
    addend = int(input[index_of_add + 1:end_addend])
    print(addend)

    if(augend < 0 and augend + addend > 0):
        print("hereproblem?")
        input = input.replace(str(input[start_augend-1]),'')
        print(input)
        start_augend -= 1


    # Recursively call the method, replacing the calculated part with the answer
    if(addend < 0 and augend + addend < 0) :
        return add_string(input[:start_augend] + str((augend + addend))
                          + input[end_addend:])
    else:
        return add_string(input[:start_augend] + str(abs(augend + addend))
                      + input[end_addend:])

def subtract_string(input):
    print(input)
    index_of_sub = input.find("-")

    # If no subtraction operations are found
    if index_of_sub == -1:
        return input

    # Find the start of the minuend
    start_minuend = index_of_sub - 1
    while start_minuend > 0 and input[start_minuend-1].isdigit():
        start_minuend -= 1

    # Calculate the start_minuend
    if(input[start_minuend:index_of_sub]=='' or input[start_minuend:index_of_sub]=='g'):
        input = input.replace('-',"neg",1)
        return subtract_string(input)
    else:
        minuend = int(input[start_minuend:index_of_sub])

    negminuend = "neg" + str(minuend)
    if (input.find(negminuend)!=-1):
        print("foundneg")
        minuend = -minuend

    end_subtrahend = index_of_sub + 1

    if(input[end_subtrahend]=='-'):
        end_subtrahend += 1
    while end_subtrahend < len(input) and input[end_subtrahend].isdigit():
        end_subtrahend += 1

    # Calculate the end_subtrahend
    subtrahend = int(input[index_of_sub + 1:end_subtrahend])
    print(subtrahend)

    # Recursively call the method, replacing the calculaed part with the answer
    if (minuend - subtrahend < 0):
        return subtract_string(input[:start_minuend] + str("neg" + str(abs(minuend - subtrahend)))
                            + input[end_subtrahend:])
    else:
        print("else")
        if (input[start_minuend-1]=='g' and minuend - subtrahend > 0):
            input = input.replace("neg",'')
        return subtract_string(input[:start_minuend] + str(abs(minuend - subtrahend))
                            + input[end_subtrahend:])

def found_negative(input, number):
    if(input.find('-'+str(number))!=-1):
        return 1
    else:
        return -1
