#include "power_of_troy.h"

namespace troy {    
    void give_new_artifact(human& human_, std::string artifact_name) {
        artifact new_artifact = artifact(artifact_name);
        human_.possession = std::make_unique<artifact>(new_artifact);
    }
    
    void exchange_artifacts(std::unique_ptr<artifact>& human_1_possession, std::unique_ptr<artifact>& human_2_possession) {
        std::swap(human_1_possession, human_2_possession);
    }
    
    void manifest_power(human& human_, std::string new_power_) {
        power new_power = power(new_power_);
        human_.own_power = std::make_shared<power>(new_power);
    }
    
    void use_power(human& caster, human& target) {
        target.influenced_by = caster.own_power;
    }
    
    int power_intensity(human& human) {
        if (human.own_power == nullptr) {
            return 0;
        }
        return human.own_power.use_count();
    }
}  // namespace troy
