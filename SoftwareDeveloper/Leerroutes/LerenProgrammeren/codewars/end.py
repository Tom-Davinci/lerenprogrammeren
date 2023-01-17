def solution(text, ending):
    word_end = ""
    for index in range(len(text) - 1, -1, -1):
        word_end = text[index] + word_end
        if word_end == ending:
            return True
    return False

def solution2(text, ending):
    return text.endswith(ending)

def solution3(text, ending):
    return ending  in text[-len(ending):]