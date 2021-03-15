groups = int(input())

total_people = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for i in range(1, groups + 1):
    people = int(input())

    total_people += people

    if people < 6:
        musala += people
    elif 6 <= people < 13:
        monblan += people
    elif 13 <= people < 26:
        kilimandjaro += people
    elif 26 <= people < 41:
        k2 += people
    else:
        everest += people


hiking_musala = musala / total_people * 100
hiking_monblan = monblan / total_people * 100
hiking_kilimandjaro = kilimandjaro / total_people * 100
hiking_k2 = k2 / total_people * 100
hiking_everest = everest / total_people * 100

print(f'{hiking_musala:.2f}%')
print(f'{hiking_monblan:.2f}%')
print(f'{hiking_kilimandjaro:.2f}%')
print(f'{hiking_k2:.2f}%')
print(f'{hiking_everest:.2f}%')