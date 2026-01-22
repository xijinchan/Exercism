#include "reverse_string.h"

namespace reverse_string {
    std::string reverse_string(std::string string_) {
        std::string reversed = "";
        for (int i = string_.length() - 1; i >= 0; --i) {
            reversed += string_.at(i);
        }
        return reversed;
    }
}  // namespace reverse_string
