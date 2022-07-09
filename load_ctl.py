import os
import tkinter as tk
import sys


startpath = os.getcwd()
path = startpath
path = path[:path.lower().find("garupdate") + 10]
path_csv = path + "\\csv\\"
try:
    os.chdir(path_csv)
except:
    pass

# функция загрузки всех файлов
def load_all_click():
    path = startpath
    path = path[:path.lower().find("garupdate") + 10]
    path_csv = path + "\\csv\\"
    path_ctl = path + "ctl\\"
    path_shb = path + "shb\\"
    csv = []
    for dirs, folder, files in os.walk(path):
        for file in files:
            if ".csv" in f"{os.path.join(dirs, file)}".lower():
                csv.append(os.path.join(dirs, file))
    for i in range(len(csv)):
        csv_file = csv[i]
        csv[i] = csv[i].replace("as", "gar")
        csv[i] = csv[i][csv[i].find("csv\\") + 4:]
        backslash = "\\"
        csv[i] = csv[i][:csv[i].find("_2")].replace(backslash, "_")
        if csv[i][0:3] != "gar":
            csv[i] = csv[i][3:7] + csv[i][0:3] + csv[i][7:]
    name_dir = os.getcwd()[os.getcwd().rfind("csv")+3:].replace("\\","")
    for file in csv:
        try:
            window.update()
            dirname = os.getcwd()
            dirfiles = os.listdir(dirname)
            fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

            logs_list = []
            for file in fullpaths:
                if os.path.isfile(file) and file.lower().endswith("log"):
                    logs_list.append(file)


            if name_dir == "":
                for log in logs_list:
                    if '0' in log or '1' in log or '2' in log or '3' in log or '4' in log or '5' in log or '6' in log or '7' in log or '8' in log or '9' in log:
                        log_l = log.replace(os.getcwd(), "")
                        new_name_dir = log_l[5:7]
                        new_path = log.replace("gar", f"{new_name_dir}\\gar")
                        os.replace(log, new_path)
            else:
                for log in logs_list:
                    if '0' in log or '1' in log or '2' in log or '3' in log or '4' in log or '5' in log or '6' in log or '7' in log or '8' in log or '9':
                        log_l = log.replace(os.getcwd(), "")
                        new_name_dir = log_l[5:7]
                        new_path = log.replace(name_dir, new_name_dir)
                        os.replace(log, new_path)
                    else:
                        new_path = log.replace(f'{name_dir}\\', '')
                        os.replace(log, new_path)
            files = []

            for file in fullpaths:
                if os.path.isfile(file) and file.lower().endswith("csv"):
                    files.append(file)
            global dict_checkbuttons
            dict_checkbuttons = {}



            j = 0

            dict_checks = {}
            for i in files:
                global cb_canvas, cb_scroll_y
                cb_canvas.pack_forget()
                cb_scroll_y.pack_forget()
                frame = tk.Frame(cb_canvas)
                var1 = tk.BooleanVar()
                var1.set(0)
                cb_canvas = tk.Canvas(frame_list, width=1200, height=900)
                cb_scroll_y = tk.Scrollbar(frame_list, orient="vertical", command=cb_canvas.yview)
                frame_show = tk.Frame(frame)
                dict_checks[i] = tk.BooleanVar()
                dict_checks[i].set(0)
                backslash = "\\"
                logs_files = []
                dirname = os.getcwd()
                dirfiles = os.listdir(dirname)

                for file in dirfiles:
                    if os.path.isfile(file) and file.lower().endswith("log"): logs_files.append(file)
                name_csv = i[i.find("csv\\") + 4:].replace("as", "gar")
                backslash = "\\"
                if name_csv[0:3] != "gar":
                    name_csv = name_csv[3:7] + name_csv[0:3] + name_csv[7:]
                name_csv = name_csv[:name_csv.find("_2")].replace(backslash, "_") + ".log"
                text_label = ""

                if name_csv in logs_files:
                    with open(name_csv, mode="r+", encoding="Windows-1251") as r:
                        for line in r.readlines():
                            if "Rows successfully loaded." in line:
                                text = line
                                text = text[:text.find("Rows")]
                                text = text.replace(" ", "").replace("\n", "")
                                text_d = text
                                text_label += text + " |"
                            elif "Total logical records read:" in line:
                                text = line
                                text = text[text.find(":"):]
                                text = text.replace(":", "").replace(" ", "").replace("\n", "")
                                text_label += " " + text
                                text_p = text

                    dict_checkbuttons[i] = tk.Checkbutton(frame_show, text=f"{i[i.rfind(backslash) + 1:]}",
                                                          font=("Times New Roman", 20),
                                                          borderwidth=1,
                                                          bg="white",
                                                          relief="ridge",
                                                          width=62,
                                                          height=1,
                                                          variable=dict_checks[i],
                                                          anchor='w')
                    dict_checkbuttons[i].pack(side=tk.LEFT, fill="x")
                    if text_d == text_p:
                        label = tk.Label(frame_show,
                                         text=text_label,
                                         font=("Times New Roman", 20),
                                         borderwidth=1,
                                         height=1,
                                         width=15,
                                         bg="white",
                                         fg="dark green",
                                         relief="ridge",
                                         )
                    else:
                        label = tk.Label(frame_show,
                                         text=text_label,
                                         font=("Times New Roman", 20),
                                         borderwidth=1,
                                         height=1,
                                         width=15,
                                         bg="white",
                                         fg="red",
                                         relief="ridge",
                                         )
                    label.pack(side=tk.LEFT, fill=tk.Y)
                    frame_show.pack(fill=tk.X)
                else:
                    dict_checkbuttons[i] = tk.Checkbutton(frame_show, text=f"{i[i.rfind(backslash) + 1:]}",
                                                          font=("Times New Roman", 20),
                                                          borderwidth=1,
                                                          bg="white",
                                                          relief="ridge",
                                                          width=77,
                                                          height=1,
                                                          variable=dict_checks[i],
                                                          anchor='w')
                    dict_checkbuttons[i].pack(side=tk.LEFT, fill=tk.X)
                    frame_show.pack(fill=tk.X)
                j += 1
                cb_canvas.create_window(0, 0, anchor='nw', window=frame)
                cb_canvas.update_idletasks()
                cb_canvas.configure(scrollregion=cb_canvas.bbox('all'),
                                    yscrollcommand=cb_scroll_y.set)
                cb_canvas.pack(fill='both', expand=True, side='left')
                cb_scroll_y.pack(fill='y', expand=True, side='right')

        except:
            print("Не удалось загрузить файл", file)
            pass
