#if !defined(PRIME_FACTORS_H)
#define PRIME_FACTORS_H
#include <vector>
#include <cmath>

using std::vector;

namespace prime_factors {
    vector<int> of(int input);
    vector<int> primes(double input, int divisor, vector<int> output);
}  // namespace prime_factors

#endif // PRIME_FACTORS_H