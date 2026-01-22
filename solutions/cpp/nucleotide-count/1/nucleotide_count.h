#if !defined(NUCLEOTIDE_COUNT_H)
#define NUCLEOTIDE_COUNT_H
#include <string>
#include <map>
#include <vector>
#include <stdexcept>

namespace nucleotide_count {
    using std::string;

    std::map<char, int> count(string chain);
}  // namespace nucleotide_count

#endif // NUCLEOTIDE_COUNT_H