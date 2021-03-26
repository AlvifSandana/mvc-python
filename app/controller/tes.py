"""
Module: tes.py

Created by alvif@usagi 
at 26/03/21
"""

def input(data):
    input_data = {}
    tmp = data.split('&')
    for x in tmp:
        input_data[x.split('=')[0]] = x.split('=')[1]
    print(tmp[2].split('=')[1])
    print(input_data)

input('nim=1119&nama=alvif&angkatan=2019')
