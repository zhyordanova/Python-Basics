yearly_tax = int(input())

sneakers = yearly_tax * 0.6
equipment = sneakers * 0.8
basketball_ball = equipment * 0.25
accessories = basketball_ball / 5

total_price = yearly_tax + sneakers + equipment + basketball_ball + accessories

print(f'{total_price:.2f}')