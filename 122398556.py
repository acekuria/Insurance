print("The Best In State Car Rental")
print()

#Enter Full name (Max length = 30 characters)
while True:
    name = input("Full name: ")
    if len(name) >= 30:
        print("Enter a maxmimum of 30 characters.")
        continue
    else:
        break

#Enter Street Address (Max lenth = 50 characters)
while True:
    address = input("Street Address: ")
    if len(address) > 50:
        print("Enter a maximum of 50 characters")
        continue
    else:
        break

#Enter Town/City (Max length = 20 characters)
while True:
    town = input("Town/City: ")
    if len(town) > 20:
        print("Enter a maxmimum of 20 characters.")
        continue
    else:
        break

#Enter County (Max length = 10 characters)
while True:
    county = input("County: ")
    if len(county) > 10:
        print("Enter a maxmimum of 10 characters.")
        continue
    else:
        break

#Enter Phone Number (Exactly 10 characters)
while True:
    phone = input("Contact Telephone Number: +353 ")
    if len(phone) > 10:
        print("Your phone number should be 10 digits long. Please try again.")
        continue
    else:
        break

#Enter Passport Number (Exactly 8 characters)
while True:
    passport = input("Passport Number: ")
    if len(passport) > 8 or len(passport) < 8:
        print("Enter 7 numbers followed by one letter")
        continue
    else:
        break

#Choose payment type (Either Mastercard or Visa)
while True:
    payment_type = str(input("Selection of Payment Type (Mastercard/Visa):"))
    payment_type = payment_type.lower()
    if payment_type == "mastercard" or payment_type == "visa":
        break
    else:
        print("We only accept Mastercard or Visa. Please Try again")
        continue

#Enter credit/debit card number (Max length = 8 numbers)
#Enter Expiry date
credit_num = input("Credit/Debit Card Number: ")
if len(credit_num) > 8:
    print("Please enter exactly 8 numeric characters.")
expm = input ("Enter month of expiry date: ")
expy = input ("Enter year of expiry date: ")
print(f'Expiry date: {expm}/{expy}')

#Table 1: Types of Vehicles
print("-------------------------------------------------------------------------------------")
print("\t                      Vehicle Type                    ")
print("-------------------------------------------------------------------------------------")

print("\t                          Car                  ")
print("\t                          Van                                  ")
print("-------------------------------------------------------------------------------------")


def car ():
    print("-------------------------------------------------------------------------------------------------")
    print("Car Model                            \t     Daily Rate     Weekly Rate     Fortnightly Rate ")
    print("                                     \t       (in €)         (in €)           (in €)     ")
    print("-------------------------------------------------------------------------------------------------")
    print("1. VW Polo 1.0 Litre (or equivalent)    \t   37.50	       236.25	        448.90")
    print("2. Opel Corsa 1.2 Litre (or equivalent)	\t   43.25	       272.48	        517.70")
    print("3. Renault Megane 1.4 Litre            	\t   49.70	       313.11	        594.91")
    print("or equivalent")
    print("4. Ford Mondeo 1.6 Litre (or equivalent)\t   55.30	       348.39	        661.95")
    print("5. Opel Zafira 8-Seater 2.0 Litre	    \t   63.15	       397.85           755.92")
    print("or equivalent")
    print("-------------------------------------------------------------------------------------------------")

#Table 2: Cars available for rental including rates
def van ():
    print("-------------------------------------------------------------------------------------------------")
    print("Van Model	                   \t     Daily Rate	    Weekly Rate     Fortnightly Rate")
    print("                                \t    (in €)         (in €)           (in €)     ")
    print("-------------------------------------------------------------------------------------------------")
    print("1. Opel Corsa Van                  \t   	 35.10	       221.13	        420.15")
    print("2. Toyota Hiace                    \t     39.90	       251.37	        477.60")
    print("3. Ford Transit	                   \t     65.40	       412.02	        782.84")
    print("4. Ford Transit Minibus (26-seater)\t     68.90	       434.07	        824.73")
    print("5. Mercedes Runner	               \t     89.60	       564.48	        1072.51")
    print("6. Nissan Patrol 4x4 	           \t     78.80	       496.44	        943.24")
    print("-------------------------------------------------------------------------------------------------")

#Calculation for rates of cars and vans
def rate_calculation(dr, wr, fr):
    sum = 0
    rent_length = int(input("How many days do you want to rent the model for?: "))
    while rent_length >= 14:
        rent_length = rent_length - 14
        sum = sum+ fr
    while rent_length >= 7:
        rent_length = rent_length - 7
        sum = sum + wr
    while rent_length >= 1:
        rent_length = rent_length - 1
        sum = sum + dr
    return sum

