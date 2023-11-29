import json

with open("suspects_2.json", "r") as sus_json:
    suspects = json.loads(sus_json.read())

with open("characteristics.json", "r") as char_json:
    characteristics = json.loads(char_json.read())

with open("dna.txt", "r") as dna_data:
    dna = dna_data.read()

for suspect in suspects:
    condition_gender = False
    condition_hair  = False
    condition_eye_color = False
    condition_race  = False
    condition_facial_shape = False

    sus_name = suspect["name"]
    
    # Gender
    sus_gender = suspect["gender"].lower()
    sus_gender_dna = characteristics["gender"][sus_gender]
    
    if dna.find(sus_gender_dna) != -1:
        condition_gender = True

    # Hair
    sus_hair = suspect["hair"].lower()
    sus_hair_dna = characteristics["hair"][sus_hair]
    
    if dna.find(sus_hair_dna) != -1:
        condition_hair = True

    # Eye
    sus_eye_color = suspect["eye_color"].lower()
    sus_eye_color_dna = characteristics["eye_color"][sus_eye_color]
    
    if dna.find(sus_eye_color_dna) != -1:
        condition_eye_color = True

    # Race
    sus_race = suspect["race"].lower()
    sus_race_dna = characteristics["race"][sus_race]
    
    if dna.find(sus_race_dna) != -1:
        condition_race = True
    
    # facial_shape
    sus_facial_shape = suspect["facial_shape"].lower()
    sus_facial_shape_dna = characteristics["facial_shape"][sus_facial_shape]
    
    if dna.find(sus_facial_shape_dna) != -1:
        condition_facial_shape = True
    
    if condition_gender and condition_hair and condition_eye_color and condition_race and condition_facial_shape:
        print(sus_name.upper() + ' did it!!')