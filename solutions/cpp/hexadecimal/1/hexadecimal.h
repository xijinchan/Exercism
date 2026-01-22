#if !defined(HEXADECIMAL_H)
#define HEXADECIMAL_H
#include <string>
#include <cmath>


using std::string;

namespace hexadecimal {
    int convert(string hex) {
        int total{};

        for (int i = 0; i < static_cast<int>(hex.size()); i++) {
            int power = static_cast<int>(hex.size()) - 1 - i;
            
            if (47 < hex[i] && hex[i] < 58) { // 1-9
                total += (hex[i] - '0') * pow(16, power);
            } else if (96 < hex[i] && hex[i] < 103) { // a-f
                total += (hex[i] - 87) * pow(16, power);
            } else {
                return 0;
            }
        }

        return total;
    }
}  // namespace hexadecimal

#endif // HEXADECIMAL_H