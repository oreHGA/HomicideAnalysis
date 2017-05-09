import pandas as pd
#  This is a class definition for the homicide class for analysis in this project
class Homicide:
    def __init__(self,singlerecord):
        self.id = singlerecord[0]
        self.city = singlerecord[1]
        self.state = singlerecord[2]
        self.year = singlerecord[3]
        self.crime_type = singlerecord[4]
        self.crime_solved = singlerecord[5]
        self.vic_sex = singlerecord[6]
        self.vic_age = singlerecord[7]
        self.vic_race = singlerecord[8]
        self.perp_sex = singlerecord[9] 
        self.perp_age = singlerecord[10]
        self.perp_race = singlerecord[11]
        self.relationship = singlerecord[12]
        self.Weapon = singlerecord[13]
        self.vic_count = singlerecord[14]
        self.perp_count = singlerecord[15]