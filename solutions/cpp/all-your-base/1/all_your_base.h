#if !defined(ALL_YOUR_BASE_H)
#define ALL_YOUR_BASE_H

#include <vector>
#include <cmath>
#include <stdexcept>

namespace all_your_base {
    std::vector<unsigned int> convert(int in_base, std::vector<unsigned int> in_digits, int out_base) {
        if (in_base < 2 || out_base < 2) {
            throw std::invalid_argument("error");
        }
        
        int base_10{};
        
        for (int i = 0; i < static_cast<int>(in_digits.size()); i++) { 
            if (static_cast<int>(in_digits[i]) >= in_base) {
                throw std::invalid_argument("error");
            } 
            base_10 += in_digits[i] * std::pow(in_base, static_cast<int>(in_digits.size()) - i - 1);
        }

        int remaining = base_10;
        int exponent = log(remaining) / log(out_base);
        std::vector<unsigned int> output{};
        int digit{};

        while (exponent >= 0) {
            digit = remaining / std::pow(out_base, exponent);
            output.push_back(digit);
            remaining -= digit * std::pow(out_base, exponent);
            exponent--;
        }
        return output;
    }
}  // namespace all_your_base

#endif // ALL_YOUR_BASE_H