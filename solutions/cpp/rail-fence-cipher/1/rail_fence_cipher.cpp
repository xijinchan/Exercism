#include "rail_fence_cipher.h"

namespace rail_fence_cipher {

    std::string encode(const std::string& plaintext, int num_rails) {        
        string plaintext_no_whitespace{};
        for (char k : plaintext) {
            if (k != ' ') {
                plaintext_no_whitespace += k;
            }
        }
        
        int i = 0;
        int row = 0;
        vector<string> rows(num_rails);
        int direction = 1;
        
        for (char letter : plaintext_no_whitespace) {
                for (int k = 0; k < num_rails; k++) {
                    if (i % (num_rails * 2 - 2) == k || i % (num_rails * 2 - 2) == (num_rails * 2) - 2 - k) {
                        rows[k] += letter;
                    }
                }
            
                row = row + direction;
                if (row == num_rails) {
                    row -= 2;
                    direction = -1;
                }
                if (row == -1) {
                    row += 2;
                    direction = 1;
                }
                i++;
        }

        string output{};

        for (string row : rows) {
            output += row;
        }

        return output;
    }
    
    std::string decode(const std::string& ciphertext, int num_rails) {
        int row = 0;
        vector<int> row_items_count(num_rails);

        // count letters per row
        int direction = 1;
        for (char letter : ciphertext) {
                row_items_count[row] += 1;

                row = row + direction;
                if (row == num_rails) {
                    row -= 2;
                    direction = -1;
                }
                if (row == -1) {
                    row += 2;
                    direction = 1;
                }
                (void)letter;
        }

        // calculate at which index each row starts
        vector<int> ciphertext_row_start_indices(num_rails);
        int sum = 0;
        for (int j = 0; j < num_rails; j++) {
            if (j == 0) {
                ciphertext_row_start_indices[j] = 0;
            } else {
                sum += row_items_count[j - 1];
                ciphertext_row_start_indices[j] = sum;
            }
        }

        string output{};
        row = 0;
        direction = 1;
        int i = 0;
        vector<int> per_row_index(num_rails, 0);

        // assemble output
        while (output.size() < ciphertext.size()) {
            if (row == 0) {
                output += ciphertext.substr(per_row_index[row], 1);
            } else {
                output += ciphertext.substr(ciphertext_row_start_indices[row] + per_row_index[row], 1);
            }
            per_row_index[row] += 1;
            row = row + direction;
            if (row == num_rails) {
                row -= 2;
                direction = -1;
                i += 1;
            }
            if (row == -1) {
                row += 2;
                direction = 1;
                i += 1;
            }
        }
        
        return output;
    }
}  // namespace rail_fence_cipher
