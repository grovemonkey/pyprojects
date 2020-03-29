## -*- coding: utf-8 -*-
#"""
#Created on Sun Dec  8 19:18:13 2019
#
#@author: Bill Smith
#"""
#startingsalary = input('Enter the starting salary: ')
#
#semiraise = .07
#invest_return = .04
#down_payment = .25
#house_cost = 1000000
#
#savings_needed = down_payment*house_cost
#
#a = 10000
#b = 0
#savings =0
#i=0
#
#while a - b > 2 and i<30:
#    c = int((a+b)/2)
#    savingsrate = c/10000
#    savings =0
#    salary = startingsalary
#    for months in range(1, 37):
#        savings_invest =  (savings*invest_return)/12
#        savingpermonth = float(salary)/12
#        savings += savingsrate*savingpermonth + savings_invest
#        if months %6 ==0:
#            salary = float(salary) * (1+ semiraise)
#    if savings < savings_needed:
#        b=c
#    elif savings > savings_needed:
#        a=c
#    i +=1
#
#print('Best savings rate: %.4f' % savingsrate)
#print('Steps in bisection search: 4%i' % i)


# Set the default values.

semiAnnualRaise = 0.07

rAnnual = 0.04

r = rAnnual/12

homeCost = 1000000

downPaymentPercent = 0.25

downPayment = downPaymentPercent * homeCost

savings = 0

monthLimit = 36

savingsRate = 0.50

# Counters

monthCounter = 0

stepCounter = 1


# Range

min = 0

max = 10000


# Request the user's starting salary

currentSalary = int(input("Enter your current salary: "))


# Save this to a separate variable so it can be reset later, when rerunning the bisection method.

presentSalary = currentSalary


# Function to run the bisection method with a lower and upper limit

def computeRate(lower, upper):
    global savings, currentSalary, monthCounter, max, min, stepCounter, savingsRate
    while (savings < downPayment):
        savingsRate = ((upper+lower)/2)/10000
        monthlySalary = currentSalary/12
        monthlyReturn = savings * r
        monthlyContribution = monthlySalary * savingsRate
        savingsRate = ((upper+lower)/2)/10000
        monthlySalary = currentSalary/12
        monthlyReturn = savings * r
        monthlyContribution = monthlySalary * savingsRate


# Bring in all the variables to be modified.


# As long as the amount in Savings is less than the down payment (25% on 1MM = $250,000), do this:



# Define variables and how they're calculated.

savingsRate = ((upper+lower)/2)/10000
monthlySalary = currentSalary/12
monthlyReturn = savings * r
monthlyContribution = monthlySalary * savingsRate


# This equation changes the value of savings as we expect it to.

savings = savings + monthlyContribution + monthlyReturn


# For every time we go through this, increase month count by 1.

monthCounter += 1


# As we increase the month count, if it happens to be divisible by 6 and yields a remainder of 0, increase the currentSalary

if monthCounter % 6 == 0:

currentSalary = currentSalary + (currentSalary*semiAnnualRaise)


# While loop repeats until savings are no longer less than the down payment needed.


# Check to see if we got to our goal in our set timeframe.

# If not, reset all the variables (including salary!), increase the step counter (aka # of iterations of the bisection method) by 1, and run the bisection method again.

# Since we took LONGER than our goal timeframe, change the minimum value for the bisection method to the savings rate used in the last iteration.

if monthCounter > monthLimit:


monthCounter = 0

savings = 0

currentSalary = presentSalary

stepCounter += 1

min = savingsRate*10000

computeRate(min, max)


# Since we achieved our goal FASTER our goal timeframe, change the maximum value for the bisection method to the savings rate used in the last iteration.

# Don't forget to reset variables and increase iteration count by 1

#### Since I reset the varaibles so frequently, maybe it should have it's own function?

#### e.g. def reset():

elif monthCounter < monthLimit:


monthCounter = 0

savings = 0

currentSalary = presentSalary

stepCounter += 1

max = savingsRate * 10000

computeRate(min, max)


# Just because we finally got to our savings goal at the expected timeframe, doesn't mean we did it right.

# Confirm that the savings value is within $100 of the down payment amount.

# If not, run it again.

# Change the savings rate by 1 (0.001, technically)

# decrease it by 0.001 if savings exceed down payment + 100

# increase it by 0.001 if savings exceed down payment - 100

# repeat as necessary

elif savings > downPayment + 100:


monthCounter = 0

savings = 0

currentSalary = presentSalary

stepCounter += 1

max = (savingsRate * 10000)-1

computeRate(min, max)


elif savings < downPayment - 100:


monthCounter = 0

savings = 0

currentSalary = presentSalary

stepCounter += 1

max = (savingsRate * 10000)+1

computeRate(min, max)


# Do the bisection method & post the results.

computeRate(min, max)

print("Rate:", savingsRate)

print("Savings:", savings)

print("Months:", monthCounter)

print("Iterations:", stepCounter)



#starting_salary = 100000  # Assuming Annual Salary of 100k 
#months_salary = starting_salary/12
#total_cost = 1000000.0
#semi_annual_rate = .07
#investment_return = 0.04
#down_payment = total_cost * 0.25
#print("down payment: ", down_payment)
#r = 0.04
#current_savings = 0.0
##months = 36
#tolerance = 100
#steps = 0
#high = 1.0
#low = 0.0
#guess = (high+low)/2.0
#total_salaries = 0.0
#tolerance = down_payment/100 # I chose this tolerance to say if my savings are between [down_payment - (downpayment + down_payment/100)]  result is admissible. (this is quite a high tolerance but you can change at leisure)
#def calSavings(current_savings,months_salary,guess,month):
#    for months in range(0,37):
#        if  months%6==1 and months >1:
#            months_salary=months_salary*(1+semi_annual_rate)
#        current_savings = current_savings + months_salary * guess
#    current_savings = current_savings * (1+0.04)
#    return(current_savings)
#
#while abs(current_savings-down_payment)>=100:
#    current_savings = calSavings(current_savings,months_salary,guess,1)
#    if  current_savings < down_payment:
#        low = guess
#        current_savings = 0.
#    elif current_savings > down_payment + tolerance:
#        high = guess
#        current_savings = 0.
#    if (steps > 100): # I chose a maximum step number of 100 because my tolerance is high
#        print("It is not possible to pay the down payment in three years.")
#        break
#    guess = (low+high)/2
#    steps = steps 
#
#print("Best saving rate: ", guess)
#print("With current savings: ", current_savings)