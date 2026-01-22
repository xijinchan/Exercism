#include "diamond.h"

namespace diamond {

// TODO: add your solution here
    std::vector<string> rows(char c) {
        int no_of_letters = c - 64;
        std::vector<string> output{};

        for (int i = 0; i < (no_of_letters); i++) {
            string row_string{};
            for (int j = 0; j < (no_of_letters * 2 - 1); j++) {
                if (j == (no_of_letters - 1) - i || j == (no_of_letters - 1) + i) {
                    char letter = 'A' + i;
                    row_string += letter;
                } else {
                    row_string += ' ';
                }
            }
            output.push_back(row_string);
        }

        std::vector<string> reversed{};

        for (int k = 1; k < static_cast<int>(output.size()); k++) {
            reversed.push_back(output[static_cast<int>(output.size()) - 1 - k]);
        }

        output.insert(output.end(), reversed.begin(), reversed.end());

        return output;
    }

}  // namespace diamond
