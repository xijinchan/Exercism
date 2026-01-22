"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    coordinate = record[1]
    return coordinate


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    number = coordinate[:-1]
    letter = coordinate[-1:]

    formatted_coordinate = (number, letter)

    return formatted_coordinate


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    return bool(convert_coordinate(azara_record[1]) == rui_record[1])


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(azara_record, rui_record) == True:
        combined_record = (azara_record[0],azara_record[1],rui_record[0],rui_record[1],rui_record[2])
        output = combined_record
        print(output)
    else:
        output = 'not a match'

    return output


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    report = ''

    for record in combined_record_group:
        # report = str('(') = report + str(record[0]) + str(record[1]) + str(record[2]) str(')\n')
        report_addition = (record[0],record[2],record[3],record[4])
        report = report + str(report_addition) + str('\n')

    print(report)

    return report