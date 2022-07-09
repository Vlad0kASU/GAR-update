import zipfile
import os
from functools import partial
import tkinter as tk
from progress.bar import IncrementalBar
import sys
import threading
import asyncio
import tkinter.ttk as ttk
from datetime import datetime

def parser(file):
    try:
        import datetime
        start = datetime.datetime
        import xml.sax
        class EventHandler(xml.sax.ContentHandler):
            def __init__(self, target):
                self.target = target

            def startElement(self, name, attrs):
                self.target.send(attrs._attrs.keys())
                self.target.send(attrs._attrs.values())

            def characters(self, text):
                self.target.send('')

            def endElement(self, name):
                self.target.send('')

        def coroutine(func):
            def start(*args, **kwargs):
                cr = func(*args, **kwargs)
                cr.__next__()
                return cr

            return start

        DictNames = Name(file)
        ListNames = list(Name(file))

        name_csv = file.lower()
        name_csv = name_csv[:-3]
        with open(f'{name_csv}csv', 'w+', encoding="UTF-8") as f:
            text = ""
            for i in DictNames.keys():
                text += DictNames[i] + "|"
            print(text[:-1], file=f)

        with open(f'{name_csv}csv', 'a+', encoding="UTF-8") as f:
            # example use
            @coroutine
            def printer():
                j = 0
                num = 0
                while True:

                    event = (yield)
                    testprint = list(event)
                    event = str(event)
                    dict_sort = {}
                    if "AS_ADDHOUSE_TYPES" in file:
                        if testprint != []:
                            if "dict_keys([" in event:
                                list_keys = testprint
                            elif "dict_values([" in event:
                                list_values = testprint
                                if len(list_keys) != len(ListNames):
                                    # list_atr = event.replace("dict_values([", "").replace("])", "").replace("'", "").replace('\n', "").split(", ")
                                    for i in range(len(ListNames)):
                                        try:
                                            if ListNames[i] != list_keys[i]:
                                                list_keys.insert(i, ListNames[i])
                                                list_values.insert(i, "")

                                        except IndexError:
                                            list_keys.append("")
                                            list_values.append("")

                                        if list_keys[len(list_keys) - 1] == "":
                                            list_keys = list_keys[:-1]
                                            list_atr = list_values[:-1]
                                dict_event = dict(zip(list_keys, list_values))
                                list_dict_keys = list(dict_event.keys())
                                dict_sort = {"AHT_ID": dict_event["ID"],
                                             "AHT_NAME": dict_event["NAME"],
                                             "AHT_SHORTNAME": dict_event["SHORTNAME"],
                                             "AHT_DESC": dict_event["DESC"],
                                             "AHT_UPDATEDATE": dict_event["UPDATEDATE"],
                                             "AHT_STARTDATE": dict_event["STARTDATE"],
                                             "AHT_ENDDATE": dict_event["ENDDATE"],
                                             "AHT_ISACTIVE": dict_event["ISACTIVE"]}
                                text = ""
                                for key in dict_sort.keys():
                                    text += dict_sort[key] + "|"
                                text = text[:-1]
                                print(text, file=f)
                        pass
                    elif "AS_APARTMENT_TYPES" in file:
                        if testprint != []:
                            if "dict_keys([" in event:
                                list_keys = testprint
                            elif "dict_values([" in event:
                                list_values = testprint
                                if len(list_keys) != len(ListNames):
                                    for i in range(len(ListNames)):
                                        try:
                                            if ListNames[i] != list_keys[i]:
                                                list_keys.insert(i, ListNames[i])
                                                list_values.insert(i, "")

                                        except IndexError:
                                            list_keys.append("")
                                            list_values.append("")

                                        if list_keys[len(list_keys) - 1] == "":
                                            list_keys = list_keys[:-1]
                                            list_atr = list_values[:-1]
                                dict_event = dict(zip(list_keys, list_values))
                                list_dict_keys = list(dict_event.keys())
                                dict_sort = {"AT_ID": dict_event["ID"],
                                             "AT_NAME": dict_event["NAME"],
                                             "AT_SHORTNAME": dict_event["SHORTNAME"],
                                             "AT_DESC": dict_event["DESC"],
                                             "AT_UPDATEDATE": dict_event["UPDATEDATE"],
                                             "AT_STARTDATE": dict_event["STARTDATE"],
                                             "AT_ENDDATE": dict_event["ENDDATE"],
                                             "AT_ISACTIVE": dict_event["ISACTIVE"]}
                                text = ""
                                for key in dict_sort.keys():
                                    text += dict_sort[key] + "|"
                                text = text[:-1]
                                print(text, file=f)
                        pass
                    elif "AS_OPERATION_TYPES" in file:
                        if testprint != []:
                            if "dict_keys([" in event:
                                list_keys = testprint
                            elif "dict_values([" in event:
                                list_values = testprint
                                if len(list_keys) != len(ListNames):
                                    for i in range(len(ListNames)):
                                        try:
                                            if ListNames[i] != list_keys[i]:
                                                list_keys.insert(i, ListNames[i])
                                                list_values.insert(i, "")

                                        except IndexError:
                                            list_keys.append("")
                                            list_values.append("")

                                        if list_keys[len(list_keys) - 1] == "":
                                            list_keys = list_keys[:-1]
                                            list_atr = list_values[:-1]
                                dict_event = dict(zip(list_keys, list_values))
                                list_dict_keys = list(dict_event.keys())
                                try:
                                    dict_sort = {"OT_ID": dict_event["ID"],
                                                 "OT_NAME": dict_event["NAME"],
                                                 "OT_SHORTNAME": dict_event["SHORTNAME"],
                                                 "OT_DESC": dict_event["DESC"],
                                                 "OT_UPDATEDATE": dict_event["UPDATEDATE"],
                                                 "OT_STARTDATE": dict_event["STARTDATE"],
                                                 "OT_ENDDATE": dict_event["ENDDATE"],
                                                 "OT_ISACTIVE": dict_event["ISACTIVE"]}
                                    text = ""
                                    for key in dict_sort.keys():
                                        text += dict_sort[key] + "|"
                                    text = text[:-1]
                                    print(text, file=f)
                                except:
                                    pass
                        pass
                    elif "AS_OBJECT_LEVELS" in file:
                        if testprint != []:
                            if "dict_keys([" in event:
                                list_keys = testprint
                            elif "dict_values([" in event:
                                list_values = testprint
                                if len(list_keys) != len(ListNames):
                                    for i in range(len(ListNames)):
                                        try:
                                            if ListNames[i] != list_keys[i]:
                                                list_keys.insert(i, ListNames[i])
                                                list_values.insert(i, "")

                                        except IndexError:
                                            list_keys.append("")
                                            list_values.append("")

                                        if list_keys[len(list_keys) - 1] == "":
                                            list_keys = list_keys[:-1]
                                            list_atr = list_values[:-1]
                                dict_event = dict(zip(list_keys, list_values))
                                list_dict_keys = list(dict_event.keys())
                                try:
                                    dict_sort = {"OL_LEVEL": dict_event["LEVEL"],
                                                 "OT_NAME": dict_event["NAME"],
                                                 "OT_SHORTNAME": dict_event["SHORTNAME"],
                                                 "OL_UPDATEDATE": dict_event["UPDATEDATE"],
                                                 "OL_STARTDATE": dict_event["STARTDATE"],
                                                 "OL_ENDDATE": dict_event["ENDDATE"],
                                                 "OL_ISACTIVE": dict_event["ISACTIVE"]}
                                    text = ""
                                    for key in dict_sort.keys():
                                        text += dict_sort[key] + "|"
                                    text = text[:-1]
                                    print(text, file=f)
                                except:
                                    pass
                        pass
                    elif "AS_HOUSE_TYPES" in file:
                        if testprint != []:
                            if "dict_keys([" in event:
                                list_keys = testprint
                            elif "dict_values([" in event:
                                list_values = testprint
                                if len(list_keys) != len(ListNames):
                                    for i in range(len(ListNames)):
                                        try:
                                            if ListNames[i] != list_keys[i]:
                                                list_keys.insert(i, ListNames[i])
                                                list_values.insert(i, "")

                                        except IndexError:
                                            list_keys.append("")
                                            list_values.append("")

                                        if list_keys[len(list_keys) - 1] == "":
                                            list_keys = list_keys[:-1]
                                            list_atr = list_values[:-1]
                                dict_event = dict(zip(list_keys, list_values))
                                list_dict_keys = list(dict_event.keys())
                                dict_sort = {"HT_ID": dict_event["ID"],
                                             "HT_NAME": dict_event["NAME"],
                                             "HT_SHORTNAME": dict_event["SHORTNAME"],
                                             "HT_DESC": dict_event["DESC"],
                                             "HT_UPDATEDATE": dict_event["UPDATEDATE"],
                                             "HT_STARTDATE": dict_event["STARTDATE"],
                                             "HT_ENDDATE": dict_event["ENDDATE"],
                                             "HT_ISACTIVE": dict_event["ISACTIVE"]}
                                text = ""
                                for key in dict_sort.keys():
                                    text += dict_sort[key] + "|"
                                text = text[:-1]
                                print(text, file=f)
                        pass
                    elif "AS_PARAM_TYPES" in file:
                        if testprint != []:
                            if "dict_keys([" in event:
                                list_keys = testprint
                            elif "dict_values([" in event:
                                list_values = testprint
                                if len(list_keys) != len(ListNames):
                                    for i in range(len(ListNames)):
                                        try:
                                            if ListNames[i] != list_keys[i]:
                                                list_keys.insert(i, ListNames[i])
                                                list_values.insert(i, "")

                                        except IndexError:
                                            list_keys.append("")
                                            list_values.append("")

                                        if list_keys[len(list_keys) - 1] == "":
                                            list_keys = list_keys[:-1]
                                            list_atr = list_values[:-1]
                                dict_event = dict(zip(list_keys, list_values))
                                list_dict_keys = list(dict_event.keys())
                                dict_sort = {"PT_ID": dict_event["ID"],
                                             "PT_NAME": dict_event["NAME"],
                                             "PT_DESC": dict_event["DESC"],
                                             "PT_CODE": dict_event["CODE"],
                                             "PT_UPDATEDATE": dict_event["UPDATEDATE"],
                                             "PT_STARTDATE": dict_event["STARTDATE"],
                                             "PT_ENDDATE": dict_event["ENDDATE"],
                                             "PT_ISACTIVE": dict_event["ISACTIVE"]}
                                text = ""
                                for key in dict_sort.keys():
                                    text += dict_sort[key] + "|"
                                text = text[:-1]
                                print(text, file=f)
                        pass
                    elif "AS_ROOM_TYPES" in file:
                        if testprint != []:
                            if "dict_keys([" in event:
                                list_keys = testprint
                            elif "dict_values([" in event:
                                list_values = testprint
                                if len(list_keys) != len(ListNames):
                                    for i in range(len(ListNames)):
                                        try:
                                            if ListNames[i] != list_keys[i]:
                                                list_keys.insert(i, ListNames[i])
                                                list_values.insert(i, "")

                                        except IndexError:
                                            list_keys.append("")
                                            list_values.append("")

                                        if list_keys[len(list_keys) - 1] == "":
                                            list_keys = list_keys[:-1]
                                            list_atr = list_values[:-1]
                                dict_event = dict(zip(list_keys, list_values))
                                list_dict_keys = list(dict_event.keys())
                                dict_sort = {"RT_ID": dict_event["ID"],
                                             "RT_NAME": dict_event["NAME"],
                                             "RT_SHORTNAME": dict_event["SHORTNAME"],
                                             "RT_DESC": dict_event["DESC"],
                                             "RT_UPDATEDATE": dict_event["UPDATEDATE"],
                                             "RT_STARTDATE": dict_event["STARTDATE"],
                                             "RT_ENDDATE": dict_event["ENDDATE"],
                                             "RT_ISACTIVE": dict_event["ISACTIVE"]}
                                text = ""
                                for key in dict_sort.keys():
                                    text += dict_sort[key] + "|"
                                text = text[:-1]
                                print(text, file=f)
                        pass
                    else:
                        list_event = []
                        if "dict_keys([" in event:
                            event = event.replace("dict_keys([", "").replace("])", "").replace("'", "").replace(
                                '\n',
                                "").split(
                                ", ")
                            list_event = event

                            event = ""

                        if "dict_values([" in event:
                            if len(list_event) != len(ListNames):
                                list_atr = event.replace("dict_values([", "").replace("])", "").replace("'",
                                                                                                        "").replace(
                                    '\n', "").split(", ")
                                for i in range(len(ListNames)):
                                    try:
                                        if ListNames[i] != list_event[i]:
                                            list_event.insert(i, ListNames[i])
                                            list_atr.insert(i, "")

                                    except IndexError:
                                        list_event.append("")
                                        list_atr.append("")

                                    if list_event[len(list_event) - 1] == "":
                                        list_event = list_event[:-1]
                                        list_atr = list_atr[:-1]

                                text = ""
                                for i in range(len(list_atr)):
                                    text += list_atr[i] + "|"
                                if j != 0:
                                    print(text[:-1], file=f)
                                else:
                                    j += 1

                            else:
                                event = str(event)
                                event = event.replace("dict_values([", "").replace("])", "").replace("'",
                                                                                                     "").replace(
                                    ", ", "|").replace('\n', "")
                                print(event, file=f)

            xml.sax.parse(file, EventHandler(printer()))
            print(start-datetime.datetime)
    except:
        pass

