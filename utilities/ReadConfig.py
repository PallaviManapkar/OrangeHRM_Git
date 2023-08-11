import configparser

config = configparser.RawConfigParser()
configfile = "F:\\Credence- CT14 batch\\Python-Automation (July_Month)\\Framework - Tushar Sir\\LogGeneration - " \
             "CredKart_Pytest_Project 05 Aug 2023\\Project-OrangeHRM\\Configuration\\config.ini"
config.read(configfile)

class ReadConfigs:
    @staticmethod
    def GetUsername():
        username = config.get('common data', 'UserName')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common data', 'PassWord')
        return password
