class Intcode:

    #begin Intcode function.
    #
    #This function takes a cmdinput list,... TODO: describe this more
    #
    #

    def __init__(self,cmdinput,inputs=[],name='',debug=False):

        self.commandline = cmdinput.copy()
        self.commandline_copy = cmdinput.copy()
        self.commandline_length = len(cmdinput)
        self.outputs = []
        self.indexpointer = 0
        self.index = 0
        self.current_opcode = '00'
        self.current_num_params = 0
        self.parameter_modes = []
        self.halt = False
        self.name = name
        self.relative_base = 0
        self.debug = debug
        self.setInputs(inputs)

    def setInputs(self,inputs):

        if isinstance(inputs,int):
            self.inputs = [inputs]
        elif isinstance(inputs,list):
            self.inputs = inputs.copy()
        else:
            print('Failed to set input. Intput can only be <int> or <list>')

    def setDebug(self,boolean):

        self.debug = boolean

    def getCommand(self):
        #this is going to return the opcode as the first element, then
        #the parameter modes.

        self.parameter_modes = []

        command = str(self.commandline[self.index])

        if len(command) == 1:
            self.current_opcode = '0' + command
        else:
            self.current_opcode = command[len(command)-2:len(command)]

        self.getNumParams()

        if len(command) > 2:
            for i in range(2,len(command)):
                self.parameter_modes.append(int(command[len(command)-1-i]))

        while len(self.parameter_modes) < self.current_num_params:
            self.parameter_modes.append(0)

    def getNumParams(self):

        self.current_num_params = 0

        if self.current_opcode == '01':
            self.current_num_params = 3
        elif self.current_opcode == '02':
            self.current_num_params = 3
        elif self.current_opcode == '03':
            self.current_num_params = 1
        elif self.current_opcode == '04':
            self.current_num_params = 1
        elif self.current_opcode == '05':
            self.current_num_params = 2
        elif self.current_opcode == '06':
            self.current_num_params = 2
        elif self.current_opcode == '07':
            self.current_num_params = 3
        elif self.current_opcode == '08':
            self.current_num_params = 3
        elif self.current_opcode == '09':
            self.current_num_params = 1
        elif self.current_opcode == '99':
            self.current_num_params = 0
        else:
            print('invalid opcode!')

################################################################################
#
# Parameter modes
#
#  Mode 0: position mode, which causes the parameter to be interpreted as a
#    position
#  Mode 1: immediate mode, parameter is interpreted as a value
#  Mode 2: relative mode,
#
################################################################################

    def getParameter(self,index,mode):

        offset = self.commandline[index]

        if mode == 0:
            if offset >= self.commandline_length:
                self.extendCommandLine(offset)
            value = self.commandline[offset]
            returnindex = offset
        elif mode == 1:
            value = offset
            returnindex = index
        elif mode == 2:
            relative_index = self.relative_base + offset
            if relative_index >= self.commandline_length:
                self.extendCommandLine(relative_index)
            value = self.commandline[relative_index]
            returnindex = relative_index
        else:
            value = 0
            returnindex = index
            print('Invalid mode!')

        return value,returnindex

    def setParameter(self,index,mode,value):

        offset = self.commandline[index]

        if mode == 0:
            if offset >= self.commandline_length:
                self.extendCommandLine(offset)
            self.commandline[offset] = value
            returnindex = offset
        elif mode == 2:
            relative_index = self.relative_base + offset
            if relative_index >= self.commandline_length:
                self.extendCommandLine(relative_index)
            self.commandline[relative_index] = value
            returnindex = relative_index
        else:
            returnindex = index
            print('Invalid mode!')

        return returnindex


    def extendCommandLine(self,index):

        difference = index - (self.commandline_length - 1)

        self.commandline.extend([0]*difference)

        self.commandline_length = len(self.commandline)

