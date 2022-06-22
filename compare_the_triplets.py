def compareTriplets(a, b):
    sum_a = 0
    sum_b = 0
    
    for i in range(len(a)): #a and b have the same length
        if a[i] > b[i]:
            sum_a += 1
        elif a[i] < b[i]:
            sum_b +=1
        
        
    return [sum_a, sum_b]
    
print(compareTriplets(a=[17,28,30], b=[17,28,30]))