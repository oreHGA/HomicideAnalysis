import pandas as pd
import homicide_class

def main():
    location = 'homicide_reports.csv'
    dataset = pd.read_csv(location, ',')
    ## next thing is to get the value based on labels
    dataset = dataset[['Record ID', 'City', 'State', 'Year', 'Crime Type', 'Crime Solved', 'Victim Sex', 'Victim Age', 'Victim Race', 'Perpetrator Sex', 'Perpetrator Age', 'Perpetrator Race', 'Relationship', 'Weapon', 'Victim Count', 'Perpetrator Count']].values
    ## now that we have what we need, the next thing is to make the Homicide class
    # next thing is to read all the records into a an array of Homicide classes
    print len(dataset)
    i = 0
    homicide_array = [] # this will be list of Homicides objects based on the homicide class
    while i < len(dataset):
        homicide_array.append(homicide_class.Homicide(dataset[i,:]))
        i = i+1
    
    print homicide_array[0].relationship

main()