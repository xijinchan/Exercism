#include "complex_numbers.h"

namespace complex_numbers {
    Complex::Complex(double real_new, double imag_new) {
        real_ = real_new;
        imag_ = imag_new;
    }
    double Complex::real() const {
        return real_;
    }
    double Complex::imag() const {
        return imag_;
    }
    double Complex::abs() const {
        return sqrt(pow(real_, 2) + pow(imag_, 2));
    }
    Complex Complex::conj() const {
        return Complex(real_, imag_ * -1);
    }
    Complex Complex::exp() const {
        return pow(std::exp(1.0) , real_) * Complex(cos(imag_), sin(imag_));
    }

    // rhs and complex operations
    Complex Complex::operator+ (const Complex& rhs) const {
        return Complex(real_ + rhs.real_, imag_ + rhs.imag_);
    }
    Complex Complex::operator- (const Complex& rhs) const {
        return Complex(real_ - rhs.real_, imag_ - rhs.imag_);
    }
    Complex Complex::operator* (const Complex& rhs) const {
        return Complex(real_ * rhs.real_ - imag_ * rhs.imag_, imag_ * rhs.real_ + real_ * rhs.imag_);
    }
    Complex Complex::operator/ (const Complex& rhs) const {
        return Complex((real_ * rhs.real_ + imag_ * rhs.imag_) / (pow(rhs.real_, 2) + pow(rhs.imag_, 2)) , (imag_ * rhs.real_ - real_ * rhs.imag_) / (pow(rhs.real_, 2) + pow(rhs.imag_, 2)));
    }
    Complex Complex::operator+ (const double& rhs) const {
        return Complex(real_ + rhs, imag_);
    }
    Complex Complex::operator- (const double& rhs) const {
        return Complex(real_ - rhs, imag_);
    }
    Complex Complex::operator* (const double& rhs) const {
        return Complex(real_ * rhs, imag_ * rhs);
    }
    Complex Complex::operator/ (const double& rhs) const {
        return Complex(real_ / rhs, imag_ / rhs);
    }

    // lhs and complex operations
    Complex operator+ (double lhs, const Complex& rhs) {
        return Complex(lhs + rhs.real_, rhs.imag_);
    }
    Complex operator- (double lhs, const Complex& rhs) {
        return Complex(lhs - rhs.real_, 0 - rhs.imag_);
    }
    Complex operator* (double lhs, const Complex& rhs) {
        return Complex(lhs * rhs.real_, lhs * rhs.imag_);
    }
    Complex operator/ (double lhs, const Complex& rhs) {
        return Complex(lhs * rhs.real_ / (pow(rhs.real_, 2) + pow(rhs.imag_, 2)), lhs * rhs.imag_ / (pow(rhs.real_, 2) + pow(rhs.imag_, 2)) * -1);
    }

}  // namespace complex_numbers
