#Internationale Feiertage

import holidays
from bs4 import BeautifulSoup
import requests
import datetime

"""
TODO:
Land zu Tag ausgebeen (again...)
"""

class internationalDays():

    def __init__(self, year):
        self.year = year
        self.internationaleTage = holidays.HolidayBase()
        self.provs = ["BW", "BY", "BYP", "BE", "BB", "HB", "HH", "HE", "MV", "NI", "NW", "RP", "SL", "SN", "ST", "SH", "TH"]
        self.usedcountries = []
        self.countryholidays = []

    def baseGermanDays(self):

        used = False
        i = 0
        for bundesland in self.provs:
            for date, name in holidays.Germany(prov= bundesland, years= self.year).items():
                if name.find(' (Observed)') != -1:
                    name = name.strip(' (Observed)')
                    
                if date in self.internationaleTage:
                    if name not in self.internationaleTage[date]:
                        self.internationaleTage[date].append(name)
                        used = True
                    
                else:
                    self.internationaleTage.update({date: [name]})
                    used = True

            if used:
                county = "Germany: " + self.provs[i]  
                self.usedcountries.append(county)
                self.countryholidays.append(holidays.Germany(prov= bundesland, years= self.year))

            used = False
            i += 1

    def baseInternationalDays(self):

        countries = [holidays.US(years= self.year), holidays.IsleOfMan(years= self.year), holidays.Japan(years= self.year), holidays.Korea(years= self.year),
                     holidays.Ireland(years= self.year), holidays.Canada(years= self.year), holidays.France(years= self.year), holidays.Italy(years= self.year), 
                     holidays.Denmark(years= self.year), holidays.UnitedKingdom(years= self.year), holidays.Austria(years= self.year), holidays.Iceland(years= self.year), 
                     holidays.Sweden(years= self.year), holidays.Spain(years= self.year), holidays.Vietnam(years= self.year),
                     holidays.Netherlands(years= self.year), holidays.India(years= self.year), holidays.HongKong(years= self.year), 
                     holidays.Switzerland(years= self.year), holidays.SouthAfrica(years= self.year), holidays.PortugalExt(years= self.year)]

        countrynames = ["US", "IsleOfMan", "Japan", "Korea", "Ireland", "Canada", "France", "Italy", "Denmark", "UnitedKingdom", "Austria",  "Iceland", "Sweden", "Spain",  "Vietnam",
                       "Netherlands", "India", "HongKong", "Switzerland", "SouthAfrica", "Portugal"]

        i = 0
        used = False
        for country in countries:
            for date, name in country.items():
                if name.find(' (Observed)') != -1:
                    name = name.strip(' (Observed)')

                if name == 'Söndag':
                    continue
                
                if date in self.internationaleTage:
                    if date not in holidays.Germany(prov= "BY", years= self.year):
                        if name not in self.internationaleTage[date]:
                            self.internationaleTage[date].append(name)
                            used = True

                else:
                    self.internationaleTage.update({date: [name]})
                    used = True

            if used:
                self.usedcountries.append(countrynames[i])
                self.countryholidays.append(country)

            used = False
            i += 1

    def modifyDay(self, datum, newname):

        if datum not in self.internationaleTage:
            self.internationaleTage.update({datum: [newname]})

        else:
            if newname not in self.internationaleTage[date]:
                self.internationaleTage[datum].append(newname)
            
            return True

        return False

    def modifyToday(self):

        page = requests.get("https://welcher-tag-ist-heute.org/")

        if page.status_code == 200:
            content = page.content

        Data = {}
        DOMdocument = BeautifulSoup(content, 'html.parser')

        Data['Title'] = DOMdocument.title.string
        dayname = Data['Title'].split(" | ")
        dayname[0] = dayname[0].split(" - ")[1]
    
        names = []
        for name in dayname:
            if "international" in name:
                names.append(name)

        today = datetime.datetime.today()
        date = today.strftime("%Y-%m-%d")
        if date in self.internationaleTage:
            for tempname in names:
                if tempname not in self.internationaleTage[date]:
                    self.internationaleTage[date].append(tempname)

        else:
            self.internationaleTage.update({date: names})



    def getDay(self, day):

        if day in self.internationaleTage:
##            i = 0
##            for used in self.countryholidays:
##                print("Here")
##                if day in used:
##                    print(day)
##                    print(self.internationaleTage.get(day))
            return self.internationaleTage.get(day)
##                i += 1

        else:
            return [], "Error"
        
    def printDays(self):
        for date, name in sorted(self.internationaleTage.items()):
            print(date, name)



def test():
    inter = internationalDays(2021)
    inter.baseGermanDays()
    inter.baseInternationalDays()
    inter.printDays()
    name = inter.getDay("2021-12-28")
    print(name)

if __name__ == "__main__":
    test()