# получаем на вызове путь файла
# if len(sys.argv) > 1:
#     zip_path = sys.argv[1]
#     try:
#
#         gar_zip = zipfile.ZipFile(zip_path)
#         gar_list = gar_zip.namelist()
#         bar = IncrementalBar("Прогресс", max=len(gar_list))
#         for i in range(len(gar_list)):
#             gar_zip.extract(gar_list[i], os.getcwd())
#             bar.next()
#             print(i)
#
#         gar_zip.close()
#     except:
#         print("Указанного файла не существует\n")
#         pass
# else:
#     while True:
#         # Ввод файла zip
#         zip_path = input("Введите путь до zip файла\n").replace('"', '').replace("'", "")
#         # zip_path = "C:\\Users\\melnikov\\Downloads\\test.zip"
#         try:
#
#             gar_zip = zipfile.ZipFile(zip_path)
#             gar_list = gar_zip.namelist()
#             gar_list = sorted(gar_list)
#             bar = IncrementalBar("Прогресс", max=len(gar_list))
#             for i in range(len(gar_list)):
#                 gar_zip.extract(gar_list[i], os.getcwd())
#                 bar.next()
#                 print(gar_list[i], 'number', i)
#             gar_zip.close()
#             break
#         except:
#             print("Указанного файла не существует\n")
# Функция выбора шапки CSV
def Name(file):
    Names = []
    if "AS_ADDR_OBJ" in file:
        if "AS_ADDR_OBJ_DIVISION" in file:
            Names = {"ID": "AOD_ID",
                     "PARENTID": "AOD_PARENTID",
                     "CHILDID": "AOD_CHILDID",
                     "CHANGEID": "AOD_CHANGEID"}
        elif "AS_ADDR_OBJ_TYPES" in file:
            Names = {"ID": "AOT_ID",
                     "LEVEL": "AOT_LEVEL",
                     "SHORTNAME": "AOT_SHORTNAME",
                     "NAME": "AOT_NAME",
                     "DESC": "AOT_DESC",
                     "UPDATEDATE": "AOT_UPDATEDATE",
                     "STARTDATE": "AOT_STARTDATE",
                     "ENDDATE": "AOT_ENDDATE",
                     "ISACTIVE": "AOT_ISACTIVE"}
        elif "AS_ADDR_OBJ_PARAMS" in file:
            Names = {"ID": "AOP_ID",
                     "OBJECTID": "AOP_OBJECTID",
                     "CHANGEID": "AOP_CHANGEID",
                     "CHANGEIDEND": "AOP_CHANGEIDEND",
                     "TYPEID": "AOP_TYPEID",
                     "VALUE": "AOP_VALUE",
                     "UPDATEDATE": "AOP_UPDATEDATE",
                     "STARTDATE": "AOP_STARTDATE",
                     "ENDDATE": "AOP_ENDDATE"}
        else:
            Names = {"ID": "AO_ID",
                     "OBJECTID": "AO_OBJECTID",
                     "OBJECTGUID": "AO_OBJECTGUID",
                     "CHANGEID": "AO_CHANGEID",
                     "NAME": "AO_NAME",
                     "TYPENAME": "AO_TYPENAME",
                     "LEVEL": "AO_LEVEL",
                     "OPERTYPEID": "AO_OPERTYPEID",
                     "PREVID": "AO_PREVID",
                     "NEXTID": "AO_NEXTID",
                     "UPDATEDATE": "AO_UPDATEDATE",
                     "STARTDATE": "AO_STARTDATE",
                     "ENDDATE": "AO_ENDDATE",
                     "ISACTUAL": "AO_ISACTUAL",
                     "ISACTIVE": "AO_ISACTIVE"}
    elif "AS_ADDHOUSE_TYPES" in file:
        Names = {"ID": "AHT_ID",
                 "NAME": "AHT_NAME",
                 "SHORTNAME": "AHT_SHORTNAME",
                 "DESC": "AHT_DESC",
                 "ISACTIVE": "AHT_UPDATEDATE",
                 "UPDATEDATE": "AHT_STARTDATE",
                 "STARTDATE": "AHT_ENDDATE",
                 "ENDDATE": "AHT_ISCATIVE"}
    elif "AS_APARTMENT_TYPES" in file:
        Names = {"ID": "AT_ID",
                 "NAME": "AT_NAME",
                 "SHORTNAME": "AT_SHORTNAME",
                 "DESC": "AT_DESC",
                 "ISACTIVE": "AT_UPDATEDATE",
                 "STARTDATE": "AT_STARTDATE",
                 "ENDDATE": "AT_ENDDATE",
                 "UPDATEDATE": "AT_ISACTIVE"}
    elif "AS_HOUSE_TYPES" in file:
        Names = {"ID": "HT_ID",
                 "NAME": "HT_NAME",
                 "SHORTNAME": "HT_SHORTNAME",
                 "DESC": "HT_DESC",
                 "ISACTIVE": "HT_UPDATEDATE",
                 "UPDATEDATE": "HT_STARTDATE",
                 "STARTDATE": "HT_ENDDATE",
                 "ENDDATE": "HT_ISACTIVE"}
    elif "AS_PARAM_TYPES" in file:
        Names = {"ID": "PT_ID",
                 "NAME": "PT_NAME",
                 "DESC": "PT_CODE",
                 "CODE": "PT_DESC",
                 "ISACTIVE": "PT_UPDATEDATE",
                 "UPDATEDATE": "PT_STARTDATE",
                 "STARTDATE": "PT_ENDDATE",
                 "ENDDATE": "PT_ISACTIVE"}
    elif "AS_ROOM_TYPES" in file:
        Names = {"ID": "RT_ID",
                 "NAME": "RT_NAME",
                 "SHORTNAME": "RT_SHORTNAME",
                 "DESC": "RT_DESC",
                 "ISACTIVE": "RT_UPDATEDATE",
                 "STARTDATE": "RT_STARTDATE",
                 "ENDDATE": "RT_ENDDATE",
                 "UPDATEDATE": "RT_ISACTIVE"}
    elif "AS_ADM_HIERARCHY" in file:
        Names = {"ID": "AH_ID",
                 "OBJECTID": "AH_OBJECTID",
                 "PARENTOBJID": "AH_PARENTOBJID",
                 "CHANGEID": "AH_CHANGEID",
                 "REGIONCODE": "AH_REGIONCODE",
                 "AREACODE": "AH_AREACODE",
                 "CITYCODE": "AH_CITYCODE",
                 "PLACECODE": "AH_PLACECODE",
                 "PLANCODE": "AH_PLANCODE",
                 "STREETCODE": "AH_STREETCODE",
                 "PREVID": "AH_PREVID",
                 "NEXTID": "AH_NEXTID",
                 "UPDATEDATE": "AH_UPDATEDATE",
                 "STARTDATE": "AH_STARTDATE",
                 "ENDDATE": "AH_ENDDATE",
                 "ISACTIVE": "AH_ISACTIVE",
                 "PATH": "AH_PATH"}
    elif "AS_APARTMENTS" in file:
        if "AS_APARTMENTS_PARAMS" in file:
            Names = {"ID": "AP_ID",
                     "OBJECTID": "AP_OBJECTID",
                     "CHANGEID": "AP_CHANGEID",
                     "CHANEGEIDEND": "AP_CHANGEIDEND",
                     "TYPEID": "AP_TYPEID",
                     "VALUE": "AP_VALUE",
                     "UPDATEDATE": "AP_UPDATEDATE",
                     "STARTDATE": "AP_STARTDATE",
                     "ENDDATE": "AP_ENDDATE"}
        else:
            Names = {"ID": "A_ID",
                     "OBJECTID": "A_OBJECTID",
                     "OBJECTGUID": "A_OBJECTGUID",
                     "CHANGEID": "A_CHANGEID",
                     "NUMBER": "A_NUMBER",
                     "APARTTYPE": "A_APARTTYPE",
                     "OPERTYPEID": "A_OPERTYPEID",
                     "PREVID": "A_PREVID",
                     "NEXTID": "A_NEXTID",
                     "UPDATEDATE": "A_UPDATETDAE",
                     "STARTDATE": "A_STARTDATE",
                     "ENDDATE": "A_ENDDATE",
                     "ISACTUAL": "A_ISACTUAL",
                     "ISACTIVE": "A_ISACTIVE"}
    elif "AS_CARPLACES" in file:
        if "AS_CARPLACES_PARAMS" in file:
            Names = {"ID": "CP_ID",
                     "OBJECTID": "CP_OBJECTID",
                     "CHANGEID": "CP_CHANGEID",
                     "CHANGEIDEND": "CP_CHANGEIDEND",
                     "TYPEID": "CP_TYPEID",
                     "VALUE" : "CP_VALUE",
                     "UPDATEDATE": "CP_UPDATEDATE",
                     "STARTDATE": "CP_STARTDATE",
                     "ENDDATE": "CP_ENDDATE"}
        else:
            Names = {"ID": "C_ID",
                     "OBJECTID": "C_OBJECTID",
                     "OBJECTGUID": "C_OBJECTGUID",
                     "CHANGEID": "CHANGEID",
                     "NUMBER": "C_NUMBER",
                     "OPERTYPEID": "C_OPERTYPEID",
                     "PREVID": "C_PREVID",
                     "NEXTID": "C_NEXTID",
                     "UPDATEDATE": "C_UPDATEDATE",
                     "STARTDATE": "C_STARTDATE",
                     "ENDDATE": "C_ENDDATE",
                     "ISACTUAL": "C_ISACTIVE",
                     "ISACTIVE": "C_ISACTIVE"}
    elif "AS_CHANGE_HISTORY" in file:
        Names = {"CHANGEID": "CH_CHANGEID",
                 "OBJECTID": "CH_OBJECTID",
                 "ADROBJECTID": "CH_ADROBJECTID",
                 "OPERTYPEID": "CH_OPERTYPEID",
                 "NDOCID": "CH_NDOCID",
                 "CHANGEDATE": "CH_CHANGEDATE"}
    elif "AS_HOUSE" in file:
        if "AS_HOUSES_PARAMS" in file:
            Names = {"ID": "HP_ID",
                     "OBJECTID": "HP_OBJECTID",
                     "CHANGEID": "HP_CHANGEID",
                     "CHANGEIDEND": "HP_CHANGEIDEND",
                     "TYPEID": "HP_TYPEID",
                     "VALUE": "HP_VALUE",
                     "UPDATEDATE": "HP_UPDATEDATE",
                     "STARTDATE": "HP_STARTDATE",
                     "ENDDATE": "HP_ENDDATE"}
        else:
            Names = {"ID": "H_ID",
                     "OBJECTID": "H_OBJECTID",
                     "OBJECTGUID": "H_OBJECTGUID",
                     "CHANGEID": "H_CHANGEID",
                     "HOUSENUM": "H_HOUSENUM",
                     "ADDNUM1": "H_ADDNUM1",
                     "ADDNUM2": "H_ADDNUM2",
                     "HOUSETYPE": "H_HOUSETYPE",
                     "ADDTYPE1": "H_ADDTYPE1",
                     "ADDTYPE2": "H_ADDTYPE2",
                     "OPERTYPEID": "H_OPERTYPEID",
                     "PREVID": "H_PREVID",
                     "NEXTID": "H_NEXTID",
                     "UPDATEDATE": "H_UPDATETDAE",
                     "STARTDATE": "H_STARTDATE",
                     "ENDDATE": "H_ENDDATE",
                     "ISACTUAL": "H_ISACTUAL",
                     "ISACTIVE": "H_ISACTIVE"}
    elif "AS_MUN_HIERARCHY" in file:
        Names = {"ID": "MH_ID",
                 "OBJECTID": "MH_OBJECTID",
                 "PARENTOBJID": "MH_PARENTOBJID",
                 "CHANGEID": "MH_CHANGEID",
                 "OKTMO": "MH_OKTMO",
                 "PREVID": "MH_PREVID",
                 "NEXTID": "MH_NEXTID",
                 "UPDATEDATE": "MH_UPDATEDATE",
                 "STARTDATE": "MH_STARTDATE",
                 "ENDDATE": "MH_ENDDATE",
                 "ISACTIVE": "MH_ISACTIVE",
                 "PATH": "MH_PATH"}
    elif "AS_NORMATIVE_DOCS" in file:
        if "AS_NORMATIVE_DOCS_KINDS" in file:
            Names = {"ID": "NDK_ID",
                     "NAME": "NDK_NAME"}
        elif "AS_NORMATIVE_DOCS_TYPES" in file:
            Names = {"ID": "NDT_ID",
                     "NAME": "NDT_NAME",
                     "STARTDATE": "NDT_STARTDATE",
                     "ENDDATE": "NDT_ENDDATE"}
        else:
            Names = {"ID": "ND_ID",
                     "NAME": "ND_NAME",
                     "DATE": "ND_DATE",
                     "NUMBER": "ND_NUMBER",
                     "TYPE": "ND_TYPE",
                     "KIND": "ND_KIND",
                     "UPDATEDATE": "ND_UPDATEDATE",
                     "ORGNAME": "ND_ORGNAME",
                     "REGNUM": "ND_REGNUM",
                     "REGDATE": "ND_REGDATE",
                     "ACCDATE": "ND_ACCDATE",
                     "COMMENT": "ND_COMMENT"}
    elif "AS_OBJECT_LEVELS" in file:
        Names = {"LEVEL": "OL_LEVEL",
                 "NAME": "OL_NAME",
                 "SHORTNAME": "OL_SHORTNAME",
                 "UPDATEDATE": "OL_UPDATEDATE",
                 "STARTDATE": "OL_STARTDATE",
                 "ENDDATE": "OL_ENDDATE",
                 "ISACTIVE": "OL_ISACTIVE"}
    elif "AS_OPERATION_TYPES" in file:
        Names = {"ID": "OT_ID",
                 "NAME": "OT_NAME",
                 "SHORTNAME": "OT_SHORTNAME",
                 "DESC": "OT_DESC",
                 "UPDATEDATE": "OT_UPDATEDATE",
                 "STARTDATE": "OT_STARTDATE",
                 "ENDDATE": "OT_ENDDATE",
                 "ISACTIVE": "OT_ISACTIVE"}
    elif "AS_REESTR_OBJECTS" in file:
        Names = {"OBJECTID": "RO_OBJECTID",
                 "OBJECTGUID": "RO_OBJECTGUID",
                 "CHANGEID": "RO_CHANGEID",
                 "ISACTIVE": "RO_ISACTIVE",
                 "LEVELID": "RO_LEVELID",
                 "CREATEDATE": "RO_CREATEDATE",
                 "UPDATEDATE": "RO_UPDATEDATE"}
    elif "AS_ROOMS" in file:
        if "AS_ROOMS_PARAMS" in file:
            Names = {"ID": "RP_ID",
                     "OBJECTID": "RP_OBJECTID",
                     "CHANGEID": "RP_CHANGEID",
                     "CHANGEIDEND": "RP_CHANGEIDEND",
                     "TYPEID": "RP_TYPEID",
                     "VALUE": "RP_VALUE",
                     "UPDATEDATE": "RP_UPDATEDATE",
                     "STARTDATE": "STARTDATE",
                     "ENDDATE": "RP_ENDDATE"}
        else:
            Names = {"ID": "R_ID",
                     "OBJECTID": "R_OBJECTID",
                     "OBJECTGUID": "R_OBJECTGUID",
                     "CHANGEID": "R_CHANGEID",
                     "NUMBER": "R_ROOMNUMBER",
                     "ROOMTYPE": "R_ROOMTYPE",
                     "OPERTYPEID": "R_OPERTYPEID",
                     "PREVID": "R_PREVID",
                     "NEXTID": "R_NEXTID",
                     "UPDATEDATE": "R_UPDATEDATE",
                     "STARTDATE": "R_STARTDATE",
                     "ENDDATE": "R_ENDDATE",
                     "ISACTUAL": "R_ISACTUAL",
                     "ISACTIVE": "R_ISACTIVE"}
    elif "AS_STEADS" in file:
        if "AS_STEADS_PARAMS" in file:
            Names = {"ID": "SP_ID",
                     "OBJECTID": "SP_OBJECTID",
                     "CHANGEID": "SP_CHANGEID",
                     "CHANGEIDEND": "SP_CHANGEIDEND",
                     "TYPEID": "SP_TYPEID",
                     "VALUE": "SP_VALUE",
                     "UPDATEDATE": "SP_UPDATEDATE",
                     "STARTDATE": "SP_STARTDATE",
                     "ENDDATE": "SP_ENDDATE"}
        else:
            Names = {"ID": "S_ID",
                     "OBJECTID": "S_OBJECTID",
                     "OBJECTGUID": "S_OBJECTGUID",
                     "CHANGEID": "S_CHANGEID",
                     "NUMBER": "S_NUMBER",
                     "OPERTYPEID": "S_OPERTYPEID",
                     "PREVID": "S_PREVID",
                     "NEXTID": "S_NEXTID",
                     "UPDATEDATE": "S_UPDATEDATE",
                     "STARTDATE": "S_STARTDATE",
                     "ENDDATE": "S_ENDDATE",
                     "ISACTUAL": "S_ISACTUAL",
                     "ISACTIVE": "S_ISACTIVE"}
    return(Names)


