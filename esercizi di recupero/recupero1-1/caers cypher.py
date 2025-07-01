from string import ascii_lowercase


def caesar_cypher_encrypt(s:str, key:int)->str:
    alfabet=ascii_lowercase
    encrypted_text:str=""

    for caracter in s:
        if caracter in alfabet:  # on verifie que seul les element de alfabet soit prit en compte:si le caracter dans la variable
            index_s = (alfabet.index(caracter) + key) % len(alfabet)
            encrypted_text += alfabet[index_s]
        else:
            encrypted_text += caracter  # cette ligne dit: si ce n est pas dans l alfabet le caracter ne change pas
    return encrypted_text

def caesar_cypher_decrypt(s:str, key:int)->str:
    alfabet=ascii_lowercase
    encrypted_text:str=""

    for caracter in s:
        if caracter in alfabet:  # on verifie que seul les element de alfabet soit prit en compte:si le caracter dans la variable
            index_s = (alfabet.index(caracter) - key) % len(alfabet) # contrairement a au dessus ici le -  sert a faire l effet inverse.
            encrypted_text += alfabet[index_s]
        else:
            encrypted_text += caracter  # cette ligne dit: si ce n est pas dans l alfabet le caracter ne change pas
    return encrypted_text


#index_s=où.comment(quoi)clee de chiffrement soit le deplacement de la lettre(-dechiffre;+chiffrer)
s="9leandro?"
key=1

print(caesar_cypher_encrypt(s, key))
s="9mfboesp?"

print(caesar_cypher_decrypt(s,key))    



























'''def cifario(X:str, key:int) -> str:
    alfabet:str=" a=>z"
    s:str=""
    for caracter in x:
        pass
    idx: alfabet.index(caracter)
    idx+=key

'''