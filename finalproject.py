'''
    File name: finalproject.py
    @author: Oreoluwa Ogundipe
    Date created: 4/27/2017
    Date last modified: 5/8/2017
    
    This is the main file. It imports a CSV file and stores it as an array. 
    It then runs all the sorting methods, step by step, to answer our questions. 
    The results is written to an output file. 
'''

import pandas as pd
import homicide_class
from nonfirearms_class import Nonfirearms
from firearms_class import Firearms
from HomicideByCity import HomicideByCity
from sort_years import sort_years
from sort_by_rel import sort_by_rel
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
def main():
    location = 'homicide_reports.csv'
    outfile = 'results.txt'
    dataset = pd.read_csv(location, ',')
    ## next thing is to get the value based on labels
    dataset = dataset[['Record ID', 'City', 'State', 'Year', 'Crime Type', 'Crime Solved', 'Victim Sex', 'Victim Age', 'Victim Race', 'Perpetrator Sex', 'Perpetrator Age', 'Perpetrator Race', 'Relationship', 'Weapon', 'Victim Count', 'Perpetrator Count']].values
    ## now that we have what we need, the next thing is to make the Homicide class
    # next thing is to read all the records into a an array of Homicide classes
    i = 0
    homicide_array = [] # this will be list of Homicides objects based on the homicide class
    while i < len(dataset):
        homicide_array.append(homicide_class.Homicide(dataset[i,:]))
        i = i+1

    #  To sort Homicide by Cities
    hListByCity =  HomicideByCity(homicide_array)
    top10Cities = hListByCity.top10HomicideCities
    top10VictimCount = hListByCity.top10HomicideCitiesVictimCount
    top10Combined = hListByCity.top10HomicideCity_Vicitim
    top10PerpAgeGroups = hListByCity.CitybyPerpAge
    top10PerpSex = hListByCity.CitybyPerpSex
    
    f = open(outfile,"a")
    f.write('Top Ten U.S Cities for Homicides: \n')
    for i in (top10Cities):
        f.write(i)
        f.write("\n")
    f.write("\n")
 
    objects = (x for x in top10Cities)
    y_pos = np.arange(10)
    vic_counts =[]
    for i in range(len(top10Combined)):
        vic_counts.append(top10Combined[i][1])

    plt.bar(y_pos, vic_counts, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Victim Counts')
    plt.xlabel('Cities')
    plt.title('Plot of cities and victim counts')
    plt.savefig("vic_count.jpg")

    f.write('Top Ten U.S Cities for Homicides: Victim Count \n')
    for i in top10Combined:
        f.write(str(i)) 
        f.write("\n")
    f.write("\n")
    f.write('Top Ten U.S Cities for Homicides: Perpetrator Age Groups \n')
    for i in top10PerpAgeGroups:
        f.write(str(i)) 
        f.write("\n")
    f.write("\n")
    f.write('Top Ten U.S Cities for Homicides: Perpetrator Sex \n')
    for i in top10PerpSex:
        f.write(str(i)) 
        f.write("\n")
    f.write("\n")
    f.close()

    #  To sort the homicides by years
    sort_years(homicide_array,outfile)

    #  To sort the homicides by the use of firearms
    Firearms(homicide_array,outfile)
    Nonfirearms(homicide_array,outfile)

    #  Sorting the homicides by the relationships
    sort_by_rel(homicide_array,outfile)
main()