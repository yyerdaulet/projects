#Implementing simple neural network
import numpy as np
import vector_van_doom
from random import randint

def storing(prediction,real):
    delta = real-prediction
    error = (real-prediction)**2
    return delta,error

def neural_network(input,weights):
    predict = vector_van_doom.elementwise_multiplication(input, weights)
    return predict

def correction(weights,delta,learning_rate):
    for i in range(len(weights)):
        weights[i] += weights[i]*delta*learning_rate

def one_iteration(input,weights,y_test,learning_rate):
    predict = neural_network(input,weights)
    delta,error = storing(predict,y_test)
    correction(weights,delta,learning_rate)

def model_training(big_input ,weights,iterations,y_test,learning_rate=0.01):
    queue = randint(0,len(y_test)-1)
    inputs = [big_input[0][queue],big_input[1][queue],big_input[2][queue]]
    y = y_test[queue]
    for i in range(iterations):
        one_iteration(inputs,weights,y,learning_rate)

toes = [8.5,9.5,9.9,9.0]
wirec = [0.65,0.8,0.8,0.9]
nfans = [1.2,1.3,0.5,1.0]

big_input = [toes,wirec,nfans]
tData = [0,1,1,1]
weights = [.1,.1,.1]
model_training(big_input,weights,30,tData,learning_rate=0.01)
print(weights)

predict = neural_network([5.0,0.9,0.1],weights)
print(f"Prediction about : {round(predict,2)*100}%")
# Case where we have only one input and 3 output

# input2 = wirec[0]
# w2 = [.3,.2,.9]
# def neural_network2(input,weights):
#     res = vector_van_doom.ele_mul(input,weights)
#     return res

#print(neural_network2(input2,w2))

# weights2 = [.4,.5,.7]
# weights3 = [.9,.3,.1]
# ww = [weights,weights2,weights3]
# #Case where we have 3 input and 3 output
# def neural_network3(input,weights):
#     output = [0,0,0]
#     for i in range(len(output)):
#         output[i] = vector_van_doom.elementwise_multiplication(input,ww[i])
#     return output
# predictions = neural_network3(input,ww)
#print("{}:4f".format(predictions))



