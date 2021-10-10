# This is a report generator
# if the filename is dot csv, it can be turned into a table.
# Note that you need to specify the separator type as custom, then as ;

def generate_report(report, filename, data):
    if report == "begin":
        begin_report(filename, data)
    elif report == "continue":
        continue_report(filename, data)
    elif report == "end":
        continue_report(filename, data)

def begin_report(filename, data):
    file = open(filename, "w+")
    write_in_report(file, data)
    file.close()

def continue_report(filename, data):
    file = open(filename, "a")
    write_in_report(file, data)
    file.close()

def write_in_report(file, data):
    file.write("\n")
    for each_data in data:
        if type(each_data) == list:
            file.write("[")
            for item in each_data[:-1]:
                file.write("%i, " % item)
            file.write("%i" % each_data[-1])
            file.write("];")
        else:
            file.write(f"{each_data};")

