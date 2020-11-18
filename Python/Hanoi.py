import numpy as np

A = []
B = []
C = []

options = {
    'A' : A,
    'B' : B,
    'C' : C
}

def moveDisc(source, target):
    if len(target) == 0:
        target.append(source.pop())
    elif target[-1] > source[-1]:
        target.append(source.pop())
    else:
        print ("You can't place a larger disc on a smaller one")
    print(A, B, C, '##############', sep='\n')
        
def main():
    
    
    discs = eval(input("how many discs? "))
    for i in range(discs-1, -1 , -1):
        A.append(i+1)

    print(A, B, C, '##############', sep='\n')

    while len(C) != discs:
        source = input("Move from: ")
        target = input("Move to: ")
        moveDisc(options[source], options[target])
        
        
    print("You win")
        
main()