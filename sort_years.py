# Finds the number of homicides for each year, and sorts the list in a descending order.
def sort_years(homicide_array,outfile):
    f = open(outfile,"a") 
    years = [[x, 0] for x in range(1980,2015)]
    # Count up homicides for each year.
    for homicide in homicide_array:
        for year in years:
            if homicide.year == year[0]:
                year[1] += 1
                break
    # Sort years based on the count, descending
    years.sort(key=lambda x: x[1], reverse=True)

    # Print years with most homicides. 

    f.write('Years with most homicides:\n')
    for x in range(5):
        f.write('[' + str(years[x][0]) + ', ' + str(years[x][1]) + ']\n')

    f.write('\n')
    f.write('Years with least homicides:\n')
    for x in range(len(years)-1, len(years)-6, -1) :
        f.write('[' + str(years[x][0]) + ', ' + str(years[x][1]) + ']\n')
   
	# Initialize years, will hold the homicide count of several years.
    year80s = 0
    year90s = 0
    year2000s = 0
    year2010s = 0
    for x in range(len(years)):
        if str(years[x][0]).startswith('198'):
            year80s += years[x][1]
        elif str(years[x][0]).startswith('199'):
            year90s += years[x][1]
        elif(str(years[x][0]).startswith('200')):
            year2000s += years[x][1]
        elif(str(years[x][0]).startswith('201')):
            year2010s += years[x][1]
    f.write('\n')
	# f.writeresult.
    f.write('Average homicides/year:\n')
    f.write('1980-1989: ' + str(year80s / 10) + '/year\n')
    f.write('1990-1999: ' + str(year90s / 10) + '/year\n')
    f.write('1999-2009: ' + str(year2000s / 10) + '/year\n')
    f.write('2009-2014: ' + str(year2010s / 5) + '/year\n')
    f.write("\n")
    f.close()