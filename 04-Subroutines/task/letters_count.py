
def letter_counter(sentence, letter):
    count = 0
    for l in sentence:
        if l == letter:
            count += 1
    return count