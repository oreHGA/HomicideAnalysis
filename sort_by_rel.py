def  sort_by_rel(homicide_array, outputLoc):
    myfile = open(outputLoc, "a")
    # list of relationship types
    relationshipList = ['Acquaintance', 'Unknown', 'Wife', 'Stranger', 'Girlfriend', 'Ex-Husband',
                        'Brother', 'Stepdaughter', 'Husband', 'Sister', 'Friend', 'Family', 'Neighbor', 'Father',
                        'In-Law', 'Son',
                        'Ex-Wife', 'Boyfriend', 'Mother', 'Common-Law Husband', 'Common-Law Wife', 'Stepfather',
                        'Stepmother',
                        'Daughter', 'Boyfriend/Girlfriend', 'Employer', 'Employee']
    # create an array to track the number of times each relationship occurs
    relationship = [[x, 0] for x in relationshipList]
    # two for each loops to increase the count for each occurance of a specific relationship
    for homicide in homicide_array:
        for relations in relationship:
            if homicide.relationship == relations[0]:
                relations[1] += 1
    # sort the list by the count variable
    relationship.sort(key=lambda x: x[1], reverse=True)
    # print the top five relationships for the perpatrator
    myfile.write("Top 5 relationships between the victim and perpatrator\n")
    for x in range(5):
        myfile.write(str(relationship[x])+"\n")
    myfile.close()