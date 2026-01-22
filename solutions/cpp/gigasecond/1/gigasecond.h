#if !defined(GIGASECOND_H)
#define GIGASECOND_H
#include <string>
#include "boost/date_time/posix_time/posix_time.hpp"

using std::string;

namespace gigasecond {
    boost::posix_time::ptime advance(boost::posix_time::ptime input);
}  // namespace gigasecond

#endif // GIGASECOND_H