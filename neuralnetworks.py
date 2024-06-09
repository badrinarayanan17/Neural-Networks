# Building neural networks 
# In neural networks each neuron is connect to the subsequent neurons with a unique weight, and it has unique bias

input = [1,2,3,2.5] # Consider these are output's from 3 neurons in the previous layer
# Either value from a input layer
# input layer - whatever values that you're tracking

weight = [0.2,0.8,-0.5,1.0] # Every unique input also has unique weight associated with it
bias = 2 # Unique Bias 

# Why only one bias - Every neuron has one bias 
output = input[0]*weight[0]+input[1]*weight[1]+input[2]*weight[2]*weight[3]+input[3]*weight[3]+bias
print(output)





