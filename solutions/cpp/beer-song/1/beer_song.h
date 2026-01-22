#if !defined(BEER_SONG_H)
#define BEER_SONG_H
#include <string>
#include <vector>

using std::string;
using std::vector;

namespace beer_song {
    string verse(int number);
    string sing(int start_verse, int end_verse=0);
}  // namespace beer_song

#endif // BEER_SONG_H