# функция конвертирования всех файлов
import asyncio
startpath = os.getcwd()
def _run_aio_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
aioloop = asyncio.new_event_loop()
t = threading.Thread(target=partial(_run_aio_loop, aioloop))
t.daemon = True  # Optional depending on how you plan to shutdown the app
t.start()

buttonT = None
async def do_urls():
    """ Creating and starting 10 tasks. """
    root = tk.Toplevel(window)
    percent = tk.StringVar()
    text = tk.StringVar()
    bar = ttk.Progressbar(root, orient="horizontal", length=300)
    bar.pack(pady=10)
    path = startpath
    xml = []
    for dirs, folder, files in os.walk(path):
        for file in files:
            if ".xml" in f"{os.path.join(dirs, file)}".lower():
                xml.append(os.path.join(dirs, file))
    GB = len(xml)
    download = 0
    speed = 1
    path = os.getcwd()
    xml = []
    for dirs, folder, files in os.walk(path):
        for file in files:
            if ".xml" in f"{os.path.join(dirs, file)}".lower():
                xml.append(os.path.join(dirs, file))
    for file in xml:
        start = datetime
        bar['value'] += (speed / GB) * 100
        download += speed
        percent.set(str(int((download / GB) * 100)) + "%" + "|")
        root.update_idletasks()
        parser(file)
        print(datetime-start)

    button_convert_all.configure(state="normal")  # Tk doesn't seem to care that this is called on another thread
    root.destroy()
def convert_all_click():
    asyncio.run_coroutine_threadsafe(do_urls(), aioloop)

def _run_aio_loop_my(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
aioloop_my = asyncio.new_event_loop()
t_my = threading.Thread(target=partial(_run_aio_loop_my, aioloop_my))
t_my.daemon = True  # Optional depending on how you plan to shutdown the app
t_my.start()

buttonT_my = None
async def do_urls_my():
    """ Creating and starting 10 tasks. """
    root = tk.Toplevel(window)
    percent = tk.StringVar()
    text = tk.StringVar()
    bar = ttk.Progressbar(root, orient="horizontal", length=300)
    bar.pack(pady=10)
    path = startpath
    xml = []
    global dict_checks
    xml = []
    for i in dict_checks.keys():

        if dict_checks[i].get() == 1:
            xml.append(i)
    if xml == []:
        if startpath != os.getcwd():
            path = os.getcwd()
            xml = []
            for dirs, folder, files in os.walk(path):
                for file in files:
                    if ".xml" in f"{os.path.join(dirs, file)}".lower():
                        xml.append(os.path.join(dirs, file))
        else:
            directory = os.getcwd()
            files = os.listdir(directory)
            xml = list(filter(lambda x: x.lower().endswith('.xml'), files))
    GB = len(xml)
    download = 0
    speed = 1
    path = os.getcwd()
    xml = []
    for dirs, folder, files in os.walk(path):
        for file in files:
            if ".xml" in f"{os.path.join(dirs, file)}".lower():
                xml.append(os.path.join(dirs, file))
    for file in xml:
        bar['value'] += (speed / GB) * 100
        download += speed
        percent.set(str(int((download / GB) * 100)) + "%" + "|")
        root.update_idletasks()
        parser(file)

    button_convert.configure(state="normal")  # Tk doesn't seem to care that this is called on another thread
    root.destroy()



# функция конвертирования выбранного файла
def convert_click():
    asyncio.run_coroutine_threadsafe(do_urls_my(), aioloop_my)
    global dict_checks
    xml = []
    for i in dict_checks.keys():

        if dict_checks[i].get() == 1:
            xml.append(i)
    if xml == []:
        if startpath != os.getcwd():
            path = os.getcwd()
            xml = []
            for dirs, folder, files in os.walk(path):
                for file in files:
                    if ".xml" in f"{os.path.join(dirs, file)}".lower():
                        xml.append(os.path.join(dirs, file))
        else:
            directory = os.getcwd()
            files = os.listdir(directory)
            xml = list(filter(lambda x: x.lower().endswith('.xml'), files))
    for file in xml:
        try:
            # bar.next()
            backslash = "\\"
            import xml.sax


            class EventHandler(xml.sax.ContentHandler):
                def __init__(self, target):
                    self.target = target

                def startElement(self, name, attrs):
                    self.target.send(attrs._attrs.keys())
                    self.target.send(attrs._attrs.values())

                def characters(self, text):
                    self.target.send('')

                def endElement(self, name):
                    self.target.send('')

            def coroutine(func):
                def start(*args, **kwargs):
                    cr = func(*args, **kwargs)
                    cr.__next__()
                    return cr

                return start

            DictNames = Name(file)
            ListNames = list(Name(file))

            name_csv = file.lower()
            name_csv = name_csv[:-3]
            with open(f'{name_csv}csv', 'w+', encoding="UTF-8") as f:
                text = ""
                for i in DictNames.keys():
                    text += DictNames[i] + "|"
                print(text[:-1], file=f)

            with open(f'{name_csv}csv', 'a+', encoding="UTF-8") as f:
                # example use
                @coroutine
                def printer():
                    j = 0
                    num = 0
                    while True:

                        event = (yield)
                        testprint = list(event)
                        event = str(event)
                        dict_sort = {}
                        if "AS_ADDHOUSE_TYPES" in file:
                            if testprint != []:
                                if "dict_keys([" in event:
                                    list_keys = testprint
                                elif "dict_values([" in event:
                                    list_values = testprint
                                    if len(list_keys) != len(ListNames):
                                        for i in range(len(ListNames)):
                                            try:
                                                if ListNames[i] != list_keys[i]:
                                                    list_keys.insert(i, ListNames[i])
                                                    list_values.insert(i, "")

                                            except IndexError:
                                                list_keys.append("")
                                                list_values.append("")

                                            if list_keys[len(list_keys) - 1] == "":
                                                list_keys = list_keys[:-1]
                                                list_atr = list_values[:-1]
                                    dict_event = dict(zip(list_keys, list_values))
                                    list_dict_keys = list(dict_event.keys())
                                    dict_sort = {"AHT_ID": dict_event["ID"],
                                                 "AHT_NAME": dict_event["NAME"],
                                                 "AHT_SHORTNAME": dict_event["SHORTNAME"],
                                                 "AHT_DESC": dict_event["DESC"],
                                                 "AHT_UPDATEDATE": dict_event["UPDATEDATE"],
                                                 "AHT_STARTDATE": dict_event["STARTDATE"],
                                                 "AHT_ENDDATE": dict_event["ENDDATE"],
                                                 "AHT_ISACTIVE": dict_event["ISACTIVE"]}
                                    text = ""
                                    for key in dict_sort.keys():
                                        text += dict_sort[key] + "|"
                                    text = text[:-1]
                                    print(text, file=f)
                            pass
                        elif "AS_APARTMENT_TYPES" in file:
                            if testprint != []:
                                if "dict_keys([" in event:
                                    list_keys = testprint
                                elif "dict_values([" in event:
                                    list_values = testprint
                                    if len(list_keys) != len(ListNames):
                                        for i in range(len(ListNames)):
                                            try:
                                                if ListNames[i] != list_keys[i]:
                                                    list_keys.insert(i, ListNames[i])
                                                    list_values.insert(i, "")

                                            except IndexError:
                                                list_keys.append("")
                                                list_values.append("")

                                            if list_keys[len(list_keys) - 1] == "":
                                                list_keys = list_keys[:-1]
                                                list_atr = list_values[:-1]
                                    dict_event = dict(zip(list_keys, list_values))
                                    list_dict_keys = list(dict_event.keys())
                                    dict_sort = {"AT_ID": dict_event["ID"],
                                                 "AT_NAME": dict_event["NAME"],
                                                 "AT_SHORTNAME": dict_event["SHORTNAME"],
                                                 "AT_DESC": dict_event["DESC"],
                                                 "AT_UPDATEDATE": dict_event["UPDATEDATE"],
                                                 "AT_STARTDATE": dict_event["STARTDATE"],
                                                 "AT_ENDDATE": dict_event["ENDDATE"],
                                                 "AT_ISACTIVE": dict_event["ISACTIVE"]}
                                    text = ""
                                    for key in dict_sort.keys():
                                        text += dict_sort[key] + "|"
                                    text = text[:-1]
                                    print(text, file=f)
                            pass
                        elif "AS_HOUSE_TYPES" in file:
                            if testprint != []:
                                if "dict_keys([" in event:
                                    list_keys = testprint
                                elif "dict_values([" in event:
                                    list_values = testprint
                                    if len(list_keys) != len(ListNames):
                                        for i in range(len(ListNames)):
                                            try:
                                                if ListNames[i] != list_keys[i]:
                                                    list_keys.insert(i, ListNames[i])
                                                    list_values.insert(i, "")

                                            except IndexError:
                                                list_keys.append("")
                                                list_values.append("")

                                            if list_keys[len(list_keys) - 1] == "":
                                                list_keys = list_keys[:-1]
                                                list_atr = list_values[:-1]
                                    dict_event = dict(zip(list_keys, list_values))
                                    list_dict_keys = list(dict_event.keys())
                                    dict_sort = {"HT_ID": dict_event["ID"],
                                                 "HT_NAME": dict_event["NAME"],
                                                 "HT_SHORTNAME": dict_event["SHORTNAME"],
                                                 "HT_DESC": dict_event["DESC"],
                                                 "HT_UPDATEDATE": dict_event["UPDATEDATE"],
                                                 "HT_STARTDATE": dict_event["STARTDATE"],
                                                 "HT_ENDDATE": dict_event["ENDDATE"],
                                                 "HT_ISACTIVE": dict_event["ISACTIVE"]}
                                    text = ""
                                    for key in dict_sort.keys():
                                        text += dict_sort[key] + "|"
                                    text = text[:-1]
                                    print(text, file=f)
                            pass
                        elif "AS_PARAM_TYPES" in file:
                            if testprint != []:
                                if "dict_keys([" in event:
                                    list_keys = testprint
                                elif "dict_values([" in event:
                                    list_values = testprint
                                    if len(list_keys) != len(ListNames):
                                        for i in range(len(ListNames)):
                                            try:
                                                if ListNames[i] != list_keys[i]:
                                                    list_keys.insert(i, ListNames[i])
                                                    list_values.insert(i, "")

                                            except IndexError:
                                                list_keys.append("")
                                                list_values.append("")

                                            if list_keys[len(list_keys) - 1] == "":
                                                list_keys = list_keys[:-1]
                                                list_atr = list_values[:-1]
                                    dict_event = dict(zip(list_keys, list_values))
                                    list_dict_keys = list(dict_event.keys())
                                    dict_sort = {"PT_ID": dict_event["ID"],
                                                 "PT_NAME": dict_event["NAME"],
                                                 "PT_DESC": dict_event["DESC"],
                                                 "PT_CODE": dict_event["CODE"],
                                                 "PT_UPDATEDATE": dict_event["UPDATEDATE"],
                                                 "PT_STARTDATE": dict_event["STARTDATE"],
                                                 "PT_ENDDATE": dict_event["ENDDATE"],
                                                 "PT_ISACTIVE": dict_event["ISACTIVE"]}
                                    text = ""
                                    for key in dict_sort.keys():
                                        text += dict_sort[key] + "|"
                                    text = text[:-1]
                                    print(text, file=f)
                            pass
                        elif "AS_OPERATION_TYPES" in file:
                            if testprint != []:
                                if "dict_keys([" in event:
                                    list_keys = testprint
                                elif "dict_values([" in event:
                                    list_values = testprint
                                    if len(list_keys) != len(ListNames):
                                        for i in range(len(ListNames)):
                                            try:
                                                if ListNames[i] != list_keys[i]:
                                                    list_keys.insert(i, ListNames[i])
                                                    list_values.insert(i, "")

                                            except IndexError:
                                                list_keys.append("")
                                                list_values.append("")

                                            if list_keys[len(list_keys) - 1] == "":
                                                list_keys = list_keys[:-1]
                                                list_atr = list_values[:-1]
                                    dict_event = dict(zip(list_keys, list_values))
                                    list_dict_keys = list(dict_event.keys())
                                    try:
                                        dict_sort = {"OT_ID": dict_event["ID"],
                                                     "OT_NAME": dict_event["NAME"],
                                                     "OT_SHORTNAME": dict_event["SHORTNAME"],
                                                     "OT_DESC": dict_event["DESC"],
                                                     "OT_UPDATEDATE": dict_event["UPDATEDATE"],
                                                     "OT_STARTDATE": dict_event["STARTDATE"],
                                                     "OT_ENDDATE": dict_event["ENDDATE"],
                                                     "OT_ISACTIVE": dict_event["ISACTIVE"]}
                                        text = ""
                                        for key in dict_sort.keys():
                                            text += dict_sort[key] + "|"
                                        text = text[:-1]
                                        print(text, file=f)
                                    except:
                                        pass
                            pass
                        elif "AS_OBJECT_LEVELS" in file:
                            if testprint != []:
                                if "dict_keys([" in event:
                                    list_keys = testprint
                                elif "dict_values([" in event:
                                    list_values = testprint
                                    if len(list_keys) != len(ListNames):
                                        for i in range(len(ListNames)):
                                            try:
                                                if ListNames[i] != list_keys[i]:
                                                    list_keys.insert(i, ListNames[i])
                                                    list_values.insert(i, "")

                                            except IndexError:
                                                list_keys.append("")
                                                list_values.append("")

                                            if list_keys[len(list_keys) - 1] == "":
                                                list_keys = list_keys[:-1]
                                                list_atr = list_values[:-1]
                                    dict_event = dict(zip(list_keys, list_values))
                                    list_dict_keys = list(dict_event.keys())
                                    try:
                                        dict_sort = {"OL_LEVEL": dict_event["LEVEL"],
                                                     "OT_NAME": dict_event["NAME"],
                                                     "OT_SHORTNAME": dict_event["SHORTNAME"],
                                                     "OL_UPDATEDATE": dict_event["UPDATEDATE"],
                                                     "OL_STARTDATE": dict_event["STARTDATE"],
                                                     "OL_ENDDATE": dict_event["ENDDATE"],
                                                     "OL_ISACTIVE": dict_event["ISACTIVE"]}
                                        text = ""
                                        for key in dict_sort.keys():
                                            text += dict_sort[key] + "|"
                                        text = text[:-1]
                                        print(text, file=f)
                                    except:
                                        pass
                            pass
                        elif "AS_ROOM_TYPES" in file:
                            if testprint != []:
                                if "dict_keys([" in event:
                                    list_keys = testprint
                                elif "dict_values([" in event:
                                    list_values = testprint
                                    if len(list_keys) != len(ListNames):
                                        for i in range(len(ListNames)):
                                            try:
                                                if ListNames[i] != list_keys[i]:
                                                    list_keys.insert(i, ListNames[i])
                                                    list_values.insert(i, "")

                                            except IndexError:
                                                list_keys.append("")
                                                list_values.append("")

                                            if list_keys[len(list_keys) - 1] == "":
                                                list_keys = list_keys[:-1]
                                                list_atr = list_values[:-1]
                                    dict_event = dict(zip(list_keys, list_values))
                                    list_dict_keys = list(dict_event.keys())
                                    dict_sort = {"RT_ID": dict_event["ID"],
                                                 "RT_NAME": dict_event["NAME"],
                                                 "RT_SHORTNAME": dict_event["SHORTNAME"],
                                                 "RT_DESC": dict_event["DESC"],
                                                 "RT_UPDATEDATE": dict_event["UPDATEDATE"],
                                                 "RT_STARTDATE": dict_event["STARTDATE"],
                                                 "RT_ENDDATE": dict_event["ENDDATE"],
                                                 "RT_ISACTIVE": dict_event["ISACTIVE"]}
                                    text = ""
                                    for key in dict_sort.keys():
                                        text += dict_sort[key] + "|"
                                    text = text[:-1]
                                    print(text, file=f)
                            pass
                        else:
                            list_event = []
                            if "dict_keys([" in event:
                                event = event.replace("dict_keys([", "").replace("])", "").replace("'", "").replace('\n',
                                                                                                                    "").split(
                                    ", ")
                                list_event = event

                                event = ""

                            if "dict_values([" in event:
                                if len(list_event) != len(ListNames):
                                    list_atr = event.replace("dict_values([", "").replace("])", "").replace("'",
                                                                                                            "").replace(
                                        '\n', "").split(", ")
                                    for i in range(len(ListNames)):
                                        try:
                                            if ListNames[i] != list_event[i]:
                                                list_event.insert(i, ListNames[i])
                                                list_atr.insert(i, "")

                                        except IndexError:
                                            list_event.append("")
                                            list_atr.append("")

                                        if list_event[len(list_event) - 1] == "":
                                            list_event = list_event[:-1]
                                            list_atr = list_atr[:-1]

                                    text = ""
                                    for i in range(len(list_atr)):
                                        text += list_atr[i] + "|"


                                else:
                                    event = str(event)
                                    event = event.replace("dict_values([", "").replace("])", "").replace("'", "").replace(
                                        ", ", "|").replace('\n', "")
                                    print(event, file=f)

                xml.sax.parse(file, EventHandler(printer()))
        except:
            print("Не удалось обработать файл", file)
            pass
    global cb_canvas, cb_scroll_y
    cb_canvas.pack_forget()
    cb_scroll_y.pack_forget()
    dirname = os.getcwd()
    dirfiles = os.listdir(dirname)

    fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

    files = []

    for file in fullpaths:
        if os.path.isfile(file) and (file.lower().endswith("xml") or file.lower().endswith("csv")): files.append(
            file)
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
        dict_checks[i] = tk.BooleanVar()
        dict_checks[i].set(0)
        backslash = "\\"
        dict_checkbuttons[i] = tk.Checkbutton(frame, text=f"{i[i.rfind(backslash) + 1:]}",
                                              font=("Times New Roman", 20),
                                              borderwidth=3,
                                              bg="white",
                                              relief="ridge",
                                              width = 77,
                                              variable=dict_checks[i],
                                              anchor='w')
        dict_checkbuttons[i].pack(fill="x")
        j += 1

    # put the frame in the canvas
    cb_canvas.create_window(0, 0, anchor='nw', window=frame)
    # make sure everything is displayed before configuring the scrollregion
    cb_canvas.update_idletasks()

    cb_canvas.configure(scrollregion=cb_canvas.bbox('all'),
                        yscrollcommand=cb_scroll_y.set)

    cb_canvas.pack(fill='both', expand=True, side='left')
    cb_scroll_y.pack(fill='y', expand=True, side='right')




# Разархивирование зип файла с прогресс баром

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
    if os.path.isfile(file) and (file.lower().endswith("xml") or file.lower().endswith("csv")): files.append(file)





# Создание GUI
window = tk.Tk()
class ResizingCanvas(tk.Canvas):
    def __init__(self,parent,**kwargs):
        tk.Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)
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
def sort_all():
    button_csv['bg'] = "White"
    button_csv['fg'] = "Black"
    button_xml['bg'] = "White"
    button_xml['fg'] = "Black"
    button_all['bg'] = 'Blue'
    button_all['fg'] = "White"

    global cb_canvas, cb_scroll_y
    cb_canvas.pack_forget()
    cb_scroll_y.pack_forget()
    dirname = os.getcwd()
    dirfiles = os.listdir(dirname)

    fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

    files = []

    for file in fullpaths:
        if os.path.isfile(file) and (file.lower().endswith("xml") or file.lower().endswith("csv")): files.append(
            file)
    global dict_checkbuttons
    dict_checkbuttons = {}
    cb_canvas = tk.Canvas(frame_list, width=1200, height=900)
    cb_scroll_y = tk.Scrollbar(frame_list, orient="vertical", command=cb_canvas.yview)

    frame = tk.Frame(cb_canvas)
    var1 = tk.BooleanVar()
    var1.set(0)
    j = 0
    global dict_checks
    dict_checks = {}
    for i in files:
        dict_checks[i] = tk.BooleanVar()
        dict_checks[i].set(0)
        backslash = "\\"
        dict_checkbuttons[i] = tk.Checkbutton(frame, text=f"{i[i.rfind(backslash) + 1:]}",
                                              font=("Times New Roman", 20),
                                              borderwidth=3,
                                              bg="white",
                                              relief="ridge",
                                              width=77,
                                              variable=dict_checks[i],
                                              anchor='w')
        dict_checkbuttons[i].pack(fill="x")
        j += 1

    # put the frame in the canvas
    cb_canvas.create_window(0, 0, anchor='nw', window=frame)
    # make sure everything is displayed before configuring the scrollregion
    cb_canvas.update_idletasks()

    cb_canvas.configure(scrollregion=cb_canvas.bbox('all'),
                        yscrollcommand=cb_scroll_y.set)

    cb_canvas.pack(fill='both', expand=True, side='left')
    cb_scroll_y.pack(fill='y', expand=True, side='right')
    pass
