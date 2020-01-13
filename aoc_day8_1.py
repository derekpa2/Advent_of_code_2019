
def countDigits(image,value):

    #count the number of times value shows up in the image list

    columns = len(image[0]) #shoud be 25

    digitcount = 0

    for i in image:
        for j in range(0,columns):
            if int(i[j]) == value:
                digitcount += 1

    return digitcount

def part1(pixels,row,column):

        image_rows = list(range(0,row))
        image_columns = list(range(0,column))

        index = 0
        layers = {}
        rows = []
        layercount = 0

        while index < len(pixels):

            for i in image_rows:
                rows.append(pixels[index:index+column])
                index += column

            layers[layercount] = rows

            rows = []
            layercount += 1

        mindigitcount = 0

        for k,j in enumerate(layers):
            digitcount = countDigits(layers[j],0)
            if digitcount < mindigitcount or k == 0:
                mindigitcount = digitcount
                layerkey = j

        onedigits = countDigits(layers[layerkey],1)
        twodigits = countDigits(layers[layerkey],2)

        return onedigits*twodigits, layers

def part2(pixels,layers,row,column):

    rowstring = ''
    image = []

    for i in range(row):
        for j in range(column):

            for k in range(len(layers)):
                value = layers[k][i][j]
                if value == '0' or value == '1':
                    pixelvalue = value
                    break
            #end layers
            rowstring += pixelvalue

        #end column
        image.append(rowstring)
        rowstring = ''
    #end row

    return image


if __name__ =="__main__":

    #read the numbers in
    #readfile = open('aoc_day7_test.txt')
    readfile = open('aoc_day8_1.txt')

    fileinput = []

    #read each line of the text file
    for line in readfile:
        fileinput.append(line)

    fileinput[0] = fileinput[0].strip()
    pixels = fileinput[0]
    #pixels = '0222112222120000'

    row = 6
    #row = 2
    column = 25
    #column = 2

    #part 1 solution
    solution1,layers = part1(pixels,row,column)
    print('Part 1 solution:\n\n' + str(solution1) + '\n\n')

    #part 2
    image = part2(pixels,layers,row,column)

    print('Part 2 solution:\n\n')

    for m in range(row):
        for n in range(column):
            value = image[m][n]
            if value == '1':
                print(value,end='')
            else:
                print(' ',end='')
        print()

    print('\n\n')





#comment
