#!/usr/bin/env python3
import os
import sys
from re import search
def funcsub(componentline):
    if search("3dspace", componentline):
        component = componentline.split('-')[0]
        stack = componentline.split('-')[2].split(':')[0]
        status = componentline.split(':')[2]
        print("component : {} \nstack : {} \nstatus : {}".format(component,stack,status))
        if search("yes", status):
            print("since the status is yes, execute {} stack {}".format(component,stack))
        else:
            print("since the status is no, ingnoring {} stack {}".format(component,stack))
            print('\n')
            print('\n')

def my_func(name):
    # subName = "hcplmappd"+"[1-2]+"+"l"
    subName = "{}{}{}".format("hcplmappd","[1-2]+","l")
    print("substring value : {}".format(subName))
    basePath = "/Apps/NPICOEDatamig/FP/Joe/test/server_details"
    # sub = re.compile(r'')
    print(f'the parameter is : {name}')
    if search(subName, name):
        # newlist = os.listdir( basePath + "/" + name)
        newlist = os.listdir("{}/{}".format(basePath,name))
        print(newlist)
        for line in newlist:
            print("selected line : " + line)
            # content = open(basePath + "/" + name + "/" + line, "r")
            content = open("{}/{}/{}".format(basePath,name,line), "r")
            for componentline in content:
                # print("component deatils : " + componentline)
                print("component deatils : {}".format(componentline))
                if search("batch", componentline):
                    component = componentline.split(':')[0]
                    # print("component : " + component)
                    print("component : {}".format(component))
                    print('\n')
                    print('\n')
                # stack = componentline.split('-')[1]
                elif search("internal", componentline) or search("3dspace", componentline):
                    funcsub(componentline)
                else:
                    print(componentline + " is invalid component")
    else:
        print("wrong value")
        exit()

my_func(sys.argv[1])