# функция загрузки выбранного файла
def load_click():

    global dict_checks
    backslash = "\\"
    csv = []
    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])
        path_csv = os.getcwd()
        path = path_csv[:path_csv.lower().find("garupdate") + 10]
    else:
        path = os.getcwd()
        path = path[:path.lower().find("garupdate") + 10]
        path_csv = path + "\\csv\\"
    path_ctl = path + "ctl\\"
    path_shb = path + "shb\\"
    for i in dict_checks.keys():

        if dict_checks[i].get() == 1:
            csv.append(f"{os.getcwd()}{i}")
    if csv == []:
        if startpath != os.getcwd():
            path = os.getcwd()
            csv = []
            for dirs, folder, files in os.walk(path):
                for file in files:
                    if ".csv" in f"{os.path.join(dirs, file)}".lower():
                        csv.append(os.path.join(dirs, file))
        else:
            directory = os.getcwd()
            files = os.listdir(directory)
            for file in range(len(files)):
                files[file] = os.path.abspath(files[file])

            csv = list(filter(lambda x: x.lower().endswith('.csv'), files))


    csv_dict = {}
    for i in range(len(csv)):
        csv_file = csv[i]
        csv[i] = csv[i].replace("as", "gar")
        csv[i] = csv[i][csv[i].find("csv\\") + 4:]
        backslash = "\\"
        backslash = backslash[0]
        csv[i] = csv[i][:csv[i].find("_2")].replace(backslash, "_")
        if csv[i][0:3] != "gar":
            csv[i] = csv[i][3:7] + csv[i][0:3] + csv[i][7:]
        csv_dict[csv[i]] = csv_file


    for file in csv_dict:
        try:
            window.update()
            if "0" in file[4:6] or "1" in file[4:6] or "2" in file[4:6] or "3" in file[4:6] or "4" in file[4:6] or "5" in file[4:6] or "6" in file[4:6] or "7" in file[4:6] or "8" in file[4:6] or "9" in file[4:6]:
                os.system(f"sqlldr GAR/GARgar@10.100.50.12/orcl12 {path_ctl}{file[4:6]}{backslash}{file} skip=1")
            else:
                os.system(f"sqlldr GAR/GARgar@10.100.50.12/orcl12 {path_ctl}{file} skip=1")
            global cb_canvas, cb_scroll_y
            cb_canvas.pack_forget()
            cb_scroll_y.pack_forget()
            dirname = os.getcwd()
            dirfiles = os.listdir(dirname)
            fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

            files = []

            for file in fullpaths:
                if os.path.isfile(file) and file.lower().endswith("csv"): files.append(file)
            global dict_checkbuttons
            dict_checkbuttons = {}
            cb_canvas = tk.Canvas(frame_list, width=1200, height=900)
            cb_scroll_y = tk.Scrollbar(frame_list, orient="vertical", command=cb_canvas.yview)

            frame = tk.Frame(cb_canvas)
            var1 = tk.BooleanVar()
            var1.set(0)
            j = 0

            dict_checks = {}
            for i in files:
                frame_show = tk.Frame(frame)
                dict_checks[i] = tk.BooleanVar()
                dict_checks[i].set(0)
                backslash = "\\"
                logs_files = []
                dirname = os.getcwd()
                dirfiles = os.listdir(dirname)

                for file in dirfiles:
                    if os.path.isfile(file) and file.lower().endswith("log"): logs_files.append(file)
                name_csv = i[i.find("csv\\")+4:].replace("as", "gar")
                backslash = "\\"
                if name_csv[0:3] != "gar":
                    name_csv = name_csv[3:7] + name_csv[0:3] + name_csv[7:]
                name_csv = name_csv[:name_csv.find("_2")].replace(backslash, "_") + ".log"
                text_label = ""

                if name_csv in logs_files:
                    with open(name_csv, mode="r+", encoding="Windows-1251") as r:
                        for line in r.readlines():
                            if "Rows successfully loaded." in line:
                                text = line
                                text = text[:text.find("Rows")]
                                text = text.replace(" ", "").replace("\n", "")
                                text_d = text
                                text_label += text + " |"
                            elif "Total logical records read:" in line:
                                text = line
                                text = text[text.find(":"):]
                                text = text.replace(":", "").replace(" ", "").replace("\n", "")
                                text_label += " " + text
                                text_p = text

                    dict_checkbuttons[i] = tk.Checkbutton(frame_show, text=f"{i[i.rfind(backslash) + 1:]}",
                                                          font=("Times New Roman", 20),
                                                          borderwidth=1,
                                                          bg="white",
                                                          relief="ridge",
                                                          width=62,
                                                          height=1,
                                                          variable=dict_checks[i],
                                                          anchor='w')
                    dict_checkbuttons[i].pack(side=tk.LEFT, fill="x")
                    if text_d == text_p:
                        label = tk.Label(frame_show,
                                         text=text_label,
                                         font=("Times New Roman", 20),
                                         borderwidth=1,
                                         height=1,
                                         width=15,
                                         bg="white",
                                         fg="dark green",
                                         relief="ridge",
                                         )
                    else:
                        label = tk.Label(frame_show,
                                         text=text_label,
                                         font=("Times New Roman", 20),
                                         borderwidth=1,
                                         height=1,
                                         width=15,
                                         bg="white",
                                         fg="red",
                                         relief="ridge",
                                         )
                    label.pack(side=tk.LEFT, fill=tk.Y)
                    frame_show.pack(fill=tk.X)
                else:
                    dict_checkbuttons[i] = tk.Checkbutton(frame_show, text=f"{i[i.rfind(backslash) + 1:]}",
                                                          font=("Times New Roman", 20),
                                                          borderwidth=1,
                                                          bg="white",
                                                          relief="ridge",
                                                          width=77,
                                                          height=1,
                                                          variable=dict_checks[i],
                                                          anchor='w')
                    dict_checkbuttons[i].pack(side=tk.LEFT, fill=tk.X)
                    frame_show.pack(fill=tk.X)
                j += 1

            cb_canvas.create_window(0, 0, anchor='nw', window=frame)
            cb_canvas.update_idletasks()
            cb_canvas.configure(scrollregion=cb_canvas.bbox('all'),
                                yscrollcommand=cb_scroll_y.set)
            cb_canvas.pack(fill='both', expand=True, side='left')
            cb_scroll_y.pack(fill='y', expand=True, side='right')


        except:
            print("Не удалось загрузить файл", file)
            pass

