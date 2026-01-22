#if !defined(SERIES_H)
#define SERIES_H
#include <string>
#include <vector>
#include <stdexcept>

using std::string;
using std::vector;

namespace series {
    vector<string> slice(string input, int length);
}  // namespace series

#endif // SERIES_H