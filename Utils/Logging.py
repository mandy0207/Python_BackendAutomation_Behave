import inspect
import logging

@staticmethod
def getLogger():
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # path = root_path + r"\Reports\logfile.log"
    # print("Root path of project:", root_path)
    filehandler = logging.FileHandler(
        r"C:\Users\msingh\PycharmProjects\pythonProject1\BackendAutomation" + r"\logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    return logger
