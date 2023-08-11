import inspect
import logging


class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("F:\Credence- CT14 batch\Python-Automation (July_Month)\Framework - Tushar Sir\LogGeneration - CredKart_Pytest_Project 05 Aug 2023\Project-OrangeHRM\Logs\OrangeHRM.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger

