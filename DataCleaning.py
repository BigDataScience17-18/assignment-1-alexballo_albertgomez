import gzip
from os import listdir

# Functions


def update_repetition_number(update_repetition_number):
    return update_repetition_number.replace(" ", "").replace("\n", "").replace("trial", "")


def open_file(file_name):
    if cont is 0:
        result_file = open("./dataResults/" + file_name, "w")
        result_file.write("# UserIdentifier  Alcoholic  Paradigm  RepetionNumber  Channel  SensorValues  \n")
        return result_file
    else:
       return open("./dataResults/" + file_name, "a")


def update_paradigm(update_paradigm):
    return update_paradigm.replace(" ", "")[1:]


for directory in listdir("./dataset-assignment1"):
    cont = 0
    root = "./dataset-assignment1/" + directory

    for file in listdir(root):
        samefile = True
        # Renaming the file
        file_root = root + "/" + file
        print(root)
        read_file = gzip.open(file_root, 'r')
        file_name=file[:-10] + ".txt"
        result_file = open_file(file_name)
        first_line = read_file.readline()
        # 4 first lines information about the data
        user_id = first_line[10:-4]
        alcoholic = first_line[5]
        read_file.readline()
        read_file.readline()
        line4_values = read_file.readline().split(",")
        paradigm = update_paradigm(line4_values[0])
        repetition_number = update_repetition_number(line4_values[1])
        values_channel = ""
        cont = 1
        # Read all the data within the file
        for line in read_file:
            if line[0] == "#":
                if values_channel != "":
                    result_file.write(values_channel + "\n")
                    values_channel = ""
                channel=line[2:-7]
                # Writing the tidy line in the result file
                result_file.write(user_id + "  " + alcoholic + "  " +
                                  paradigm + "  " + repetition_number + "  " + channel)
            else:
                values_channel = line.split(" ")[3].replace("\n", "  ") + values_channel

        result_file.write(values_channel + "\n")
        result_file.close()
        read_file.close()

