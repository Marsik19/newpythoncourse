import datetime


# parent class
class Info:
    def __init__(self, type):
        self.type = type
        self.descriptionText = input("Your news description: ")
        self.titleAd = self.type + " --------------------------------\n"
    # method for override
    def writeAdd(self):
        print("METHOD TO OVERRIDE!!!")

# class for adding news
class News(Info):
    # initialization for class
    def __init__(self):
        super().__init__("NEWS")
        self.city = input("Write city: ")
        # receive current time
        self.time = datetime.datetime.now()
        # creating news
        self.fullDescription = self.descriptionText + "\n" + self.city + ", " + str(self.time) + "\n"

    # write description in txt
    def writeAdd(self):
        # work with file
        dataFile = open('task5.txt', 'a')
        dataFile.write(self.titleAd)
        dataFile.write(self.fullDescription)
        dataFile.write("\n")
        dataFile.close()

# class for adding personal advertisement
class PersonalAd(Info):
    def __init__(self):
        super().__init__("PersonalAd")
        # input end data
        self.expirationDate = datetime.datetime.strptime(input("Write expiration date (example: day/month/year): "),
                                                         '%d/%m/%y')
        # calculating days for ad
        self.daysToExpiration = str((self.expirationDate - datetime.datetime.now()).days) + " days to expire."
        # creating ad
        self.fullDescription = self.descriptionText + "\n" + str(self.expirationDate) + ", " + str(
            self.daysToExpiration) + "\n"

    def writeAdd(self):
        dataFile = open('task5.txt', 'a')
        dataFile.write(self.titleAd)
        dataFile.write(self.fullDescription)
        dataFile.write("\n")
        dataFile.close()

# class for adding sport news
class SportNews(Info):
    def __init__(self):
        super().__init__("Sport News")
        self.city = input("Write city: ")
        self.country = input("Write country: ")
        self.kindOfSport = input("Write kind of sport: ")
        self.dateOfPublishing = datetime.datetime.now()
        # creating sport news
        self.fullDescription = self.descriptionText + "\n" + self.city + ", " + self.country + ", " + self.kindOfSport + ", " + str(
            self.dateOfPublishing) + "\n"

    def writeAdd(self):
        dataFile = open('task5.txt', 'a')
        dataFile.write(self.titleAd)
        dataFile.write(self.fullDescription)
        dataFile.write("\n")
        dataFile.close()


def mainFunc():
    number = input(
        """Select that you want to add in your file: \n1. - Add news. \n2. - Add private add. \n3. - Add sport news.\n""")
    if __isInputNumberValid(int(number)):
        __writeInfoInTxtFile(number)
    else:
        print("Your number not correct, please try again!")
        mainFunc()


def __isInputNumberValid(number):
    return number <= 3 and number >= 1


def __isGraduationSurveyNumberValid(number):
    return number <= 2 and number >= 1

# switch case for choosing operation with ads
def __graduationSurvey():
    number = input("\nSelect what you want:\n 1 - Continue,\n 2 - Finish.\n")
    if __isGraduationSurveyNumberValid(int(number)):
        match (int(number)):
            case 1:
                mainFunc()
            case 2:
                return
    else:
        print("Your number not correct, please try again!")
        __graduationSurvey()

# write news
def __writeNews():
    # create class object
    news = News()
    # call news method
    news.writeAdd()


def __writePersonalAd():
    personalAd = PersonalAd()
    personalAd.writeAdd()


def __writeSportAd():
    sportNews = SportNews()
    sportNews.writeAdd()

# switch case for choosing type of ad
def __writeInfoInTxtFile(number):
    match (int(number)):
        case 1:
            __writeNews()
            __graduationSurvey()
        case 2:
            __writePersonalAd()
            __graduationSurvey()
        case 3:
            __writeSportAd()
            __graduationSurvey()


mainFunc()
