#include "nth_prime.h"
#include <vector>
#include <stdexcept>

namespace nth_prime {
    int nth(int input) {
        if (input == 0) {
            throw std::domain_error("there is no zeroth prime");
        }
            
        std::vector<int> primes = {};
        bool is_prime = true;
        int candidate = 2;
        
        while (static_cast<int>(primes.size()) != input) {
            is_prime = true;
            if (candidate <= 3) {
                for (int each_number = 2; each_number < candidate; ++each_number) {
                    if (candidate % each_number == 0) {
                        is_prime = false;
                        break;
                    } else {
                        continue;
                    }
                }
            } else {
                for (int i = 0; i < static_cast<int>(primes.size()); ++i) {
                    if (candidate % primes[i] == 0) {
                        is_prime = false;
                        break;
                    } else {
                        continue;
                    }
                }
            }
            if (is_prime == true) primes.push_back(candidate);
            if (static_cast<int>(primes.size()) == input) return candidate;
            if (candidate >= 3) {
                candidate += 2;
            } else {
                candidate += 1;
            }
        }
        throw std::runtime_error("nth value not found");
    }
}  // namespace nth_prime
