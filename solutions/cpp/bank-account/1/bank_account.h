#if !defined(BANK_ACCOUNT_H)
#define BANK_ACCOUNT_H

#include <stdexcept>
#include <mutex>

namespace Bankaccount {
    enum class Account_status {
        open,
        closed
    };
    class Bankaccount {  // class Bankaccount
        private:
            int balance_{};
            Account_status status{};
            std::mutex mtx;
        public:
            Bankaccount() {
                status = Account_status::closed;
            }
            int balance() {
                std::lock_guard<std::mutex> lock(mtx);
                if (status == Account_status::closed) {
                    throw std::runtime_error("Account closed");
                }
                return balance_;
            }
            void deposit(int value) {
                std::lock_guard<std::mutex> lock(mtx);
                if (status == Account_status::closed) {
                    throw std::runtime_error("Account closed");
                }
                if (value < 0) {
                    throw std::runtime_error("invalid deposit");
                }
                balance_ += value;;
            }
            void withdraw(int value) {
                std::lock_guard<std::mutex> lock(mtx);
                if (status == Account_status::closed) {
                    throw std::runtime_error("Account closed");
                }
                if (value > balance_) {
                    throw std::runtime_error("Withdrawal exceeds balance");
                }
                if (value < 0) {
                    throw std::runtime_error("invalid withdrawal");
                }
                balance_ -= value;
            }
            Bankaccount open() {
                std::lock_guard<std::mutex> lock(mtx);
                if (status == Account_status::open) {
                    throw std::runtime_error("Account already opened");
                }
                if (status == Account_status::closed) {
                    status = Account_status::open;
                }
                status = Account_status::open;
                return Bankaccount();
            };
            void close() {
                std::lock_guard<std::mutex> lock(mtx);
                if (status == Account_status::closed) {
                    throw std::runtime_error("Account already closed");
                }
                status = Account_status::closed;
                balance_ = 0;
            }
    };
}  // namespace Bankaccount

#endif  // BANK_ACCOUNT_H