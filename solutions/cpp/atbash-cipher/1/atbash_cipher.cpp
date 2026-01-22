#include "atbash_cipher.h"

namespace atbash_cipher {
    string alphabet = "abcdefghijklmnopqrstuvwxyz";

    string encode(string input) {
        string output{};
        int counter{};
        
        for (int i = 0; i < static_cast<int>(input.size()); ++i){
            char c = input[i]; 
            if (std::isalpha(c)) {
                int letter_index = 25 - alphabet.find(std::tolower(c));
                output = output + alphabet[letter_index];
            } else if (std::isdigit(c)) {
                output = output + c;
            } else {
                continue;
            }
            counter += 1;
            if (counter % 5 == 0 && i < static_cast<int>(input.size()) - 1) { 
                output += " ";
            }
        }
        return remove_spaces(output);
    }

    string decode(string input) {
        string output{};
        int counter{};
        
        for (int i = 0; i < static_cast<int>(input.size()); ++i){
            char c = input[i]; 
            if (std::isalpha(c)) {
                int letter_index = 25 - alphabet.find(std::tolower(c));
                output = output + alphabet[letter_index];
            } else if (std::isdigit(c)) {
                output = output + c;
            } else {
                continue;
            }
            counter += 1;
        }
        return output;
    }

    string remove_spaces(string& s) {
        int last = s.size() - 1;
        while (last >= 0 && s[last] == ' ')
            --last;
        return s.substr(0, last + 1);
    }
}  // namespace atbash_cipher