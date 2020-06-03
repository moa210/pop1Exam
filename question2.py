# student number 12915798

def replace(s):
    new_str = ""
    for i in range( 0, len( s ) ):
        if s[i].isupper():
            new_str += s[i]
        elif s[i].islower():
            new_str += s[i].upper()
        else:
            new_str += s[i]
    return new_str

# error one -  we use double quotes for denoting string here on line 6 we use single quotation mark for 'a'
# and 'z';  we are comparing two different data types a substring of the string passed to character
#
# error two - strings are immutable therefore the assignment on line 7 is en error - string does not support such
# an assigment / we are unable to change chars in the string
