# import numpy as np
# arr = np.array([1,2,3,4,10,11])

# def simpleArraySum(ar):
#     return ar.sum()
# print(simpleArraySum(arr))

def simpleArraySum(ar):
    ar_sum = 0
    for i in ar:
        ar_sum = ar_sum + i
    return ar_sum
    
print(simpleArraySum(ar=[1,2,3,4,10,11]))