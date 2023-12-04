import json

with open("suspects_2.json", "r") as sus_json:
    suspects = json.loads(sus_json.read())

with open("characteristics.json", "r") as char_json:
    characteristics = json.loads(char_json.read())

with open("dna.txt", "r") as dna_data:
    dna = dna_data.read()

for suspect in suspects:
    char_matched = 0
    for characteristic in characteristics:
        char_value = suspects[suspect][characteristic].lower()
        char_dna = characteristics[characteristic][char_value]
        
        if dna.find(char_dna) != -1:
            char_matched += 1
        else:
            break
    
    if char_matched == len(characteristics):
        print(suspect.title() + ' did it!!')
        break
