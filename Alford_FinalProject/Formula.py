'''
Name: Mahaly Marcelin
email: marcelml@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: Final Project for this class!
Anything else that's relevant: hello
'''

from PIL import Image
import json 

'''
def location_finder(json_file):
    groups = open(json_file)
    groups = json.load(groups)
    alford = [x for x in groups["Alford"]]
    return print(alford)

print(location_finder("EncryptedGroupHints.json"))
'''


'''
def location_finder(team_name, json_file, txt_file):
    groups = open(json_file)
    groups = json.load(groups)
    indexes = [x for x in groups[team_name]]
    print(indexes) #this is temp cuz squigly line is annoying
    with open(txt_file, "rt") as english:
        english_list = [x for x in english]
    print(english_list) # temp as well for squigly line
    
    return 
'''

#function to locate the secret location
def location_finder(team_name, json_file, txt_file):
    # this opens json file, then turns into dictionary
    groups = open(json_file)
    groups = json.load(groups)
    
    # iterate & place into list; turn list of strings into those of integers
    indexes = [x for x in groups[team_name]]
    indexes = [int(x) for x in indexes]
    # print(indexes) #this is temp
    
    # turn text file into list. work cited: 
        #https://www.geeksforgeeks.org/how-to-read-text-file-into-list-in-python/   
    my_file = open(txt_file, "r")
    data = my_file.read()
    data_list = data.split("\n")
    my_file.close()
    #print(data_list) # temp as well
    
    
    # create new sublist of words using json indexes
    sub = list(map(data_list.__getitem__, indexes))
    
    #turn sublist into sentence! work cited:
        #https://tinyurl.com/3ypwz65h
    sentence = " ".join(sub)
    
    return print(sentence)


def load_pic(file_name):
    img = Image.open(file_name)
    img.show()
    return



