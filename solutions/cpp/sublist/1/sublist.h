#pragma once

#include <vector>
#include <algorithm>

using std::vector;

namespace sublist {

enum class List_comparison {
    equal,
    sublist,
    unequal,
    superlist
};

// TODO: add your solution here
    List_comparison sublist(vector<int> list_one, vector<int> list_two);  
    bool isSubset(vector<int> subset, vector<int> superset);
}  // namespace sublist
