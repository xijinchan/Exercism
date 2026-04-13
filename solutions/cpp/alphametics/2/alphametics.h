#if !defined(ALPHAMETICS_H)
#define ALPHAMETICS_H

#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <cmath>

using std::string;
using std::vector;

namespace alphametics {

    class alphametic_sum {
        public:
            int value{};
            string puzzle{};
            std::unordered_map<char, int> legend;
            vector<string> addends{};
            std::unordered_set<char> first_chars_set{};
            std::unordered_set<char> letters{};
            string checksum_string;
            
            alphametic_sum(string input) {
                puzzle = input;

                string current_word{};
                bool result_segment_reached = false;
                bool current_word_added = false;

                // populate legend keys, addends & checksum_string on object creation
                for (char c : input) {
                    if (c == '=') {
                        result_segment_reached = true;
                        continue;
                    }
                    if (c == ' ' || c == '+') {
                        if (current_word_added == false) {
                            addends.push_back(current_word);
                            current_word_added = true;
                            first_chars_set.insert(current_word[0]);
                            current_word = "";
                        }
                        continue;
                    }
                    if (letters.find(c) == letters.end()) {
                        letters.insert(c);
                    }
                    if (result_segment_reached) {
                        checksum_string += c;
                    } else {
                        current_word_added = false;
                        current_word += c;
                    }
                }
                first_chars_set.insert(checksum_string[0]);
            }

        int has_value() {
            return value;
        }

        int at(char input) {
            return legend[input];
        }

        auto& operator*() {
        return *this;
        }
    };

    alphametic_sum solve(string input);
}  // namespace alphametics

#endif  // ALPHAMETICS_H
