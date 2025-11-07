test_dict = {'ShampooBottle' : 8, 'Lipbalm': 4, 'Handcreme' : 4, 'Hairoil' : 7, 'NailFile' : 2, "Conditioner" : 9, "HairBrush": 4}

print("The original directory is", str(test_dict))

F = 9

res = 0
for key in test_dict:
    if test_dict[key]==F:
        res = res + 1

print("Frequency of F is:",  str(res))