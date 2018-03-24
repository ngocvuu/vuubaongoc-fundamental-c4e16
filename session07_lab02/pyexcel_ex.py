import pyexcel

a_list_of_dictionaries = [
    {
        "name": "Hung",
        "age": 89
    },
    {
        "name": "Nam",
        "age": 26
    }
]

pyexcel.save_as(records=a_list_of_dictionaries,
    dest_file_name="test.xlsx")
