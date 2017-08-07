class Neuron(object):

    def __init__(self, charge, name, directions=None, role="a"):
        self.name = name
        if directions == NeuralList or role != "output":
            self.directions = directions
        else:
            print(TypeError("The directions must be a NeuralList type!"))
        self.charge = charge

    def __str__(self):
        return self.name

    def stimulate(self):
        charge_dist = self.charge / self.directions.length
        for direction in self.directions.list:
            direction.charge += charge_dist
            if direction.directions.length != 0:
                direction.stimulate()
        self.charge = 0

    def introduce(self, neuron):
        self.directions.introduce(neuron)

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
        print(self.list)

class NeuralNetwork():

    def __init__(self, height=1, length=1):
        self.network = []
        for column_inc in range(length):
            self.network.append([])
            for row_inc in range(height):
                current_neuron = Neuron(1, str(column_inc)+str(row_inc), NeuralList())
                self.network[column_inc].append(current_neuron)
                if len(self.network) >= 2:
                    self.network[column_inc-1][row_inc].introduce(current_neuron)

    def showDirectionLengths(self):
        for column in self.network:
            for neuron in column:
                print(neuron.directions.length)

    def totallyStimulate(self):
        for neuron in self.network[0]:
            neuron.stimulate()
        for neuron in self.network[-1]:
            print(neuron.charge)
        
