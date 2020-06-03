# student number 12915798


def shortest_atom(str):
    sub_str_arr = []
    for i in range( len( str ) ):
        sub_str_arr.append( str[:i] )

    for i in sub_str_arr[:1:-1]:
        if str.count( i ) > 1:
            offset = str[len( i ):].find( i )
            return str[:len( i ) + offset]

    return str


print( shortest_atom( "ababab" ) )
print( shortest_atom( "abcabc" ) )
print( shortest_atom( "abcab" ) )

assert shortest_atom( "ababab" ) == "ab"  # must be True
assert shortest_atom( "abcabc" ) == "abc"  # must be True
assert shortest_atom( "abcab" ) == "abcab"  # must be True