# Список файлов
import os
dirname = os.getcwd()
dirfiles = os.listdir(dirname)
fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

global dirs, files
dirs = []
dirs.append(os.getcwd())

files = []


for file in fullpaths:
    if os.path.isdir(file): dirs.append(file)
    if os.path.isfile(file) and file.lower().endswith("csv"): files.append(file)

# Создание GUI
window = tk.Tk()
# Фрейм для показа информации
frame_info = tk.Frame(window)
frame_info.pack()
frame_info.columnconfigure(1, weight=1, minsize=200)
frame_info.rowconfigure([0,1], weight=1, minsize=20)
# Фрейм для сортировки ALL, CSV, XML
frame_sort = tk.Frame(frame_info)
frame_sort.grid(column=1, row=0)
frame_sort.columnconfigure([0, 1, 2], weight=1, minsize=10)
frame_sort.rowconfigure(0, weight=1, minsize=5)



frame_list_and_buttons = tk.Frame(frame_info)
frame_list_and_buttons.grid(column=1, row=1)
frame_list_and_buttons.columnconfigure(0, weight=1, minsize=200)
frame_list_and_buttons.rowconfigure([0,1], weight=1, minsize=20)

# Фрейм для списка файлов
frame_list = tk.Frame(frame_list_and_buttons)
global dict_checkbuttons
dict_checkbuttons = {}
global cb_canvas, cb_scroll_y
cb_canvas = tk.Canvas(frame_list, width=1200, height=900)
cb_scroll_y = tk.Scrollbar(frame_list, orient="vertical", command=cb_canvas.yview)

