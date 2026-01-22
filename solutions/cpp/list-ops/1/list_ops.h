#pragma once

#include <vector>

using std::vector;

namespace list_ops {

// TODO: add your solution here
    void append(vector<int>& left, vector<int>& right);
    vector<int> concat(vector<vector<int>> input);
    vector<vector<int>> concat(vector<vector<vector<int>>> input);
    
    template<typename F>
    vector<int> filter(vector<int> input, F lambda_func) {
        vector<int> output{};
        
        for (int i : input) {
            if (lambda_func(i) == true) {
                output.push_back(i);
            }
        }
        return output;
    };

    unsigned long int length(vector<int> input);

    template<typename F>
    vector<int> map(vector<int> input, F lambda_func) {
        vector<int> output{};
        
        for (int i : input) {
            output.push_back(lambda_func(i));
        }
        return output;
    };

    template<typename F>
    int foldl(vector<int> input, int acc, F lambda_func) {
        if (input.empty()) {
            return acc;
        }
        int output = lambda_func(acc, input[0]);

        for (int i = 1; i < static_cast<int>(input.size()); i++) {
            output = lambda_func(output, input[i]);
        }
        return output;
    }

    template<typename F>
    double foldl(vector<double> input, double acc, F lambda_func) {
        if (input.empty()) {
            return acc;
        }
        double output = lambda_func(acc, input[0]);

        for (double i = 1; i < static_cast<int>(input.size()); i++) {
            output = lambda_func(output, input[i]);
        }
        return output;
    }

    template<typename F>
    int foldr(vector<int> input, int acc, F lambda_func) {
        if (input.empty()) {
            return acc;
        }
        int output = lambda_func(acc, input[static_cast<int>(input.size())-1]);

        for (int i = static_cast<int>(input.size())-2; i > -1; i--) {
            output = lambda_func(output, input[i]);
        }
        return output;
    }

    template<typename F>
    double foldr(vector<double> input, double acc, F lambda_func) {
        if (input.empty()) {
            return acc;
        }
        double output = lambda_func(acc, input[static_cast<int>(input.size())-1]);

        for (double i = static_cast<int>(input.size())-2; i > -1; i--) {
            output = lambda_func(output, input[i]);
        }
        return output;
    }

    vector<int> reverse(vector<int> input);
    vector<vector<int>> reverse(vector<vector<int>> input);
    
}  // namespace list_ops
