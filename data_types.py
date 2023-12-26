###################################################################################
# Python is dynamically typed language meaning that you dont need to explicitly   #
# declares the data type of the variables. The interpreter infers the data type   #
# based on the value assigned.                                                    #
###################################################################################


print ("\n\nBelow are the 7 basics data type in python :\n\n")

print("\t1. Numeric data types :\n")
int_var = 5
float_var = 3.14
complex_var = 1 + 2j
print("\t\tint_var = {0}\t\ttype(int_var) = {1}".format(int_var,type(int_var)))
print("\t\tfloat_var = {0}\ttype(float_var) = {1}".format(float_var,type(float_var)))
print("\t\tcomplex_var = {0}\ttype(complex_var) = {1}".format(complex_var,type(complex_var)))


print("\n\n\t2. String data types :\n")
string_var = "Hello, python !"
print("\t\tstring_var = {0}\ttype(str_var) = {1}".format(string_var,type(string_var)))


print("\n\n\t3. Boolean data types :\n")
bool_var = True
print("\t\tbool_var = {0}\t\ttype(bool_var) = {1}".format(bool_var,type(bool_var)))


print("\n\n\t4. Sequence data types :\n")
list_var = [1,2,3]          # Ordered and Mutable
touple_var = (4,5,6)        # Ordered and Immutable
range_var = range(7,10)     # Used for creating sequence of numbers
print("\t\tlist_var = {0}\t\ttype(list_var) = {1}".format(list_var,type(list_var)))
print("\t\ttouple_var = {0}\t\ttype(touple_var) = {1}".format(touple_var,type(touple_var)))
print("\t\trange_var = {0}\ttype(range_var) = {1}".format(range_var,type(range_var)))


print("\n\n\t5. Set data types :\n")
set_var = {1,2,3}                       # Unordered and Mutable
frozenset_var = frozenset({4,5,6})      # Unordered and Immutable
print("\t\tset_var = {0}\t\t\ttype(set_var) = {1}".format(set_var,type(set_var)))
print("\t\tfrozenset_var = {0}\ttype(frozenset_var) = {1}".format(frozenset_var,type(frozenset_var)))


print("\n\n\t6. Mapping data types :\n")
dict_var = {"name" : "Horizon", "age" : 26, "location" : "pune"}    # Dictionary type (Unordered collection of key-value pairs)
print("\t\tdict_var = {0}\ttype(dict_var) = {1}".format(dict_var,type(dict_var)))


print("\n\n\t7. None types :\n")
none_var = None     # None type represent absent of values or null value
print("\t\tnone_var = {0}\ttype(none_var) = {1}".format(none_var,type(none_var)))


print("\n\n\n")