from fns.constant.strconst import StringConstants


def dirify(dir_name: str):
    return dir_name if dir_name.endswith(StringConstants.FWD_SLASH) else dir_name + StringConstants.FWD_SLASH


def append_dir_name(parent_dir_path, dir_name):
    path = dirify(parent_dir_path)
    dirified_name = dirify(dir_name)

    return path + dirified_name


def append_file_name(parent_dir_path, file_name):
    return dirify(parent_dir_path) + file_name
