from random import random

class Neuron(object):

    def __init__(self, charge_req, name, directions=None, role="a"):
        self.name = name
        self.charge = 0 #charge is aditive, if the current charge is ever greater than the charge_req then it will stimulate
        self.importance = 1 #importance is additive, each importance puts another entry of the same neuron into the weighted network
        self.charge_req = charge_req #charge required to stimulate
        self.role = role #role determines whether neuron is:
        """input (i, isnt a direction, has directions, never loses charge, stimulates upon input such as keyboard input)
        associative (a, is a direction, has directions, loses charge, stimulates upon recieving enough charge)
        or
        output(o, is a direction, has no directions, loses charge, outputs upon recieving enough charge, output includes print output)"""
        if directions == NeuralList or role != "o":
            self.directions = directions
        else:
            print(TypeError("The directions must be a NeuralList type!"))

    def __str__(self):
        return self.name

    def stimulate(self):
        charge_dist = self.charge / self.directions.length
        for direction in self.directions.list:
            direction.charge += charge_dist
            if direction.directions.length != 0 and direction.charge > direction.charge_req:
                direction.stimulate()
        self.charge = 0

    def introduce(self, neuron):
        self.directions.introduce(neuron)

    def reduce(self, neuron):
        self.directions.reduce(neuron)

class NeuralList():

    def __init__(self):
        self.list = []
        self.length = 0

    def introduce(self, neuron):
        if type(neuron) == Neuron:
            self.list.append(neuron)
            self.length += 1
        else:
            print(TypeError("The new neuron must be a Neuron object!"))

    def reduce(self, neuron):
        new_l = []
        for direction in self.list:
            if direction != neuron:
                new_l.append(direction)
        self.list = new_l
        self.length -= 1

class NeuralNetwork():

    def __init__(self, height=1, length=1):
        self.network = []
        self.length = length
        self.height = height
        for column_inc in range(length):
            self.network.append([])
            for row_inc in range(height):
                current_neuron = Neuron(1, str(column_inc)+str(row_inc), NeuralList())
                self.network[column_inc].append(current_neuron)
                if len(self.network) >= 2:
                    self.network[column_inc-1][row_inc].introduce(current_neuron)

    def showValues(self, value):
        picture = ""
        for column in self.network:
            picture += "\n"
            for neuron in column:
                if value == "length":
                    picture += str(neuron.directions.length)
                elif value == "charge":
                    picture += str(neuron.charge)
        print(picture)

    def totallyStimulate(self):
        for neuron in self.network[0]:
            neuron.stimulate()
        for neuron in self.network[-1]:
            print(neuron.charge)
    
    def mutate(self):
        weightedNetwork = []
        maxHeight = 0
        currentLength = 0
        for column in self.network:
            weightedNetwork.append([])
            currentHeight = 0
            for neuron in column:
                for occ in range(neuron.importance):
                    weightedNetwork[currentLength].append(neuron)
                    currentHeight += 1
            if currentHeight > maxHeight:
                maxHeight = currentHeight
            currentLength += 1
        choice1, choice3 = int(self.length*random()), int(4*random())
        choice2 = int(len(self.network[choice1])*random())
        return(weightedNetwork[choice1][choice2])

def countOccurences(net):
    occNet = []
    for column in range(net.length):
        occNet.append([])
        for neuron in range(net.height):
            occNet[column].append(0)
    for mutation in range(100000):
        place = str(net.mutate())
        occNet[int(place[0])][int(place[1])] += 1
    print(occNet)
    picture = ""
    for column in occNet:
        picture += "\n"
        for neuron in column:
            picture += str(neuron)+' '
    print(picture)

        
