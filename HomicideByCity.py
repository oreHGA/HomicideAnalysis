# -*- coding: utf-8 -*-
"""
Created on Fri May  5 20:53:27 2017
@author: Connor Zablow 815560792 CS496 SDSU
"""
from operator import itemgetter

class HomicideByCity:

    CityHomicideList = []
    top10HomicideCities = []
    top10HomicideCitiesVictimCount = []
    top10HomicideCity_Vicitim = []
    CitybyPerpAge = []
    CitybyPerpSex = []
    
    def __init__(self, homicide_array):
        
        city_names = []
        #find only unique city names
        for homicide in homicide_array:
            if homicide.city not in city_names:
                city_names.append(homicide.city)
        
        #sort the list - alpha 
        city_names.sort()
        city_homicide_data = []
        city_dict = {}
        for i in range(len(city_names)):
            city_dict[city_names[i]] = 0

        
        for homicide in homicide_array:
            city_dict[homicide.city] +=  homicide.vic_count
        sorted_homicide_count = sorted(city_dict.items(), key=itemgetter(1), reverse=True)
        
        for x,y  in sorted_homicide_count:
            self.CityHomicideList.append([x,y])

        #sort the list by maximum homicides victim count
        self.top10HomicideCity_Vicitim = self.CityHomicideList[0:10]
        
        #extract top 10 cities and their victim count
        for x in range(0, 10):
            self.top10HomicideCities.append(self.CityHomicideList[x][0])
            self.top10HomicideCitiesVictimCount.append(self.CityHomicideList[x][1])
       
        #find age groups for each top U.S city
        for topCity in self.top10HomicideCities:
            group18 = 0
            group25 = 0
            group45 = 0
            groupOld = 0
            for homicide in homicide_array:
                if topCity == homicide.city:
                    age = int(homicide.perp_age)
                    if age < 18 and age > 5:
                        group18 = group18 + 1
                    elif age >= 18 and age < 26:
                        group25 = group25 + 1 
                    elif age >= 26 and age < 46:
                        group45 = group45 + 1
                    elif age >= 46:
                        groupOld = groupOld + 1
            self.CitybyPerpAge.append([topCity, {'0-17': group18, '18-25': group25, '26-45': group45, '46+': groupOld}])
       
        #find age groups for each top U.S city
        for topCity in self.top10HomicideCities:
            male = 0
            female = 0
            unknown = 0
            for homicide in homicide_array:
                if topCity == homicide.city:
                    sex = homicide.perp_sex
                    if sex == 'Male':
                        male = male + 1
                    elif sex == 'Female':
                        female = female + 1
                    elif sex == 'Unknown':
                        unknown = unknown + 1
            self.CitybyPerpSex.append([topCity, {'Male': male, 'Female': female, 'Unknown': unknown}])