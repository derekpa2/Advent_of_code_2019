
class LineObject:

    def __init__(self,initial_x,initial_y,line):

        #intialize the LineObject
        #initial_x, initial_y are the initial x and y coordinates
        #line is the string, e.g. 'R1002'. direction is Up (U), Right (R), Down (D), or Left (L)
        #distance is the magnitude of the line
        #final_x, final_y are the final x and y coordinates
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.line = line

        self.direction = self.line[0]
        self.distance = int(self.line[1:len(self.line)])

        final_x = self.initial_x
        final_y = self.initial_y

        if self.direction == 'U':
            final_y = final_y + self.distance
        elif self.direction == 'R':
            final_x = final_x + self.distance
        elif self.direction == 'D':
            final_y = final_y - self.distance
        elif self.direction == 'L':
            final_x = final_x - self.distance
        else:
            print("no valid direction!")

        self.final_x = final_x
        self.final_y = final_y

    def calculateDistance(self):

        return [self.final_x,self.final_y]


def calculateIntersection(line1,line2):

    #line1 and line2 are line objects

    line1xmin = min(line1.initial_x,line1.final_x)
    line1xmax = max(line1.initial_x,line1.final_x)
    line1ymin = min(line1.initial_y,line1.final_y)
    line1ymax = max(line1.initial_y,line1.final_y)

    line2xmin = min(line2.initial_x,line2.final_x)
    line2xmax = max(line2.initial_x,line2.final_x)
    line2ymin = min(line2.initial_y,line2.final_y)
    line2ymax = max(line2.initial_y,line2.final_y)

    x_coordinate = 0
    y_coordinate = 0

    #print('[line1.initial_x,line1.initial_y],[line1.final_x,line1.final_y]')
    #print([line1.initial_x,line1.initial_y],[line1.final_x,line1.final_y])
    #print('[line1xmin,line1xmax],[line1ymin,line1ymax]')
    #print([line1xmin,line1xmax,line1ymin,line1ymax])
    #print('[line2.initial_x,line2.initial_y],[line2.final_x,line2.final_y]')
    #print([line2.initial_x,line2.initial_y],[line2.final_x,line2.final_y])
    #print('[line2xmin,line2xmax],[line2ymin,line2ymax]')
    #print([line2xmin,line2xmax,line2ymin,line2ymax])


    if (
            (line2.final_x < line1xmax and line2.final_x > line1xmin) and
            (line1.final_y < line2ymax and line1.final_y > line2ymin)
        ):
        x_coordinate = line2.final_x
        y_coordinate = line1.final_y
        #else:
            #   print('lines do not intersect')
    elif (
            (line2.final_y < line1ymax and line2.final_y > line1ymin) and
            (line1.final_x < line2xmax and line1.final_x > line2xmin)
        ):
        x_coordinate = line1.final_x
        y_coordinate = line2.final_y
        #else:
            #print('lines do not intersect')
    #else:
        #print('Lines are parallel!')

    return [x_coordinate,y_coordinate]


if __name__ =="__main__":

    #read the numbers in
    readfile = open('aoc_day3_1.txt')

    fileinput = []

    #read each line of the text file
    for line in readfile:
        fileinput.append(line)

    #splits the string up and makes it into a list of integers
    #map(x,y) assigns the list y to a type x, and returns a list object
    #list(map(x,y)) converts that list object to a list
    line1 = list(fileinput[0].split(','))
    line2 = list(fileinput[1].split(','))

    line1[len(line1)-1] = line1[len(line1)-1].strip()
    line2[len(line2)-1] = line2[len(line2)-1].strip()

    #line1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
    #line2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

    #line1 = ['R8','U5','L5','D3']
    #line2 = ['U7','R6','D4','L4']

    line1objectlist = []
    initial_x = 0
    initial_y = 0

    #creating object arrays
    for i in range(len(line1)):
        line1objectlist.append(LineObject(initial_x,initial_y,line1[i]))
        initial_x = line1objectlist[i].final_x
        initial_y = line1objectlist[i].final_y
        #print(line1[i])
        #print(line1objectlist[i].direction,line1objectlist[i].distance)
        #print(line1objectlist[i].initial_x,line1objectlist[i].initial_y,line1objectlist[i].final_x,line1objectlist[i].final_y)


    line2objectlist = []
    initial_x = 0
    initial_y = 0

    for j in range(len(line2)):
        line2objectlist.append(LineObject(initial_x,initial_y,line2[j]))
        initial_x = line2objectlist[j].final_x
        initial_y = line2objectlist[j].final_y
        #print(line2[j])
        #print(line2objectlist[j].direction,line2objectlist[j].distance)
        #print(line2objectlist[j].initial_x,line2objectlist[j].initial_y,line2objectlist[j].final_x,line2objectlist[j].final_y)

    arrayintersection = []
    m = 0

    #this loop will calculate all intersections
    for k in range(len(line1)):
        for l in range(len(line2)):
            m = m + 1
            #print(m)
            returnvalue = calculateIntersection(line1objectlist[k],line2objectlist[l])
            #print(line1objectlist[k].line,line2objectlist[l].line)
            if returnvalue[0] != 0 or returnvalue[1] != 0:
                #print("intersection!")
                #print(returnvalue)
                arrayintersection.append([returnvalue[0],returnvalue[1],line1objectlist[k].line,line2objectlist[l].line])

    print(arrayintersection)
    print(line1)
    print(line2)

    total_distance = []

    #this loop will calculate the total distance to each intersection.
    for n in range(len(arrayintersection)):

        indexline1 = line1.index(arrayintersection[n][2])
        indexline2 = line2.index(arrayintersection[n][3])

        o = 0
        line1_total_distance = 0

        while o < indexline1:

            line1_total_distance = line1_total_distance + line1objectlist[o].distance
            o = o + 1

        line1_total_distance = line1_total_distance + \
            abs(arrayintersection[n][0] - line1objectlist[indexline1].initial_x) + \
            abs(arrayintersection[n][1] - line1objectlist[indexline1].initial_y)

        print('line 1 total distance is', line1_total_distance)

        p = 0
        line2_total_distance = 0

        while p < indexline2:

            line2_total_distance = line2_total_distance + line2objectlist[p].distance
            p = p + 1

        line2_total_distance = line2_total_distance + \
            abs(arrayintersection[n][0] - line2objectlist[indexline2].initial_x) + \
            abs(arrayintersection[n][1] - line2objectlist[indexline2].initial_y)

        print('line 2 total distance is', line2_total_distance)

        total_distance.append(line1_total_distance + line2_total_distance)

    print(total_distance)

    print('Minimum total distance is', min(total_distance))













#comment
