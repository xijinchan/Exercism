#if !defined(ARMSTRONG_NUMBERS_H)
#define ARMSTRONG_NUMBERS_H
#include <cmath>
#include <string>

using std::string;

namespace armstrong_numbers {
    bool is_armstrong_number(int input) {
        string input_string = std::to_string(input);
        int power = input_string.size();
        int total{};
        
        for (int i = 0; i < power; i++) {
            total += pow(input_string[i] - '0', power);
        }

        return (total == input);
    }
}  // namespace armstrong_numbers

#endif // ARMSTRONG_NUMBERS_H