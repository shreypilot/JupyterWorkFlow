# argv is not array  it is list type .available in sys module 
 # argument which is passing at the time of excution are called command line arguments


from sys import argv
print("The Number of command li ne arguments",len(argv))
print("The LIst of Command Line ARguments",argv)
print("command line arguments one by one")
for x in argv:
    print(x)