#hours 45
hrs = int(raw_input("Enter Hours:"))
#rate 10.50
rate = float(raw_input("Enter Rate:"))

def gross_pay(hrs,  rate):
    if hrs > 40:
        plus = hrs - 40
        pay = (40 * rate) + ((plus * rate) * 1.5)
    else:
        pay = hrs * rate

	return pay

