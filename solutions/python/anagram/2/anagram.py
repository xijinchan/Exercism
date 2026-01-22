def find_anagrams(word, candidates):
    anagram_set = []

    for candidate in candidates:
        anagram = True
        word_lowercase = word.lower()
        candidate_lowercase = candidate.lower()
        
        if len(word) != len(candidate) or candidate.lower() == word.lower():
            anagram = False
            continue
        for letter in candidate_lowercase:         
            if letter in word_lowercase and candidate_lowercase.count(letter) == word_lowercase.count(letter):
                continue
            else:
                anagram = False
                break

        if anagram is True: anagram_set.append(str(candidate))
            
    return anagram_set

