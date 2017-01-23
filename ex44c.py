# alter before or after
class Parent(object):
    def altered(self):
        print "PARENT altered()"
        
class Child(Parent):
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
    ''' these four lines will print out 
    CHILD, BEFORE PARENT altered()
    PARENT altered()
    CHILD, AFTER PARENT altered()'''  
    # super can get the Parent.altered version 

dad = Parent()
son = Child()

dad.altered()
son.altered()      