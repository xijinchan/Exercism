#include "sum_of_multiples.h"

namespace sum_of_multiples {
    int to(vector<int> base_values, int level) {
        if (base_values.size() == 0) {
            return 0;
        };

        vector<int> multiples = {};
        for (unsigned long i = 0; i < base_values.size(); ++i) {
            int multiplier_max = level / base_values[i];
            if (level % base_values[i] == 0) {
                --multiplier_max;
            }

            for (int k = 1; k <= multiplier_max; ++k) {
                multiples.push_back(base_values[i] * k);
            }
        }
    
        // Sort the vector and remove duplicates
        std::sort(multiples.begin(), multiples.end());
        vector<int>::iterator it = unique(multiples.begin(), multiples.end()); // sorts vector placing duplicates at end
        multiples.resize(distance(multiples.begin(), it)); // resize to remove trailing duplicates

        int output = {};
        for (auto& n : multiples)
            output += n;

        return output;
    };
}  // namespace sum_of_multiples
