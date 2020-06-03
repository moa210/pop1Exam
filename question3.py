# student number 12915798


def swap_min_max(L):
    max_num = max( L )
    min_num = min( L )
    new_list = []
    for i in range( 0, len( L ) ):

        if (L[i] == max_num) and (i != len( L ) - 1) and (L[i] > L[i + 1]):
            new_list.append( min_num )
        elif (L[i] == min_num) and (i != len( L ) - 1) and (L[i] < L[i + 1]):
            new_list.append( max_num )
        elif L[i] == max_num and i == len( L ) - 1:
            new_list.append( min_num )
        elif L[i] == min_num and i == len( L ) - 1:
            new_list.append( max_num )
        else:
            new_list.append( L[i] )
    return new_list


list1 = swap_min_max( [10, 20, 30, 40] )
list2 = swap_min_max( [30, 30, 2, -10, -10, 0] )
print( ' '.join( map( str, list1 ) ) )
print( ' '.join( map( str, list2 ) ) )

# def test_mytest():
assert swap_min_max( [10, 20, 30, 40] ) == [40, 20, 30, 10]
assert swap_min_max( [-10, 2, 30, 0] ) == [30, 2, -10, 0]
assert swap_min_max( [30, 30, 2, -10, -10, 0] ) == [30, -10, 2, -10, 30, 0]
assert swap_min_max( [23] ) == [23]
assert swap_min_max( [12, 1] ) == [1, 12]
assert swap_min_max( [-12, -1] ) == [-1, -12]
