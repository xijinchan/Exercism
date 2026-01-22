#include "phone_number.h"

namespace phone_number {
    phone_number::phone_number(string input) {
        if (input.substr(0, 2) == "+1") {
            number_formatted = input.substr(3, input.size());
        }
        
        for (int i = 0; i < static_cast<int>(input.size()); i++) {
            if (std::isdigit(input[i])) {
                number_ = number_ + input[i];
            }
        }

        if (number_.size() == 11 && number_[0] == '1') {
            number_ = number_.substr(1, number_.size());
        }
        
        if (number_.size() < 10 || number_.size() > 11) throw std::domain_error("Error");
        if (number_.size() == 11 && number_[0] != '1') throw std::domain_error("Error");
        if (area_code()[0] == '0' || area_code()[0] == '1') throw std::domain_error("Error");
        if (exchange_code()[0] == '0' || exchange_code()[0] == '1') throw std::domain_error("Error");
    }

    string phone_number::number() {
        return number_;
    }

    string phone_number::area_code() {
        return number_.substr(0, 3);
    }

    string phone_number::exchange_code() {
        return number_.substr(3, 6);
    }

    phone_number::operator string() const {
        return number_formatted;
    }
}  // namespace phone_number
