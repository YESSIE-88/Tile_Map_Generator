#Jessie Sellars

import random

#Looping until the user gives a valid input
while True:
    #Defining file_name as a string
    file_name = input("\nWhat do you want to name your data file: ")
    #Checking to see if the user did not give an empty string or just spaces and ending the loop
    if file_name != "" and not(file_name.isspace()):
        break
    print("Your input was not valid try again")

#Looping until the user gives a valid input
while True:
    #Defining tile_names as a list that we will use to store the file names of the images
    tile_names = input("\nGive me the name of the images with spaces in between: ")
    #Checking to see if the user did not give an empty string and ending the loop
    if tile_names != "":
        break
    print("Your input was not valid try again")

#Defining size as the width and heigh dimensions
size = [0, 0]
#Defining questions as strings width and height
question = ["width", "height"]
#Looping 2 times (for width and height)
for i in range(2):
    #Looping until a vlid input is given
    while True:
        #Using try incase an invalid input is given
        try:
            #Asking the user the dimension of the either the width or height and replacing it in the list
            size[i] = int(input(("\nGive me the " + question[i] + " of the tile map: ")))
            break
        #If it crashes tell the user his input did not work
        except:
            print("That was not a valid input")

#Creating a new file and making sure we are in append mode
file_hndl = open(file_name, "a")

#Adding the name of the image files to file_hndl
file_hndl.write(tile_names + "\n" + str(size[0]) +" " + str(size[1]) + "\n")

#Looping enough times to cover every row
for i in range(size[1]):
    #Looping enough times to cover every tile in the row
    for i in range(size[0]):
        #Defining tile_type as a random integer from 1 to 5
        tile_type = random.randint(1, 5)
        #20% of tile map will tiles other than the first so (1/5) probability
        if tile_type == 5:
            #Adding a random tile to file_hndl other than the first
            file_hndl.write(str(random.randint(1, (len(tile_names.split()) - 1))))
        #If its not a special tile add the first one to file_hndl
        else:
            file_hndl.write("0")
    #Going to the next line to move to the next row
    file_hndl.write("\n")

#Closing the file
file_hndl.close()
