import datetime
import json
import os

# parent class
class Info:
    def __init__(self, type=None, parsedObject=None):
        if parsedObject is None:
            self.type = type
            self.descriptionText = input("Your news description: ")
            self.titleAd = self.type + " --------------------------------\n"
        else:
            self.type = parsedObject.type
            self.descriptionText = parsedObject.descriptionText
            self.titleAd = self.type + " --------------------------------\n"

    # method for override
    def writeAdd(self):
        print("METHOD TO OVERRIDE!!!")


# class for adding news
class News(Info):
    # initialization for class
    def __init__(self, parsedObject=None):
        if parsedObject == None:
            super().__init__("NEWS")
            self.city = input("Write city: ")
        else:
            super().__init__(None, parsedObject)
            self.city = parsedObject.city
        # receive current time
        self.time = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
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
    def __init__(self, parsedObject=None):
        if parsedObject is None:
            super().__init__("PersonalAd")
            # input end data
            self.expirationDate = datetime.datetime.strptime(input("Write expiration date (example: day/month/year): "),
                                                             '%d/%m/%y')
        else:
            super().__init__(None, parsedObject)
            self.expirationDate = datetime.datetime.strptime(parsedObject.expirationDate, '%d/%m/%y')

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
    def __init__(self, parsedObject):
        if parsedObject is None:
            super().__init__("Sport News")
            self.city = input("Write city: ")
            self.country = input("Write country: ")
            self.kindOfSport = input("Write kind of sport: ")
            self.team1 = input("Team 1: ")
            self.team2 = input("Team 2: ")
            self.scoreTeam1 = input("Score of team 1:")
            self.scoreTeam2 = input("Score of team 2:")
        else:
            super().__init__(None, parsedObject)
            self.city = parsedObject.city
            self.country = parsedObject.country
            self.kindOfSport = parsedObject.kindOfSport
            self.team1 = parsedObject.team1
            self.team2 = parsedObject.team2
            self.scoreTeam1 = parsedObject.scoreTeam1
            self.scoreTeam2 = parsedObject.scoreTeam2

        self.dateOfPublishing = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        # creating sport news
        self.fullDescription = self.descriptionText + "\n" + self.city + ", " + self.country + ", " + self.kindOfSport + ", " + str(
            self.dateOfPublishing) + "\n" + "team 1: " + self.team1 + "\n" + "team 2:" + self.team2 + "\n" + "Score: " + self.scoreTeam1 + ":" + self.scoreTeam2 + "\n" + "Winner: " + self.winner()

    def writeAdd(self):
        dataFile = open('task5.txt', 'a')
        dataFile.write(self.titleAd)
        dataFile.write(self.fullDescription)
        dataFile.write("\n")
        dataFile.close()

    def winner(self):
        if self.scoreTeam1 > self.scoreTeam2:
            return self.team1
        elif self.scoreTeam1 < self.scoreTeam2:
            return self.team2
        else:
            return "draw"


def mainFunc():
    number = input(
        """Select that you want to add in your file: \n1. - Add news. \n2. - Add private add. \n3. - Add sport news.\n4. - Load data from file (please write filePath or will be used standart path)\n""")
    if __isInputNumberValid(int(number)):
        __writeInfoInTxtFile(number)
    else:
        print("Your number not correct, please try again!")
        mainFunc()


def __isInputNumberValid(number):
    return number <= 4 and number >= 1


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
def __writeNews(parsedObject=None):
    # create class object
    news = News(parsedObject)
    # call news method
    news.writeAdd()


def __writePersonalAd(parsedObject=None):
    personalAd = PersonalAd(parsedObject)
    personalAd.writeAdd()


def __writeSportAd(parsedObject=None):
    sportNews = SportNews(parsedObject)
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
        case 4:
            __writeTextFromPath()


def __writeTextFromPath():
    filePath = input("Please write filePath or will be used standart path. Press ENTER if you want load data from standart path or enter your own.\n")

    __parseFromFile(None if len(filePath) == 0 else filePath)
    print("Data was loaded to main file with ads, and previous file was deleted.\n")
    __graduationSurvey()

class AdParsedObject(object):
    def __init__(self, city, country, type, descriptionText, expirationDate, kindOfSport, team1, team2, scoreTeam1, scoreTeam2):
        self.city = city
        self.country = country
        self.type = type
        self.descriptionText = descriptionText
        self.expirationDate = expirationDate
        self.kindOfSport = kindOfSport
        self.team1 = team1
        self.team2 = team2
        self.scoreTeam1 = scoreTeam1
        self.scoreTeam2 = scoreTeam2


def __parseFromFile(filePath=None):
    if filePath is None:
        if os.path.isfile("json.txt"):
            __writeAdsFromTxtFile("json.txt")
        else:
            print("Sorry, file not found. Please try again.")
            __writeTextFromPath()
    else:
        if os.path.isfile(filePath):
            __writeAdsFromTxtFile(filePath)
            os.remove(filePath)
        else:
            print("Sorry, file not found. Please try again.")
            __writeTextFromPath()



def __writeAdsFromTxtFile(filePath):
    with open(filePath, "r+") as file:

        if os.path.getsize(filePath) == 0:
            print("Sorry, but file doesn`t have new data.")
        else:
            listJSON = json.load(file)
            for iteratedJson in listJSON:

                jsonObject = AdParsedObject(**iteratedJson)
                match jsonObject.type:
                    case "NEWS":
                        __writeNews(jsonObject)
                    case "PersonalAd":
                        __writePersonalAd(jsonObject)
                    case "Sport News":
                        __writeSportAd(jsonObject)
            file.truncate(0)

#__parseFromFile()
mainFunc()
