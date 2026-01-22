#if !defined(TRIANGLE_H)
#define TRIANGLE_H
#include <stdexcept>

namespace triangle {
    enum class flavor {
        equilateral,
        isosceles,
        scalene
    };
    triangle::flavor kind(float a, float b, float c) {
        if (a <= 0 or b <= 0 or c <= 0) {
            throw std::domain_error("illegal length(s)");
        }
        if (a + b < c or b + c < a or a + c < b) {
            throw std::domain_error("inequality error");
        }
        if (a == b && b == c) {
            return triangle::flavor::equilateral;
        } else if (a == b or b == c or a == c) {
            return triangle::flavor::isosceles;
        }
        return triangle::flavor::scalene;
    }
}  // namespace triangle

#endif // TRIANGLE_H