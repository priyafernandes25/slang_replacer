import csv
import re
import os

#print("Remember not to use any void character in continuation")
string_="DIY d0nt @sk m3 "
#Directory name
current_dir=os.path.dirname(os.path.realpath(__file__))
print(current_dir)

def translator(user_string):
    print("Input: ",string_)
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

print("Output after removing slangs: ",translator(string_))
