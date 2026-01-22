#if !defined(CRYPTO_SQUARE_H)
#define CRYPTO_SQUARE_H

#include <string>
#include <cctype>
#include <cmath>
#include <vector>

using std::string;
using std::vector;

namespace crypto_square {
    class cipher {
        private:
            string text_original{};
            string text_normalized{};
        public:
            cipher(string input);
            string normalized_cipher_text();
    };
}  // namespace crypto_square

#endif // CRYPTO_SQUARE_H