def sort_xml():
    button_csv['bg'] = "White"
    button_csv['fg'] = "Black"
    button_xml['bg'] = "Blue"
    button_xml['fg'] = "White"
    button_all['bg'] = 'White'
    button_all['fg'] = "Black"
    global cb_canvas, cb_scroll_y
    cb_canvas.pack_forget()
    cb_scroll_y.pack_forget()
    dirname = os.getcwd()
    dirfiles = os.listdir(dirname)

    fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

    files = []

    for file in fullpaths:
        if os.path.isfile(file) and file.lower().endswith("xml"): files.append(
            file)
    global dict_checkbuttons
    dict_checkbuttons = {}
    cb_canvas = tk.Canvas(frame_list, width=1200, height=900)
    cb_scroll_y = tk.Scrollbar(frame_list, orient="vertical", command=cb_canvas.yview)

    frame = tk.Frame(cb_canvas)
    var1 = tk.BooleanVar()
    var1.set(0)
    j = 0
    global dict_checks
    dict_checks = {}
    for i in files:
        dict_checks[i] = tk.BooleanVar()
        dict_checks[i].set(0)
        backslash = "\\"
        dict_checkbuttons[i] = tk.Checkbutton(frame, text=f"{i[i.rfind(backslash) + 1:]}",
                                              font=("Times New Roman", 20),
                                              borderwidth=3,
                                              bg="white",
                                              relief="ridge",
                                              width=77,
                                              variable=dict_checks[i],
                                              anchor='w')
        dict_checkbuttons[i].pack(fill="x")
        j += 1

    # put the frame in the canvas
    cb_canvas.create_window(0, 0, anchor='nw', window=frame)
    # make sure everything is displayed before configuring the scrollregion
    cb_canvas.update_idletasks()

    cb_canvas.configure(scrollregion=cb_canvas.bbox('all'),
                        yscrollcommand=cb_scroll_y.set)

    cb_canvas.pack(fill='both', expand=True, side='left')
    cb_scroll_y.pack(fill='y', expand=True, side='right')
    pass
