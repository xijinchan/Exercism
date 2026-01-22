#if !defined(FOOD_CHAIN_H)
#define FOOD_CHAIN_H
#include <string>
#include <vector>

using std::string;
using std::vector;

namespace food_chain {
    string middle_lines(string animal, int animal_index);
    string verse(int number);
    string verses(int start, int end);
    string sing();
}  // namespace food_chain

#endif // FOOD_CHAIN_H