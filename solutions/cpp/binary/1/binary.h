#if !defined(BINARY_H)
#define BINARY_H
#include <string>
#include <cmath>
#include <cctype>

using std::string;

namespace binary {
    int convert(string input) {
        int total{};
        
        for (int i = 0; i < static_cast<int>(input.size()); i++) {
            int right_i = (static_cast<int>(input.size()) - 1) - i;
            
            if (!isdigit(input[right_i])) {
                return 0;
            }

            if (input[right_i] == '1') {
                total += pow(2, i);
            }
        }

        return total;
    }
}  // namespace binary

#endif // BINARY_H