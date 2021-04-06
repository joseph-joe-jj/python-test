import yaml
import logging


config_file = 'test.yaml'
list_line = []


class ExecutionLines:
    def __init__(self, line, stack, active):
        self.line = line
        self.stack = stack
        self.status = active

    def get_line(self):
        return self.line

    def get_stack(self):
        return self.stack

    def get_line_status(self):
        return self.status

    def execute(self):
        # do whatever
        print("triggering stack {}:".format(self.stack))
        print("          ----> using line {}".format(self.line))



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


def load_lines(yaml_data):
    for k, v in yaml_data.items():
        for ele in v:
            active_line = ele.split('-')[1]
            active_stack = k
            g = ExecutionLines(active_line, active_stack, v[ele])
            list_line.append(g)


def load_yaml(file, logger):
    try:
        with open(file, 'r') as stream:
            logger.warning("File {} loaded successfully".format(file))
            data_objects = yaml.full_load(stream)
            return data_objects

    except yaml.YAMLError as yaml_err:
        logger.exception("Error occurred {}".format(yaml_err))

    finally:
        stream.close()


def main():
    try:
        logger = log_init("main")

        logger.warning("trying to load file {} ".format(config_file))
        conf_objects = load_yaml(file=config_file, logger=logger)

        logger.warning("parsing execution lines")
        load_lines(conf_objects)

        logger.warning("listing the status of lines:")
        for k in list_line:
            if k.status:
                k.execute()

    except Exception as err:
        logger.warning("error occurred {}".format(err))

    finally:
        pass


if __name__ == "__main__":
    main()
