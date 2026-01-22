#if !defined(DARTS_H)
#define DARTS_H

#include <cmath>

namespace darts {
    int score(float x, float y) {
        float distance = sqrt((x * x) + (y * y));
        if (distance > 10) { return 0;}
        if (distance > 5) { return 1;}
        if (distance > 1) { return 5;}
        return 10;
    }
} // namespace darts

#endif //DARTS_H