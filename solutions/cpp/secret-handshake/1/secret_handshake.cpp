#include "secret_handshake.h"

namespace secret_handshake {
    std::vector<string> commands(int input) {
        
        // convert to binary
        int remainder = 0;
        int quotient = input;
        string input_binary = "";
        
        while (quotient >= 1) {
            remainder = quotient % 2;
            quotient = quotient / 2;
            input_binary = std::to_string(remainder) + input_binary;
        } 

        // translate actions
        std::vector<string> actions = {"wink", "double blink", "close your eyes", "jump"};
        std::vector<string> output = {};
        bool reverse = false;

        // evaluate left most for reversal
        if (input_binary.length() > 4 and input_binary.substr(0, 1) == "1") {
            reverse = true;
            input_binary = input_binary.substr(1, input_binary.length() - 1);
        }

        // make actions list
        for (int i = 0; i < static_cast<int>(input_binary.length()); ++i) {
            if (input_binary[input_binary.length() - 1 - i] == '1') {
                output.push_back(actions[i]);
            }
        }

        if (reverse == true) {
            std::reverse(output.begin(), output.end());
        }
        
        return output;
    }
}  // namespace secret_handshake
