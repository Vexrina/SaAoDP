import itertools

def winner(a,b):
    for i in range(len(a)):
        if(a[i]<=b[i]):
            return True
    return False

s1 = "cxy"
s2 = "byz"
per1 = list(itertools.permutations(s1))
per2 = list(itertools.permutations(s2))
print(per1[0])
result = False
for i in per1:
    if(winner(per1[i], per2[i])):
        result = True
        break
print(result)