################################################################################
#
# ADD
#
#  Adds together numbers read from two positions and stores the result
#  in a third position
#
################################################################################

    def add(self,index):

        firstnumber,firstindex = self.getParameter(index + 1, self.parameter_modes[0])
        secondnumber,secondindex = self.getParameter(index + 2, self.parameter_modes[1])
        thirdnumber = firstnumber + secondnumber

        thirdindex = self.setParameter(index + 3,self.parameter_modes[2],thirdnumber)

        if self.debug:
            print('Add: ',end='')
            print('[' + str(firstindex) + '] ' + str(firstnumber),end=' + ')
            print('[' + str(secondindex) + '] ' + str(secondnumber),end=' = ')
            print('[' + str(thirdindex) + '] ' + str(thirdnumber))

        return index + self.current_num_params + 1

################################################################################
#
# MULTIPLY
#
#  Multiplies together numbers read from two positions and stores the result
#  in a third position
#
################################################################################

    def multiply(self,index):

        firstnumber,firstindex = self.getParameter(index + 1, self.parameter_modes[0])
        secondnumber,secondindex = self.getParameter(index + 2, self.parameter_modes[1])
        thirdnumber = firstnumber * secondnumber

        thirdindex = self.setParameter(index + 3,self.parameter_modes[2],thirdnumber)

        if self.debug:
            print('Multiply: ',end='')
            print('[' + str(firstindex) + '] ' + str(firstnumber),end=' * ')
            print('[' + str(secondindex) + '] ' + str(secondnumber),end=' = ')
            print('[' + str(thirdindex) + '] ' + str(thirdnumber))

        return index + self.current_num_params + 1

################################################################################
#
# INPUT
#
#  Takes a single integer as input and saves it to the position given
#  by its only parameter.
#
#  If there are no inuputs, the program halts.
#
################################################################################

    def saveInput(self,index):

        #print(len(self.inputs))

        if len(self.inputs) > 0:
            inputindex = self.setParameter(index + 1,self.parameter_modes[0],self.inputs[0])
            if self.debug:
                print('Input: ',end='')
                print('[' + str(inputindex) + '] ' + str(self.inputs[0]))
            self.inputs.pop(0)
            return index + self.current_num_params + 1
        else:
            print('Input: need more inputs. Program is exiting...')
            self.indexpointer = index
            self.halt = True
            #print('Need more inputs!')
            return index

################################################################################
#
# OUTPUT
#
#  Outputs the value of its only parameter
#
################################################################################

    def outputParam(self,index):

        output,outputindex = self.getParameter(index + 1, self.parameter_modes[0])

        self.outputs.append(output)

        if self.debug:
            print('Output: ',end='')
            print('[' + str(outputindex) + '] ' + str(output))

        return index + self.current_num_params + 1

################################################################################
#
# JUMP IF TRUE
#
#  If the first parameter is non-zero, it sets the instruction pointer to
#  the value from the second parameter. Otherwise, it does nothing.
#
################################################################################

    def jumpIfTrue(self,index):

        firstnumber,firstindex = self.getParameter(index + 1, self.parameter_modes[0])
        secondnumber,secondindex = self.getParameter(index + 2, self.parameter_modes[1])

        if self.debug:
            print('Jump if True: ',end='')
            print('[' + str(firstindex) + '] ' + str(firstnumber),end=' != 0 ')

        if firstnumber != 0:
            print('True! Jumping to [' + str(secondindex) + '] ' + str(secondnumber))
            return secondnumber
        else:
            print('False!')
            return index + self.current_num_params + 1

################################################################################
#
# JUMP IF FALSE
#
#  If the first parameter is zero, it sets the instruction pointer to
#  the value from the second parameter. Otherwise, it does nothing.
#
################################################################################

    def jumpIfFalse(self,index):

        firstnumber,firstindex = self.getParameter(index + 1, self.parameter_modes[0])
        secondnumber,secondindex = self.getParameter(index + 2, self.parameter_modes[1])

        if self.debug:
            print('Jump if False: ',end='')
            print('[' + str(firstindex) + '] ' + str(firstnumber),end=' != 0 ')

        if firstnumber == 0:
            if self.debug:
                print('False! Jumping to...[' + str(secondindex) + '] ' + str(secondnumber))
            return secondnumber
        else:
            if self.debug:
                print('True!')
            return index + self.current_num_params + 1

