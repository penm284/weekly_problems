import string
import numpy as np

#arr stores keyboard characters
row1 = ["q","w","e","r","t","y","u","i","o","p"]
row2 = ["a","s","d","f","g","h","j","k","l"]
row3 = ["z","x","c","v","b","n","m",",","]

def shift_encrypt(character_index, shift, arr):
    #calculate total shift
    total_shift = int(character_index) + int(shift)
    #check boundaries of shift
    if total_shift  > len(arr)-1:
        #change shift value if total_shift is > len of arr
        total_shift = total_shift - len(arr)
    #retrieve new index
    shifted = arr[total_shift]
    return shifted





def shift_decyrpt(character_index, shift, arr):
    #find total shift
    total_shift = int(character_index) - int(shift)
    #check boundaries of shift
    if total_shift < 0:
        #if total_shift is < 0 adjust shift_val
        total_shift = total_shift + len(arr)
    #retrieve new index
    shifted = arr[total_shift]
    return shifted




    #clear the arr to store the output




    #convert the shift val into string

    #get shift values for each line from input
    #loop through each character


        #if character is space append to encrypted


        #keep track of which characters are upper and lower


        #retrieve key of special_characters arr from val
        #find character line and index

        #fix lower and upper






    #empty arr to store output




    #convert shit to str



    #retrieve shift_val


    #loop through each character

        #if character is space append to encrypted



        #keep track of upper or lower

                #obtain key of special_characters

        #find line, index, and then shift

            #fix lower and upper
