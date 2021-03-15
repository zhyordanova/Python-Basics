# •	Торта  – цената ѝ е 20% от наема на залата
# •	Напитки – цената им е 45% по-малко от тази на тортата
# •	Аниматор – цената му е 1/3 от цената за наема на залата

rent_hall = int(input())

cake = rent_hall * 0.2
drinks = cake - (cake * 0.45)
animator = 1/3 * rent_hall

total = rent_hall +cake + drinks + animator

print (total)