def sort_csv():
    button_csv['bg'] = "Blue"
    button_csv['fg'] = "White"
    button_xml['bg'] = "White"
    button_xml['fg'] = "Black"
    button_all['bg'] = 'White'
    button_all['fg'] = "Black"
    global cb_canvas, cb_scroll_y
    cb_canvas.pack_forget()
    cb_scroll_y.pack_forget()
    dirname = os.getcwd()
    dirfiles = os.listdir(dirname)

    fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

    files = []

    for file in fullpaths:
        if os.path.isfile(file) and file.lower().endswith("csv"): files.append(
            file)
    global dict_checkbuttons
    dict_checkbuttons = {}
    cb_canvas = tk.Canvas(frame_list, width=1200, height=900)
    cb_scroll_y = tk.Scrollbar(frame_list, orient="vertical", command=cb_canvas.yview)

    frame = tk.Frame(cb_canvas)
    var1 = tk.BooleanVar()
    var1.set(0)
    j = 0
    global dict_checks
    dict_checks = {}
    for i in files:
        dict_checks[i] = tk.BooleanVar()
        dict_checks[i].set(0)
        backslash = "\\"
        dict_checkbuttons[i] = tk.Checkbutton(frame, text=f"{i[i.rfind(backslash) + 1:]}",
                                              font=("Times New Roman", 20),
                                              borderwidth=3,
                                              bg="white",
                                              relief="ridge",
                                              width=77,
                                              variable=dict_checks[i],
                                              anchor='w')
        dict_checkbuttons[i].pack(fill="x")
        j += 1

    # put the frame in the canvas
    cb_canvas.create_window(0, 0, anchor='nw', window=frame)
    # make sure everything is displayed before configuring the scrollregion
    cb_canvas.update_idletasks()

    cb_canvas.configure(scrollregion=cb_canvas.bbox('all'),
                        yscrollcommand=cb_scroll_y.set)

    cb_canvas.pack(fill='both', expand=True, side='left')
    cb_scroll_y.pack(fill='y', expand=True, side='right')
    pass
