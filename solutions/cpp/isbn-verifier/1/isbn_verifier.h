#if !defined(ISBN_VERIFIER_H)
#define ISBN_VERIFIER_H

#include <string>

using std::string;

namespace isbn_verifier {
    bool is_valid(string input) {
        int subtotal{};
        int multiplier = 10;
        int digit{};

        for (int i = 0; i < static_cast<int>(input.size()); i++) {
            if (input[i] == '-') { continue;}
            if (input[i] == 'X') {
                if (i != static_cast<int>(input.size()) - 1) { return false;}
                digit = 10;
            } else {
                digit = input[i] - 48;
            }
            
            subtotal += digit * multiplier;
            multiplier--;
        }

        if (multiplier != 0) {return false;}
        if (subtotal % 11 == 0) { return true;}
        return false;
    }
} // namespace isbn_verifier

#endif // ISBN_VERIFIER_H