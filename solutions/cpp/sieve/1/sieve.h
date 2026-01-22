#if !defined(SIEVE_H)
#define SIEVE_H
#include <stdexcept>
#include <vector>

namespace sieve {
    std::vector<int> primes(int limit);
}  // namespace sieve

#endif // SIEVE_H