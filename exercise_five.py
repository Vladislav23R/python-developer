earnings = float(input('Enter you earnings: '))
costs = float(input('Enter you costs: '))

fin_result = earnings - costs

if fin_result <= 0:
    print(f'Sorry, your company is operating at a loss: {fin_result}')
else:
    profitability = round(earnings / costs, 2)
    staff = int(input('Enter the number of employees: '))
    profit = round(fin_result / staff, 2)
    print(f'Your profit was: {fin_result} \nProfitability - {profitability} \nEmployee / staff = {profit}')


