#if !defined(ALPHAMETICS_H)
#define ALPHAMETICS_H

#include <string>
#include <unordered_map>
#include <vector>
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
            std::unordered_map<char, int> weights;
            vector<string> addends{};
            std::unordered_set<char> first_chars_set{};
            std::unordered_set<char> letters{};
            string checksum_string;
            vector<int> digits_permutation = {0,1,2,3,4,5,6,7,8,9};
            
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

                // pre-compute letter weights
                for (auto letter : letters) {
                    int weight{};

                    for (auto addend: addends) {
                        for (int i = 0; i < static_cast<int>(addend.size()); i++) {
                            if (addend[i] == letter) {
                                int column = static_cast<int>(addend.size()) - i - 1;
                                int column_value = std::pow(10, column);
                                weight += column_value;
                            }
                        }
                    }

                    for (int i = 0; i < static_cast<int>(checksum_string.size()); i++) {
                        if (checksum_string[i] == letter) {
                            int column = static_cast<int>(checksum_string.size()) - i - 1;
                            int column_value = std::pow(10, column);
                            weight -= column_value;
                        }
                    }

                    weights[letter] = weight;
                }
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
