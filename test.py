#!/usr/bin/env python3
import os
import sys
from re import search
import pathlib
import logging

logger = logging.getLogger("app")
log_stdout = logging.StreamHandler()
log_stdout.setLevel(logging.DEBUG)
log_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
log_stdout.setFormatter(log_format)
logger.addHandler(log_stdout)



def funcsub(componentline):
    if search("3dspace", componentline):
        component = componentline.split('-')[0]
        stack = componentline.split('-')[2].split(':')[0]
        status = componentline.split(':')[2]
        print("component : {} \nstack : {} \nstatus : {}".format(component, stack, status))
        if search("yes", status):
            print("since the status is yes, execute {} stack {}".format(component, stack))
        else:
            print("since the status is no, ignoring {} stack {}".format(component, stack))
            print('\n')
            print('\n')


    elif search("internal", componentline):
        component = componentline.split('-')[0]
        stack = componentline.split('-')[2].split(':')[0]
        status = componentline.split(':')[2]
        print("component : {} \nstack : {} \nstatus : {}".format(component, stack, status))
        if search("yes", status):
            print("since the status is yes, execute {} stack {}".format(component, stack))
        else:
            print("since the status is no, ingnoring {} stack {}".format(component, stack))
            print('\n')
            print('\n')
    else:
        print("invalid input")


def my_func(name):
    sub_name = "hcplmappd[1-2]+l"

    base_path = "/Apps/NPICOEDatamig/FP/Joe/test/server_details"
    file_base_path = pathlib.Path(base_path)
    if file_base_path.is_dir():
        logger.debug("{} path is valid".format(file_base_path))

    if search(sub_name, name):
        new_list = os.listdir(
            "{}/{}".format(base_path, name)
        )

        for line in new_list:
            print("selected line : " + line)
            content = open("{}/{}/{}".format(base_path, name, line), "r")

            for component_line in content:
                print("component details : {}".format(component_line))
                if search("batch", component_line):
                    component = component_line.split(':')[0]

                elif search("internal", component_line) or search("3dspace", component_line):
                    funcsub(component_line)

                else:
                    print(component_line + " is invalid component")
    else:
        print("wrong value")
        exit()


my_func(sys.argv[1])
