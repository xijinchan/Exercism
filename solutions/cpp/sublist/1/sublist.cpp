#include "sublist.h"

namespace sublist {

// TODO: add your solution here

    bool isSubset(vector<int> subset, vector<int> superset) {
        int superset_size = static_cast<int>(superset.size());
        int subset_size = static_cast<int>(subset.size());
        bool match = false;
        
        for (int i = 0; i < (superset_size - subset_size + 1); i++) {
            if (superset[i] == subset[0]) {
                for (int j = 1; j < subset_size; j++) {
                    if (superset[i+j] == subset[j]) {
                        match = true;
                        if (j == subset_size - 1) {
                            return true;
                        }
                        continue;
                    } else {
                        match = false;
                        continue;
                    }
                }
            }
        }
        return match;
    }
    
    List_comparison sublist(vector<int> list_one, vector<int> list_two) {

        if (list_one == list_two) {
            return List_comparison::equal;            
        }

        if (list_two.empty()) {
            return List_comparison::superlist;
        }

        if (list_one.empty()) {
            return List_comparison::sublist;
        }

        if (isSubset(list_one, list_two)) {
            return List_comparison::sublist;
        }

        if (isSubset(list_two, list_one)) {
            return List_comparison::superlist;
        }

        return List_comparison::unequal;
    }
}  // namespace sublist
