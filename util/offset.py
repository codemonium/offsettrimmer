from os.path import dirname, join


def write(input_path, filename, class_start_dt, recording_start_dt, seek_from):
    offset = class_start_dt - recording_start_dt - seek_from
    offset_in_ms = int(offset.total_seconds() * 1000)

    offset_path = join(dirname(input_path), f'{filename}.offset')
    with open(offset_path, "w") as offset_file:
        offset_file.write(str(offset_in_ms))
