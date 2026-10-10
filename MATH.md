# Math
This is all the math involved to make this neuron.

## The Neuron
The neuron uses the equation, $\hat{y} = wx + b$, as the format where w is weight, b is bias, and $\hat{y}$ is the prediction. This equation is the same as the equation of a line which is why the coordinates given as inputs must be colinear.

## Error and Loss
The neuron makes a prediction using the weight and bias given. Then the neuron calculates how far off it was using $e_i=\hat{y}_i - y_i$ where e is the error and i is the input. Next, the neuron finds the loss. I chose to use Mean Squared Loss so I calculate loss by squaring each prediction and then finding the mean of them which can be written with the given formula where n is the number of inputs.

$$
L=\frac{1}{n}\sum_{i=1}^{n}e^2_i
$$

## Partial Derivatives with respect to Bias and Weight
Finding the derivative gives the rate of change for both bias and weight, allowing us to get an estimate of a good number to modify weight and bias by.

Partial Derivative with respect to Weight:

$$
\frac{\partial L}{\partial w} = \frac{2}{n}\sum_{i=1}^{n}x_i (wx_i+b-y_i)
$$

Partial Derivative with respect to Bias:

$$
\frac{\partial L}{\partial b} = \frac{2}{n}\sum_{i=1}^{n}(wx_i+b-y_i)
$$

## Gradient Descent 
During gradient descent we multiply the learning rate ($\alpha$) by the partial derivative and then add that to the weight/ bias. Reducing the learning rate will make the response much more precise but it will take many more iterations. Increasing the learning rate will lower precision but also lower iteration count, which could be useful for smaller calculations in video games.

$$
w\leftarrow w - \alpha \frac{\partial L}{\partial w}
$$

$$
b\leftarrow b - \alpha \frac{\partial L}{\partial b}
$$
