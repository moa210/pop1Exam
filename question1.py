# student number 12915798

def fun(L1, L2):
    if L1 == [] and L2 == []:
        return []
    else:
        return [(L1[0] + L2[0]) / 2] + fun( L1[1:], L2[1:] )

# if both lists empty (it is the last call) the fun starts returning values which are
# added to divsion by two of 1st and 2nd element plus
# return of fun on L1 and L2 minus the first element
# recursive calls on both lists minus first element
