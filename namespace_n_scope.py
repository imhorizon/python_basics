

print("\n\nBuilt-in-namespace : dir(__builtins__) : \n\n{}".format(dir(__builtins__)))


print("\n\nGlobal-namespace : globals() : \n\n{}".format(globals()))

global_var = 5

print("\n\nGlobal-namespace after declaring variable global_var with value 5 : globals() : \n\n{}".format(globals()))

def f(x, y) :
    print("\n\nStart of method f()")
    print("\nLocals(): \n{}\n".format(locals()))
    
    s = "foo"
    print("After declaring varaible s with value 'foo' ")
    print("Locals(): \n{}\n\n".format(locals()))

    def g() : 
        print ("Start of method g()")
        print("\nLocals(): \n{}".format(locals()))
        z = "bar"                           # Declared local variable z for method g()
        print("After declaring varaible z with value 'var' ")
        print("Locals(): \n{}\n".format(locals()))
        print("\nGlobal-namespace inside method g(): globals() : \n\n{}".format(globals())) # Checking global variables
        print ("\nEnd of method g()")
    
    g()

    print("\nAfter declaring varaible s with value 'foo' and calling method g() :")
    print("Locals(): \n{}\n".format(locals()))
    print("\nGlobal-namespace inside method f(): globals() : \n\n{}".format(globals())) # Checking global variables
        

    print("\nEnd of method f()\n\n")

f(10, 20)

