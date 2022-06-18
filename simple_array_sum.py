# import numpy as np
# arr = np.array([1,2,3,4,10,11])

# def simpleArraySum(ar):
#     return ar.sum()
# print(simpleArraySum(arr))

def simpleArraySum2(ar):
    ar_sum = 0
    for i in ar:
        ar_sum = ar_sum + i
    return ar_sum
    
print(simpleArraySum2(ar=[1,2,3,4,10,11]))