class Intcode:

    #begin Intcode function.
    #
    #This function takes a cmdinput string, replaces index 1 with noun,
    #replaces index 2 with verb, and returns the output at 0
    #
    #

    def __init__(self,cmdinput,inputs=[],name=''):

        self.commandline = cmdinput.copy()
        self.commandline_copy = cmdinput.copy()
        self.inputs = inputs.copy()
        self.commandline_length = len(cmdinput)
        self.outputs = []
        self.indexpointer = 0
        self.halt = False
        self.name = name

    def setInputs(self,inputs):
        #TODO: make this parse integers as well.
        self.inputs = inputs.copy()

    def getCommand(self,index):
        #this is going to return the opcode as the first element, then
        #the parameter modes.

        parameter_modes = []

        command = str(self.commandline[index])

        if len(command) == 1:
            opcode = '0' + command
        else:
            opcode = command[len(command)-2:len(command)]

        num_params = self.getNumParams(opcode)

        if len(command) > 2:
            for i in range(2,len(command)):
                parameter_modes.append(int(command[len(command)-1-i]))

        while len(parameter_modes) < num_params:
            parameter_modes.append(0)

        return opcode,parameter_modes

    def getNumParams(self,opcode):

        num_params = 0

        if opcode == '01':
            num_params = 3
        elif opcode == '02':
            num_params = 3
        elif opcode == '03':
            num_params = 1
        elif opcode == '04':
            num_params = 1
        elif opcode == '05':
            num_params = 2
        elif opcode == '06':
            num_params = 2
        elif opcode == '07':
            num_params = 3
        elif opcode == '08':
            num_params = 3

        return num_params

    def getParameter(self,index,mode):

        if mode == 0:
            value = self.commandline[self.commandline[index]]
        else:
            value = self.commandline[index]

        return value

    def add(self,index,opcode,parameter_modes):

        num_params = self.getNumParams(opcode)

        firstnumber = self.getParameter(index + 1, parameter_modes[0])
        secondnumber = self.getParameter(index + 2, parameter_modes[1])
        thirdnumber = firstnumber + secondnumber

        self.commandline[self.commandline[index + 3]] = thirdnumber

        return index + num_params + 1

    def multiply(self,index,opcode,parameter_modes):
        num_params = self.getNumParams(opcode)

        firstnumber = self.getParameter(index + 1, parameter_modes[0])
        secondnumber = self.getParameter(index + 2, parameter_modes[1])
        thirdnumber = firstnumber * secondnumber

        self.commandline[self.commandline[index + 3]] = thirdnumber

        return index + num_params + 1

    def saveInput(self,index,opcode,parameter_modes):
        num_params = self.getNumParams(opcode)

        #print(len(self.inputs))

        if len(self.inputs) > 0:
            self.commandline[self.commandline[index + 1]] = self.inputs[0]
            self.inputs.pop(0)
            #print('Have enough inputs.')
            return index + num_params + 1
        else:
            self.indexpointer = index
            self.halt = True
            #print('Need more inputs!')
            return index

    def outputParam(self,index,opcode,parameter_modes):
        num_params = self.getNumParams(opcode)

        self.outputs.append(self.getParameter(index + 1, parameter_modes[0]))

        #print('THE OUTPUT OF OPCODE = 4 is',self.outputs)

        return index + num_params + 1

    def jumpIfTrue(self,index,opcode,parameter_modes):
        num_params = self.getNumParams(opcode)

        firstnumber = self.getParameter(index + 1, parameter_modes[0])
        secondnumber = self.getParameter(index + 2, parameter_modes[1])

        if firstnumber != 0:
            return secondnumber
        else:
            return index + num_params + 1

    def jumpIfFalse(self,index,opcode,parameter_modes):
        num_params = self.getNumParams(opcode)

        firstnumber = self.getParameter(index + 1, parameter_modes[0])
        secondnumber = self.getParameter(index + 2, parameter_modes[1])

        if firstnumber == 0:
            return secondnumber
        else:
            return index + num_params + 1

    def lessThan(self,index,opcode,parameter_modes):
        num_params = self.getNumParams(opcode)

        firstnumber = self.getParameter(index + 1, parameter_modes[0])
        secondnumber = self.getParameter(index + 2, parameter_modes[1])

        if firstnumber < secondnumber:
            value = 1
        else:
            value = 0

        self.commandline[self.commandline[index + 3]] = value

        return index + num_params + 1

    def equals(self,index,opcode,parameter_modes):
        num_params = self.getNumParams(opcode)

        firstnumber = self.getParameter(index + 1, parameter_modes[0])
        secondnumber = self.getParameter(index + 2, parameter_modes[1])

        if firstnumber == secondnumber:
            value = 1
        else:
            value = 0

        self.commandline[self.commandline[index + 3]] = value

        return index + num_params + 1

    def run(self):
        index = self.indexpointer
        self.halt = False

        while index < self.commandline_length:

            opcode,parameter_modes = self.getCommand(index)

            #print(self.commandline[index],',',opcode,',',parameter_modes)

            if opcode == '01':
                iterator = self.add(index,opcode,parameter_modes)
            elif opcode == '02':
                iterator = self.multiply(index,opcode,parameter_modes)
            elif opcode == '03':
                iterator = self.saveInput(index,opcode,parameter_modes)
            elif opcode == '04':
                iterator = self.outputParam(index,opcode,parameter_modes)
            elif opcode == '05':
                iterator = self.jumpIfTrue(index,opcode,parameter_modes)
            elif opcode == '06':
                iterator = self.jumpIfFalse(index,opcode,parameter_modes)
            elif opcode == '07':
                iterator = self.lessThan(index,opcode,parameter_modes)
            elif opcode == '08':
                iterator = self.equals(index,opcode,parameter_modes)
            elif opcode == '99':
                iterator = self.commandline_length
                #print('End of Command for ' + self.name + '!')
                return 99
            else:
                print('Not a valid opcode!!')
                iterator = self.commandline_length

            index = iterator

            if self.halt:
                return 0

        return 0
