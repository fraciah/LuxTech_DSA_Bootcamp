def simpleArraySum(ar):
    ar_sum = 0
    for i in ar:
        ar_sum += i
    return ar_sum
arr=[1,2,3,4,10,11]
print(simpleArraySum(arr))

# import numpy as np
# arr = np.array([1,2,3,4,10,11])

# def simpleArraySum2(ar):
#     return ar.sum()
# print(simpleArraySum2(arr))