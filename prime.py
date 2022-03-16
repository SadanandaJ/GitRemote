#num = int(input("Enter a number: "))  # convert string to int

for num in range(1,100):
    s = open("C:Users/DELL/Desktop/newpy.txt",'a+')
    isDivisible = False;

    i = 2;
    while i < num:
        if num % i == 0:
            isDivisible = True;
            print("{} is divisible by {}".format(num, i))
            break;  # this line is the only addition.
        i += 1;

    if isDivisible:
        s.write("{} is NOT a Prime number\n".format(num))
    else:
        s.write("{} is a Prime number\n".format(num))
s.close()
