import os
from progress.bar import IncrementalBar
from datetime import datetime


import sys


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
                     "VALUE": "CP_VALUE",
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
    return (Names)





def main():
    dict_conding = {
        'Ҡ': "K",
        'Ң': 'H',
        'Ә': 'Э',
        'Ҙ': 'З',
        'Һ': "h",
        'ә': 'э',
        'ҙ': 'з',
        '¸': '.',
        '\u2003': '',
        'җ': 'ж',
        '┐': 'т',
        '\u200b': '',
        '\u2002': '',
        'Ă': 'A',
        'Ç': 'C',
        'Ě': 'E',
        'Ι': 'I',
        '\u2000': "",
        '½': '0,5',
        '\ue00b': '',
        '\ue007': '',
        'ѐ': 'e'
    }
    decoding_table = (
        '\x00'  # 0x00 -> NULL
        '\x01'  # 0x01 -> START OF HEADING
        '\x02'  # 0x02 -> START OF TEXT
        '\x03'  # 0x03 -> END OF TEXT
        '\x04'  # 0x04 -> END OF TRANSMISSION
        '\x05'  # 0x05 -> ENQUIRY
        '\x06'  # 0x06 -> ACKNOWLEDGE
        '\x07'  # 0x07 -> BELL
        '\x08'  # 0x08 -> BACKSPACE
        '\t'  # 0x09 -> HORIZONTAL TABULATION
        '\n'  # 0x0A -> LINE FEED
        '\x0b'  # 0x0B -> VERTICAL TABULATION
        '\x0c'  # 0x0C -> FORM FEED
        '\r'  # 0x0D -> CARRIAGE RETURN
        '\x0e'  # 0x0E -> SHIFT OUT
        '\x0f'  # 0x0F -> SHIFT IN
        '\x10'  # 0x10 -> DATA LINK ESCAPE
        '\x11'  # 0x11 -> DEVICE CONTROL ONE
        '\x12'  # 0x12 -> DEVICE CONTROL TWO
        '\x13'  # 0x13 -> DEVICE CONTROL THREE
        '\x14'  # 0x14 -> DEVICE CONTROL FOUR
        '\x15'  # 0x15 -> NEGATIVE ACKNOWLEDGE
        '\x16'  # 0x16 -> SYNCHRONOUS IDLE
        '\x17'  # 0x17 -> END OF TRANSMISSION BLOCK
        '\x18'  # 0x18 -> CANCEL
        '\x19'  # 0x19 -> END OF MEDIUM
        '\x1a'  # 0x1A -> SUBSTITUTE
        '\x1b'  # 0x1B -> ESCAPE
        '\x1c'  # 0x1C -> FILE SEPARATOR
        '\x1d'  # 0x1D -> GROUP SEPARATOR
        '\x1e'  # 0x1E -> RECORD SEPARATOR
        '\x1f'  # 0x1F -> UNIT SEPARATOR
        ' '  # 0x20 -> SPACE
        '!'  # 0x21 -> EXCLAMATION MARK
        '"'  # 0x22 -> QUOTATION MARK
        '#'  # 0x23 -> NUMBER SIGN
        '$'  # 0x24 -> DOLLAR SIGN
        '%'  # 0x25 -> PERCENT SIGN
        '&'  # 0x26 -> AMPERSAND
        "'"  # 0x27 -> APOSTROPHE
        '('  # 0x28 -> LEFT PARENTHESIS
        ')'  # 0x29 -> RIGHT PARENTHESIS
        '*'  # 0x2A -> ASTERISK
        '+'  # 0x2B -> PLUS SIGN
        ','  # 0x2C -> COMMA
        '-'  # 0x2D -> HYPHEN-MINUS
        '.'  # 0x2E -> FULL STOP
        '/'  # 0x2F -> SOLIDUS
        '0'  # 0x30 -> DIGIT ZERO
        '1'  # 0x31 -> DIGIT ONE
        '2'  # 0x32 -> DIGIT TWO
        '3'  # 0x33 -> DIGIT THREE
        '4'  # 0x34 -> DIGIT FOUR
        '5'  # 0x35 -> DIGIT FIVE
        '6'  # 0x36 -> DIGIT SIX
        '7'  # 0x37 -> DIGIT SEVEN
        '8'  # 0x38 -> DIGIT EIGHT
        '9'  # 0x39 -> DIGIT NINE
        ':'  # 0x3A -> COLON
        ';'  # 0x3B -> SEMICOLON
        '<'  # 0x3C -> LESS-THAN SIGN
        '='  # 0x3D -> EQUALS SIGN
        '>'  # 0x3E -> GREATER-THAN SIGN
        '?'  # 0x3F -> QUESTION MARK
        '@'  # 0x40 -> COMMERCIAL AT
        'A'  # 0x41 -> LATIN CAPITAL LETTER A
        'B'  # 0x42 -> LATIN CAPITAL LETTER B
        'C'  # 0x43 -> LATIN CAPITAL LETTER C
        'D'  # 0x44 -> LATIN CAPITAL LETTER D
        'E'  # 0x45 -> LATIN CAPITAL LETTER E
        'F'  # 0x46 -> LATIN CAPITAL LETTER F
        'G'  # 0x47 -> LATIN CAPITAL LETTER G
        'H'  # 0x48 -> LATIN CAPITAL LETTER H
        'I'  # 0x49 -> LATIN CAPITAL LETTER I
        'J'  # 0x4A -> LATIN CAPITAL LETTER J
        'K'  # 0x4B -> LATIN CAPITAL LETTER K
        'L'  # 0x4C -> LATIN CAPITAL LETTER L
        'M'  # 0x4D -> LATIN CAPITAL LETTER M
        'N'  # 0x4E -> LATIN CAPITAL LETTER N
        'O'  # 0x4F -> LATIN CAPITAL LETTER O
        'P'  # 0x50 -> LATIN CAPITAL LETTER P
        'Q'  # 0x51 -> LATIN CAPITAL LETTER Q
        'R'  # 0x52 -> LATIN CAPITAL LETTER R
        'S'  # 0x53 -> LATIN CAPITAL LETTER S
        'T'  # 0x54 -> LATIN CAPITAL LETTER T
        'U'  # 0x55 -> LATIN CAPITAL LETTER U
        'V'  # 0x56 -> LATIN CAPITAL LETTER V
        'W'  # 0x57 -> LATIN CAPITAL LETTER W
        'X'  # 0x58 -> LATIN CAPITAL LETTER X
        'Y'  # 0x59 -> LATIN CAPITAL LETTER Y
        'Z'  # 0x5A -> LATIN CAPITAL LETTER Z
        '['  # 0x5B -> LEFT SQUARE BRACKET
        '\\'  # 0x5C -> REVERSE SOLIDUS
        ']'  # 0x5D -> RIGHT SQUARE BRACKET
        '^'  # 0x5E -> CIRCUMFLEX ACCENT
        '_'  # 0x5F -> LOW LINE
        '`'  # 0x60 -> GRAVE ACCENT
        'a'  # 0x61 -> LATIN SMALL LETTER A
        'b'  # 0x62 -> LATIN SMALL LETTER B
        'c'  # 0x63 -> LATIN SMALL LETTER C
        'd'  # 0x64 -> LATIN SMALL LETTER D
        'e'  # 0x65 -> LATIN SMALL LETTER E
        'f'  # 0x66 -> LATIN SMALL LETTER F
        'g'  # 0x67 -> LATIN SMALL LETTER G
        'h'  # 0x68 -> LATIN SMALL LETTER H
        'i'  # 0x69 -> LATIN SMALL LETTER I
        'j'  # 0x6A -> LATIN SMALL LETTER J
        'k'  # 0x6B -> LATIN SMALL LETTER K
        'l'  # 0x6C -> LATIN SMALL LETTER L
        'm'  # 0x6D -> LATIN SMALL LETTER M
        'n'  # 0x6E -> LATIN SMALL LETTER N
        'o'  # 0x6F -> LATIN SMALL LETTER O
        'p'  # 0x70 -> LATIN SMALL LETTER P
        'q'  # 0x71 -> LATIN SMALL LETTER Q
        'r'  # 0x72 -> LATIN SMALL LETTER R
        's'  # 0x73 -> LATIN SMALL LETTER S
        't'  # 0x74 -> LATIN SMALL LETTER T
        'u'  # 0x75 -> LATIN SMALL LETTER U
        'v'  # 0x76 -> LATIN SMALL LETTER V
        'w'  # 0x77 -> LATIN SMALL LETTER W
        'x'  # 0x78 -> LATIN SMALL LETTER X
        'y'  # 0x79 -> LATIN SMALL LETTER Y
        'z'  # 0x7A -> LATIN SMALL LETTER Z
        '{'  # 0x7B -> LEFT CURLY BRACKET
        '|'  # 0x7C -> VERTICAL LINE
        '}'  # 0x7D -> RIGHT CURLY BRACKET
        '~'  # 0x7E -> TILDE
        '\x7f'  # 0x7F -> DELETE
        '\u0402'  # 0x80 -> CYRILLIC CAPITAL LETTER DJE
        '\u0403'  # 0x81 -> CYRILLIC CAPITAL LETTER GJE
        '\u201a'  # 0x82 -> SINGLE LOW-9 QUOTATION MARK
        '\u0453'  # 0x83 -> CYRILLIC SMALL LETTER GJE
        '\u201e'  # 0x84 -> DOUBLE LOW-9 QUOTATION MARK
        '\u2026'  # 0x85 -> HORIZONTAL ELLIPSIS
        '\u2020'  # 0x86 -> DAGGER
        '\u2021'  # 0x87 -> DOUBLE DAGGER
        '\u20ac'  # 0x88 -> EURO SIGN
        '\u2030'  # 0x89 -> PER MILLE SIGN
        '\u0409'  # 0x8A -> CYRILLIC CAPITAL LETTER LJE
        '\u2039'  # 0x8B -> SINGLE LEFT-POINTING ANGLE QUOTATION MARK
        '\u040a'  # 0x8C -> CYRILLIC CAPITAL LETTER NJE
        '\u040c'  # 0x8D -> CYRILLIC CAPITAL LETTER KJE
        '\u040b'  # 0x8E -> CYRILLIC CAPITAL LETTER TSHE
        '\u040f'  # 0x8F -> CYRILLIC CAPITAL LETTER DZHE
        '\u0452'  # 0x90 -> CYRILLIC SMALL LETTER DJE
        '\u2018'  # 0x91 -> LEFT SINGLE QUOTATION MARK
        '\u2019'  # 0x92 -> RIGHT SINGLE QUOTATION MARK
        '\u201c'  # 0x93 -> LEFT DOUBLE QUOTATION MARK
        '\u201d'  # 0x94 -> RIGHT DOUBLE QUOTATION MARK
        '\u2022'  # 0x95 -> BULLET
        '\u2013'  # 0x96 -> EN DASH
        '\u2014'  # 0x97 -> EM DASH
        '\ufffe'  # 0x98 -> UNDEFINED
        '\u2122'  # 0x99 -> TRADE MARK SIGN
        '\u0459'  # 0x9A -> CYRILLIC SMALL LETTER LJE
        '\u203a'  # 0x9B -> SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
        '\u045a'  # 0x9C -> CYRILLIC SMALL LETTER NJE
        '\u045c'  # 0x9D -> CYRILLIC SMALL LETTER KJE
        '\u045b'  # 0x9E -> CYRILLIC SMALL LETTER TSHE
        '\u045f'  # 0x9F -> CYRILLIC SMALL LETTER DZHE
        '\xa0'  # 0xA0 -> NO-BREAK SPACE
        '\u040e'  # 0xA1 -> CYRILLIC CAPITAL LETTER SHORT U
        '\u045e'  # 0xA2 -> CYRILLIC SMALL LETTER SHORT U
        '\u0408'  # 0xA3 -> CYRILLIC CAPITAL LETTER JE
        '\xa4'  # 0xA4 -> CURRENCY SIGN
        '\u0490'  # 0xA5 -> CYRILLIC CAPITAL LETTER GHE WITH UPTURN
        '\xa6'  # 0xA6 -> BROKEN BAR
        '\xa7'  # 0xA7 -> SECTION SIGN
        '\u0401'  # 0xA8 -> CYRILLIC CAPITAL LETTER IO
        '\xa9'  # 0xA9 -> COPYRIGHT SIGN
        '\u0404'  # 0xAA -> CYRILLIC CAPITAL LETTER UKRAINIAN IE
        '\xab'  # 0xAB -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
        '\xac'  # 0xAC -> NOT SIGN
        '\xad'  # 0xAD -> SOFT HYPHEN
        '\xae'  # 0xAE -> REGISTERED SIGN
        '\u0407'  # 0xAF -> CYRILLIC CAPITAL LETTER YI
        '\xb0'  # 0xB0 -> DEGREE SIGN
        '\xb1'  # 0xB1 -> PLUS-MINUS SIGN
        '\u0406'  # 0xB2 -> CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
        '\u0456'  # 0xB3 -> CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
        '\u0491'  # 0xB4 -> CYRILLIC SMALL LETTER GHE WITH UPTURN
        '\xb5'  # 0xB5 -> MICRO SIGN
        '\xb6'  # 0xB6 -> PILCROW SIGN
        '\xb7'  # 0xB7 -> MIDDLE DOT
        '\u0451'  # 0xB8 -> CYRILLIC SMALL LETTER IO
        '\u2116'  # 0xB9 -> NUMERO SIGN
        '\u0454'  # 0xBA -> CYRILLIC SMALL LETTER UKRAINIAN IE
        '\xbb'  # 0xBB -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
        '\u0458'  # 0xBC -> CYRILLIC SMALL LETTER JE
        '\u0405'  # 0xBD -> CYRILLIC CAPITAL LETTER DZE
        '\u0455'  # 0xBE -> CYRILLIC SMALL LETTER DZE
        '\u0457'  # 0xBF -> CYRILLIC SMALL LETTER YI
        '\u0410'  # 0xC0 -> CYRILLIC CAPITAL LETTER A
        '\u0411'  # 0xC1 -> CYRILLIC CAPITAL LETTER BE
        '\u0412'  # 0xC2 -> CYRILLIC CAPITAL LETTER VE
        '\u0413'  # 0xC3 -> CYRILLIC CAPITAL LETTER GHE
        '\u0414'  # 0xC4 -> CYRILLIC CAPITAL LETTER DE
        '\u0415'  # 0xC5 -> CYRILLIC CAPITAL LETTER IE
        '\u0416'  # 0xC6 -> CYRILLIC CAPITAL LETTER ZHE
        '\u0417'  # 0xC7 -> CYRILLIC CAPITAL LETTER ZE
        '\u0418'  # 0xC8 -> CYRILLIC CAPITAL LETTER I
        '\u0419'  # 0xC9 -> CYRILLIC CAPITAL LETTER SHORT I
        '\u041a'  # 0xCA -> CYRILLIC CAPITAL LETTER KA
        '\u041b'  # 0xCB -> CYRILLIC CAPITAL LETTER EL
        '\u041c'  # 0xCC -> CYRILLIC CAPITAL LETTER EM
        '\u041d'  # 0xCD -> CYRILLIC CAPITAL LETTER EN
        '\u041e'  # 0xCE -> CYRILLIC CAPITAL LETTER O
        '\u041f'  # 0xCF -> CYRILLIC CAPITAL LETTER PE
        '\u0420'  # 0xD0 -> CYRILLIC CAPITAL LETTER ER
        '\u0421'  # 0xD1 -> CYRILLIC CAPITAL LETTER ES
        '\u0422'  # 0xD2 -> CYRILLIC CAPITAL LETTER TE
        '\u0423'  # 0xD3 -> CYRILLIC CAPITAL LETTER U
        '\u0424'  # 0xD4 -> CYRILLIC CAPITAL LETTER EF
        '\u0425'  # 0xD5 -> CYRILLIC CAPITAL LETTER HA
        '\u0426'  # 0xD6 -> CYRILLIC CAPITAL LETTER TSE
        '\u0427'  # 0xD7 -> CYRILLIC CAPITAL LETTER CHE
        '\u0428'  # 0xD8 -> CYRILLIC CAPITAL LETTER SHA
        '\u0429'  # 0xD9 -> CYRILLIC CAPITAL LETTER SHCHA
        '\u042a'  # 0xDA -> CYRILLIC CAPITAL LETTER HARD SIGN
        '\u042b'  # 0xDB -> CYRILLIC CAPITAL LETTER YERU
        '\u042c'  # 0xDC -> CYRILLIC CAPITAL LETTER SOFT SIGN
        '\u042d'  # 0xDD -> CYRILLIC CAPITAL LETTER E
        '\u042e'  # 0xDE -> CYRILLIC CAPITAL LETTER YU
        '\u042f'  # 0xDF -> CYRILLIC CAPITAL LETTER YA
        '\u0430'  # 0xE0 -> CYRILLIC SMALL LETTER A
        '\u0431'  # 0xE1 -> CYRILLIC SMALL LETTER BE
        '\u0432'  # 0xE2 -> CYRILLIC SMALL LETTER VE
        '\u0433'  # 0xE3 -> CYRILLIC SMALL LETTER GHE
        '\u0434'  # 0xE4 -> CYRILLIC SMALL LETTER DE
        '\u0435'  # 0xE5 -> CYRILLIC SMALL LETTER IE
        '\u0436'  # 0xE6 -> CYRILLIC SMALL LETTER ZHE
        '\u0437'  # 0xE7 -> CYRILLIC SMALL LETTER ZE
        '\u0438'  # 0xE8 -> CYRILLIC SMALL LETTER I
        '\u0439'  # 0xE9 -> CYRILLIC SMALL LETTER SHORT I
        '\u043a'  # 0xEA -> CYRILLIC SMALL LETTER KA
        '\u043b'  # 0xEB -> CYRILLIC SMALL LETTER EL
        '\u043c'  # 0xEC -> CYRILLIC SMALL LETTER EM
        '\u043d'  # 0xED -> CYRILLIC SMALL LETTER EN
        '\u043e'  # 0xEE -> CYRILLIC SMALL LETTER O
        '\u043f'  # 0xEF -> CYRILLIC SMALL LETTER PE
        '\u0440'  # 0xF0 -> CYRILLIC SMALL LETTER ER
        '\u0441'  # 0xF1 -> CYRILLIC SMALL LETTER ES
        '\u0442'  # 0xF2 -> CYRILLIC SMALL LETTER TE
        '\u0443'  # 0xF3 -> CYRILLIC SMALL LETTER U
        '\u0444'  # 0xF4 -> CYRILLIC SMALL LETTER EF
        '\u0445'  # 0xF5 -> CYRILLIC SMALL LETTER HA
        '\u0446'  # 0xF6 -> CYRILLIC SMALL LETTER TSE
        '\u0447'  # 0xF7 -> CYRILLIC SMALL LETTER CHE
        '\u0448'  # 0xF8 -> CYRILLIC SMALL LETTER SHA
        '\u0449'  # 0xF9 -> CYRILLIC SMALL LETTER SHCHA
        '\u044a'  # 0xFA -> CYRILLIC SMALL LETTER HARD SIGN
        '\u044b'  # 0xFB -> CYRILLIC SMALL LETTER YERU
        '\u044c'  # 0xFC -> CYRILLIC SMALL LETTER SOFT SIGN
        '\u044d'  # 0xFD -> CYRILLIC SMALL LETTER E
        '\u044e'  # 0xFE -> CYRILLIC SMALL LETTER YU
        '\u044f'  # 0xFF -> CYRILLIC SMALL LETTER YA
    )
    notdecodingtable = ['Ҡ', 'Ң', 'Ә', 'Ҙ', 'Һ', 'ә', 'ҙ', '¸', '\u2003', 'җ', '┐', '\u200b', '\u2002', 'Ă', 'Ç', 'Ě', 'Ι', '\u2000', '½', '\ue00b', '\ue007', 'ѐ']
    path = os.getcwd()
    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])
    xml = []

    for dirs, folder, files in os.walk(os.getcwd()):
        for fil in files:
            if ".xml" in f"{os.path.join(dirs, fil)}".lower():
                # if "venv" not in f"{os.path.join(dirs, file)}".lower() and ".idea" not in f"{os.path.join(dirs, file)}".lower():
                xml.append(os.path.join(dirs, fil))
    directory = os.getcwd()
    files = os.listdir(directory)
    bar = IncrementalBar('Прогресс', max=len(xml))
    global file
    for file in xml:
        try:

            bar.next()
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
            name_dir_csv = name_csv[name_csv.rfind("garupdate")+10:name_csv.rfind("as")]
            backslash= "\\"
            name_dir_csv = name_dir_csv[name_dir_csv.find(backslash)+1:]
            name_csv = name_csv[name_csv.rfind("as"):]

            dir = os.getcwd()
            dir = dir[:dir.rfind("GARUPDATE")+10]
            # dir = name_csv[len(path):]
            if not os.path.isdir(f"{dir}\csv"):
                os.mkdir(f"{dir}\csv")
            dir = dir+"\csv\\"+name_dir_csv
            # dir = f"{path}\csv{dir}"

            if "0" in dir or "1" in dir or "2" in dir or "3" in dir or "4" in dir or '5' in dir or '6' in dir or'7' in dir or '8' in dir or "9" in dir:
                if not os.path.isdir(f"{dir}"):
                    os.mkdir(f"{dir}")
            dir = dir+name_csv
            with open(f'{dir}csv', 'w+', encoding="Windows-1251") as f:
                text = ""
                for i in DictNames.keys():
                    text += DictNames[i] + "|"
                print(text[:-1], file=f)

            with open(f'{dir}csv', 'a+', encoding="Windows-1251") as f:
                # example use
                @coroutine
                def printer():
                    j = 0
                    num = 0
                    global file

                    if "AS_ADDHOUSE_TYPES" in file:
                        while True:

                            event = (yield)
                            testprint = list(event)
                            event = str(event)
                            dict_sort = {}

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
                                        text += dict_sort[key].replace("\n", " ") + "|"
                                    try:
                                        print(text[:-1], file=f)
                                    except:
                                        for s in text:
                                            if s not in decoding_table:
                                                if s not in notdecodingtable:
                                                    notdecodingtable.append(s)
                                        newtext = ""
                                        for s in text:
                                            try:
                                                newtext += dict_conding[s]
                                            except:
                                                if s not in decoding_table:
                                                    newtext += ""
                                                else:
                                                    newtext += s
                                        print(newtext[:-1], file=f)
                            pass
                    elif "AS_ADDHOUSE_TYPES" in file:
                        while True:

                            event = (yield)
                            testprint = list(event)
                            event = str(event)
                            dict_sort = {}

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
                                        text += dict_sort[key].replace("\n", " ") + "|"
                                    try:
                                        print(text[:-1], file=f)
                                    except:
                                        for s in text:
                                            if s not in decoding_table:
                                                if s not in notdecodingtable:
                                                    notdecodingtable.append(s)
                                        newtext = ""
                                        for s in text:
                                            try:
                                                newtext += dict_conding[s]
                                            except:
                                                if s not in decoding_table:
                                                    newtext += ""
                                                else:
                                                    newtext += s
                                        print(newtext[:-1], file=f)
                            pass
                    elif "AS_APARTMENT_TYPES" in file:
                        while True:

                            event = (yield)
                            testprint = list(event)
                            event = str(event)
                            dict_sort = {}
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
                                        text += dict_sort[key].replace("\n", " ") + "|"
                                    try:
                                        print(text[:-1], file=f)
                                    except:
                                        for s in text:
                                            if s not in decoding_table:
                                                if s not in notdecodingtable:
                                                    notdecodingtable.append(s)
                                        newtext = ""
                                        for s in text:
                                            try:
                                                newtext += dict_conding[s]
                                            except:
                                                if s not in decoding_table:
                                                    newtext += ""
                                                else:
                                                    newtext += s
                                        print(newtext[:-1], file=f)
                            pass
                    elif "AS_HOUSE_TYPES" in file:
                        while True:

                            event = (yield)
                            testprint = list(event)
                            event = str(event)
                            dict_sort = {}
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
                                        text += dict_sort[key].replace("\n", " ") + "|"
                                    try:
                                        print(text[:-1], file=f)
                                    except:
                                        for s in text:
                                            if s not in decoding_table:
                                                if s not in notdecodingtable:
                                                    notdecodingtable.append(s)
                                        newtext = ""
                                        for s in text:
                                            try:
                                                newtext += dict_conding[s]
                                            except:
                                                if s not in decoding_table:
                                                    newtext += ""
                                                else:
                                                    newtext += s
                                        print(newtext[:-1], file=f)
                            pass
                    elif "AS_PARAM_TYPES" in file:
                        while True:

                            event = (yield)
                            testprint = list(event)
                            event = str(event)
                            dict_sort = {}
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
                                        text += dict_sort[key].replace("\n", " ") + "|"
                                    try:
                                        print(text[:-1], file=f)
                                    except:
                                        for s in text:
                                            if s not in decoding_table:
                                                if s not in notdecodingtable:
                                                    notdecodingtable.append(s)
                                        newtext = ""
                                        for s in text:
                                            try:
                                                newtext += dict_conding[s]
                                            except:
                                                if s not in decoding_table:
                                                    newtext += ""
                                                else:
                                                    newtext += s
                                        print(newtext[:-1], file=f)
                            pass
                    elif "AS_OPERATION_TYPES" in file:
                        while True:

                            event = (yield)
                            testprint = list(event)
                            event = str(event)
                            dict_sort = {}
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
                                            text += dict_sort[key].replace("\n", " ") + "|"
                                        try:
                                            print(text[:-1], file=f)
                                        except:
                                            for s in text:
                                                if s not in decoding_table:
                                                    if s not in notdecodingtable:
                                                        notdecodingtable.append(s)
                                            newtext = ""
                                            for s in text:
                                                try:
                                                    newtext += dict_conding[s]
                                                except:
                                                    if s not in decoding_table:
                                                        newtext += ""
                                                    else:
                                                        newtext += s
                                            print(newtext[:-1], file=f)
                                    except:
                                        pass
                            pass
                    elif "AS_OBJECT_LEVELS" in file:
                        while True:

                            event = (yield)
                            testprint = list(event)
                            event = str(event)
                            dict_sort = {}
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
                                                     "OL_NAME": dict_event["NAME"],
                                                     "OL_SHORTNAME": dict_event["SHORTNAME"],
                                                     "OL_UPDATEDATE": dict_event["UPDATEDATE"],
                                                     "OL_STARTDATE": dict_event["STARTDATE"],
                                                     "OL_ENDDATE": dict_event["ENDDATE"],
                                                     "OL_ISACTIVE": dict_event["ISACTIVE"]}
                                        text = ""
                                        for key in dict_sort.keys():
                                            text += dict_sort[key].replace("\n", " ") + "|"
                                        try:
                                            print(text[:-1], file=f)
                                        except:
                                            for s in text:
                                                if s not in decoding_table:
                                                    if s not in notdecodingtable:
                                                        notdecodingtable.append(s)
                                            newtext = ""
                                            for s in text:
                                                try:
                                                    newtext += dict_conding[s]
                                                except:
                                                    if s not in decoding_table:
                                                        newtext += ""
                                                    else:
                                                        newtext += s
                                            print(newtext[:-1], file=f)
                                    except:
                                        pass
                            pass
                    elif "AS_ROOM_TYPES" in file:
                        while True:

                            event = (yield)
                            testprint = list(event)
                            event = str(event)
                            dict_sort = {}
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
                                        text += dict_sort[key].replace("\n", " ") + "|"
                                    try:
                                        print(text[:-1], file=f)
                                    except:
                                        for s in text:
                                            if s not in decoding_table:
                                                if s not in notdecodingtable:
                                                    notdecodingtable.append(s)
                                        newtext = ""
                                        for s in text:
                                            try:
                                                newtext += dict_conding[s]
                                            except:
                                                if s not in decoding_table:
                                                    newtext += ""
                                                else:
                                                    newtext += s
                                        print(newtext[:-1], file=f)
                            pass
                    else:
                        while True:

                            event = (yield)
                            # testprint = list(event)

                            check_event = str(event)
                            dict_sort = {}
                            if "dict_keys([" in check_event:

                                list_event = list(event)

                                event = ""

                            if "dict_values([" in check_event:
                                list_atr = list(event)
                                if len(list_event) != len(ListNames):

                                    for i in range(len(ListNames)):

                                        try:
                                            if ListNames[i] != list_event[i]:
                                                list_event.insert(i, ListNames[i])
                                                list_atr.insert(i, "")

                                        except IndexError:
                                            list_event.append("")
                                            list_atr.append("")

                                    if len(list_event) != len(ListNames):
                                        if list_event[len(list_event) - 1] == "":
                                            list_event = list_event[:-1]
                                            list_atr = list_atr[:-1]

                                    text = ""
                                    for i in range(len(list_atr)):
                                        text += list_atr[i].replace("\n", " ") + "|"
                                    if list_atr[0] != "":
                                        try:
                                            print(text[:-1], file=f)
                                        except:
                                            for s in text:
                                                if s not in decoding_table:
                                                    if s not in notdecodingtable:
                                                        notdecodingtable.append(s)
                                            newtext = ""
                                            for s in text:
                                                try:
                                                    newtext += dict_conding[s]
                                                except:
                                                    if s not in decoding_table:
                                                        newtext += ""
                                                    else:
                                                        newtext += s
                                            print(newtext[:-1], file=f)


                                else:
                                    event = list(event)
                                    text=""
                                    for i in range(len(list_atr)):
                                        text+= list_atr[i].replace("\n", " ")+"|"
                                    try:
                                        print(text[:-1], file=f)
                                    except:
                                        for s in text:
                                            if s not in decoding_table:
                                                if s not in notdecodingtable:
                                                    notdecodingtable.append(s)
                                        newtext = ""
                                        for s in text:
                                            try:
                                                newtext += dict_conding[s]
                                            except:
                                                if s not in decoding_table:
                                                    newtext += ""
                                                else:
                                                    newtext += s
                                        print(newtext[:-1], file=f)
                            # print(notdecodingtable)
                xml.sax.parse(file, EventHandler(printer()))

        except:
            print("Не удалось обработать файл", file)
            pass



if __name__ == '__main__':
    main()
