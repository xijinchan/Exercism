#include "trinary.h"

namespace trinary {
    int to_decimal(string input) {
        int output = 0;

        for (int i = 0; i < static_cast<int>(input.size()); ++i) {
            if (input[i] != 48 && input[i] != 49 && input[i] != 50) { // ascii codes for 0, 1, 2
                return 0;
            }
            
            int digit = static_cast<int>(input[i]) - 48;
            output = output + (digit * std::pow(3, input.size() - i - 1));
        }

        return output;
    }
}  // namespace trinary
