#'ABCDA' ---> A
#'ABCDE' ---> None
def recu(word):
    hashset =  set()
    for n in word:
        if n in hashset:
            return n
        hashset.add(n)
    return None
recur = ['A','B','C','D','A']
print(recu(recur))
