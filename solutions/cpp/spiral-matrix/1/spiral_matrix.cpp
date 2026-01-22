#include "spiral_matrix.h"

namespace spiral_matrix {

// TODO: add your solution here
    std::vector<std::vector<unsigned int>> spiral_matrix(int size) {

        // create empty vector of vectors
        std::vector<std::vector<unsigned int>> output(size, std::vector<unsigned int>(size, 0));

        int x = 0;
        int y = 0;
        std::string orientation = "R";
        
        for (int i = 0; i < (size * size); i++) {
            if (orientation == "R") {
                if (x == size - 1) { // initial boundary
                    output[y][x] = i + 1;
                    y += 1;
                    orientation = "D";
                } else if (output[y][x+1] == 0) { // fill right
                    output[y][x] = i + 1;
                    x += 1;
                } else { // turn
                    output[y][x] = i + 1;
                    y += 1;
                    orientation = "D";
                }
            } else if (orientation == "D") {
                if (y == size - 1) { // initial boundary
                    output[y][x] = i + 1;
                    x -= 1;
                    orientation = "L";
                } else if (output[y+1][x] == 0) { // fill down
                    output[y][x] = i + 1;
                    y += 1;
                } else { // turn
                    output[y][x] = i + 1;
                    x -= 1;
                    orientation = "L";
                }
            } else if (orientation == "L") {
                if (x == 0) { // initial boundary
                    output[y][x] = i + 1;
                    y -= 1;
                    orientation = "U";
                } else if (output[y][x-1] == 0) { // fill left
                    output[y][x] = i + 1;
                    x -= 1;
                } else { // turn
                    output[y][x] = i + 1;
                    y -= 1;
                    orientation = "U";
                }
            } else if (orientation == "U") {
                if (y == 0) { // initial boundary
                    output[y][x] = i + 1;
                    x += 1;
                    orientation = "R";
                } else if (output[y-1][x] == 0) { // fill up
                    output[y][x] = i + 1;
                    y -= 1;
                } else { // turn
                    output[y][x] = i + 1;
                    x += 1;
                    orientation = "R";
                }
            }
        }
        
        return output;
    }
}  // namespace spiral_matrix
