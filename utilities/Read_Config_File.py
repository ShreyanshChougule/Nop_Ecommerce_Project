import configparser

data = configparser.RawConfigParser()
data.read(".//Configurations//Config.ini")


class Read_Confi_File:

    @staticmethod
    def URL():
        UL = data.get("Nop_Ecommerce_Proect", "URL")
        return UL

    @staticmethod
    def Email():
        ML = data.get("Common_Data", "Email")
        return ML

    @staticmethod
    def Password():
        PS = data.get("Common_Data", "Password")
        return PS

    @staticmethod
    def Excel_Path():
        Path = data.get("Common_Data", "Excel_Path")
        return Path
