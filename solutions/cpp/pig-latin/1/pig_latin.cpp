#include "pig_latin.h"

#include <vector>
#include <unordered_set>

using std::vector;

namespace pig_latin {

// TODO: add your solution here
    string translate(string input) {
        string result{};
        std::unordered_set<std::string> rule_1 = {"a","i","u","e","o","xr","yt"};
        vector<string> input_split{};
        int start = 0;
        int end = 0;
        string start_consonants{};
        bool next_word = false;


        // split input sentence
        for (int i = 0; i < static_cast<int>(input.size()); i++) {
            if (input[i + 1] == ' ' or i == static_cast<int>(input.size()) - 1) {
                end = i + 1;
                input_split.push_back(input.substr(start, end - start));
                start = i + 2;
            }
        }

        // rule 1
        for (string& word : input_split) {
            // rule 1
            if (word != input_split[0]) {
                result += " ";
            }
            
            if (rule_1.count(std::string(1, word[0])) || rule_1.count(word.substr(0, 2))) {
                result += word + "ay";
                continue;
            }

            // rule 2, 3, 4
            for (int i = 0; i < static_cast<int>(word.size()); i++) {
                if ((rule_1.count(std::string(1, word[i])) == 0 && rule_1.count(word.substr(0, 2)) == 0)) {
                    // rule 3
                    if (word.substr(i, 2) == "qu") {
                        start_consonants = word.substr(0, i + 2);
                        result += word.substr(i + 2, static_cast<int>(word.size()) - 1) + start_consonants + "ay";
                        next_word = true;
                    }
                    // rule 4
                    if (word.substr(i, 1) == "y") {
                        if (i == 0) {
                            start_consonants = "y";
                            start = i + 1;
                        } else {
                            start_consonants = word.substr(0, i);
                            start = i;
                        }
                        result += word.substr(start, static_cast<int>(word.size()) - 1) + start_consonants + "ay";
                        next_word = true;
                    }
                    continue;
                }
                if (next_word == true) {
                    next_word = false;
                    break;
                }

                // rule 2
                start_consonants = word.substr(0, i);
                result += word.substr(i, static_cast<int>(word.size()) - 1) + start_consonants + "ay";
                break;
            }
        }        
            
        return result;
    }
}  // namespace pig_latin
