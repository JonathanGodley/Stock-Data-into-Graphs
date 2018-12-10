###  Programmer : Jonathan Godley
###  Date: 22 Mar 2015
###  This program reads a list of numbers from a file, calculates some statistics related to
###    those numbers, and then prints the results to the screen, using two different methods.
###
###  Note: Information on Standard Deviation Formulas & the Inspiration for how to lay it out in my 
###    programming came from the Math is Fun website, specifically the page located at 
###    https://www.mathsisfun.com/data/standard-deviation-formulas.html
###
###  Note: Information on error handling & a Basic guide on how to implement them came from Python.org, 
###    specifically https://docs.python.org/2/tutorial/errors.html although no code was directly copied
###    or used, it was an extremely valuable resource.

def calculateStatisticsFrom(filename):  
  
  fullPathName = getMediaPath(filename)    # Concatenates media path with file name to get the full path
  try:  
    file = open(fullPathName, "r")           # Opens the file at the end of the full path in read mode
    statData =[]                             # Initialises empty list
    statCount, statMean, statMax, statMin, statSD = 0,0,0,0,0   # initialises and declares several values as 0
    
    for line in file:                        # Loops through each line in the opened file, converting each 
      statData.append(float(line))           #   line into a floating point and inputting it into the list.
    file.close()                             # Closes file when it's no longer needed.
  
    # Max Calculation
    statMax = statData[0]                    # Sets the statMax value to the first value in the list so it can be compared
    for value in statData: 
      if value > statMax:                    # Compares each value in the list against statMax, either proceding to the next
        statMax = value                      #   value or declaring the new highest value as the new statMax 
  
    # Min Calculation - same as max but in reverse
    statMin = statData[0]
    for value in statData:
      if value < statMin:
        statMin = value
  
    # Mean Calculation
    for value in statData:
      statMean = statMean + value             # Adds each value together incrementally
      statCount += 1                          # Increments Count by 1 each loop
    statMean = statMean / statCount           # Divides the sum of the values by the number of values, resulting in Mean value.

    # Standard Dev. Calculation
    for value in statData:
      statSD += (value - statMean) ** 2            # For each number in list, subtract mean & square result, adding final result to total
    statSD = (statSD / (statCount - 1)) ** 0.5     # Find the mean of the new results and then square root the value obtained to get S.D.
   
  except (IOError, ValueError, IndexError):         # Catches invalid files, files without the proper data and empty files and returns an error
    showError("Invalid file or no file selected!")
  except (exception):                               # Catch-all for unexpected errors
    showError("Unexpected error occured!")
  else:   
    # Print Results
    print("Max = " + str(statMax))
    print("Min = " + str(statMin))
    print("Mean = " + str(round(statMean,4)) + " (4 d.p.)")               # round function used to round floating points
    print("Standard Deviation = " + str(round(statSD,4)) + " (4 d.p.)")   #   to four decimal places rather than truncating
  

def selectFileCalculateStatistics():
  try: 
    filename = pickAFile()
    file = open(filename, "r")           # Opens the file at the end of the full path in read mode
    statData =[]                             # Initialises empty list
    statCount, statMean, statMax, statMin, statSD = 0,0,0,0,0   # initialises and declares several values as 0
  
    for line in file:                        # Loops through each line in the opened file, converting each 
      statData.append(float(line))           #   line into a floating point and inputting it into the list.
    file.close()                             # Closes file when it's no longer needed.
  
    # Max Calculation
    statMax = statData[0]                    # Sets the statMax value to the first value in the list so it can be compared
    for value in statData: 
      if value > statMax:                    # Compares each value in the list against statMax, either proceding to the next
        statMax = value                      #   value or declaring the new highest value as the new statMax 
  
    # Min Calculation - same as max but in reverse
    statMin = statData[0]
    for value in statData:
      if value < statMin:
        statMin = value
  
    # Mean Calculation
    for value in statData:
      statMean = statMean + value             # Adds each value together incrementally
      statCount += 1                          # Increments Count by 1 each loop
    statMean = statMean / statCount           # Divides the sum of the values by the number of values, resulting in Mean value.

    # Standard Dev. Calculation
    for value in statData:
      statSD += (value - statMean) ** 2            # For each number in list, subtract mean & square result, adding final result to total
    statSD = (statSD / (statCount - 1)) ** 0.5     # Find the mean of the new results and then square root the value obtained to get S.D.
  
  except (IOError, ValueError, IndexError):         # Catches invalid files, files without the proper data and empty files and returns an error
    showError("Invalid file or no file selected!")
  except (exception):                               # Catch-all for unexpected errors
    showError("Unexpected error occured!")
  else:  
    # Print Results in a message box, by concatenating strings and newline symbols to split the results across multiple lines in the msg box
    showInformation("Max = " + str(statMax) + "\n" + "Min = " + str(statMin) + 
      "\n" + "Mean = " + str(round(statMean,4)) + " (4 d.p.)" + "\n" + "Standard Deviation = " + str(round(statSD,4)) + " (4 d.p.)")
    
    
    
