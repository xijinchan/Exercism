#if !defined(COMPLEX_NUMBERS_H)
#define COMPLEX_NUMBERS_H
#include <cmath>

namespace complex_numbers {
    class Complex {
        public:
            Complex(double real_new, double imag_new);
            double real_{};
            double imag_{};
            double real() const;
            double imag() const;
            double abs() const;
            Complex conj() const;
            Complex exp() const;
            Complex operator+ (const Complex& rhs) const;
            Complex operator- (const Complex& rhs) const;
            Complex operator* (const Complex& rhs) const;
            Complex operator/ (const Complex& rhs) const;
            Complex operator+ (const double& rhs) const;
            Complex operator- (const double& rhs) const;
            Complex operator* (const double& rhs) const;
            Complex operator/ (const double& rhs) const;
    };

    Complex operator+ (double lhs, const Complex& rhs);
    Complex operator- (double lhs, const Complex& rhs);
    Complex operator* (double lhs, const Complex& rhs);
    Complex operator/ (double lhs, const Complex& rhs);

}  // namespace complex_numbers

#endif  // COMPLEX_NUMBERS_H