button_all = tk.Button(frame_sort,
                       width=6,
                       height=1,
                       text="ALL",
                       font=("Times New Roman", 20),
                       bg="Blue",
                       fg="White",
                       relief="groove",
                       command=sort_all)
button_csv = tk.Button(frame_sort,
                       width=6,
                       height=1,
                       text="CSV",
                       font=("Times New Roman", 20),
                       bg="White",
                       relief="groove",
                       command=sort_csv)
button_xml = tk.Button(frame_sort,
                       width=6,
                       height=1,
                       text="XML",
                       font=("Times New Roman", 20),
                       bg="White",
                       relief="groove",
                       command=sort_xml)
button_all.pack(side='left', anchor='w')
button_xml.pack(side='left', anchor="w")
button_csv.pack(side='left', anchor='w')
# Фрейм для показа списка файлов и нижних кнопок
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
    dict_checks[i] = tk.BooleanVar()
    dict_checks[i].set(0)
    backslash = "\\"
    dict_checkbuttons[i] = tk.Checkbutton(frame,text=f"{i[i.rfind(backslash) + 1:]}",
                                          font=("Times New Roman", 20),
                                          borderwidth=3,
                                          bg="white",
                                          relief="ridge",
                                          width=77,
                                          variable=dict_checks[i],
                                          anchor='w')
    dict_checkbuttons[i].pack(fill="x")
    j+=1


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

