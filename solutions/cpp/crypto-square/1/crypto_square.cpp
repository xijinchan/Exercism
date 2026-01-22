#include "crypto_square.h"

namespace crypto_square {
    cipher::cipher(string input) {
        text_original = input;
    }
    string cipher::normalized_cipher_text() {
        string lower_case{};
        for (char c : text_original) {
            if (isalnum(c)) {
                lower_case += std::tolower(c);
            }
        }
        
        int no_of_columns = ceil(std::sqrt(lower_case.size()));
        double no_of_rows{};
        if (no_of_columns == 0) {
            no_of_rows = 0;
        } else {
            no_of_rows = ceil(static_cast<double>(lower_case.size()) / no_of_columns);
        }
        vector<string> rows{};
        string line{};
        
        for (int i = 0; i < no_of_rows; i++) {
            line = lower_case.substr(i * no_of_columns, no_of_columns);
            line += string(no_of_columns - line.size(), ' ');
            rows.push_back(line);
        }

        string output{};

        for (int j = 0; j < no_of_columns; j++) {
            for (int k = 0; k < no_of_rows; k++) {
                output += rows[k].substr(j, 1);
            }
            if (j != no_of_columns - 1) {
                output += ' ';
            }
        }

        return output;
    }
}  // namespace crypto_square
