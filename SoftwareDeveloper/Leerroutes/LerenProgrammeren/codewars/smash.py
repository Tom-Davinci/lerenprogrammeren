def smash(words : list) -> str:
    smashed = ""
    for index in range( len(words)):
        if index == 0:
            smashed += words[index]
        else:
            smashed += f" {words[index]}"
    return smashed

def smash2(words):
    return " ".join(words)

words = ["hoi", "ik", "ben", "tom", ":D"]
print( smash2(words))