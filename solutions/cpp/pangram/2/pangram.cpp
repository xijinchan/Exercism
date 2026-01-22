#include "pangram.h"
#include <algorithm>

namespace pangram {
    bool is_pangram(std::string sentence) {
        std::transform(sentence.begin(), sentence.end(), sentence.begin(), ::tolower);
        
        std::string alphabet = "abcdefghijklmnopqrstuvwxyz";
        
        for (char i : alphabet) {
            if (sentence.find(i) != std::string::npos) {
                continue;
            } else {
                return false;
            }
        }
        return true;
    }
}  // namespace pangram
