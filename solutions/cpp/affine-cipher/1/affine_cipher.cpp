#include "affine_cipher.h"

namespace affine_cipher {

// TODO: add your solution here
    string encode(string input, int a, int b) {
        if (coprime_check(a, 26) == false) {
            throw std::invalid_argument("Invalid argument");
        }
        
        string output{};
        int char_count{};
        char j{};
        int i{};
        
        for (char letter : input) {
            if (int(letter) < 65 || int(letter) > 122) {
                if (47 < int(letter) && int(letter) < 57) {
                    j = letter;
                } else {
                    continue;
                }
            }
            if (char_count % 5 == 0 && char_count > 0) {
                output += ' ';
            }
            if (int(letter) > 57) {
                i = int(tolower(letter)) - 97;
                j = char(((a * i + b) % 26) + 97);
            }
            output += j;
            char_count += 1;
        }
        
        return output;
    }
 
    string decode(string input, int a, int b) {
        if (coprime_check(a, 26) == false) {
            throw std::invalid_argument("Invalid argument");
        }
        
        int y{};
        char k{};
        string output{};
        
        for (char letter: input) {
            if (letter == ' ') {
                continue;
            }

            if (47 < int(letter) && int(letter) < 57) {
                output += letter;
                continue;
            }
            
            y = int(letter) - 97;
            k = (mod_inverse(a, 26) * (y - b)) % 26;
            if (k < 0) {
                k += 26;
            }
            output += char(k + 'a');
        }

        std::cout << output;
        
        return output;
    }

    // Helper: Extended Euclidean Algorithm
    // Returns gcd(a, m) and sets x, y such that a*x + m*y = gcd
    long long extended_gcd(long long a, long long m, long long& x, long long& y) {
        if (a == 0) {
            x = 0;
            y = 1;
            return m;
        }
        long long x1, y1;
        long long g = extended_gcd(m % a, a, x1, y1);
        x = y1 - (m / a) * x1;
        y = x1;
        return g;
    }

    // Returns the modular multiplicative inverse of a modulo m
    // (i.e. a number x such that (a * x) % m == 1)
    // Returns -1 if the inverse does not exist (gcd(a, m) != 1)
    long long mod_inverse(long long a, long long m) {
        if (m == 1) return 0;               // edge case: mod 1 is always 0
        long long x, y;
        long long g = extended_gcd(a, m, x, y);
        if (g != 1) {
            return -1;                      // inverse does not exist
        }
        // Make the result positive and in range [0, m-1]
        return (x % m + m) % m;
        }

    bool coprime_check(int a, int m) {
        if (m % a == 0) {
            return false;
        }
        for (int p = 2; p < a / 2; p++) {
            if (a % p == 0) {
                if (m % p == 0) {
                    return false;
                }
            }
        }
        return true;
    }

}  // namespace affine_cipher
