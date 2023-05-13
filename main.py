import os
import json
import faker
import datetime

from faker import Faker
from datetime import datetime

country_file = open("country_config.txt", "r")
dir_path = './SampleData/'
count = 0
country_list = []
People = []

class Person:

    def __init__(self, Name, Address, License_Plate, Iban, Favorite_Color, Company, Credit_Card):
        self.Name = Name
        self.Address = Address
        self.License_Plate = License_Plate
        self.Iban = Iban
        self.Favorite_Color = Favorite_Color
        self.Company = Company
        self.Credit_Card = Credit_Card

    def dump(self):
        return {"People":   {'Name': self.Name, 
                            'Address': self.Address,
                            'License_Plate': self.License_Plate,
                            'Iban': self.Iban,
                            'Favorite_Color': self.Favorite_Color,
                            'Company': self.Company,
                            'Credit_Card': self.Credit_Card}}

def generate_sample_data(sample_quantity):

    for line in country_file:

        if len(line.strip()) > 0:

            country_list.append(line.strip())

    f = Faker(country_list)

    while sample_quantity > -1:
        
        Name = f.name()
        Address = f.address()
        License_Plate = f.license_plate()
        Iban = f.iban()
        Favorite_Color = f.safe_color_name()
        Company = f.company()
        Credit_Card = f.credit_card_number()

        People.append(Person(Name, Address, License_Plate, Iban, Favorite_Color, Company, Credit_Card))

        sample_quantity -= 1
       
    jsonString = json.dumps([Person.dump() for Person in People])
    jsonFile = open('./SampleData/SP' + str(count).zfill(5) + '.json', "w")
    jsonFile.write(jsonString)
    jsonFile.close()

    logs_file = open("logs.txt", "a")
    logs_file.write('SP' + str(count).zfill(5) + '.json' + ' has been created at ' + str(datetime.now()) + '!\n')

for path in os.listdir(dir_path):

    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1

generate_sample_data(int(input('Enter the sample size: ')))