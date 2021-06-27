import inspect
import logging


class logGeneration:
    @staticmethod
    def customLogger(logLevel=logging.DEBUG):

        # Gets the name of the class / method from where this method is called
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # By default, log all messages
        logger.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler("../../../rideCell_Selenium_Framework/rideCell_Framework_UI_Logs/automation.log", mode='a')
        fileHandler.setLevel(logLevel)

        formatter = logging.Formatter('%(asctime)s - %(module)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        return logger
