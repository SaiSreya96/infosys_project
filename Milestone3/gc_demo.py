import gc

class Demo:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")

a = Demo()
b = Demo()

a.ref = b
b.ref = a   # circular reference

del a
del b

gc.collect()  # force garbage collection
print("Garbage collection completed")
