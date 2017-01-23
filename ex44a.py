# try to avoid multi inheritance
# implicit inheritance
class Parent(object):
    def implicit(self):
        print "PARENT implicit()"
        
class Child(Parent):
    # pass means I want an emply block
    # Child will inherit all of its behavior from Parent
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()    