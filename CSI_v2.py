import json

with open("suspects_2.json", "r") as sus_json:
    suspects = json.loads(sus_json.read())

with open("characteristics.json", "r") as char_json:
    characteristics = json.loads(char_json.read())

with open("dna.txt", "r") as dna_data:
    dna = dna_data.read()

char_matched = 0

for suspect in suspects:
    for characteristic in characteristics.keys():
        char_value = suspects[suspect][characteristic].lower()
        char_dna = characteristics[characteristic][char_value]
        
        if dna.find(char_dna) != -1:
            char_matched += 1
        else:
            char_matched = 0
            break
    
    if char_matched == len(characteristics):
        print(suspect.title() + ' did it!!')
        break
