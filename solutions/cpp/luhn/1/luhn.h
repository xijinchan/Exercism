#if !defined(LUHN_H)
#define LUHN_H
#include <string>
#include <cctype>

using std::string;

namespace luhn {
    bool valid(string input) {
        string input_formatted{};
        int counter{};
        int doubled{};
        int total{};
        
        for (int i = static_cast<int>(input.size()) - 1; i >= 0; i--) {
            if (input[i] != ' ') {
                counter++;
                if (!std::isdigit(input[i])) {
                    return false;
                }
                if (counter % 2 == 0 and input[i] != '9') {
                    doubled = ((input[i] - '0') * 2) % 9;
                    input_formatted = std::to_string(doubled) + input_formatted;
                    total += doubled;
                } else {
                    input_formatted = input[i] + input_formatted;
                    total += input[i] - '0';
                }
            }
        }
        
        if (input_formatted.size() < 2) {
            return false;
        }

        return (total % 10 == 0);
    }
}  // namespace luhn

#endif // LUHN_H