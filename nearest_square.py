import math

def perfect_numb(n):
    if (math.sqrt(n)-math.floor(math.sqrt(n))==0):
        return True 
    return False
def nearest_square(n):
    if n<0:
        return 0
        quit()
    if perfect_numb(n):
        return int(n)
    else:
        smaller_numb= -1
        i=0
        i=n+1
        
        i =n-1
        while True:
            if perfect_numb(i):
                smaller_numb=i
                break
            else:
                i=i-1
        return ((smaller_numb))