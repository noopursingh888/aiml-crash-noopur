def calculate_tip(bill, tip_percent):

    tip_amount = (bill * tip_percent) / 100

    total_amount = bill + tip_amount

    return {
        "Tip": tip_amount,
        "Total": total_amount
    }


# return gives value back to function caller
# print only displays output on screen


result1 = calculate_tip(1000, 10)
print(result1)

result2 = calculate_tip(2500, 15)
print(result2)

result3 = calculate_tip(5000, 20)
print(result3)