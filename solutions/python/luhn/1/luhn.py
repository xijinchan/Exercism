class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        digits = self.card_num
        digits = digits.replace(' ','')

        if any((len(self.card_num) < 2, digits == '0')): return False
        try:
            int(digits)
        except:
            return False

        digits_2nds = [int(digits[i]) for i in range(-2,-(len(digits)+1),-2)]
        digits_1sts = [int(digits[i]) for i in range(-1,-(len(digits)+1),-2)]
        digits_2nds_doubled = [i * 2 - 9 if i * 2 > 9 else i * 2 for i in digits_2nds]

        total = sum(digits_1sts) + sum(digits_2nds_doubled)
        
        return bool(total % 10 == 0)