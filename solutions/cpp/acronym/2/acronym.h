#if !defined(ACRONYM_H)
#define ACRONYM_H
#include <string>
#include <cctype>

using std::string;

namespace acronym {
    string acronym(string input) {
        string output{};
        output += input[0];
        
        for (int i = 1; i < static_cast<int>(input.size()); i++) {
            if (input[i] == ' '&& input[i+1] != '-' && input[i+1] != '_' && i != static_cast<int>(input.size()) - 1) {
                output += toupper(input[i+1]);
            }
            if (input[i] == '-' && input[i+1] != ' ') {
                output += toupper(input[i+1]);
            }
            if (input[i] == '_' && input[i+1] != ' ') {
                output += toupper(input[i+1]);
            }
        }

        return output;
    }
}  // namespace acronym

#endif // ACRONYM_H