alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import random

class Cipher:
    key = ''
    
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join([alphabet[random.randint(0,9)] for k in range(100)])
        else:
            self.key = key
        
    def encode(self, text):    
        self.key = ''.join([self.key[k % len(self.key)] for k in range(len(text))])        
        text_encoded = ''.join([alphabet[(alphabet.index(k) + alphabet.index(self.key[i])) % 26] for i, k in enumerate(text)])
        return text_encoded


    def decode(self, text_encoded):
        self.key = ''.join([self.key[k % len(self.key)] for k in range(len(text_encoded))])    
        text = ''.join([alphabet[(alphabet.index(text_encoded[k]) - alphabet.index(self.key[k])) % 26] for k in range(len(text_encoded))])
        return text