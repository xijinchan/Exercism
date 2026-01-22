#include "run_length_encoding.h"

namespace run_length_encoding {

// TODO: add your solution here
    string encode(string input) {
        int counter{1};
        string output{};
        for (int i = 0; i < static_cast<int>(input.size()); i++) {
            if (input[i + 1] == input[i]) {
                counter += 1;
            } else {
                if (counter == 1) {
                    output += input[i];
                } else {
                    output += std::to_string(counter) + input[i];                    
                }
                counter = 1;
            }
        }
        return output;
    }

    string decode(string input) {
        string output{};
        string n_string{};

        for (int i = 0; i < static_cast<int>(input.size()); i++) {
            if (std::isdigit(input[i])) {
                n_string += input[i];
            } else {
                if (n_string == "") {n_string = "1";}
                string fragment(std::stoi(n_string), input[i]);
                output += fragment;
                n_string = "";
            }
        }

        return output;
    }
}  // namespace run_length_encoding
