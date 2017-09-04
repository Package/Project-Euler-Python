def read_single_line_file(file_name):
    with open(file_name) as f:
        content = f.readline()
    return [x.replace("\"", "") for x in str(content).split(',')]


def read_multiline_file(file_name):
    with open(file_name) as f:
        return [x.replace("\n", "") for x in f.readlines()]
