print("Hi, this is your first Python script!")
print("""Here some basic operation,
between the operands 11 and 2:""")
print("Sum: " + str(11+2))
print('Difference: ' + str(11-2))
print("Multiplication: "+str(11*2))
print("Division: "+str(11/2))
print("Modulo: "+str(11%2))
print("Power: "+str(11**2))
print("Floor division: "+str(11/2))
print("Now i will repeat \"Hello wordl!\" for three times:")
print("HelloWorld!"*3)
print("Now let's define some variables, and then print their values separately.")
myName="giocic2"
myPrefix="_"
myAge=20
print(myName)
print(myPrefix)
print(myAge)
# print("Now i delete \'myName\' variable and try to print it anyway.")
# del myName
# print(myName)
# print("Can this message be desplayed after the print error?")
# NB: Of course not. The error ended the program.
# This is the way you can write comments (only single line is accepted).
# Otherwise you should use docstrings.
print("Let's take some user input.")
print("Write the time you read on your watch (no padding zeros needed).")
hh=input("hours: ")
hh='{:02d}'.format(hh)
mm=input("minutes: ")
mm='{:02d}'.format(mm)
# In this case Python automatically recognise that the input is a number.
# String conversione for print is needed.
print("The time you wrote is "+str(hh)+':'+str(mm))
