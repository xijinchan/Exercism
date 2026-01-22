#include "zebra_puzzle.h"

#include <iostream>

namespace zebra_puzzle {
    Solution solve() {
        Solution solution;

        House red, green, ivory, yellow, blue;
        Person p1, p2, p3, p4, p5;
        
        vector<House*> Houses = {&yellow, &blue, &ivory, &green, &red};
        vector<Person*> Persons = {&p1, &p2, &p3, &p4, &p5};

        // The Englishman lives in the red house.
        p1.nationality = "Englishman";
        red.person = &p1;

        // The Spaniard owns the dog.
        p2.nationality = "Spaniard";
        p2.animal = "dog";

        // The Ukrainian drinks tea.
        p3.nationality = "Ukrainian";
        p3.drink = "tea";

        // The Norwegian lives in the first house.
        p4.nationality = "Norwegian";

        // The Japanese person plays chess.
        p5.nationality = "Japanese";
        p5.hobbie = "chess";
        
        // The Norwegian lives next to the blue house. (& The Norwegian lives in the first house.)
        blue.position = 2; // red is English thus not 1. ivory, green = 3,4 or 4,5 so yellow is 1
        yellow.position = 1; // painter's house, blue animal is "horse", Norwegian lives in house 1
        yellow.person = &p4; // Norwegian lives in house 1 
        p4.hobbie = "painting"; // The person in the yellow house is a painter.

        
        // The green house is immediately to the right of the ivory house. Ivory, green is 3,4 or 4,5. Red is remaining 5 or 3.
        struct PositionSetup {
            int red;
            int ivory;
            int green;
        };
        
        std::vector<PositionSetup> setups = {
            {5, 3, 4},
            {3, 4, 5}
        };

        bool solved = false;

        for (const auto& setup : setups) { // for red, ivory, green 3,4,5 and 5,3,4
            red.position = setup.red;
            ivory.position = setup.ivory;
            green.position = setup.green;
        
            vector<Person*> persons_remaining = {&p2, &p3, &p5};
            vector<std::string> animals_remaining = {"fox", "horse", "snail", "zebra"};
            vector<std::string> drinks_remaining = {"coffee", "milk", "orange juice", "water"};
            vector<std::string> hobbies_remaining = {"dancing", "football", "reading"};

            // solve with permutations for remaining
            do { // persons_remaining
                    do { // animals_remaining
                            do { // drinks_remaining
                                    do { // hobbies_remaining
                                            blue.person = persons_remaining[0];
                                            ivory.person = persons_remaining[1];
                                            green.person = persons_remaining[2];
    
                                            p1.animal = animals_remaining[0];
                                            p3.animal = animals_remaining[1];
                                            p4.animal = animals_remaining[2];
                                            p5.animal = animals_remaining[3];
    
                                            p1.drink = drinks_remaining[0];
                                            p2.drink = drinks_remaining[1];
                                            p4.drink = drinks_remaining[2];
                                            p5.drink = drinks_remaining[3];
    
                                            p1.hobbie = hobbies_remaining[0];
                                            p2.hobbie = hobbies_remaining[1];
                                            p3.hobbie = hobbies_remaining[2];
    
                                            if (check_constraints(p1, p2, p3, p4, p5, red, ivory, green, yellow, blue) == true) {
                                                solved = true;
                                                break;
                                            }
                                    } while (std::next_permutation(hobbies_remaining.begin(), hobbies_remaining.end()));
                                if (solved == true) { break;}
                            } while (std::next_permutation(drinks_remaining.begin(), drinks_remaining.end()));
                        if (solved == true) { break;}
                    } while (std::next_permutation(animals_remaining.begin(), animals_remaining.end()));
                if (solved == true) { break;}
            } while (std::next_permutation(persons_remaining.begin(), persons_remaining.end()));
        if (solved == true) { break;}
        }
            
        for (Person* p : Persons) {
            if (p->drink == "water") {
                solution.drinksWater = p->nationality;
            }
            if (p->animal == "zebra") {
                solution.ownsZebra = p->nationality;
            }
        }
        
        return solution;
    }

    bool check_constraints(Person& p1, Person& p2, Person& p3, Person& p4, Person& p5, House& red, House& ivory, House& green, House& yellow, House& blue) {
        std::vector<House*> Houses = {&yellow, &blue, &red, &ivory, &green};

        // The person in the green house drinks coffee.
        if (green.person->drink != "coffee") {
            return false;
        }

        // The snail owner likes to go dancing.
        for (Person* p : vector<Person*> {&p1, &p3, &p4, &p5}) {
            if (p->animal == "snail") {
                if (p->hobbie != "dancing") {
                    return false;
                }
            }
        }

        // The person in the middle house drinks milk.
        for (House* h : vector<House*> {&red, &ivory}) {
            if (h->position == 3) {
                if (h->person->drink != "milk") {
                    return false;
                }
            }
        }
        
        // The person who enjoys reading lives in the house next to the person with the fox.
        bool reading_next_to_fox = false;
        for (Person* p : vector<Person*> {&p2, &p3, &p4, &p5}) {
            if (p->hobbie == "reading") {
                for (int i = 1; i < 4; i++) {
                    if (Houses[i]->person == p) {
                        if (Houses[i-1]->person->animal == "fox" || Houses[i+1]->person->animal == "fox") {
                            reading_next_to_fox = true;
                        }
                    }
                } 
            }
        }
        if (reading_next_to_fox == false) {
            return false;
        }

        // The painter's house is next to the house with the horse.
        // ** horse is 2 / blue
        if (blue.person->animal != "horse") {
            return false;
        }
        

        // The person who plays football drinks orange juice.
        for (Person* p : vector<Person*> {&p1, &p2, &p3}) {
            if (p->hobbie == "football") {
                if(p->drink != "orange juice") {
                    return false;
                }
            }
        }

        return true;
    }
    
}  // namespace zebra_puzzle