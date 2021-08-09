from datetime import timedelta
from os.path import dirname, join

import subprocess


def run_dry_trim(input_path, seek_from, seek_to):
    dry_seek_to = seek_from + timedelta(seconds=10)
    subprocess.run(
        __get_dry_run_command(input_path, seek_from, dry_seek_to,
                              join(dirname(input_path), "a.temp.mkv"))
    )

    dry_seek_from = seek_to - timedelta(seconds=10)
    subprocess.run(
        __get_dry_run_command(input_path, dry_seek_from, seek_to,
                              join(dirname(input_path), "b.temp.mkv"))
    )


def run_trim(input_path, filename, seek_from, seek_to):
    output_path = join(dirname(input_path), f'{filename}.mkv')
    return subprocess.run(__get_run_command(input_path, filename, seek_from, seek_to, output_path))


def __get_dry_run_command(input_path, seek_from, seek_to, output_path):
    return [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-ss", str(seek_from),
        "-to", str(seek_to),
        "-c", "copy",
        output_path
    ]


def __get_run_command(input_path, filename, seek_from, seek_to, output_path):
    return [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-ss", str(seek_from),
        "-to", str(seek_to),
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "17",
        "-vf", "format=yuv420p",
        "-c:a", "copy",
        output_path
    ]


def write_log(input_path, filename, completed_process):
    log_path = join(dirname(input_path), f'{filename}.log')
    with open(log_path, "w") as log_file:
        command = " ".join(f'"{arg}"' for arg in completed_process.args)
        log_file.write(command)
