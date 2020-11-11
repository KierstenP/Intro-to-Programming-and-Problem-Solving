def run_length_string_encoder(string):
    lst = []
    counter = 1
    string += " "

    for i in range(len(string)-1):
        currentVariable = string[i]
        nextVariable = string[i+1]

        if currentVariable == nextVariable:
            counter += 1
        else:
            lst.append([currentVariable, counter])
            counter = 1

    return lst

def run_length_string_decoder(lst):
    string = ""
    for i in lst:
        string += i[0]*i[1]

    return string