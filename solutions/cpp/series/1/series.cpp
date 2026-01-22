#include "series.h"

namespace series {
    vector<string> slice(string input, int length) {
        if (length > static_cast<int>(input.size())) throw std::domain_error("input too large");
        if (length <= 0) throw std::domain_error("length needs to be integer");
        
        vector<string> output{};

        for (int i = 0; i + length <= static_cast<int>(input.size()); i++) {
            output.push_back(input.substr(i, length));
        }
        return output;
    }
}  // namespace series
