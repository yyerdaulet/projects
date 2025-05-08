import numpy as np

def elementwise_multiplication(vecA, vecB):
    res = 0
    if len(vecA) == len(vecB):
        for i in range(len(vecA)):
           res += vecA[i] * vecB[i]
    return res

def elementwise_addition(vecA, vecB):
    res = 0
    if len(vecA) == len(vecB):
        for i in range(len(vecA)):
            res += vecA[i] + vecB[i]
    return res

def vector_sum(vecA):
    res = 0
    for i in range(len(vecA)):
        res += vecA[i]

    return res

def vector_avg(vecA):
    res = 0
    for i in vecA:
        res += i

    return res/len(vecA)


def ele_mul(scalar,vecA):
    output = [0,0,0]
    if len(vecA) == len(output):
        for i in range(len(vecA)):
            output[i] = scalar *vecA[i]

    return output

