#if !defined(PERFECT_NUMBERS_H)
#define PERFECT_NUMBERS_H

#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <stdexcept>

using std::string;
using std::vector;

namespace perfect_numbers {  // namespace perfect_numbers
    enum class classification {
        perfect,
        abundant,
        deficient
    };
    
    vector<int> factors(int number) {
        vector<int> factors_{};
        
        for (int i = 1; i <= std::sqrt(number); i++) {
            if (number % i == 0 && i != number && std::find(factors_.begin(), factors_.end(), i) == factors_.end()) {
                factors_.push_back(i);

                if (i > 1) {
                    int j = number / i;

                    if (i != j) {
                        factors_.push_back(j);                      
                    }                      
                } 
            }
        }

        return factors_;
    };
    
    int aliquot_sum(int number) {
        vector<int> factors_ = factors(number);
        int sum{};

        for (int i : factors_) {
            sum += i;
        }

        return sum;
    };
    
    classification classify(int number) {
        if (number < 1) {
            throw std::domain_error("error");
        }
         
        int sum = aliquot_sum(number);

        if (sum == number) {
            return classification::perfect;
        } else if (number < sum) {
            return classification::abundant;
        } else {
            return classification::deficient;
        }
    };
}
#endif  // PERFECT_NUMBERS_H