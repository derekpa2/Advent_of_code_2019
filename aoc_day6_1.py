
class Orbit:

    #this is the orbit class.
    #name is the name of the body.
    #length is the length from the center of mass (COM)
    #children is a list of all the orbiting bodies
    #totallength is the sum of all the chilren's lengths
    #
    #there is only one method, the addChild method. This appends a children
    #to the node. In effect it adds and object to orbit this body.

    def __init__(self,name,length=0):
        self.name = name
        self.length = length
        self.children = []
        self.totallength = 0

    def addChild(self,orbitObj):
        self.children.append(orbitObj)


def findOrbits(orbitlist,name):

    #this helper function takes a list of orbits and finds the matches where
    #the first element is equal do the name. It then returns the full orbits
    #(both elements) of each match

    #TODO: make this better. Use generators or something like that

    indicies = []
    orbits = []

    #first, find the indicies of all the matches
    for i in orbitlist:
        if i[0] == name:
            indicies.append(orbitlist.index(i))

    #pop the indicies off of the orbit list, needs to be done in reverse order
    #or else the wrong elements will be removed.
    for j in range(len(indicies)):
        child = orbitlist.pop(indicies[len(indicies) - j -1])
        orbits.append(child[1])

    return orbits


def buildTree(orbitlist,name,length):

    #create the orbit object. This is a node
    orbitObject = Orbit(name,length)

    #find the children by calling the findOrbits function
    children = findOrbits(orbitlist,name)

    #iterate over all the chilren that were found. This will create the child object,
    #then set those created objects as chilren to this object. Don't forget to
    #calculate the length!
    for i in children:
        childObject = buildTree(orbitlist,i,orbitObject.length + 1)
        orbitObject.addChild(childObject)
        orbitObject.totallength += childObject.totallength + childObject.length

    return orbitObject

def findOrbitTransfers(orbit,orbitone,orbittwo):

    #The matchstring is used to immediately return if a match is found.
    #This effectively returns the "first" match in which both chilren match
    #the orbitone and orbittwo string, and is a way to return the calculated
    #length to the calling function.
    matchstring = 'Found match!'
    boolone, booltwo = False, False

    #if the name matches the matchstring, we're done, return what was given.
    #if any of the names match orbitone, we've found one match.
    #store the length to be returned or used in the length calculation later
    #if any of the names match orbitone, we've found another match.
    #store the length to be returned or used in the length calculation later

    for index,i in enumerate(orbit.children):
        name, length = findOrbitTransfers(i,orbitone,orbittwo)
        if name == matchstring:
            return name, length
        elif name == orbitone:
            boolone = True
            lengthone = length
        elif name == orbittwo:
            booltwo = True
            lengthtwo = length

    #if orbitone and orbittwo are both found, we're done!
    #return the matchstring so the calling function will succeed.
    #return the calculated length. formula determined by inspection of the example
    #if orbitone is found, return the name and length to the calling function.
    #if orbittwo is found, return the name and length to the calling function.
    #if nothing is found (or there were no children), just return the name and length.

    if boolone and booltwo:
        return matchstring, (lengthone - orbit.length - 1) + (lengthtwo - orbit.length - 1)
    elif boolone:
        return orbitone, lengthone
    elif booltwo:
        return orbittwo, lengthtwo
    else:
        return orbit.name, orbit.length




if __name__ =="__main__":

    #read the numbers in
    #readfile = open('aoc_day6_1.txt')
    readfile = open('aoc_day6_1.txt')

    orbitlist = []

    #read each line of the text file
    for line in readfile:
        element = line.split(')')
        element[1] = element[1].strip()
        orbitlist.append(element)

    orbitlistcopy = orbitlist.copy()

    #day 1, builds the tree.
    orbitNode = buildTree(orbitlist,'COM',0)

    print(orbitNode.totallength)

    #day 2, calculates the least amount of orbit transfers
    resultname,resultlength = findOrbitTransfers(orbitNode,'YOU','SAN')

    print('Result is:',resultname,resultlength)



#comment
