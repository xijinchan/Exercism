#if !defined(LARGEST_SERIES_PRODUCT_H)
#define LARGEST_SERIES_PRODUCT_H

#include <string>
#include <stdexcept>

using std::string;

namespace largest_series_product {
    int largest_product(string input, int series_length) {
        if (series_length > static_cast<int>(input.length())) { throw std::domain_error("error");}
        if (input == "" && series_length > 0) { throw std::domain_error("error");}
        if (series_length < 0) { throw std::domain_error("error");}
        
        int largest_product{0};
        string series{};
        int series_product;
        
        for (int i = 0; i < static_cast<int>(input.length()) - series_length + 1; i++) {
            series = input.substr(i, series_length);

            series_product = 1;
            for (auto c : series) {
                if (c < 48 || c > 57) {
                    throw std::domain_error("error");
                }
                series_product = series_product * (static_cast<int>(c) - 48);
            }

            if (series_product > largest_product) {
                largest_product = series_product;
            }
        }
        
        return largest_product;
    }
} // largest_series_product

#endif // LARGEST_SERIES_PRODUCT_H