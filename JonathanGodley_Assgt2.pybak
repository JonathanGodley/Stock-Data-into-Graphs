###  Programmer : Jonathan Godley - c3188072
###  Date: 18 May 2015
###  This program reads stock market data from a file and draws plots related to the data,
###  saving the plots as jpeg image files
###
###  Note: Information on the variables involved in the string.split() function was obtained from 
###    https://docs.python.org/2/library/stdtypes.html & although no code was directly copied
###    or used, it was an extremely valuable resource.

def showVolumeChart(sizeOption):
  
  ### -Init & Declare Variables- ###
  # Initialises empty lists 
  dataDate =[]                                
  dataVolume =[] 
  # Initialises and declares several values as 0
  count, chartWidth, chartHeight, lineDiff, lineHeight = 0,0,0,0,0	
  labelPosition, labelDiff, yValue, yMax, yMin, yDiff = 0,0,0,0,0,0    
  barHeight, barWidth, barPosition = 0,0,0
  # Initialises empty string
  tempLine = ""
  # Sets Initial Bar Colour
  barColour = blue

   

 
  try: 
    filename = pickAFile()		     # Prompts the user to pick a file
    file = open(filename, "r")        	     # Opens the file at the end of the full path in read mode
    

    ### -Set Width & Height of Graph- ###
    if sizeOption == 1:	  #Setting the ChartWidth using the parameter provided
      chartWidth = 600
    elif sizeOption == 2:
      chartWidth = 700
    elif sizeOption == 3:
      chartWidth = 800
    elif sizeOption != 1 or sizeOption != 2 or sizeOption != 3:       # If no or an Invalid parameter is entered
      chartWidth = 700				        #    then set to medium as a Default
      showError("Invalid Size Option Input!\nDefaulting to Medium Size.")
    
    # Obtain the chart height from selected chartWidth   
    chartHeight = int(chartWidth * 0.75)    
    
    ### -Retrieve Data from file- ###
    
    for line in file:                   # Loops through each line in the opened file, converting each 
      if count != 0:                    # Skips the first header line as it's unnesscesary in this instance
        tempLine = line.split(",")               # Splits the line every "," and puts the result in "tempLine"
        dataDate.append(tempLine[0])             # Appends the split data into appropriate lists
        dataVolume.append(float(tempLine[5]))
      count += 1
    file.close()                             # Closes file when it's no longer needed.

    ### -Draw Empty Picture- ###
    volChartPicture = makeEmptyPicture(chartWidth, chartHeight)
    
    ### -Labels- ###
    addText(volChartPicture, int(chartWidth*0.01), int(chartHeight*0.5), "Volume", darkGray)
    # Write Filename at Bottom of Picture, snipping file extension and anything preceding the name of the file, 
    #     assuming filenames stick to the format "StockDataXXX.csv"
    addText(volChartPicture, int(chartWidth*0.5), int(chartHeight*0.98), filename[-16:-4], darkGray)
    
    # Dynamically sets initial position of date labels & works out the distance needed between them. 
    labelPosition = chartWidth * 0.15
    labelDiff = ((chartWidth - chartWidth * 0.15))/10
    
    for date in dataDate:
      addText(volChartPicture, int(labelPosition), int(chartHeight*0.94), date[:-3], darkGray) #places the date text & cuts the year from the string
      labelPosition = labelPosition + labelDiff
    
    
    
    ### -Horizontal Lines + Y Axis Labels- ###
    lineHeight = chartHeight*0.90    # Sets position of first line
    lineDiff = ((chartHeight*0.90 - chartHeight*0.04))/10 # Determines dist. between lines 
    
    # Find Max value so Y values can be populated
    yMax = dataVolume[0]
    for value in dataVolume: 
      if value > yMax:
        yMax = value  
    
    yDiff = yMax / 10  # Determines the dynamic difference between the Y Values
    
    #Loops through to draw the Y Labels and Horizontal Lines       
    for x in range(0, 11):
      addLine(volChartPicture, int(chartWidth * 0.12), int(lineHeight), int(chartWidth * 0.98), int(lineHeight), gray) 
      addText(volChartPicture, int(chartWidth * 0.09), int(lineHeight), ('%.2f' % yValue), darkGray)
      lineHeight = lineHeight - lineDiff
      yValue = yValue + yDiff
    
    ### -Columns- ###
    
    #Dynamically set initial bar Width
    barWidth = (chartWidth - (chartWidth * 0.15))/15
        
    #Set Initial Position
    barPosition = (chartWidth * 0.15)
    
    #Find yMin so Graph can be properly coloured
    yMin = dataVolume[0]
    for value in dataVolume:
      if value < yMin:
        yMin = value
    
    
    #draw Columns
    for x in range(0, 10):
      if dataVolume[x] == yMax: #If largest value, bar colour is red
        barColour = red
      elif dataVolume[x] == yMin: #If smallest value, bar colour is green
        barColour = green
      #Sets Bar Height dynamically, depending on available space and range of values
      barHeight = (dataVolume[x]/yMax)*((chartHeight*0.90) - (chartHeight*0.04))
      addRectFilled(volChartPicture, int(barPosition), int((chartHeight*0.90)-int(barHeight)), int(barWidth), int(barHeight), barColour)
      barPosition += labelDiff
      barColour = blue #Resets Bar Colour back to blue, in case it was changed in the IF statement
 
  except (IOError, ValueError, IndexError):         # Catches invalid files, files without the proper data and empty files and returns an error
    showError("Invalid file or no file selected!")
  except (exception):                               # Catch-all for unexpected errors
    showError("Unexpected error occurred!")
  else:  
    show(volChartPicture)                           # If there aren't any errors, show completed Graph

