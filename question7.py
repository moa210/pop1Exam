# student number 12915798

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_info(self):
        return f"{self.first_name} {self.last_name}"

    def get_name(self):
        return self.first_name, self.last_name

    def __eq__(self, obj):
        return isinstance( obj, Person ) and obj.get_info() == self.get_info()


class Adult( Person ):
    def __init__(self, first_name, last_name, phone_num):
        super().__init__( first_name, last_name )
        self.phone_number = phone_num

    def get_phone(self):
        return f"{self.phone_number}"


class Child( Person ):
    def __init__(self, first_name, last_name, mum, dad):
        super().__init__( first_name, last_name )
        self.mother = mum
        self.father = dad

    def get_info(self):
        mum_name = " ".join( self.mother.get_name() )
        dad_name = " ".join( self.father.get_name() )
        return f"{self.first_name} {self.last_name} {mum_name} {dad_name}"

    def get_parents(self):
        return self.mother, self.father


p = Person( "Mary", "Ann" )
a = Adult( "John", "Doe", "1234567" )
c = Child( "Richard", "Doe", p, a )
print( a.get_info() )
print( c.get_name() )
print( c.get_info() )
print( c.get_parents() )
assert a.get_info() == "John Doe"  # must be True
assert c.get_name() == ("Richard", "Doe")  # must be True
assert c.get_info() == "Richard Doe Mary Ann John Doe"  # must be True
assert c.get_parents() == (p, a)  # must be True
