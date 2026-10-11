# Neuron
This is an Artificial Intelligence neuron that works in the exact same way as large language models. To use it, place 5 unique colinear coordinates in the inputs and correctOutputs lists, with the x coordinates as the input.

# How it works
1. The Neuron predicts the output when given the input and assuming weight and bias are 0.
2. The Neuron finds the loss and derivative of the loss to find how far off it was from the correct solution.
3. The Neuron adjusts weight and bias based on the derivative.
4. Steps 1-3 repeat until loss is less than 0.00000001
5. The Neuron estimates the value of weight and bias to 3 decimal places.

[See the Math involved](MATH.md)