frame = tk.Frame(cb_canvas)
global dict_checks
dict_checks = {}
j = 0
for i in files:
    frame_show = tk.Frame(frame)
    dict_checks[i] = tk.BooleanVar()
    dict_checks[i].set(0)
    backslash = "\\"
    logs_files = []
    dirname = os.getcwd()
    dirfiles = os.listdir(dirname)

    for file in dirfiles:
        if os.path.isfile(file) and file.lower().endswith("log"): logs_files.append(file)
    name_csv = i[i.find("csv\\") + 4:].replace("as", "gar")
    backslash = "\\"
    if name_csv[0:3] != "gar":
        name_csv = name_csv[3:7] + name_csv[0:3] + name_csv[7:]
    name_csv = name_csv[:name_csv.find("_2")].replace(backslash, "_") + ".log"
    text_label = ""

    if name_csv in logs_files:
        with open(name_csv, mode="r+", encoding="Windows-1251") as r:
            for line in r.readlines():
                if "Rows successfully loaded." in line:
                    text = line
                    text = text[:text.find("Rows")]
                    text = text.replace(" ", "").replace("\n", "")
                    text_d = text
                    text_label += text + " |"
                elif "Total logical records read:" in line:
                    text = line
                    text = text[text.find(":"):]
                    text = text.replace(":", "").replace(" ", "").replace("\n", "")
                    text_label += " " + text
                    text_p = text

        dict_checkbuttons[i] = tk.Checkbutton(frame_show, text=f"{i[i.rfind(backslash) + 1:]}",
                                              font=("Times New Roman", 20),
                                              borderwidth=1,
                                              bg="white",
                                              relief="ridge",
                                              width=62,
                                              height=1,
                                              variable=dict_checks[i],
                                              anchor='w')
        dict_checkbuttons[i].pack(side=tk.LEFT, fill="x")
        if text_d == text_p:
            label = tk.Label(frame_show,
                             text=text_label,
                             font=("Times New Roman", 20),
                             borderwidth=1,
                             height=1,
                             width=15,
                             bg="white",
                             fg="dark green",
                             relief="ridge",
                             )
        else:
            label = tk.Label(frame_show,
                             text=text_label,
                             font=("Times New Roman", 20),
                             borderwidth=1,
                             height=1,
                             width=15,
                             bg="white",
                             fg="red",
                             relief="ridge",
                             )
        label.pack(side=tk.LEFT, fill=tk.Y)
        frame_show.pack(fill=tk.X)
    else:
        dict_checkbuttons[i] = tk.Checkbutton(frame_show, text=f"{i[i.rfind(backslash) + 1:]}",
                                              font=("Times New Roman", 20),
                                              borderwidth=1,
                                              bg="white",
                                              relief="ridge",
                                              width=77,
                                              height=1,
                                              variable=dict_checks[i],
                                              anchor='w')
        dict_checkbuttons[i].pack(side=tk.LEFT, fill=tk.X)
        frame_show.pack(fill=tk.X)
    j += 1

