# try to avoid multi inheritance
'''
class SuperFun(Child, BadStuff):
    pass
When you have implicit actions on a SuperFun instance, 
Python has to look up possible functions in both Child and BadStuff
'''

# common use of super with __init__
''' 
class Child(Parent):
    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init()
'''        
# implicit inheritance
class Parent(object):
    def implicit(self):
        print "PARENT implicit()"
        
class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()    
# override explicitly
class Parent(object):
    def override(self):
        print "PARENT override()"
        
class Child(Parent):
    def override(self):
        print "CHILD override()"
        
dad = Parent()
son = Child()

dad.override()
son.override()    

# alter before or after
class Parent(object):
    def altered(self):
        print "PARENT altered()"
        
class Child(Parent):
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()        