#include <string>
#include <vector>

namespace election {

// The election result struct is already created for you:

struct ElectionResult {
    // Name of the candidate
    std::string name{};
    // Number of votes the candidate has
    int votes{};
};

// TODO: Task 1
// vote_count takes a reference to an `ElectionResult` as an argument and will
// return the number of votes in the `ElectionResult.

int vote_count(election::ElectionResult& ElectionResult_) {
    return ElectionResult_.votes;
}

// TODO: Task 2
// increment_vote_count takes a reference to an `ElectionResult` as an argument
// and a number of votes (int), and will increment the `ElectionResult` by that
// number of votes.

void increment_vote_count(election::ElectionResult& ElectionResult_, int number_of_votes) {
    ElectionResult_.votes += number_of_votes;
}

// TODO: Task 3
// determine_result receives the reference to a final_count and returns a
// reference to the `ElectionResult` of the new president. It also changes the
// name of the winner by prefixing it with "President". The final count is given
// in the form of a `reference` to `std::vector<ElectionResult>`, a vector with
// `ElectionResults` of all the participating candidates.

election::ElectionResult& determine_result(std::vector<ElectionResult>& final_count) {
    int most_votes{0};
    int most_votes_index{0};
    for (int i{0}; i < final_count.size(); ++i) {
        if (final_count[i].votes > most_votes) {
            most_votes = final_count[i].votes;
            most_votes_index = i;
        }
    }
    final_count[most_votes_index].name = "President " + final_count[most_votes_index].name;
    return final_count[most_votes_index];
}

}  // namespace election