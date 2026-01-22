#include "grains.h"
#include <cmath>

namespace grains {
    double square(double number) {
        double result = pow(2.0, number - 1);
        return result;
    }
    double total() {
        return pow(2, 64);
    }
}  // namespace grains
