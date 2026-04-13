#include "alphametics.h"

namespace alphametics {

    alphametic_sum solve(string input) {
        alphametic_sum result{input};

        if (result.letters.empty()) return result;

        std::vector<char> letters(result.letters.begin(), result.letters.end());

        // Precompute weights (fast vector)
        std::vector<long long> weight(256, 0);

        // addends treated as positive values
        for (const auto& addend : result.addends) {
            long long place = 1;
            for (int i = static_cast<int>(addend.size()) - 1; i >= 0; --i) {
                weight[addend[i]] += place;
                place *= 10;
            }
        }

        // checksum as negative values
        long long place = 1;
        for (int i = static_cast<int>(result.checksum_string.size()) - 1; i >= 0; --i) {
            weight[result.checksum_string[i]] -= place;
            place *= 10;
        }

        std::vector<int> assignment(letters.size(), -1);
        std::vector<bool> used(10, false);

        // Backtracking function
        auto search = [&](auto&& self, size_t idx) -> bool {
            if (idx == letters.size()) { // if we reached the bottom of the tree
                // Check if solution is valid, i.e. addends weightings * values cancels out checksum
                long long total = 0;
                for (size_t i = 0; i < letters.size(); ++i) {
                    total += weight[letters[i]] * assignment[i];
                }

                // if solution found, i.e. addends * weights = checksum, or they cancel out in other words
                if (total == 0) {
                    for (size_t i = 0; i < letters.size(); ++i) {
                        result.legend[letters[i]] = assignment[i];
                    }
                    long long value = 0;
                    for (char c : result.checksum_string) {
                        value = value * 10 + result.legend[c];
                    }
                    result.value = static_cast<int>(value);
                    return true;
                }
                return false;
            }

            char letter = letters[idx];
            bool is_leading = result.first_chars_set.count(letter);

            //  try all possible digits for current letter position (idx). idx also simultaneously indicates recursion level
            for (int d = 0; d < 10; ++d) {
                if (used[d]) continue;
                if (is_leading && d == 0) continue;

                assignment[idx] = d; // place digit
                used[d] = true;

                if (self(self, idx + 1)) { // recursive call for next letter
                    return true;
                }

                // backtrack if no solution found in recursive calls / sub branches
                used[d] = false;
                assignment[idx] = -1;
            }
            return false;
        };

        search(search, 0); // initial idx
        return result;
    }

}  // namespace alphametics