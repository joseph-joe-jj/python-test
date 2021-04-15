#!/usr/bin/env python3
import yaml
import logging
import sys
import os

def log_init(context):
    log = logging.getLogger(context)
    log_stdout = logging.StreamHandler()
    log.setLevel(logging.DEBUG)
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d ')
    log_stdout.setFormatter(log_format)
    log.addHandler(log_stdout)
    return log

def server_info(svr_info):
    print(svr_info)
    if len(svr_info) > 2:
        logger.error('You have specified too many arguments')
        sys.exit()
    if len(svr_info) < 2:
        logger.error('You need to specify the path to be listed')
        sys.exit()
    server = svr_info[1].split('.')[0]
    print(server)
    return server

def app_list(path):
    final_app_list = []
    instance_list = os.listdir(path)
    for x in instance_list:
        if "yaml" in x:
            final_app_list.append(x)
    return final_app_list

def get_data(file):
    with open(file, 'r') as stream:
        logger.info("selected file : {}".format(file))
        data_loaded = yaml.full_load(stream)
        logger.info("yaml file is read from {} & the data fetched are {} :".format(file,data_loaded))
    return data_loaded

def filter_data(input_data):
    new_data =  get_data(input_data)
    if new_data:
        result = []
        for component,stack_details in new_data.items():
            logger.info("The component is {} & stack deatils are {}".format(component,stack_details))
            for k,status in stack_details.items():
                stack = k.split('-')[1]
                if status:
                    result.append((component,stack))
        logger.info("yaml file key value pairs are filtered and separated")
        return result

def execute_data(final_data,instance_name):
    for k,v in final_data:
        print("execute {} stack {}".format(k,v))
    logger.info("the mws {} components are all executed.".format(instance_name.split('.')[0]))

try:
    logger = log_init("main")
    server = None
    server = server_info(sys.argv)
    data = "/Apps/NPICOEDatamig/FP/Joe/test/server_details/" + server
    print(data)
    instance_list = app_list(data)
    if instance_list:
        logger.info("final list of MWS instance to be processed {}".format(instance_list))
        for app_file in instance_list:
            app_data = data + "/" + app_file 
            refined_data = filter_data(app_data)
            if refined_data:
                execute_data(refined_data,app_file)
            else:
                logger.warning("empty file")
    else:
        logger.warning("no file")

except yaml.YAMLError as err:
    logger.error("Error occurred {}".format(err))
except FileNotFoundError as err1:
    logger.error("Error occurred {}".format(err1))
except AttributeError as err2:
    logger.error("Error occurred {}".format(err2))
except IndexError as err3:
    logger.error("Error occurred {}".format(err3))
