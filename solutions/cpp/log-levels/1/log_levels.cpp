#include <string>

namespace log_line{
    std::string message(std::string line) {
        int start_index = line.find(":") + 2;
        return line.substr(start_index);
    }

    std::string log_level(std::string line) {
        int end_index = line.find("]") - 1;
        return line.substr(1, end_index);
    }

    std::string reformat(std::string line) {
        std::string message_ = message(line);
        std::string log_level_ {log_level(line)};
        std::string formatted {message_ + " (" + log_level_ + ")"};
        return formatted;
    }
} // namespace log_line
