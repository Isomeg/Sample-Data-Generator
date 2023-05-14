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

    def __init__(self, Name, Date_of_Birth, Timezone, Country, Country_Code, City, Phone_Number, Address, Postal_code, Email, License_Plate, Currency_Name, Currency_Code, Currency_Symbol, Cryptocurrency_Name, Cryptocurrency_Code, Iban, Swift, Credit_Card, Credit_Card_Expire, Credit_Card_security_Code, Favorite_Color, Favorite_Emoji, Company, Job, Current_Location, Username, IPV4, IPV6):
        self.Name = Name
        self.Date_of_Birth = str(Date_of_Birth)
        self.Timezone = Timezone
        self.Country = Country
        self.Country_Code = Country_Code
        self.City = City
        self.Phone_Number = Phone_Number
        self.Address = Address
        self.Postal_code = Postal_code
        self.Email = Email
        self.License_Plate = License_Plate
        self.Currency_Name = Currency_Name
        self.Currency_Code = Currency_Code
        self.Currency_Symbol = Currency_Symbol
        self.Cryptocurrency_Name = Cryptocurrency_Name
        self.Cryptocurrency_Code = Cryptocurrency_Code
        self.Iban = Iban
        self.Swift = Swift
        self.Credit_Card = Credit_Card
        self.Credit_Card_Expire = Credit_Card_Expire
        self.Credit_Card_security_Code = Credit_Card_security_Code
        self.Favorite_Color = Favorite_Color
        self.Favorite_Emoji = Favorite_Emoji
        self.Company = Company
        self.Job = Job
        self.Current_Location = Current_Location
        self.Username = Username
        self.IPV4 = IPV4
        self.IPV6 = IPV6                                              

    def dump(self):
        return {"People":  {'Name': self.Name, 
                            'Date_of_Birth': self.Date_of_Birth,
                            'Timezone': self.Timezone,
                            'Country': self.Country,
                            'Country_Code': self.Country_Code,
                            'City': self.City,
                            'Phone_Number': self.Phone_Number,
                            'Address': self.Address,
                            'Postal_code': self.Postal_code,
                            'Email': self.Email,
                            'License_Plate': self.License_Plate,
                            'Currency_Name': self.Currency_Name,
                            'Currency_Code': self.Currency_Code,
                            'Currency_Symbol': self.Currency_Symbol,
                            'Cryptocurrency_Name': self.Cryptocurrency_Name,
                            'Cryptocurrency_Code': self.Cryptocurrency_Code,
                            'Iban': self.Iban,
                            'Swift': self.Swift,
                            'Credit_Card': self.Credit_Card,
                            'Credit_Card_Expire': self.Credit_Card_Expire,
                            'Credit_Card_security_Code': self.Credit_Card_security_Code,
                            'Favorite_Color': self.Favorite_Color,
                            'Favorite_Emoji': self.Favorite_Emoji,
                            'Company': self.Company,
                            'Job': self.Job,
                            'Current_Location': self.Current_Location,
                            'Username': self.Username,
                            'IPV4': self.IPV4,
                            'IPV6': self.IPV6}}

def generate_sample_data(sample_quantity):

    for line in country_file:

        if len(line.strip()) > 0:

            country_list.append(line.strip())

    f = Faker(country_list)

    while sample_quantity > -1:
        
        Name = f.name()
        Date_of_Birth = f.date_of_birth()
        Timezone = f.timezone()
        Country = f.country()
        Country_Code = f.country_code()
        City = f.city()
        Phone_Number = f.phone_number()
        Address = f.address()
        Postal_code = f.postcode()
        Email = f.ascii_free_email()
        License_Plate = f.license_plate()
        Currency_Name = f.currency_name() 
        Currency_Code = f.currency_code()
        Currency_Symbol = f.currency_symbol()
        Cryptocurrency_Name = f.cryptocurrency_name()
        Cryptocurrency_Code = f.cryptocurrency_code()
        Iban = f.iban()
        Swift = f.swift()
        Credit_Card = f.credit_card_number()
        Credit_Card_Expire = f.credit_card_expire()
        Credit_Card_security_Code = f.credit_card_security_code()
        Favorite_Color = f.safe_color_name()
        Favorite_Emoji = f.emoji()
        Company = f.company()
        Job = f.job()
        Current_Location = f.location_on_land()
        Username = f.user_name()
        IPV4 = f.ipv4()
        IPV6 = f.ipv6()                                                

        People.append(Person(Name, Date_of_Birth, Timezone, Country, Country_Code, City, Phone_Number, Address, Postal_code, Email, License_Plate, Currency_Name, Currency_Code, Currency_Symbol, Cryptocurrency_Name, Cryptocurrency_Code, Iban, Swift, Credit_Card, Credit_Card_Expire, Credit_Card_security_Code, Favorite_Color, Favorite_Emoji, Company, Job, Current_Location, Username, IPV4, IPV6))

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