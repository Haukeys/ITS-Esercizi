import string

def count_unique_words(text:str)->dict[str, int]:

    words = text.split()
    word_count = {}
    
    # les differentes ponctuations
    symbole = string.punctuation
    
    for word in words:
        
        clean_word = word.strip(symbole).lower()
        
        #chaque mot avec sa position dans la phrase 
        if clean_word:
            
            if clean_word in word_count:
                word_count[clean_word] += 1
            else:
                word_count[clean_word] = 1 #la premiere fois il faut mettre le mot mais aussi un terme vide
    
    return word_count 


text = "Hello, world! Hello... PYTHON? world."
output = count_unique_words(text)

print(output)