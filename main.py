"""F€2.30 is charged for the first to the seventh kilometer,
 from the eighth kilometer it is €1.65 per km. In addition, there is the basic fee of €3.90.
  A surcharge of €1.50 will be charged for journeys on account or payment with coupons or vouchers."""

print("Welcome in Berlin taxi price Calculator")
cupon = input("Do you have cupon? (y for Yes)")
cupon_var = 1.5
if cupon == "y":
    bool_cupon = True
else:
    bool_cupon = False
str = str(input("Enter a shortcut for given scale (k for kilometers, p for price). :"))
if str:
    num = input("Enter digits : ")
    if num == "":
        print("try again")
    elif str == "k":
        num = float(num)
        if num <= 7 and bool_cupon:
            less = num * 2.30 + 3.90 + cupon_var
            print("your price is", round(less, 2), "EUR","addin cupon cost" ,cupon_var,"it is included in your price")
        elif num <= 7:
            less = num * 2.30 + 3.90
            print("your price is", round(less, 2), "EUR")
        elif num >= 8 and bool_cupon:
            more = num * 1.65 + 3.90 + cupon_var
            print("your price is", round(more, 2), "EUR","addin cupon cost" ,cupon_var,"it is included in your price")
        elif num >= 8:
            more = num * 1.65 + 3.90
            print("your price is", round(more, 2), "EUR")
    elif str == "p":
        num = float(num)
        if num <= 20 and bool_cupon:
            less = num / 2.30 - 3.90 - cupon_var
            print("you should travel for this price :", round(less, 2), "KM")
        elif num <= 20:
            less = num / 2.30 - 3.90
            print("you should travel for this price :", round(less, 2), "KM")
        elif num >= 20.01 and bool_cupon:
            more = num / 1.65 - 3.90 - cupon_var
            print("you should travel for this price :", round(more, 2), "KM")
        elif num >= 20.01:
            more = num / 1.65 - 3.90
            print("you should travel for this price :", round(more, 2), "KM")
else:
    print("please try again")




