from fruitmand import fruitmand

fruitmand.append({
    'name' : 'watermelon',
    'weight' : 2080,
    'color' : 'green',
    'round' : True
})

total = 0

for index in range(0, len(fruitmand)):
    total += fruitmand[index].get("weight")

print(total)