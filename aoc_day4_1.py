
def isValidPassword(index):

    index = str(index)

    consecutive_check = False
    decreasing_check = True
    valid_password = False
    last_value = 0
    counter = 0
    counterlist =[]

    for j in range(5):

        print(index[j],index[j+1])

        if index[j] == index[j+1]:
            counter = counter + 1
        else:
            counterlist.append(counter)
            counter = 0

        if index[j] > index[j+1]:
            decreasing_check = False

    if counter > 0:
        counterlist.append(counter)

    for k in range(len(counterlist)):
        if counterlist[k] == 1:
            consecutive_check = True

    if consecutive_check and decreasing_check:
        valid_password = True

    #print(counterlist)

    return valid_password

if __name__ =="__main__":

    #read the numbers in
    readfile = open('aoc_day4_1.txt')

    fileinput = []

    #read each line of the text file
    for line in readfile:
        fileinput.append(line)

    fileinput[0] = fileinput[0].strip()

    #input string is 193651-649729
    inputstring = fileinput[0].split('-')
    minimum, maximum = int(inputstring[0]), int(inputstring[1])

    #minimum = 111111
    #maximum = 111199

    passwords = []

    for i in range(minimum, maximum):

        validpass = isValidPassword(i)

        if validpass:
            passwords.append(i)

    print(passwords)
    print(len(passwords))

    #print(isValidPassword(112233))
    #print(isValidPassword(123444))
    #print(isValidPassword(111122))





#comment
