#include "collatz_conjecture.h"
#include <stdexcept>

namespace collatz_conjecture {
    int steps(int input) {
        if (input <= 0) {
            throw std::domain_error("invalid input");
        }
        int n = input;
        int steps_count = 0;
        
        while (n != 1) {
            if (n == 1) {
                break;
            }
            if (n % 2 == 0) {
                n = n / 2;
                ++steps_count;
                continue;
            } else {
                n = (n * 3) + 1;
                ++steps_count;
                continue;
            }
        }

        return steps_count;
    }
}  // namespace collatz_conjecture
