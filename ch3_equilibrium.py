#!/usr/bin/python3

import sys
import numpy as np

def exit():
    print()
    print("Exiting...")
    quit()

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

    x1, y1, x2, y2 = argv[0],argv[1],argv[2],argv[3]

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
    print("-- x1:{} -- y1:{} --".format(argv[0], argv[1]))
    print()
    print("----Agent 2----")
    print("-- x2:{} -- y2:{} --".format(argv[2], argv[3]))
    print()


if __name__ == "__main__":
    main(sys.argv[1:])
