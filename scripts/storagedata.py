def readData(file, line=None, option=None):
    """Read the data from a file and return the content
    line=INT the line number to read
    option="len" gives out line amount
    """

    data_file = open(file, "r")
    readed_file = data_file.readlines()
    data_file.close()

    if option == "len":
        return len(readed_file)
    elif line == None:
        return readed_file
    else:
        return readed_file[line-1].replace("\n", "")

    return 0

def overwriteData(file, line, data):
    """Overwrite data to a file
    overwrite file,
    line to overwrite,
    data to overwrite"""

    old_data = readData(file)
    data += "\n"
    try:
        tempvar = old_data
        tempvar[line-1] = data
        new_data = tempvar
        del tempvar
    except IndexError:
        tempvar = old_data
        tempvar.append(data)
        new_data = tempvar
        del tempvar
    _writeData(file, new_data)

def _writeData(file, new_data):
    """Write the data given from user"""

    data_file = open(file, "w")
    data_file.writelines(new_data)
    data_file.close()