################################################################################
#
# LESS THAN
#
#  If the first parameter is less than the second parameter, it stores 1
#  in the position given by the third parameter. Otherwise, it stores 0.
#
################################################################################

    def lessThan(self,index):

        firstnumber,firstindex = self.getParameter(index + 1, self.parameter_modes[0])
        secondnumber,secondindex = self.getParameter(index + 2, self.parameter_modes[1])

        if firstnumber < secondnumber:
            value = 1
        else:
            value = 0

        thirdindex = self.setParameter(index + 3,self.parameter_modes[2],value)

        if self.debug:
            print('Less than: ',end='')
            print('[' + str(firstindex) + '] ' + str(firstnumber),end=' < ')
            print('[' + str(secondindex) + '] ' + str(secondnumber),end=' , ')
            print('Store ' + str(value) + ' at [' + str(thirdindex),end=']\n')

        return index + self.current_num_params + 1

################################################################################
#
# EQUALS
#
#  If the first parameter is equal to the second parameter, it stores 1
#  in the position given by the third parameter. Otherwise, it stores 0
#
################################################################################

    def equals(self,index):

        firstnumber,firstindex = self.getParameter(index + 1, self.parameter_modes[0])
        secondnumber,secondindex = self.getParameter(index + 2, self.parameter_modes[1])

        if firstnumber == secondnumber:
            value = 1
        else:
            value = 0

        thirdindex = self.setParameter(index + 3,self.parameter_modes[2],value)

        if self.debug:
            print('Equals: ',end='')
            print('[' + str(firstindex) + '] ' + str(firstnumber),end=' == ')
            print('[' + str(secondindex) + '] ' + str(secondnumber),end=' , ')
            print('Store ' + str(value) + ' at [' + str(thirdindex),end=']\n')

        return index + self.current_num_params + 1

#################################################################
#
# SET RELATIVE BASE
#
#################################################################

    def setRelativeBase(self,index):

        number,numberindex = self.getParameter(index+1,self.parameter_modes[0])

        self.relative_base += number

        if self.debug:
            print('Set Relative Base: ',end='')
            print('[' + str(numberindex) + '] ' + str(numberindex))

        return index + self.current_num_params + 1

#################################################################
#
# RUN INTCODE
#
#################################################################

    def run(self):
        self.index = self.indexpointer
        self.halt = False

        if self.debug:
            printstring = "#"*50
            print('\n' + printstring)
            print('Begin Intcode' + '\n')

        while self.index < self.commandline_length:

            self.getCommand()

            if self.current_opcode == '01':
                iterator = self.add(self.index)
            elif self.current_opcode == '02':
                iterator = self.multiply(self.index)
            elif self.current_opcode == '03':
                iterator = self.saveInput(self.index)
            elif self.current_opcode == '04':
                iterator = self.outputParam(self.index)
            elif self.current_opcode == '05':
                iterator = self.jumpIfTrue(self.index)
            elif self.current_opcode == '06':
                iterator = self.jumpIfFalse(self.index)
            elif self.current_opcode == '07':
                iterator = self.lessThan(self.index)
            elif self.current_opcode == '08':
                iterator = self.equals(self.index)
            elif self.current_opcode == '09':
                iterator = self.setRelativeBase(self.index)
            elif self.current_opcode == '99':
                iterator = self.commandline_length

                if self.debug:
                    if self.name != '':
                        print('\n'+ 'End of Intcode for ' + self.name + '!')
                    else:
                        print('\n' + 'End of Intcode!')

                    printstring = "#"*50
                    print(printstring + '\n')

                return 99
            else:
                print('Not a valid opcode!!')
                iterator = self.commandline_length

            self.index = iterator

            if self.halt:
                return 0

        return 0
