#include "rotational_cipher.h"

#include <vector>

namespace rotational_cipher {

// TODO: add your solution here
    string rotate(string input, int n) {
        std::vector<char> alphabet = {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        string output{};
        
        for (char c : input) {
            if (c > 96 && c < 123) {
                output += (((c + n) % 97) % 26) + 97;
            } else if (64 < c && c < 91) {
                output += (((c + n) % 64) % 26) + 64;
            } else {
                output += c;
            }
        }
        return output;
    }
}  // namespace rotational_cipher
