#if !defined(RNA_TRANSCRIPTION_H)
#define RNA_TRANSCRIPTION_H
#include <string>

namespace rna_transcription {
    using std::string;

    char to_rna(char char_);
    string to_rna(string strand);
}  // namespace rna_transcription

#endif // RNA_TRANSCRIPTION_H