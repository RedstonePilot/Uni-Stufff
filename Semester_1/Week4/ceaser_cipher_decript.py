import string
lower = string.ascii_lowercase
plain_text = "bpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc bmtt bpmu bw lw. bpm jil vmea qa bpib bpmg lw epib gwc bmtt bpmu bw lw."



def ceaser_decrypt(plain_text,shift):
    cipher_text = []
    for char in plain_text:
        if char not in lower:
            cipher_text.append(char)
        else:
            index = lower.index(char)
            new_index = (index - shift)%26
            cipher_text.append(lower[new_index])
    if "the" in "".join(cipher_text):
        print(shift)
        print("".join(cipher_text), shift)


for i in range(26):
    ceaser_decrypt(plain_text,i+1)