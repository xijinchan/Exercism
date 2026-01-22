#include "bob.h"

namespace bob {
    string hey(string hey_bob) {
        string bob_response{};

        if (hey_bob.empty() || regex_match(hey_bob, regex("^\\s*$"))) {
            bob_response = "Fine. Be that way!";
        } else if (regex_match(hey_bob, regex("[A-Z? %^*@#$(*^]+")) and hey_bob.back() == '?') {
            if (regex_search(hey_bob, regex("[a-zA-Z]")) == false) {
                bob_response = "Sure.";
            } else {
                bob_response = "Calm down, I know what I'm doing!";
            }
        } else if (regex_match(hey_bob, regex("[A-Z!0-9 ,%^*@#$(*^]+")) and hey_bob.back() != '?') {
            if (regex_search(hey_bob, regex("[a-zA-Z]")) == false) {
                bob_response = "Whatever.";
            } else {
                bob_response = "Whoa, chill out!";
            }
        } else if (hey_bob.back() == '?') {
            bob_response = "Sure.";
        } else if (hey_bob.find("bob") != string::npos) {
            bob_response = "Fine. Be that way!";
        } else if (hey_bob.back() == ' ') {
            if (hey_bob.find("?") != string::npos) {
                bob_response = "Sure.";
            } else {
                bob_response = "Whatever.";
            }
        } else {
            bob_response = "Whatever.";
        }
        
        return bob_response;
    }
}  // namespace bob
