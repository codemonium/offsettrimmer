from datetime import datetime as dt
from datetime import time

from os.path import basename, splitext


def seek(string):
    time_value = time.fromisoformat(string)
    seek_value = dt.combine(dt.min, time_value) - dt.min
    return seek_value


def time_only(string):
    return time.fromisoformat(string)


def get_rec_start_dt(input_path):
    ext = splitext(input_path)[1]
    return dt.strptime(basename(input_path), f'%Y-%m-%d %H-%M-%S{ext}')


def get_class_start_dt(input_path, start_time):
    recording_start_dt = get_rec_start_dt(input_path)
    return dt.combine(recording_start_dt.date(), start_time)
