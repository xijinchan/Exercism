#include "lasagna_master.h"
#include <iostream>

namespace lasagna_master {
    int preparationTime(vector<string> layers, int time_per_layer) {
        return layers.size() * time_per_layer;
    }
    amount quantities(vector<string> layers) {
        int noodle_layers = std::count(layers.begin(), layers.end(), "noodles");
        int sauce_layers = std::count(layers.begin(), layers.end(), "sauce");
        return {noodle_layers * 50, sauce_layers * 0.2};
    }
    void addSecretIngredient(vector<string>& myList, vector<string> friendsList) {
        myList.back() = friendsList.back();
    }
    vector<double> scaleRecipe(const vector<double> quantities, int number_of_portions) {
        vector<double> scaled = {};
        for (int i = 0; i < static_cast<int>(quantities.size()); ++i) {
            scaled.push_back(quantities[i] / 2 * number_of_portions);
        }
        return scaled;
    }
    void addSecretIngredient(vector<string>& myList, string secret_ingredient) {
        myList.back() = secret_ingredient;
    }


}  // namespace lasagna_master
