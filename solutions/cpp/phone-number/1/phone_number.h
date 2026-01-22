#if !defined(PHONE_NUMBER_H)
#define PHONE_NUMBER_H
#include <string>
#include <cctype>
#include <stdexcept>

using std::string;

namespace phone_number {
    class phone_number {
        private:
            string number_{};
            string number_formatted{};
        public:
            phone_number(string input);
            string number();
            string area_code();
            string exchange_code();
            operator string() const;
    };

}  // namespace phone_number

#endif // PHONE_NUMBER_H