def drawCandlestickChart(inputDataFile, outputImageName, sizeOption):

  ### -Init & Declare Variables- ###
  # Initialises empty lists 
  dataDate =[]
  dataOpenPrice =[]
  dataHighPrice =[]
  dataLowPrice =[]
  dataClosePrice =[]                        
  dataVolume =[] 
  # Initialises and declares several values as 0
  count, chartWidth, chartHeight, lineDiff, lineHeight = 0,0,0,0,0	
  labelPosition, labelDiff, yValue, yMaxHigh, yMinLow, yDiff = 0,0,0,0,0,0    
  barHeight, barTop, barWidth, barPosition = 0,0,0,0
  wickX, wickY1, wickY2 = 0,0,0
  # Initialises empty string
  tempLine = ""
  # Sets Initial Bar Colour
  barColour = white
  wickColour = black
  
  fullPathName = getMediaPath(inputDataFile)    # Concatenates media path with file name to get the full path
    
  try:
    ### -Retrieve Data from file- ###  
    
    file = open(fullPathName, "r")           # Opens the file at the end of the full path in read mode
    
    for line in file:                            # Loops through each line in the opened file, converting each 
      if count != 0:                             # Skips the first header line as it's unnesscesary in this instance
        tempLine = line.split(",")               # Splits the line every "," and puts the result in "tempLine"
        dataDate.append(tempLine[0])             # Appends the split data into appropriate lists
        dataOpenPrice.append(float(tempLine[1]))
        dataHighPrice.append(float(tempLine[2]))
        dataLowPrice.append(float(tempLine[3]))
        dataClosePrice.append(float(tempLine[4]))               
        dataVolume.append(float(tempLine[5]))
      count += 1
    file.close()                             # Closes file when it's no longer needed.
    
    ### -Set Width & Height of Graph- ###
    if sizeOption == 1:	  #Setting the ChartWidth using the parameter provided
      chartWidth = 600
    elif sizeOption == 2:
      chartWidth = 700
    elif sizeOption == 3:
      chartWidth = 800
    elif sizeOption != 1 or sizeOption != 2 or sizeOption != 3:       # If no or an Invalid parameter is entered
      chartWidth = 700				        #    then set to medium as a Default
      showError("Invalid Size Option Input!\nDefaulting to Medium Size.")
    
    # Obtain the chart height from selected chartWidth   
    chartHeight = int(chartWidth * 0.75)   

    ### -Draw Empty Picture- ###
    csChartPicture = makeEmptyPicture(chartWidth, chartHeight)
  
    ### -Labels- ###
    addText(csChartPicture, int(chartWidth*0.01), int(chartHeight*0.5), "Price ($)", darkGray)
    # Write Filename at Bottom of Picture, snipping file extension and anything preceding the name of the file, 
    #     assuming filenames stick to the format "StockDataXXX.csv"
    addText(csChartPicture, int(chartWidth*0.5), int(chartHeight*0.98), inputDataFile[:-4], darkGray)
    
    # Dynamically sets initial position of date labels & works out the distance needed between them. 
    labelPosition = chartWidth * 0.15
    labelDiff = ((chartWidth - chartWidth * 0.15))/10
    
    for date in dataDate:
      addText(csChartPicture, int(labelPosition), int(chartHeight*0.94), date[:-3], darkGray) #places the date text & cuts the year from the string
      labelPosition = labelPosition + labelDiff
  
    ### -Horizontal Lines + Y Axis Labels- ###
    lineHeight = chartHeight*0.90    # Sets position of first line
    lineDiff = ((chartHeight*0.90 - chartHeight*0.04))/10 # Determines dist. between lines 
    
    # Find Highest High value so Y values can be populated
    yMaxHigh = dataHighPrice[0]
    for value in dataHighPrice: 
      if value > yMaxHigh:
        yMaxHigh = value  
    
    #Find Lowest Low value
    yMinLow = dataLowPrice[0]
    for value in dataLowPrice:
      if value < yMinLow:
        yMinLow = value
    
    # Determines the dynamic difference between the Y Values
       
    yDiff = (yMaxHigh - yMinLow) / 10  
    yValue = yMinLow
    
    #Loops through to draw the Y Labels and Horizontal Lines       
    for x in range(0, 11):
      addLine(csChartPicture, int(chartWidth * 0.12), int(lineHeight), int(chartWidth * 0.98), int(lineHeight), gray) 
      addText(csChartPicture, int(chartWidth * 0.09), int(lineHeight), ('%.2f' % yValue), darkGray)
      lineHeight = lineHeight - lineDiff
      yValue = yValue + yDiff
    
    

    ### -Columns And Lines- ###
    
    #Dynamically set initial bar Width
    barWidth = (chartWidth - (chartWidth * 0.15))/15
        
    #Set Initial Position
    barPosition = (chartWidth * 0.15)  
  
    

    #Draw Lines
    for x in range(0,10):
      wickX = barPosition + (labelDiff * x) + (0.5* barWidth) # Sets the x position to the same as the label + 1/2 column width
      
      # ((dataHighPrice[x]-yMinLow)/(yMaxHigh - yMinLow)) makes the number easier to process & works out what area of the graph
      #   that the value belongs to in the form of a percentage, which when multiplied by ((chartHeight*0.90) - (chartHeight*0.04)) 
      #   scales it to the available area put aside for the graph and when called with int(chartHeight*0.90)-int(wickY1) assigns it 
      #   correct y value
      
      wickY1 = ((dataHighPrice[x]-yMinLow)/(yMaxHigh - yMinLow))*((chartHeight*0.90) - (chartHeight*0.04))
      wickY2 = ((dataLowPrice[x]-yMinLow)/(yMaxHigh - yMinLow))*((chartHeight*0.90) - (chartHeight*0.04))
      
      addLine(csChartPicture, int(wickX), int(chartHeight*0.90)-int(wickY1), int(wickX), int(chartHeight*0.90)-int(wickY2), wickColour)
    
    #Draw Columns
    # ((dataClosePrice[x]-yMinLow)/(yMaxHigh - yMinLow)) makes the number easier to process & works out what area of the graph
    #   that the value belongs to in the form of a percentage, which when multiplied by ((chartHeight*0.90) - (chartHeight*0.04)) 
    #   scales it to the available area put aside for the graph and when called with int(chartHeight*0.90)-int(wickY1) assigns it 
    #   correct y value
    #
    # barHeight = barTop-((dataOpenPrice[x]-yMinLow)/(yMaxHigh - yMinLow))*((chartHeight*0.90) - (chartHeight*0.04))
    #   very similar to barTop= it works out the coordinate for the y Axis but in this instance for the bottom of the column.
    #   it then subtracts the barTop integer to leave it with the difference between them that can be used as a distance/length variable 
    
    for x in range(0,10):
      barTop =((dataClosePrice[x]-yMinLow)/(yMaxHigh - yMinLow))*((chartHeight*0.90) - (chartHeight*0.04))
      barHeight = barTop-((dataOpenPrice[x]-yMinLow)/(yMaxHigh - yMinLow))*((chartHeight*0.90) - (chartHeight*0.04))       
      if dataClosePrice[x] <= dataOpenPrice[x]:  #sets to black and reverses Open & Close Prices
        barColour = black
        barTop = ((dataOpenPrice[x]-yMinLow)/(yMaxHigh - yMinLow))*((chartHeight*0.90) - (chartHeight*0.04))
        barHeight = barTop-((dataClosePrice[x]-yMinLow)/(yMaxHigh - yMinLow))*((chartHeight*0.90) - (chartHeight*0.04)) 
      if barHeight <= 1:
        barHeight = 1 # Ensures that a candle is drawn even if it has no/little movement 
      addRectFilled(csChartPicture, int(barPosition), int(chartHeight*0.90)-int(barTop), int(barWidth), int(barHeight), barColour)
      # a second unfilled rectangle is drawn so that the white filled rectangles have a black outline, making them more visible.
      addRect(csChartPicture, int(barPosition), int(chartHeight*0.90)-int(barTop), int(barWidth), int(barHeight), black)
      barPosition += labelDiff
      barColour = white #Resets Bar Colour back to white, in case it was changed in the IF statement

   
  except (IOError, ValueError, IndexError):         # Catches invalid files, files without the proper data and empty files and returns an error
    showError("Invalid file or no file selected!")
  except (exception):                               # Catch-all for unexpected errors
    showError("Unexpected error occurred!")
  else:  
    show(csChartPicture)                           # If there aren't any errors, show completed Graph
    writePictureTo(csChartPicture, outputImageName) # Saves image to the media path with the filename & extension entered as a paremeter