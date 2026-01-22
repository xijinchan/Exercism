#include "hamming.h"
#include <stdexcept>

namespace hamming {
    int compute(string strand_1, string strand_2) {
        if (strand_1.size() != strand_2.size()) {
            throw std::domain_error("Error");
        };
        
        int distance{};
        
        for (unsigned long i = 0; i < strand_1.size(); ++i) {
            if (strand_1[i] == strand_2[i]) {
                continue;
            } else {
                ++distance;
            }
        };
        
        return distance;  
    };
}  // namespace hamming
