from config.configure import Configure

# config = configparser.RawConfigParser()
# config.read(r".//config//config.ini")


class ReadConfig:

    @staticmethod
    def getUrl():
        url = Configure.baseUrl
        return url

    @staticmethod
    def getUseremail():
        email = Configure.useremail
        return email

    @staticmethod
    def getPassword():
        pwd = Configure.password
        return pwd
