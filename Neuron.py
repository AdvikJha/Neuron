inputs = [1, 2, 3, 4, 5]
correctOutputs = [3, 5, 7, 9, 11]

weight = 0
bias = 0

learningRate = 0.01
iterationCount = 0

def neuron(x, w, b):
    return w*x + b


def calculateLoss(weight, bias, inputs, correctOutputs):
    sumOfErrorSquareds = 0.0

    for x in inputs:
        prediction = neuron(x, weight, bias)

        error = prediction - correctOutputs[x-1]
        errorSquared = error ** 2

        sumOfErrorSquareds = sumOfErrorSquareds + errorSquared

    lossMSE = sumOfErrorSquareds / len(inputs)
    return lossMSE

print("Loss MSE: " + str(calculateLoss(weight, bias, inputs, correctOutputs)))

def calculateGradients(weight, bias, inputs, correctOutputs):
    gradientWeight = 0.0
    gradientBias = 0.0

    for x in inputs:
        prediction = neuron(x, weight, bias)
        error = prediction - correctOutputs[x-1]
        gradientBias = gradientBias + 2*error
        gradientWeight = gradientWeight + 2*x*error
    gradientWeight = gradientWeight/ len(inputs)
    gradientBias = gradientBias/ len(inputs)
    return gradientWeight, gradientBias

print("Gradient Weight and Bias: " + str(calculateGradients(weight, bias, inputs, correctOutputs)))

LossMSE = calculateLoss(weight, bias, inputs, correctOutputs)

while LossMSE >= 0.00000001:
    iterationCount = iterationCount + 1

    gradientWeight, gradientBias = calculateGradients(weight, bias, inputs, correctOutputs)

    weight = weight - gradientWeight * learningRate
    bias = bias - gradientBias * learningRate

    LossMSE = calculateLoss(weight, bias, inputs, correctOutputs)

    print("\nIteration #", iterationCount)
    print("Weight: ", weight)
    print("Bias: ", bias)
    print("Loss", LossMSE)

weight = round(weight, 3)
bias = round(bias, 3)

#Final Report

print("\n\n\nUsed ", iterationCount, " iterations")
print("Final Weight: ", weight)
print("Final Bias: ", bias)

while True:
    newX = input("\nInput your x value to get the y value that matches this pattern or press enter to leave: ")
    try:
        print(neuron(float(newX), weight, bias))
    except TypeError:
        break
    except ValueError:
        break
