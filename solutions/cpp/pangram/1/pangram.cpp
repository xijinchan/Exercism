#include "pangram.h"
#include <algorithm>
#include <iostream>

namespace pangram {
    bool is_pangram(std::string sentence) {
        std::transform(sentence.begin(), sentence.end(), sentence.begin(), ::tolower);
        
        std::string alphabet[26] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};

        for (int i = 0; i < 26; ++i) {
            if (sentence.find(alphabet[i]) != std::string::npos) {
                continue;
            } else {
                return false;
            }
        }
        std::cout << "return true!";
        return true;
    }
}  // namespace pangram
