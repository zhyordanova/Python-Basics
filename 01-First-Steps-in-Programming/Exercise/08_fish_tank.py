# Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.

length = int(input())
width = int(input())
height  = int(input())
persent_occupied_volume = float(input())

volume_aquarium = length * width * height
total_litters = volume_aquarium * 0.001
persent_occupied = persent_occupied_volume * 0.01
litters = total_litters * (1 - persent_occupied)

print(litters)
