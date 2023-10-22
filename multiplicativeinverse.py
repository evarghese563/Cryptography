
def tfunc(t1,t2, q ):
    '''Calculate T'''
    t = t1 - t2*q
    return t

def multinv(a,b):
    '''Function where you find the multiplicative inverse'''
    q = 0
    r = 0
    t1 = 0
    t2 = 1
    t = 0
    while(b != 0 ):

        if b != 0 :
            q = a//b
            r = a % b
            t = tfunc(t1,t2,q)

            a = b
            b = r
            t1 = t2
            t2 = t
        else:
            a = b
            b = r
            t1 = t2
            t2 = t
            
    return t1


if __name__ == '__main__':

    print("Input the value of a")
    a = int(input())
    print("Input the value of p")
    p = int(input())

    mi = multinv(p,a)

    print(mi)