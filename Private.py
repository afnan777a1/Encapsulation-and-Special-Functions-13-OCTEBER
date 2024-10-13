class myClass:

    __privateVar = 50

    def __privMeth(self):
        print("I'm inside class privmeth Method myClass")

    def hello(self):
        print("Private Variable value: ", myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privMeth
print(foo.__privateVar)