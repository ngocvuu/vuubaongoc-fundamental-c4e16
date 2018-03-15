teencode = {
    "hc" : "học",
    "ng": "người",
    "pt": "phải thêm",
    "eny": "em người yêu",
    "any": "anh người yêu"
}

while True:
    for key in teencode:
        print(key,end = "\t")
    print()
    print("*" * 30)


    your_code = input("Your code? ")

    if your_code in teencode:
        print("Code: ", your_code)
        print("Translation: ",teencode[your_code])

    else:
        contribute = input("Do you want to contribute this word? (Y/N)?").upper()
        if contribute == "Y":
            translation = input("Translation? ")
            teencode[your_code] = translation
            print("Updated")
        else:
            print("You're Done")
            break
