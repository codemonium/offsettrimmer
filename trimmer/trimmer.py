import trimmer.encoder as enc
import util.offset as offset
import util.timeutil as tu


def trim(dry, input_path, start_time, seek_from, seek_to):
    if dry:
        __do_dry_trim(input_path, seek_from, seek_to)
    else:
        __do_trim(input_path, start_time, seek_from, seek_to)


def __do_dry_trim(input_path, seek_from, seek_to):
    enc.run_dry_trim(input_path, seek_from, seek_to)


def __do_trim(input_path, start_time, seek_from, seek_to):
    rec_start_dt = tu.get_rec_start_dt(input_path)
    class_start_dt = tu.get_class_start_dt(input_path, start_time)

    filename = class_start_dt.strftime("%Y-%m-%d-LIVE-REC-%H-%M-%S")

    offset.write(input_path, filename, class_start_dt, rec_start_dt, seek_from)

    completed_process = enc.run_trim(input_path, filename, seek_from, seek_to)
    enc.write_log(input_path, filename, completed_process)
