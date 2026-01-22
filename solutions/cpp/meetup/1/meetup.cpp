#include "meetup.h"

namespace meetup {
    scheduler::scheduler(boost::date_time::months_of_year month_, int year_) {
        month = month_;
        year = year_;
        first_date = boost::gregorian::date(year_, month_, 1);
        last_date = first_date + boost::gregorian::months(1) - boost::gregorian::days(1);
        first_weekday = first_date.day_of_week();
        last_weekday = last_date.day_of_week();
    }


    boost::gregorian::date scheduler::teenth(int day_) const {
        if ((first(day_) + boost::gregorian::days(7)).day() > 12) {
            return first(day_) + boost::gregorian::days(7);
        }
        if ((first(day_) + boost::gregorian::days(14)).day() < 20) {
            return first(day_) + boost::gregorian::days(14);
        }
        return boost::gregorian::date(1900, 1, 1); // default return 
    }

    boost::gregorian::date scheduler::monteenth() const {        
        return teenth(1);
    }
    boost::gregorian::date scheduler::tuesteenth() const {
        return teenth(2);
    }
    boost::gregorian::date scheduler::wednesteenth() const {
        return teenth(3);
    }
    boost::gregorian::date scheduler::thursteenth() const {
        return teenth(4);
    }
    boost::gregorian::date scheduler::friteenth() const {
        return teenth(5);
    }
    boost::gregorian::date scheduler::saturteenth() const {
        return teenth(6);
    }
    boost::gregorian::date scheduler::sunteenth() const {
        return teenth(0);
    }


    boost::gregorian::date scheduler::first(int day_) const {
        for (int i = 0; i < 7; ++i) {
            if ((first_weekday + i) % 7 == day_) {
                return boost::gregorian::date(year, month, 1 + i);
            }
        }
        return boost::gregorian::date(1900, 1, 1); // default return
    }

    boost::gregorian::date scheduler::first_monday() const {
        return first(1);
    }

    boost::gregorian::date scheduler::first_tuesday() const {
        return first(2);
    }
    boost::gregorian::date scheduler::first_wednesday() const {
        return first(3);
    }
    boost::gregorian::date scheduler::first_thursday() const {
        return first(4);
    }
    boost::gregorian::date scheduler::first_friday() const {
        return first(5);
    }
    boost::gregorian::date scheduler::first_saturday() const {
        return first(6);
    }
    boost::gregorian::date scheduler::first_sunday() const {
        return first(0);
    }


    boost::gregorian::date scheduler::second_monday() const {
        return first(1) + boost::gregorian::days(7);
    }
    boost::gregorian::date scheduler::second_tuesday() const {
        return first(2) + boost::gregorian::days(7);
    }
    boost::gregorian::date scheduler::second_wednesday() const {
        return first(3) + boost::gregorian::days(7);
    }
    boost::gregorian::date scheduler::second_thursday() const {
        return first(4) + boost::gregorian::days(7);
    }
    boost::gregorian::date scheduler::second_friday() const {
        return first(5) + boost::gregorian::days(7);
    }
    boost::gregorian::date scheduler::second_saturday() const {
        return first(6) + boost::gregorian::days(7);
    }
    boost::gregorian::date scheduler::second_sunday() const {
        return first(0) + boost::gregorian::days(7);
    }


    boost::gregorian::date scheduler::third_monday() const {
        return first(1) + boost::gregorian::days(14);
    }
    boost::gregorian::date scheduler::third_tuesday() const {
        return first(2) + boost::gregorian::days(14);
    }
    boost::gregorian::date scheduler::third_wednesday() const {
        return first(3) + boost::gregorian::days(14);
    }
    boost::gregorian::date scheduler::third_thursday() const {
        return first(4) + boost::gregorian::days(14);
    }
    boost::gregorian::date scheduler::third_friday() const {
        return first(5) + boost::gregorian::days(14);
    }
    boost::gregorian::date scheduler::third_saturday() const {
        return first(6) + boost::gregorian::days(14);
    }
    boost::gregorian::date scheduler::third_sunday() const {
        return first(0) + boost::gregorian::days(14);
    }


    boost::gregorian::date scheduler::fourth_monday() const {
        return first(1) + boost::gregorian::days(21);
    }
    boost::gregorian::date scheduler::fourth_tuesday() const {
        return first(2) + boost::gregorian::days(21);
    }
    boost::gregorian::date scheduler::fourth_wednesday() const {
        return first(3) + boost::gregorian::days(21);
    }
    boost::gregorian::date scheduler::fourth_thursday() const {
        return first(4) + boost::gregorian::days(21);
    }
    boost::gregorian::date scheduler::fourth_friday() const {
        return first(5) + boost::gregorian::days(21);
    }
    boost::gregorian::date scheduler::fourth_saturday() const {
        return first(6) + boost::gregorian::days(21);
    }
    boost::gregorian::date scheduler::fourth_sunday() const {
        return first(0) + boost::gregorian::days(21);
    }


    boost::gregorian::date scheduler::last(int day_) const {
        for (int i = 0; i < 7; ++i) {
            if ((last_weekday - i + 7) % 7 == day_) {
                return boost::gregorian::date(last_date.year(), last_date.month(), last_date.day() - i);
            }
        }
        return boost::gregorian::date(1900, 1, 1); // default return
    }

    boost::gregorian::date scheduler::last_monday() const {
        return last(1);
    }    
    boost::gregorian::date scheduler::last_tuesday() const {
        return last(2);
    }
    boost::gregorian::date scheduler::last_wednesday() const {
        return last(3);
    }
    boost::gregorian::date scheduler::last_thursday() const {
        return last(4);
    }
    boost::gregorian::date scheduler::last_friday() const {
        return last(5);
    }
    boost::gregorian::date scheduler::last_saturday() const {
        return last(6);
    }
    boost::gregorian::date scheduler::last_sunday() const {
        return last(0);
    }


}  // namespace meetup
