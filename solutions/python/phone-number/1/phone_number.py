class PhoneNumber:
    def __init__(self, number):
        if len([k for k in number if k.isalpha() is True]) > 0: raise ValueError('letters not permitted')
        punctuation = [',','?','!',',',';',':','—','[',']','{','}','"',"'",'...']
        if len([k for k in number if k in punctuation]) > 0: raise ValueError('punctuations not permitted')

        number_formatted = [k for k in number if k.isnumeric() is True]
        number_formatted = ''.join(number_formatted)
        print(number_formatted)
        
        if len(number_formatted) < 10: raise ValueError("incorrect number of digits")
        if len(number_formatted) > 11: raise ValueError("more than 11 digits")
        if len(number_formatted) == 11:
            if number_formatted[0] == '1':
                number_formatted = number_formatted[1:]
            else:
                raise ValueError("11 digits must start with 1")
        if len(number_formatted) == 10:
            if number_formatted[0] == '0': raise ValueError('area code cannot start with zero')
            if number_formatted[0] == '1': raise ValueError('area code cannot start with one')
            if number_formatted[3] == '0': raise ValueError('exchange code cannot start with zero')
            if number_formatted[3] == '1': raise ValueError('exchange code cannot start with one')

        self.number = number_formatted
        self.area_code = number_formatted[0:3]

    def pretty(self):
        return '(' + self.number[0:3] + ')-' + self.number[3:6] + '-' + self.number[6:]