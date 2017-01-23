# you can use modules to achive the same result
# guidelines: 1. Avoid multiple inheritance at all costs
# 2. Use composition to package code into modules that are used in many different unrelated places and situations.
# 3. Use inheritance only when there are clearly related reusable pieces of code
class Other(object):
    def override(self):
        print "OTHER override()"
    def implicit(self):
        print "OTHER implicit()"
    def altered(self):
        print "OTHER altered()"
        
class Child(object):
    def __init__(self):
        self.other = Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print "CHILD override()"
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"
        
son = Child()

son.implicit()
son.override()
son.altered()        
        