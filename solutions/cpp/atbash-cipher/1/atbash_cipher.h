#if !defined(ATBASH_CIPHER_H)
#define ATBASH_CIPHER_H
#include <string>
#include <vector>
#include <cctype>
#include <algorithm>

using std::string;

namespace atbash_cipher {
    string encode(string input);
    string decode(string input);
    string remove_spaces(string& s);
}  // namespace atbash_cipher

#endif // ATBASH_CIPHER_H