#Program to find out the information of any Phone Number
#by Krish Lalwani

#Importing needed libraries and Modules
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

#Heading
print ("------------PHONE NUMBER INFOMATION FINDER-------------")

#Taking the number as input from the user.
p_number = input("Enter the Phone number with Country Code:\n")

#Parsing the Phone Number
phone = phonenumbers.parse(p_number)

#Getting the Infomation of the Phone Number
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, 'en')
region = geocoder.description_for_number(phone, 'en')
valid = phonenumbers.is_valid_number(phone)
international = phonenumbers.can_be_internationally_dialled(phone)

#Showing the Details
print("The details of Phone Number " , phone, "is:")
print("Time is ", time)
print("Carrier is ", car)
print("Region is", region)
print("Is Number Active: ", valid)
print("Can receive International calls:", international)
print("\n\n\nProgram authored by Krish Lalwani...")


#End of Program...