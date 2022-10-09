# import regex module for checking valid input
import re


def main():
    while True:
        print("Please enter your equation (or type quit): ")
        inp = input()
        if inp == "quit":
            break
        elif inp == "":
            print ("Error - Please give a valid input")
        else:
            print(calculate(inp))

def calculate(input):
    answer = input_check(input)
    if(answer != input):
        return answer
    answer = answer.replace("--",'+')
    answer = multiply_string(answer)
    answer = add_string(answer)
    answer = subtract_string(answer)
    # replace special string "neg" with '-' once all operation have been calculated
    return int(answer)

def input_check(input):
    pattern = r'[^0-9+*-]'
    check = re.sub(pattern, '',input)
    check = check.replace("-+",'')
    check = check.replace("-*",'')

    # Return an invalid input error if any incorrect values are given
    if (len(input) > len(check)):
        return "Error - Invalid input given"
    # Check for any non-negative operators that repeat, e.g. "+++++", "***"
    repcheck1 = re.search(r'((\*)\2{1,})',check)
    repcheck2 = re.search(r'((\+)\2{1,})',check)
    # Special case of more that 2 '-', "--" = '+', "------" = Ignore
    repcheck3 = re.search(r'((\-)\2{2,})',check)
    # If the repetition checks contain anything, return an invalid error input
    if (repcheck1 != None or repcheck2 != None or repcheck3 != None):
        return "Error - Invalid input given"
    else:
        return input

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
    # If the first character of the string is '+' remove it
    elif index_of_add == 0:
        input = input.replace('+','',1)
        return add_string(input)

    # Find the augend (number to which another is added)
    start_augend = index_of_add - 1
    while start_augend > 0 and input[start_augend-1].isdigit():
        start_augend -= 1

    # Calculate the augend
    augend = int(input[start_augend:index_of_add])

    # Check if augend is a negative number
    if((found_negative(input[:index_of_add], augend))==1 ):
        augend = -augend

    # Find the end of the addend
    end_addend = index_of_add + 1
    if (input[end_addend]=='-'):
        end_addend += 1

    # Find end of the addend
    while end_addend < len(input) and input[end_addend].isdigit():
        end_addend += 1

    # Calculate the addend
    addend = int(input[index_of_add + 1:end_addend])

    # Conditional replacements for a negative augend but positive addition result
    if(augend < 0 and augend + addend > 0):
        if(start_augend != 1):
            input = input.replace(str(input[start_augend-1]),'+',1)
        else:
            input = input.replace(str(input[start_augend-1]),'',1)
            start_augend -= 1

    # Decrement the end_addend index if there are no more values following
    # in the string and end_addend is not the end of the string
    if (operator_left(input[end_addend:])==-1 and end_addend < len(input)):
        end_addend -= 1


    # Recursively call the method, replacing the calculated part with the result
    # Return here if the result is negative due to a negative addend
    if(addend < 0 and augend + addend < 0) :
        return add_string(input[:start_augend] + str((augend + addend))
                          + input[end_addend:])
    # Otherwise return the absolute value of the result
    else:
        return add_string(input[:start_augend] + str(abs(augend + addend))
                            + input[end_addend:])

def subtract_string(input):
    # Find the index of the '-' operator in the string
    index_of_sub = input.find("-")

    # If no subtraction operations are found
    if index_of_sub == -1:
        input = input.replace("neg", "-")
        input = input.replace('-','', input.count('-')-1)
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

    # Check if the the minuend is a negative number
    negminuend = "neg" + str(minuend)
    if (input.find(negminuend)!=-1):
        minuend = -minuend

    end_subtrahend = index_of_sub + 1

    # Find the end of the subtrahend, number to be subtracted from the minuend
    if(input[end_subtrahend]=='-'):
        end_subtrahend += 1
    while end_subtrahend < len(input) and input[end_subtrahend].isdigit():
        end_subtrahend += 1

    # Calculate the end_subtrahend
    subtrahend = int(input[index_of_sub + 1:end_subtrahend])

    # Recursively call the method, replacing the '-' operator with a placeholder
    # if the result is negative to avoid infinite recursive checks
    if (minuend - subtrahend < 0):
        return subtract_string(input[:start_minuend] + str("neg" + str(abs(minuend - subtrahend)))
                            + input[end_subtrahend:])
    # Otherwise, recursively call the result, replacing the placeholder "neg"
    # if the result would not be negative and there is a negative placeholder
    # in front
    else:
        if (input[start_minuend-1]=='g' and minuend - subtrahend > 0):
            input = input.replace("neg",'')
        return subtract_string(input[:start_minuend] + str(abs(minuend - subtrahend))
                            + input[end_subtrahend:])

def operator_left(input):
    if(input.find('*')!=-1 or input.find('-')!= -1 or input.find('+')!=-1):
        return 1
    else:
        return -1

def found_negative(input, number):
    if(input.find('-'+str(number))!=-1):
        return 1
    else:
        return -1

if __name__ == '__main__':
    main()
