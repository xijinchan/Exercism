#if !defined(SAY_H)
#define SAY_H
#include <string>
#include <stdexcept>
#include <vector>
#include <iostream>

namespace say {
    std::string in_english(long long unsigned int number_);
    std::string convert_chunk(int number);
}  // namespace say

#endif // SAY_H