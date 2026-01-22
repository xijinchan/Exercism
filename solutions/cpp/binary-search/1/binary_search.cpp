#include "binary_search.h"

namespace binary_search {
    int find(vector<int> data, int number) {
        if (data.size() < 1) {
            throw std::domain_error( "invalid data" );
        }
        int start = 0;
        int end = data.size();
        int middle{};

        for (int i = 0; i < 12; ++i) {
            middle = start + ((end - start) / 2);
            if (start == end or end - start == 1) {
                if (data[start] == number) {
                    return start;
                } else if (data[end] == number) {
                    return end;
                } else {
                    throw std::domain_error( "not found" );
                }
            }
            if (data[middle] == number) {
                return middle;
            } else if (data[middle] > number) {
                end = middle;
            } else {
                start = middle;
            }
        }

        return number;
    }
}  // namespace binary_search
