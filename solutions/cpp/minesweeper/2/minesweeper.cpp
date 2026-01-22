#include "minesweeper.h"

namespace minesweeper {

// TODO: add your solution here
    vector<string> annotate(vector<string> input) {
        if (input.empty()) {
            return {};
        }
        
        int no_of_cols = input[0].size();
        int no_of_rows = input.size();

        // 1. create mine-count vector with n elements where n == total no of positions
        
        vector<int> row_int(no_of_cols);
        vector<vector<int>> mine_count(no_of_rows, row_int);

        string row_string(no_of_cols, ' ');
        vector<string> output(no_of_rows, row_string);
        

        // 2. go through input vector and if mine, add mine to position and add +1 to surrounding positions in mine-count vector
        
        for (int i = 0; i < no_of_cols; i++) {
            for (int j = 0; j < no_of_rows; j++) {
                if (input[j][i] == '*') {
                    output[j][i] = '*';
                    if (j > 0) { // position N
                        mine_count[j-1][i] += 1;
                        if (i < no_of_cols - 1) { // position NE
                            mine_count[j-1][i+1] += 1;
                        }
                        if (i > 0) { // position NW
                            mine_count[j-1][i-1] += 1;
                        }
                    }
                    if (i < no_of_cols - 1) { // position E
                        mine_count[j][i+1] += 1;
                    }
                    if (j < no_of_rows - 1) { // position S
                        mine_count[j+1][i] += 1;
                        if (i < no_of_cols - 1) { // position SE
                            mine_count[j+1][i+1] += 1;
                        }
                        if (i > 0) { // position SW
                            mine_count[j+1][i-1] += 1;
                        }
                    }
                    if (i > 0) { // position W
                        mine_count[j][i-1] += 1;
                    }
                }
            }
        }
        
        
        // 3. add mine_count counts to output vector

        for (int i = 0; i < no_of_cols; i++) {
            for (int j = 0; j < no_of_rows; j++) {
                if (output[j][i] != '*') {
                    if (mine_count[j][i] != 0) {
                        output[j][i] = '0' + mine_count[j][i];
                    }
                }
            }
        }
            
        return output;
    }
}  // namespace minesweeper
