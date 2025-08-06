words = ["the", "sky", "is", "blue"]
flipped_sentence = ""

for word in words:
    stack = []   
    for i in word:
        stack.append(i)
    
    while stack:
        flipped_sentence += stack.pop()
    

    flipped_sentence += ' '

flipped_sentence = flipped_sentence

print("Flipped sentence:", flipped_sentence)
