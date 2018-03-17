string = "ThiS is String with Upper and lower case Letters"
string = string.lower()
string = string.replace(" ","")
#create an empty dictionary

frequency = {}

for letter in string:
    frequency[letter] = string.count(letter) #ham count pythonic

print(frequency)

#chuyen frequency thanh list de dung ham sort
list_frequency = list(frequency.items())

print(list_frequency)

#chuyen list_frequency thanh dict de chuan bi print
dict_frequency = dict(list_frequency)

for key in dict_frequency:
    print(key, dict_frequency[key])
