#if !defined(GRADE_SCHOOL_H)
#define GRADE_SCHOOL_H
#include <string>
#include <vector>
#include <map>
#include <algorithm>

namespace grade_school {
    class school {
        public:
        std::map<int, std::vector<std::string>> roster_{};
        auto roster() const {
            return roster_;
        };
        void add(std::string name_, int grade_) {
            roster_[grade_].push_back(name_);
            sort(roster_[grade_].begin(), roster_[grade_].end());
        };
        std::vector<std::string> grade(int grade_) const {
            // Return a copy of the vector, not a reference, to avoid changing vector
            auto roster_copy = roster_.find(grade_);
            if (roster_copy != roster_.end()) {
                return roster_copy->second; // Return vector 2nd dimension item(s)
            }
            return {}; // Return an empty vector if grade not found
        };
    };
}  // namespace grade_school

#endif // GRADE_SCHOOL_H