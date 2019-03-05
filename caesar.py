def caesar_cipher(string, shift):
#capital vs lowercase
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#possible shift
    num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)
#data structure to store
    dic1 = {}
    dic2 = {}
    dic3 = {}
    count = 1
#add 1 to index val
    for x in range(len(alpha)):
        dic1[x+1] = alpha[x]
    for y in alpha:
        dic2[y] = count
        count += 1
    for y in ALPHA:
        dic3[y] = count
        count += 1
# making the string into a list
    word = list(string)
#creating new arr
    new = []
#iterating through list
    for letter in word:
        if letter in alpha:
            new_pos = dic2[letter]
            new_pos += shift
            if new_pos > 26:
                new_pos -= 26
                new_letter = dic1[new_pos]
# add shifted letter to arr
                new.append(new_letter)
            else:
#if already in dic
                new_letter = dic1[new_pos]
                new.append(new_letter)
        elif letter in ALPHA:
            new_pos = dic3[letter]
            new_pos += shift
            if new_pos > 26:
                new_pos -= 26
                new_letter = dic1[new_pos]
                new.append(new_letter)
            else:
                new_letter = dic1[new_pos]
                new.append(new_letter)
        else:
            new.append(letter)
#join new arr
    print(''.join(new))
#call function
caesar_cipher("good job!", 1)




def decrypt(string, shift):
#list
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)
#new dic
    dic1 = {}
    dic2 = {}
    count = 1
    for x in range(len(alpha)):
        dic1[x+1] = alpha[x]
    for y in alpha:
        dic2[y] = count
        count += 1
#decrypt word new list
    word = list(string)
# new arr
    new = []
#shift input by 0-26 and find what that new index val is and store in new_letter
    for letter in word:
        if letter in alpha:
            new_pos = dic2[letter]
            new_pos -= shift
            if new_pos < 0:
                new_pos += 26
                new_letter = dic1[new_pos]
                new.append(new_letter)
            else:
                new_letter = dic1[new_pos]
                new.append(new_letter)
        else:
            new.append(letter)
#join new word
    print(''.join(new))
#call function
decrypt("hppe kpc!", 1)
