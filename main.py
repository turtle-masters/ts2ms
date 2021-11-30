import csv
from pathlib import Path
from os import path


def get_timestamps(input_file):
    reader = csv.reader(input_file)
    output_list = []

    for line in reader:
        output_list.append(line[6])

    return output_list


def convert_to_int(sn):
    number = 0
    i = 0

    for c in sn:
        if c == '0':
            number = number + 0
        elif c == '1':
            number = number + 1
        elif c == '2':
            number = number + 2
        elif c == '3':
            number = number + 3
        elif c == '4':
            number = number + 4
        elif c == '5':
            number = number + 5
        elif c == '6':
            number = number + 6
        elif c == '7':
            number = number + 7
        elif c == '8':
            number = number + 8
        elif c == '9':
            number = number + 9

        if i == 0:
            number = number * 10
        i = i + 1

    return number


def convert_to_ms(to_be_converted):
    output = []

    for ts in to_be_converted:
        hours = convert_to_int(ts[11:13])
        minutes = convert_to_int(ts[14:16])
        seconds = convert_to_int(ts[17:19])
        milliseconds = float(convert_to_int(ts[20:])) / 10

        final = milliseconds + seconds * 1000 + minutes * 60 * 1000 + hours * 60 * 60 * 1000
        output.append(str(final) + '\n')

    return output


def get_output_path(input_path):
    output_string = ''
    file_name = ''

    for part in input_file_path.parts:
        if part[2:] != '.csv':
            output_string = output_string + '\\' + part
        else:
            file_name = part[:-4]

    return output_string[1:], file_name


def write_converted_file(original_file, new_timestamps):
    lines = original_file.read().splitlines()
    first_line_skipped = False
    i = 0

    for line in lines:
        if first_line_skipped:
            lines[i] = line + ', ' + new_timestamps[i]
        else:
            lines[i] = line + ', millis'
            first_line_skipped = True
        i = i + 1

    original_file.writelines(lines)
    return True


if __name__ == '__main__':
    input_file_path = Path(input('path to .csv file to convert: '))

    with open(input_file_path, encoding='utf-8') as file:
        timestamps = get_timestamps(file)
        converted_ts = convert_to_ms(timestamps)
        output_path, output_name = get_output_path(input_file_path)

        with open(Path(output_path + '\\' + output_name + '_CONVERTED.csv'), 'w+') as new_file:
            new_file.writelines(converted_ts)

        print("Timestamps successfully added to log file!")