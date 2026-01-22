#include "flower_field.h"

#include <iostream>

namespace flower_field {

// TODO: add your solution here
    vector<string> annotate(vector<string> input) {
        if (!input.empty()) {
            if (input == vector<string>{""}) { return input;}
            
            int no_of_rows = static_cast<int>(input.size());
            int no_of_cols = static_cast<int>(input[0].size());
        
            vector<string> output{};
            int count{};
            string row_string{};

            for (int i = 0; i < no_of_rows; i++) {
                for (int j = 0; j < no_of_cols; j++) {
                    if (input[i][j] == '*') {
                        row_string += '*';
                        continue;
                    }
                    if (i != 0 && no_of_rows > 1) { // North
                        if (input[i-1][j] == '*') {
                            count += 1;
                        }
                        if (j < no_of_cols - 1) { // NE
                            if (input[i-1][j+1] == '*') {
                                count += 1;
                            }
                        }
                        if (j > 0) { // NW
                            if (input[i-1][j-1] == '*') {
                                count += 1;
                            }
                        }
                    }
                    if (j < no_of_cols - 1) { // East
                        if (input[i][j+1] == '*') {
                            count += 1;
                        }
                    }
                    if (i != no_of_rows - 1 && no_of_rows > 1) { // South
                        if (input[i+1][j] == '*') {
                            count += 1;
                        }
                        if (j < no_of_cols - 1) {
                            if (input[i+1][j+1] == '*') {  // SE
                                count += 1;
                            }
                        }
                        if (j > 0) { // SW
                            if (input[i+1][j-1] == '*') {
                                count += 1;
                            }
                        }
                    }
                    if (j > 0) { // West
                        if (input[i][j-1] == '*') {
                            count += 1;
                        }
                    }
                    
                    if (count == 0) {
                        row_string += ' ';
                    } else {
                        row_string += std::to_string(count);
                    }
                    count = 0;
                }
                output.push_back(row_string);
                row_string = "";
            }
            return output;
        }
        return {};
    }
}  // namespace flower_field
