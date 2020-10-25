def convert(input):
    arabic = 0
    numerals = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}   # Dictionary of numeral values
    input = list(input)
    for i in range(len(input)):     # Checks the values from the input and finds the numeral equivalent
        if (i+1) == len(input) or numerals[input[i]] >= numerals[input[i+1]]:
            arabic += numerals[input[i]]
        else:
            arabic -= numerals[input[i]]        #If the numeral is followed by a larger one, it must be a negative

    return arabic
