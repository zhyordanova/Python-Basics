count_easter_bread = int(input())
cover_eggs= int(input())
cookies_kg = int(input())


easter_bread = count_easter_bread * 3.2
eggs = cover_eggs * 4.35
cookies = cookies_kg * 5.4
price_eggs = cover_eggs * 12 * 0.15

cost = easter_bread + eggs + cookies + price_eggs

print(f'{cost:.2f}')