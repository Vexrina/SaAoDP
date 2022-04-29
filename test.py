from stack import Stack
AddVote = Stack()
YesOrNo = True
def Add(letter, stack: Stack):
    stack.push(letter)
    return None

def Vote(letter, stack: Stack):
    if not stack.is_empty():
        a = stack.pop()
        if a == letter:
            return True
        else: 
            return False
    else:
        return False

def instruction(path, parties, iteration):
    temp = None
    if path[iteration] == "A":
        temp = Add(parties[iteration], AddVote)
    elif path[iteration] == "V":
        temp = Vote(parties[iteration], AddVote)
    return temp

def __main__(path, parties):
    counter = 0
    check = False
    while counter < len(path)-1:
        temp = instruction(path, parties, counter)
        if temp is not None:
            if temp:
                counter+=1
            else:
                break
        else:
            counter += 1 
        check = temp
    if check: print("yes")
    else: print("no")


__main__("AAVV", "abab")
__main__("AVAAAVVV", "zzxyxxyx")
__main__("V","z")