#!/usr/bin/python3

import sys
import numpy as np

def exit():
    print()
    print("Exiting...")
    quit()

def compute_equilibrium(u1, x1, y1, u2, x2, y2):

    print("returning all values")

    return(u1,x1,y1,u2,x2,y2)

def main(argv):
    print("-----------------------------")
    print("This program computes the point of equilibrium for a simple two-agent")
    print("double-auction market containing only two goods: x & y.")
    print("The agents' initial endowments for the two goods are given by")
    print("the arguments provided:")

    if len(argv) != 4:
        print()
        print("Please enter four arguments of the form:")
        print("x1 y1 x2 y2")
        exit()

    x1, y1, x2, y2 = int(argv[0]),int(argv[1]),int(argv[2]),int(argv[3])

    print("----Agent 1----")
    print("-- x1:{} -- y1:{} --".format(x1, y1))
    print()
    print("----Agent 2----")
    print("-- x2:{} -- y2:{} --".format(x2, y2))
    print()
    
    u1 = (100*x1) - (x1**2 / 2) + y1
    u2 = ((3/4) * np.log(x2)) + ((1/4) * np.log(y1))

    print("-----------------------------")
    print("The hard-coded utility functions for the agents are below:")
    
    print("----Agent 1----")
    print("-- u1:{} --".format("(100*x1) - (x1**2 / 2) + y1"))
    print()
    print("----Agent 2----")
    print("-- u2:{} --".format("((3/4) * np.log(x2)) + ((1/4) * np.log(y1))"))
    print()

    results = compute_equilibrium(u1,x1,y1,u2,x2,y2)

    print("The market reaches equilibrium at the state:")
    print(results)


if __name__ == "__main__":
    main(sys.argv[1:])
