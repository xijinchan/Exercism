#ifndef AFFINE_CIPHER_H
#define AFFINE_CIPHER_H

#include <string>
#include <iostream>
#include <cmath>

using std::string;

namespace affine_cipher {

// TODO: add your solution here
    string encode(string input, int a, int b);
    string decode(string input, int a, int b);
    long long extended_gcd(long long a, long long m, long long& x, long long& y);
    long long mod_inverse(long long a, long long m);
    bool coprime_check(int a, int m);
}  // namespace affine_cipher

#endif  // AFFINE_CIPHER_H
