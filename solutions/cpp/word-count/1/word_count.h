#if !defined(WORD_COUNT_H)
#define WORD_COUNT_H
#include <string>
#include <map>
#include <boost/algorithm/string.hpp>

using std::string;
using std::map;

namespace word_count {
    map<string, int> words(string input);
}  // namespace word_count

#endif // WORD_COUNT_H