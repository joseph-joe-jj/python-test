#!/usr/bin/env python3
import os
import sys
from re import search
def funckeycheck(key, componentline):
    component = componentline.split('-')[0]
    stack = componentline.split('-')[2].split(':')[0]
    status = componentline.split(':')[2]
    print("component : {} \nstack : {} \nstatus : {}".format(component,stack,status))
    if search("yes", status):
        print("since the status is yes, execute {} stack {}".format(component,stack))
        print("invoke {}.sh".format(key))
        print('\n')
    else:
        print("since the status is no, ingnoring {} stack {}".format(component,stack))
        print('\n')
def funcsub(componentline):
    if search("3dspace", componentline):
        funckeycheck("3dspace",componentline)
    elif search("internal", componentline):
        funckeycheck("internal",componentline)
    else:
        print("invalid input")
def my_func(name):
    # subName = "hcplmappd"+"[1-2]+"+"l"
    subName = "{}{}{}".format("hcplmappd","[1-2]+","l")
    print("substring value : {}".format(subName))
    basePath = "/Apps/NPICOEDatamig/FP/Joe/test/server_details"
    print(f'the parameter is : {name}')
    if search(subName, name):
        newlist = os.listdir("{}/{}".format(basePath,name))
        print(newlist)
        for line in newlist:
            print("selected line : " + line)
            content = open("{}/{}/{}".format(basePath,name,line), "r")
            for componentline in content:
                print("component details : {}".format(componentline))
                if search("batch", componentline):
                    component = componentline.split(':')[0]
                    print("component : {}".format(component))
                    print('\n')
                elif search("internal", componentline) or search("3dspace", componentline):
                    funcsub(componentline)
                else:
                    print("{} is invalid component".format(componentline))
    else:
        print("wrong value")
        exit()
my_func(sys.argv[1])
