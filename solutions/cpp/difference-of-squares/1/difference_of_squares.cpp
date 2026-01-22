#include "difference_of_squares.h"
#include <cmath>

namespace difference_of_squares {
    int square_of_sum(int input) {
        int sum = 0;
        for (int i = 1; i <= input; ++i) {
            sum += i;
        }
        return std::pow(sum, 2);
    }
    int sum_of_squares(int input) {
        int squares = 0;
        for (int i = 1; i <= input; ++i) {
            squares += std::pow(i, 2);
        }
        return squares;
    }
    int difference(int input) {
        return square_of_sum(input) - sum_of_squares(input);
    }
}  // namespace difference_of_squares
