sentence = "function takes this Just letter when returns Kata that Just only one only will five same with like reversed word"

def spin_words(sentence):
    converted = []
    lista = []
    lista = sentence.split(" ")
    converted = [i[::-1] if len(i) >= 5 else i for i in lista ]
    converted = " ".join(converted)
    return converted

print(spin_words(sentence))