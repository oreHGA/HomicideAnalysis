 '''
    File name: homicide_year_sort.py
    Authors: Simen Davanger Wilberg, ...
    Date created: 4/30/2017
    Date last modified: 5/8/2017
    
    This is a class definition for the homicide class.
    An homicide instance is created for each row in the CSV file.
'''

def sort_years(self, homicide_array):
    years = [[x, 0] for x in range(1980,2017)]
    # didnt realise the cases was listen by year..
    for homicide in homicide_array:
        for year in years:
            if homicide.year == year[0]:
                year[1] += 1
                break
    years.sort(key=lambda x: x[1], reverse=True)

    print "Years with most homicides:"
    for x in range(5):
        print years[x]

    print "Years with least homicides:"
    for x in range(len(years)-1, len(years)-6, -1):
        print years[x]
