#include "alphametics.h"

namespace alphametics {

// TODO: add your solution here
    alphametic_sum solve(string input) {
        alphametic_sum result{input};
        string answer{};
        bool valid{};
        std::vector<char> letters_vec(result.letters.begin(), result.letters.end());
        int max_iterations = 700000;
        int k = 0;

        // do while next permutation (generate new permutation)
        do {
            valid = true;
            result.legend.clear();
            answer = "";
            int sum{};

            // skip leading 0 solutions
            for (size_t i = 0; i < result.letters.size(); i++) {
                char letter = letters_vec[i];
                if (result.first_chars_set.count(letter) && result.digits_permutation[i] == 0) {
                    valid = false;
                    break;
                }
            }

            if (valid == false) {
                continue;
            }

            // precomputed weights * permutation digits
            for (size_t i = 0; i < result.letters.size(); i++) {
                char letter = letters_vec[i];
                sum += result.weights[letter] * result.digits_permutation[i];
            }

            // if addends balances out checksum weightings, solution found
            if (sum == 0) {
                // assign to letters
                for (size_t i = 0; i < result.letters.size(); i++) {
                    char letter = letters_vec[i];
                    result.legend[letter] = result.digits_permutation[i];
                }

                // compute checksum value
                long long checksum = 0;
                for (char c : result.checksum_string) {
                    checksum = checksum * 10 + result.legend[c];
                }

                result.value = static_cast<int>(checksum);

                return result;
            }

            k += 1;
        } while (std::next_permutation(result.digits_permutation.begin(), result.digits_permutation.end()) && k < max_iterations);

        return result;
    }
}  // namespace alphametics