# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit_sum = float(input())
term_deposit_months = int(input())
yearly_interest_rate = float(input()) / 100

result = deposit_sum + term_deposit_months * ((deposit_sum * yearly_interest_rate) / 12)

print(result)