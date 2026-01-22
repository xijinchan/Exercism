#if !defined(BINARY_SEARCH_H)
#define BINARY_SEARCH_H

#include <vector>
#include <stdexcept>

using std::vector;

namespace binary_search {
    int find(vector<int> data, int number);
}  // namespace binary_search

#endif // BINARY_SEARCH_H