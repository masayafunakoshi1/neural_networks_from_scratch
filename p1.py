
def first_layer_neuron():
    #This is the base calculation of any neuron, first layer or middle layers
    inputs = [1, 2, 3] #from an input layer
    # e.g. if it was a sensor for CPU temps, these would be each of the sensor outputs OR it could be from another neuron

    #every input has a weight, every neuron only has 1 bias
    weights = [3.1, 2.1, 8.7] 
    bias = 3 #every unique neuron has a unique bias

    output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
    return "First Layer Neuron: {}".format(output)

def inner_neuron():
    inputs = [1, 2, 3, 2.5]
    weights = [0.2, 0.8, -0.5, 1.0]
    bias = 2.0

    output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + inputs[3] * weights[3] + bias
    return "Inner Neuron: {}".format(output)

def three_neurons():
    inputs = [1, 2, 3, 2.5] #output from a previous layer
    #inputs can't really change, since they're most likely from the previous layer
    #so the way to tweak/shift the direction of the output is by adjusting the weights and biases
    weights1 = [0.2, 0.8, -0.5, 1.0]
    weights2 = [0.5, -0.91, 0.26, -0.5]
    weights3 = [-0.26, -0.27, 0.17, 0.87]
    bias1 = 2.0
    bias2 = 3.0
    bias3 = 0.5
    
    output = [
        inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1, 
        inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2, 
        inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3
        ]
    return output

if __name__ == '__main__':
    print(first_layer_neuron())
    print(inner_neuron())
    print(three_neurons())