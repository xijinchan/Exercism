#if !defined(HAMMING_H)
#define HAMMING_H
#include <string>

namespace hamming {
    using std::string;

    int compute(string strand_1, string strand_2);
}  // namespace hamming

#endif // HAMMING_H