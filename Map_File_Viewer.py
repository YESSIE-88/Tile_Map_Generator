#Jessie Sellars

import pygame

#Looping until the user gives a file that exists
while True:
    #Using try incase the given file does not exist
    try:
        file_name = input("\nGive me the name of the tile map file: ")
        #Opening the file in read mode
        file_hndl = open(file_name, "r")
        break
    except:
        print("That file does not exist")

#Defining lst_tile_files as a list of the file names for each tile image
lst_tile_files = (file_hndl.readline()).split()

#Looping for each image in
for i in range(len(lst_tile_files)):
    #Using try incase it crashes because the specified image does not exist
    try:
        pygame.image.load(lst_tile_files[i])
    #If it crashes print that the image specified does not exist and terminates the program
    except:
        print(f"The image file {lst_tile_files[i]} does not exist")
        exit()

#Defining size as a list with two items width and heigh
size = (file_hndl.readline()).split()

#Defining lst_tile_type as a list where we will store all the numbers of the data file
lst_tile_type = []
#Looping height times to visit each row
for i in range (int(size[1])):
    #Adding the row i to lst_tile_type
    lst_tile_type.append(file_hndl.readline())
    #Removing the unecessary characters ("\n")
    #lst_tile_type[i] = (lst_tile_type[i])[0:int(size[0])]

#Defining img as a pygame loaded image of the first item of lst_tile_files
img = pygame.image.load(lst_tile_files[0])
#Setting tile_size as the size of img (all tiles should be same dimentions
tile_size = img.get_size()
#Setting the display to be big enough to have the entire tile map
screen = pygame.display.set_mode((int(size[0]) * tile_size[0], int(size[1]) * tile_size[1]))

#Looping to visit each row
for i in range(int(size[1])):
    #Defining row as the curent row that is being visited
    row = lst_tile_type[i]
    #Looping to visit each columb of the row
    for j in range(int(size[0])):
        try:
            #Setting temp_img as as a pygame loaded image of the j item in the i row of lst_tile_files
            temp_img = pygame.image.load(lst_tile_files[int(row[j])])
        #If there is an error in the tile map instead use the default tile
        except:
            #Setting temp_img as a pygame loaded image of the first item of lst_tile_files
            temp_img = pygame.image.load(lst_tile_files[0])
        #Adding temp_img to the right i row in the map with the j columb
        screen.blit(temp_img, (j * tile_size[0], i * tile_size[1]))

#Updating the pygame window
pygame.display.update()

#Keeps the pygame window open until the user exits it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

#Closing the file
file_hndl.close()