# put the frame in the canvas
cb_canvas.create_window(0, 0, anchor='nw', window=frame)
# make sure everything is displayed before configuring the scrollregion
cb_canvas.update_idletasks()

cb_canvas.configure(scrollregion=cb_canvas.bbox('all'),
                 yscrollcommand=cb_scroll_y.set)

cb_canvas.pack(fill='both', expand=True, side='left')
cb_scroll_y.pack(fill='y', expand=True, side='right')
frame_list.grid(column=0, row=0)
# Фрейм для кнопок
frame_buttons = tk.Frame(frame_list_and_buttons)
canvas = tk.Canvas(frame_buttons, width=1200, height=100)

tk.Button(canvas,
          width=28,
          height=1,
          text="Загрузить в БД выбранное",
          font=("Times New Roman", 14),
          bg="White",
          relief="groove",
          command=load_click).pack(side="left")
tk.Button(canvas,
          width=28,
          height=1,
          text="Загрузить в БД все",
          font=("Times New Roman", 14),
          bg="White",
          relief="groove",
          command=load_all_click).pack(side="left")
canvas.pack(fill='both', expand=True, side='top')
frame_buttons.grid(column=0, row=1)
# Фрейм для списка папок
frame_dir = tk.Frame(frame_info)
frame_dir.grid(column=0, row=1)
global list_button
dict_button = {}
canvas = tk.Canvas(frame_dir, width=400, height=950)
scroll_y = tk.Scrollbar(frame_dir, orient="vertical", bg='yellow', command=canvas.yview)

