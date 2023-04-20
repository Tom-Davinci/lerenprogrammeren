def dirReduc(arr):
    lastDir, reducing = "", True
    opposites = {
        "NORTH" : "SOUTH",
        "SOUTH" : "NORTH",
        "EAST" : "WEST",
        "WEST" : "EAST"
    }
    while reducing:
        reducing = False
        for index in range(3):
            print(index)
            print(arr)
            if lastDir == opposites[arr[index]]:
                arr.pop(index)
                arr.pop(index - 1)
                reducing = True
            lastDir = arr[index]
    return arr

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))