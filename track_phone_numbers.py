import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+94701404652")
phone_number2 = phonenumbers.parse("+94763441171")
phone_number3 = phonenumbers.parse("+94716886067")
phone_number4 = phonenumbers.parse("+94712324082")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));
print(geocoder.description_for_number(phone_number3,"en"));
print(geocoder.description_for_number(phone_number4,"en"));

#LETS TRACK PHONE NUMBERS

