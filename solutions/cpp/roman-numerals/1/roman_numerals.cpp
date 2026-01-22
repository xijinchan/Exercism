#include "roman_numerals.h"

namespace roman_numerals {
    string convert(int input) {
        std::map<int, char> letters = {{1, 'I'}, {5, 'V'}, {10, 'X'}, {50, 'L'}, {100, 'C'}, {500, 'D'}, {1000, 'M'}};
        string romanised = "";


        if (letters.find(input) != letters.end()) {
            romanised = letters[input];
        } else {
            for (int i = 0; i < static_cast<int>(std::to_string(input).size()); i++) {
                int reverse_digit_index = std::abs(i - (static_cast<int>(std::to_string(input).size() - 1)));
                int current_digit = static_cast<int>(std::to_string(input)[i]) - 48;
        
                if (current_digit < 4) {
                    romanised += string(current_digit, letters[stoi("1" + string(reverse_digit_index, '0'))]);
                } else if (current_digit == 4) {
                    romanised += letters[stoi("1" + string(reverse_digit_index, '0'))];
                    romanised += letters[stoi("5" + string(reverse_digit_index, '0'))];
                } else if (current_digit == 5) {
                    romanised += letters[stoi("5" + string(reverse_digit_index, '0'))];
                } else if (current_digit < 9) {
                    romanised += letters[stoi("5" + string(reverse_digit_index, '0'))];
                    romanised += string(current_digit - 5, letters[stoi("1" + string(reverse_digit_index, '0'))]);
                } else if (current_digit == 9) {
                    romanised += letters[stoi("1" + string(reverse_digit_index, '0'))];
                    romanised += letters[stoi("1" + string(reverse_digit_index + 1, '0'))];
                }
            }
        }
        
        return romanised;
    }
}  // namespace roman_numerals