button_convert = tk.Button(canvas,
          width=28,
          height=1,
          text="Конвертировать в CSV выбранное",
          font=("Times New Roman", 14),
          bg="White",
          relief="groove",
          command=convert_click).pack(side="left")
button_convert_all = tk.Button(canvas,
          width=28,
          height=1,
          text="Конвертировать в CSV все",
          font=("Times New Roman", 14),
          bg="White",
          relief="groove",
          command=convert_all_click).pack(side="left")
tk.Button(canvas,
          width=28,
          height=1,
          text="Загрузить в БД выбранное",
          font=("Times New Roman", 14),
          bg="White",
          relief="groove").pack(side="left")
tk.Button(canvas,
          width=28,
          height=1,
          text="Загрузить в БД все",
          font=("Times New Roman", 14),
          bg="White",
          relief="groove").pack(side="left")
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
        if os.path.isfile(file) and (file.lower().endswith("xml") or file.lower().endswith("csv")): files.append(
            file)
    global dict_checkbuttons
    dict_checkbuttons = {}
    cb_canvas = tk.Canvas(frame_list, width=1200, height=900)
    cb_scroll_y = tk.Scrollbar(frame_list, orient="vertical", command=cb_canvas.yview)

    frame = tk.Frame(cb_canvas)
    var1 = tk.BooleanVar()
    var1.set(0)

    j = 0
    global dict_checks
    dict_checks = {}
    for i in files:
        dict_checks[i] = tk.BooleanVar()
        dict_checks[i].set(0)
        backslash = "\\"
        dict_checkbuttons[i] = tk.Checkbutton(frame, text=f"{i[i.rfind(backslash) + 1:]}",
                                              font=("Times New Roman", 20),
                                              borderwidth=3,
                                              bg="white",
                                              relief="ridge",
                                              width=77,
                                              variable=dict_checks[i],
                                              anchor='w')
        dict_checkbuttons[i].pack(fill="x")
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
        button_csv['bg'] = "White"
        button_csv['fg'] = "Black"
        button_xml['bg'] = "White"
        button_xml['fg'] = "Black"
        button_all['bg'] = "Blue"
        button_all['fg'] = "White"

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

#
        self.notChoisedDirButton
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.notChoisedDirButton.setFont(font)
        self.notChoisedDirButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border : solid black;\n"
"border-width : 2px 2px 2px 2px;\n"
"\n"
"")
        self.notChoisedDirButton.setObjectName("notChoisedDirButton")
        self.verticalLayout.addWidget(self.notChoisedDirButton)
#

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
