import numpy as np

class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)

        self.weights = 2 * np.random.random((3,1)) - 1

    def sigmioid(self,x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self,x):
        return x * (1 - x)
    
    def train(self, training_inputs, training_outputs, training_iterations):

        for iteration in range(training_iterations):

            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.weights = adjustments

    def think(self, inputs):
        bias = 1
        inputs = inputs.astype(float)
        output = self.sigmioid(np.dot(inputs, self.weights) + bias) 
        
        return output

if __name__ == "__main__":

    neural_network = NeuralNetwork()

    print("Random Starting synaptic weights: ")
    print(neural_network.weights)

    training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

    training_outputs = np.array([[0,1,1,0]]).T

    neural_network.train(training_inputs, training_outputs, 10000)

    print("Synaptic weights after training")
    print(neural_network.weights)

    A = str(input("input 1: "))
    B = str(input("input 2: "))
    C = str(input("input 3: "))

    print("New situation: input data =", A, B, C)
    print('Output data: ')
    print(neural_network.think(np.array([A,B,C])))