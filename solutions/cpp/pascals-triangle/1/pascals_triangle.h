#if !defined(PASCALS_TRIANGLE_H)
#define PASCALS_TRIANGLE_H

#include <vector>

namespace pascals_triangle {
    std::vector<std::vector<int>> generate_rows(int no_of_rows) {

        std::vector<std::vector<int>> output{};

        for (int i = 0; i < no_of_rows; i++) {
            
            if (i == 0) {
                output.push_back({1});
            } else {
                std::vector<int> row{};
                
                for (int j = 0; j < static_cast<int>(output[i-1].size() + 1); j++) {
                    if (j == 0 || j == static_cast<int>(output[i-1].size())) {
                        row.push_back(1);
                    } else {
                        int digit{};

                        digit = output[i-1][j-1] + output[i-1][j];
                        row.push_back(digit);
                    }
                }

                output.push_back(row);
            }
        }

    return output;
    }
}  // namespace pascals_triangle

#endif // PASCALS_TRIANGLE_H