import os
import sys
from progress.bar import IncrementalBar
def main():

    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])
        path_csv = os.getcwd()
        path = path_csv[:path_csv.lower().find("garupdate") + 10]
    else:
        path = os.getcwd()
        path = path[:path.lower().find("garupdate") + 10]
        path_csv = path + "\\csv\\"
    path_ctl = path + "\\ctl\\"
    path_shb = path + "\\shb\\"
    if not os.path.isdir(f"{path}\ctl"):
        os.mkdir(f"{path}\ctl")



    csv= []

    for dirs, folder, files in os.walk(path_csv):
        for fil in files:
            if ".csv" in f"{os.path.join(dirs, fil)}".lower():
                # if "venv" not in f"{os.path.join(dirs, file)}".lower() and ".idea" not in f"{os.path.join(dirs, file)}".lower():
                csv.append(os.path.join(dirs, fil))

    bar = IncrementalBar('Прогресс', max=len(csv))
    files = os.listdir(path_shb)
    shb_ctl = []
    for file in files:
        if ".ctl" in file:
            shb_ctl.append(file)
    csv_dict = {}
    for i in range(len(csv)):
        csv_file = csv[i]
        csv[i] = csv[i][csv[i].find("csv\\")+4:].replace("as", "gar")
        backslash = "\\"
        csv[i] = csv[i][:csv[i].find("_2")].replace(backslash,"_")
        if csv[i][0:3] != "gar":
            csv[i] = csv[i][3:7]+csv[i][0:3]+csv[i][7:]
        csv_dict[csv[i]] = csv_file

    bar = IncrementalBar('Прогресс', max=len(csv_dict))

    for key in csv_dict.keys():
        bar.next()
        for shb in shb_ctl:
            shb_compare = shb[:-4]
            if key == shb_compare:
                with open(path_shb+shb, "r+", encoding="Windows-1251") as s:
                    with open (path_ctl+shb, "w+", encoding="Windows-1251") as c:
                        for line in s.readlines():
                            if "INFILE" in line:
                                table = csv_dict[key].replace("\\\\", backslash)
                                print(f"INFILE '{table}'", file=c)
                            elif "INTO TABLE" in line:
                                print(f"INTO TABLE {key}", file=c)
                            else:
                                print(line, file=c,end="")
            elif (key[7:] == shb_compare[7:]) and ("xx" in shb):
                dir_ctl = key[4:6]
                if not os.path.isdir(f"{path}\ctl\{dir_ctl}"):
                    os.mkdir(f"{path}\ctl\{dir_ctl}")
                sh = path_ctl + dir_ctl+backslash+key +".ctl"


                with open(path_shb+shb, "r+", encoding="Windows-1251") as s:
                    with open (sh, "w+", encoding="Windows-1251") as c:
                        for line in s.readlines():
                            if "INFILE" in line:
                                backslash = "\\"
                                backslash = backslash[0]
                                table = csv_dict[key].replace("\\\\", backslash)
                                print(f"INFILE '{table}'", file=c)
                            elif "INTO TABLE" in line:
                                print(f"INTO TABLE {key}", file=c)
                            else:
                                print(line, file=c, end="")

    pass
if __name__ == '__main__':
    main()