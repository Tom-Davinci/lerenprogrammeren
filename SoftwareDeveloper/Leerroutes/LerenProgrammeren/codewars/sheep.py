def count_sheep(n):
    end = ""
    for i in range(1, n + 1):
        end += f"{i} sheep..."
    return end

print(count_sheep(6))