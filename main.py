import yaml
import logging

config_file = 'test.yaml'
lineList = []


def log_init(context):
    log = logging.getLogger("main")
    log_stdout = logging.StreamHandler()
    log_stdout.setLevel(logging.DEBUG)
    log_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d '
    )
    log_stdout.setFormatter(log_format)
    log.addHandler(log_stdout)
    return log


def get_context(data_loaded):
    for k, v in data_loaded.items():
        for ele in v:
            if v[ele]:
                active_line = ele.split('-')[1]
                active_stack = k
                lineList.append({active_line:active_stack})
                # print("item {} line is {}, stack is {}".format(cnt,active_line, active_stack))


def display(lines):
    for k, v in lines.items():
        print(k, "===>", v)


try:
    with open(config_file, 'r') as stream:
        logger = log_init("main")
        logger.warning("File {} loaded successfully".format(config_file))
        data_loaded = yaml.full_load(stream)
        logger.warning("Function executed")
        get_context(data_loaded)
        print(lineList)

except yaml.YAMLError as err:
    logger.warning("Error occurred {}".format(err))

finally:
    stream.close()