def new_dir():
    global cb_canvas, cb_scroll_y
    cb_canvas.pack_forget()
    cb_scroll_y.pack_forget()
    dirname = os.getcwd()
    dirfiles = os.listdir(dirname)
    fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

    files = []

    for file in fullpaths:
        if os.path.isfile(file) and file.lower().endswith("csv"): files.append(file)
    global dict_checkbuttons
    dict_checkbuttons = {}
    cb_canvas = tk.Canvas(frame_list, width=1200, height=900)
    cb_scroll_y = tk.Scrollbar(frame_list, orient="vertical", command=cb_canvas.yview)

    frame = tk.Frame(cb_canvas)
    var1 = tk.BooleanVar()
    var1.set(0)
    j = 0

    dict_checks = {}
    for i in files:
        frame_show = tk.Frame(frame)
        dict_checks[i] = tk.BooleanVar()
        dict_checks[i].set(0)
        backslash = "\\"
        logs_files = []
        dirname = os.getcwd()
        dirfiles = os.listdir(dirname)

        for file in dirfiles:
            if os.path.isfile(file) and file.lower().endswith("log"): logs_files.append(file)
        name_csv = i[i.find("csv\\") + 4:].replace("as", "gar")
        backslash = "\\"
        if name_csv[0:3] != "gar":
            name_csv = name_csv[3:7] + name_csv[0:3] + name_csv[7:]
        name_csv = name_csv[:name_csv.find("_2")].replace(backslash, "_") + ".log"
        text_label = ""

        if name_csv in logs_files:
            with open(name_csv, mode="r+", encoding="Windows-1251") as r:
                for line in r.readlines():
                    if "Rows successfully loaded." in line:
                        text = line
                        text = text[:text.find("Rows")]
                        text = text.replace(" ", "").replace("\n", "")
                        text_d = text
                        text_label += text + " |"
                    elif "Total logical records read:" in line:
                        text = line
                        text = text[text.find(":"):]
                        text = text.replace(":", "").replace(" ", "").replace("\n", "")
                        text_label += " "+text
                        text_p = text

            dict_checkbuttons[i] = tk.Checkbutton(frame_show, text=f"{i[i.rfind(backslash) + 1:]}",
                                                  font=("Times New Roman", 20),
                                                  borderwidth=1,
                                                  bg="white",
                                                  relief="ridge",
                                                  width=62,
                                                  height=1,
                                                  variable=dict_checks[i],
                                                  anchor='w')
            dict_checkbuttons[i].pack(side=tk.LEFT, fill="x")
            if text_d == text_p:
                label = tk.Label(frame_show,
                                 text=text_label,
                                 font=("Times New Roman", 20),
                                 borderwidth=1,
                                 height=1,
                                 width=15,
                                 bg="white",
                                 fg="dark green",
                                 relief="ridge",
                                 )
            else:
                label = tk.Label(frame_show,
                                 text=text_label,
                                 font=("Times New Roman", 20),
                                 borderwidth=1,
                                 height=1,
                                 width=15,
                                 bg="white",
                                 fg="red",
                                 relief="ridge",
                                 )
            label.pack(side=tk.LEFT, fill=tk.Y)
            frame_show.pack(fill=tk.X)
        else:
            dict_checkbuttons[i] = tk.Checkbutton(frame_show, text=f"{i[i.rfind(backslash) + 1:]}",
                                                  font=("Times New Roman", 20),
                                                  borderwidth=1,
                                                  bg="white",
                                                  relief="ridge",
                                                  width=77,
                                                  height=1,
                                                  variable=dict_checks[i],
                                                  anchor='w')
            dict_checkbuttons[i].pack(side=tk.LEFT, fill=tk.X)
            frame_show.pack(fill=tk.X)
        j += 1

    # put the frame in the canvas
    cb_canvas.create_window(0, 0, anchor='nw', window=frame)
    # make sure everything is displayed before configuring the scrollregion
    cb_canvas.update_idletasks()

    cb_canvas.configure(scrollregion=cb_canvas.bbox('all'),
                        yscrollcommand=cb_scroll_y.set)

    cb_canvas.pack(fill='both', expand=True, side='left')
    cb_scroll_y.pack(fill='y', expand=True, side='right')

frame = tk.Frame(canvas)

class mybutton(tk.Button):
    backslash = "\\"
    def dir_click(self):
        for i in dict_button.keys():
            dict_button[i]["bg"] = "White"
            dict_button[i]["fg"] = "Black"
        self["bg"] = "Blue"
        self["fg"] = "White"

        try:
            os.chdir(self.name)
        except:
            try:
                os.chdir('..')
                os.chdir(self.name)
            except:
                pass

        new_dir()

    def __init__(self, parent,name, frame):
        super().__init__(parent,
                                bg="White",
                                fg="Black",
                                activebackground="Blue",
                                text=f"{name[name.rfind(backslash)+1:]}",
                                font=("Times New Roman", 20),
                                height=1,
                                width=26,
                                borderwidth=3,
                                relief="ridge",
                                )
        self.name = name
        self.frame_list = frame_list
        self["command"] = self.dir_click

for i in dirs:
    backslash = "\\"
    i = f"{i[i.rfind(backslash)+1:]}"
    dict_button[i] = (mybutton(frame, i, frame_list))
    dict_button[i].pack()


# put the frame in the canvas
canvas.create_window(0, 0, anchor='nw', window=frame)
# make sure everything is displayed before configuring the scrollregion
canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'),
                 yscrollcommand=scroll_y.set)

canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', expand=True, side='right')


# Смена цвета главной директории
directory = os.getcwd()
backslash = "\\"
directory = directory[directory.rfind(backslash)+1:]
dict_button[directory]['bg']="Blue"
dict_button[directory]["fg"]="White"
# Запуск GUI
window.mainloop()
