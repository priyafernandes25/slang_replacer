import csv
import re
import os

#print("Remember not to use any void character in continuation")
string_="#i h0w r u? i w@s f9 b4 we m3t"
print("Input: ",string_)
#string_="#*&&"
#Directory name
current_dir=os.path.dirname(__file__)
#TO CHECK TEXT ENCRYPTION
#alphabets = digits = special =c= 0
c=1
def encryption(string_):
    alphabets = digits = special =c= 0
    for i in range(len(string_)):
        if(string_[i].isalpha()):
            alphabets = alphabets + 1
        elif(string_[i].isdigit()):
            digits = digits + 1
        else:
            special = special + 1
    #print("\nTotal Number of Alphabets in this String :  ", alphabets)
    #print("Total Number of Digits in this String :  ", digits)
    #print("Total Number of Special Characters in this String :  ", special)
    #print("Total length of String is: ",len(string_));
    if(special<=0.50*len(string_)):
       # print("The text is not encrypted")
        c=1 #flag made 1
        
    else:
        print("The text is encrypted")
        c=0
        return
    return c
l=encryption(string_);
if(l==1): # remaining functions will work only if text is not encrypted   
    def translator(user_string):
        
        #user_string=replacer(user_str)
        user_string = user_string.split(" ")
        j = 0
        for _str in user_string:
            # File path which consists of Abbreviations.
            fileName=os.path.join(current_dir,"slangdict.txt")
            # File Access mode [Read Mode]
            accessMode = "r"
            with open(fileName, accessMode) as myCSVfile:
                # Reading file as CSV with delimiter as "=", so that abbreviation are stored in row[0] and phrases in row[1]
                dataFromFile = csv.reader(myCSVfile, delimiter="=")
                # Removing Special Characters.
                _str = re.sub('[^a-zA-Z0-9-_.]', '', _str)
                for row in dataFromFile:
                    # Check if selected word matches short forms[LHS] in text file.
                    if _str.upper() == row[0]:
                        # If match found replace it with its appropriate phrase in text file.
                        user_string[j] = row[1]
                myCSVfile.close()
            j = j + 1
        # Replacing commas with spaces for final output.
        final_string=(' '.join(user_string))
        return final_string

    def replacer(check_string):
        
        final_string=encryption(check_string)
        final_string=translator(check_string)
        fileName=os.path.join(current_dir,"replacedict.txt")
        # File Access mode [Read Mode]
        accessMode = "r"
        user_string=""
        for i in range(len(final_string)):
            x= final_string[i]
            with open(fileName, accessMode) as myCSVfile:
                #print(x)
                # Reading file as CSV with delimiter as "=", so that abbreviation are stored in row[0] and phrases in row[1]
                dataFromFile = csv.reader(myCSVfile, delimiter="=")
                for row in dataFromFile:
                    #print(row[0])
                    # Check if selected word matches short forms[LHS] in text file.
                    if x == row[0]:
                        #print(row[1])
                        # If match found replace it with its appropriate phrase in text file.
                        x = row[1]
                user_string=''.join((user_string,x));
            myCSVfile.close()
        # Replacing commas with spaces for final output.
        return user_string
    #to check whether the text is encrypted or not

      
   
    
if(l==1):#only if not encrypted print
    print("Output after removing slangs: ",replacer(string_))
