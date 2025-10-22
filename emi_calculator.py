principle = 10000000
rate_of_interest = 8
duration_in_year = 30
time_to_pay = 0
montly_rate = rate_of_interest/ 12 /100

numerator = principle * montly_rate*(1+montly_rate)**(duration_in_year * 12)

denominator = (1+montly_rate)**(duration_in_year*12)-1

emi = numerator/denominator
print("EMI=",emi)
total_annual_emi = emi * 12
i = 1
while principle>0:
    annual_interest = (principle*rate_of_interest)/100
    print("year=",i)
    print("annual_interest=",annual_interest)
    principle_cut = total_annual_emi - annual_interest 
    principle -= principle_cut
    lumsum = 500000
    if lumsum and i >= 2:
        principle -= lumsum
    if principle<=0:
        break
    
    i+=1

    print("principle=",principle)
    time_to_pay +=1

print(time_to_pay)
print("principle=",principle)

