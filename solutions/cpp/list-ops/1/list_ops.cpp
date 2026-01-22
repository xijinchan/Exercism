#include "list_ops.h"

namespace list_ops {

// TODO: add your solution here
    void append(vector<int>& left, vector<int>& right) {
        for (int i : right) {
            left.push_back(i);
        }
    }

    vector<int> concat(vector<vector<int>> input) {
        vector<int> output{};
        for (vector<int> v : input) {
            for (int i : v) {
                output.push_back(i);
            }
        }        
        return output;
    }
    vector<vector<int>> concat(vector<vector<vector<int>>> input) {
        vector<vector<int>> output{};
        for (vector<vector<int>> v : input) {
            for (vector<int> w : v) {
                    output.push_back(w);
            }
        }
        return output;
    }
    unsigned long int length(vector<int> input) {
        unsigned long int count{};
        for (int i : input) {
            (void)i;
            count += 1;
        }
        return count;
    }

    vector<int> reverse(vector<int> input) {
        vector<int> output{};
        
        for (int i : input) {
            output.insert(output.begin(), i);
        }
        return output;
    }

    vector<vector<int>> reverse(vector<vector<int>> input) {
        vector<vector<int>> output{};
        
        for (vector<int> i : input) {
            output.insert(output.begin(), i);
        }
        return output;
    }

}  // namespace list_ops
