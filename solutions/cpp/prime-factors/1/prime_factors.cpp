#include "prime_factors.h"

namespace prime_factors {
    vector<int> of(int input) {

        int divisor = 2;
        vector<int> output{};

        return primes(input, divisor, output);
    }

    vector<int> primes(double input, int divisor, vector<int> output) {        
        while (std::fmod(input, divisor) == 0) {
            output.push_back(static_cast<int>(divisor));
            input = input / divisor;
        }
        
        if (input / divisor <= 1) {
            return output;
        }
        
        divisor += 1;
        return primes(input, divisor, output);
    }
}  // namespace prime_factors
