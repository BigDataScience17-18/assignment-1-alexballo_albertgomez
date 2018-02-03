import gzip
from os import listdir

for directory in listdir("./dataset-assignment1"):
    cont=0
    root = "./dataset-assignment1/" + directory
    for file in listdir(root):
        samefile= True
        file_root= root + "/" + file
    #for file in directory:
        print(root)

        read_file = gzip.open(file_root, 'r')

        file_name=file[:-10] + ".txt"
        if cont is 0:
            result_file = open("./dataResults/" + file_name, "w")
            result_file.write("# UserIdentifier  Alcoholic  Paradigm  RepetionNumber  Channel  SensorValues  \n")
        else:
            result_file= open("./dataResults/"+file_name, "a")

        first_line= read_file.readline()
        user_id=first_line[10:-4]
        alcoholic= first_line[5]
        read_file.readline()
        read_file.readline()
        line4_values= read_file.readline().split(",")
        paradigm=line4_values[0].replace(" ","")[1:]
        repetion_number=line4_values[1].replace(" ","").replace("\n","").replace("trial","")
        values_channel=""
        cont=1

        for line in read_file:
            if line[0] == "#":
                if values_channel != "":
                    result_file.write(values_channel + "\n")
                    values_channel=""
                channel=line[2:-7]
                result_file.write(user_id + "  " + alcoholic + "  " + paradigm + "  " + repetion_number + "  " + channel )
            else:
                values_channel= line.split(" ")[3].replace("\n", "  ") + values_channel
        result_file.write(values_channel + "\n")
        result_file.close()
        read_file.close()