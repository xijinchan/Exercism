# -*- coding: utf-8 -*-
from datetime import datetime

'''    Refactoring done:
Replaced repeated code with functions
Replaced string code blocks with fstrings
Reduced code repetition across locales, merged into one with if conditionals used for code unique to locale
Replaced block of ifs with if any()
Replaced loops with list comprehension

See 'Refactored' entries below '''

class LedgerEntry:
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry

# Refactored: replaced repeated codeblocks with function
def write_entry_change_to_table(locale, currency, entrychange):
    if locale == 'NL':
        change_str = f'{currency} '
        if entrychange < 0:
            change_str += '-'
        delimiter_1, delimiter_2 = '.', ','
    else:
        change_str = ''
        if entrychange < 0:
            change_str = '('
        change_str += f'{currency}'
        delimiter_1, delimiter_2 = ',','.'
    change_currency = abs(int(entrychange / 100.0))
    currency_parts = []
    while change_currency > 0:
        currency_parts.insert(0, str(change_currency % 1000))
        change_currency = change_currency // 1000
    # Refactored: replaced code blocks with fstrings
    if len(currency_parts) == 0:
        change_str += f'0{delimiter_2}'
    else:
        change_str += f'{delimiter_1}'.join([k for k in currency_parts]) + f'{delimiter_2}'
    change_cents = abs(entrychange) % 100
    change_cents = str(change_cents)
    if len(change_cents) < 2:
        change_cents = '0' + change_cents
    change_str += change_cents
    if locale == 'NL':
        return ' ' * (12 - len(change_str)) + change_str + f"{' '}"
    else:
        return ' ' * (12 - len(change_str)) + change_str + f"{')' if entrychange < 0 else ' '}"
        

# Refactored: reduced code repetition across locales, merged into one with if conditionals used for code unique to locale
def format_entries(currency, locale, entries):
    # Generate Header Row
    # Refactored: deleted superfluous string concatenation
    if locale == 'en_US':
        table = 'Date       | Description               | Change       '
    elif locale == 'nl_NL':
        table = 'Datum      | Omschrijving              | Verandering  '

    while len(entries) > 0:
        table += '\n'

        # Find next entry in order
        # Refactored: replaced block of ifs with if any()
        min_entry_index = -1
        for i in range(len(entries)):
            entry = entries[i]
            if i == 0: min_entry_index = i
            min_entry = entries[min_entry_index]
            if any([
                entry.date < min_entry.date,
                entry.date == min_entry.date and entry.change < min_entry.change,
                entry.date == min_entry.date and entry.change == min_entry.change and entry.description < min_entry.description
            ]):
                min_entry_index = i
                continue

        entry = entries[min_entry_index]
        entries.pop(min_entry_index)

        # Write entry date to table
        month = entry.date.month
        day = entry.date.day
        year = entry.date.year

        # Refactored: replaced string codeblock with fstrings
        if locale == 'en_US':
            table += f'{month if month > 9 else "0" + str(month)}/{day if day > 9 else "0" + str(day)}/{("0" * (len(str(year)) - 4)) + str(year)} | '
        elif locale == 'nl_NL':
            table += f'{day if day > 9 else "0" + str(day)}-{month if month > 9 else "0" + str(month)}-{("0" * (len(str(year)) - 4)) + str(year)} | '
            

        # Write entry description to table
        # Truncate if necessary
        # Refactored: replaced loops with list comprehension
        if len(entry.description) > 25:
            table += ''.join([str(entry.description[k]) for k in range(22)]) + '... | '
        else:
            table += ''.join([entry.description[k] if len(entry.description) > k else ' ' for k in range(25)]) + ' | '

            # Write entry change to table
            # Refactored: replaced repeated codeblocks with function
        if currency == 'USD': currency_symbol = '$'
        if currency == 'EUR': currency_symbol = '€'
        if locale == 'en_US': locale_symbol = 'US'
        if locale == 'nl_NL': locale_symbol = 'NL'
            
        table += write_entry_change_to_table(locale_symbol, currency_symbol, entry.change)

    return table