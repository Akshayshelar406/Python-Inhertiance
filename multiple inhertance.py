class Felix:
    def felixMethod(self):
        print("This is from felix class")

class FelixITs():
    def felixItsMethod(self):
        print("This is from Felix ITs Class")

class FelixITSystem(Felix, FelixITs):
    def felixItSystemMethod(self):
        print("This is from Felix ITs System")

f = FelixITSystem()
f.felixMethod()
f.felixItsMethod()
f.felixItSystemMethod()