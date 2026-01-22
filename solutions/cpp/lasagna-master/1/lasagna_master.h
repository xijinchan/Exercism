#pragma once
#include <vector>
#include <algorithm>
#include <string>

using std::vector;
using std::string;

namespace lasagna_master {
    
    struct amount {
        int noodles;
        double sauce;
    };
    
    int preparationTime(vector<string> layers, int time_per_layer=2);
    amount quantities(vector<string> layers);
    void addSecretIngredient(vector<string>& myList, vector<string> friendsList);
    vector<double> scaleRecipe(vector<double> amounts_per_2_portions, int number_of_portions);
    void addSecretIngredient(vector<string>& myList, string secret_ingredient);

}  // namespace lasagna_master