while True:
    option = str(input("Enter Car or Van to see the expenses of your chosen vehicle: "))
    option = option.lower()
    if option == "car":
        car()

        while True:
            car_choice = int(input("Please enter the number next to the model next to the car model you would like to buy: "))
            if car_choice == 1:
                vehicle_total = rate_calculation(37.50, 236.25, 448.9)
                vehicle_total = round(vehicle_total, 2)

                print("Cost of this service excluding VAT(23%):", vehicle_total)

                break
            elif car_choice == 2:
                vehicle_total = rate_calculation(43.25, 272.48, 517.70)
                vehicle_total = round(vehicle_total, 2)

                print("Cost of this service excluding VAT(23%):", vehicle_total)
                break
            elif car_choice == 3:
                vehicle_total = rate_calculation(49.7, 313.11, 594.91)
                vehicle_total = round(vehicle_total, 2)

                print("Cost of this service excluding VAT(23%):", vehicle_total)
                break
            elif car_choice == 4:
                vehicle_total = rate_calculation(55.3, 348.39, 661.95)
                vehicle_total = round(vehicle_total, 2)

                print("Cost of this service excluding VAT(23%):", vehicle_total)
                break
            elif car_choice == 5:
                vehicle_total = rate_calculation(63.15, 397.85, 755.92)
                vehicle_total = round(vehicle_total, 2)

                print("Cost of this service excluding VAT(23%):", vehicle_total)

                break
            else:
                print("Please choose the appropriate car model numbers")
                print()
                continue

        break
    elif option == "van":
        van()
        while True:
            van_choice = int(input("Please enter the number next to the model next to the car model you would like to buy: "))
            if van_choice == 1:
                vehicle_total = rate_calculation(35.10, 221.13, 420.15)
                vehicle_total = round(vehicle_total, 2)

                print("Cost of this service excluding VAT(23%):", vehicle_total)

                break
            elif van_choice == 2:
                vehicle_total = rate_calculation(39.90, 251.37, 477.60)
                vehicle_total = round(vehicle_total, 2)

                print("Cost of this service excluding VAT(23%):", vehicle_total)
                break
            elif van_choice == 3:
                vehicle_total = rate_calculation(65.40, 412.02, 782.84)
                vehicle_total = round(vehicle_total, 2)

                print("Cost of this service excluding VAT(23%):", vehicle_total)

                break
            elif van_choice == 4:
                vehicle_total = rate_calculation(68.90, 434.07, 824.73)
                vehicle_total = round(vehicle_total, 2)

                print("Cost of this service excluding VAT(23%):", vehicle_total)
                break
            elif van_choice == 5:
                vehicle_total = rate_calculation(89.60, 564.48, 1072.51)
                vehicle_total = round(vehicle_total, 2)
                print("Cost of this service excluding VAT(23%):", vehicle_total)

                break
            elif van_choice == 6:
                vehicle_total = rate_calculation(78.80, 496.44, 943.24)
                vehicle_total = round(vehicle_total, 2)
                print("Cost of this service excluding VAT(23%):", vehicle_total)

                break
            else:
                print("Please choose the appropriate van model numbers")
                print()
                continue
        break
    else:
        print("Invalid Option. Please enter either car or van.")
        continue


#Table of Optional Extras
print()

print("""-----------------------------------------------------------------------------------------------------------

Extra	                                             Rate in € (Ex VAT)")
-----------------------------------------------------------------------------------------------------------
1. Child Seat (Cars only)	                               22 
2. Ski Equipped (Cars + 4x4 only)	                       78
3. Roof-Mounted Luggage Rack (Cars + 4x4 only)             44
4. Additional Drivers	                               7 (per day)
5. End the Program"
-----------------------------------------------------------------------------------------------------------""")
Total = 0

#Calculation for the optional extras the customer wants
while True:
    answer = input("Please enter the number of the corresponding extra feature you would like or else enter 5 to end the program: ")
    if answer == "1":
        Total =  22 + Total
        Total = round(Total ,2)
        print("Total Cost (excluding VAT) = ",Total,".")
        continue
    if answer == "2":
        Total =  78 + Total
        Total = round(Total ,2)

        print("Total Cost (excluding VAT) = ",Total,".")
        continue
    if answer == "3":
        Total = 44 + Total
        Total = round(Total ,2)

        print("Total Cost (excluding VAT) = ",Total,".")
        continue

    if answer == "4":
        Total = 7 + Total
        Total = round(Total ,2)

        print("Total Cost (excluding VAT)= ",Total,".")
        continue
    if answer == "5":
        Total = Total
        print()
        print("Total Cost (excluding VAT) = ",Total + vehicle_total,".")
        break
print()
Total_Cost_with_VAT = (Total + vehicle_total) *1.23
Total_Cost_with_VAT = round(Total_Cost_with_VAT ,2)
print("Total Cost (including VAT) = f",Total_Cost_with_VAT,".")
print()
print("Thank you for applying to the BIS Car Rental!\nWe will review your application and email you shortly.\nGoodbye!")

