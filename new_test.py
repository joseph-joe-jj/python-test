#!/usr/bin/env python3
import yaml
import logging

data = "/Apps/NPICOEDatamig/FP/Joe/test/server_details/test.yaml"

def log_init(context):
    log = logging.getLogger(context)
    log_stdout = logging.StreamHandler()
    log_stdout.setLevel(logging.DEBUG)
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d ')
    log_stdout.setFormatter(log_format)
    log.addHandler(log_stdout)
    return log

def get_data(file):
    with open(file, 'r') as stream:
        print("selected file : {}".format(file))
        data_loaded = yaml.full_load(stream)
        logger = log_init("FETCH_DATA")
        logger.warning("yaml file read from {}".format(file))
        print(data_loaded)
        return data_loaded

def filter_data(input_data):
    new_data =  get_data(input_data)
    result = []
    for component,stack_details in new_data.items():
        print("The component is {} & stack deatils are {}".format(component,stack_details))
        for k,status in stack_details.items():
            stack = k.split('-')[1]
            if status:
                result.append((component,stack))
    logger = log_init("FILTER_DATA")
    logger.warning("yaml file key value pairs are filtered and separated")
    return result


def execute_data(final_data):
    for k,v in final_data:
        print("execute {} stack {}".format(k,v))
    logger = log_init("EXECUTE")
    logger.warning("the mws components are all executed")

try:
    logger = log_init("main")
    refined_data = filter_data(data)
    execute_data(refined_data)
except yaml.YAMLError as err:
    logger.warning("Error occurred {}".format(err))
    print("The errors : \n{}".format(err))
