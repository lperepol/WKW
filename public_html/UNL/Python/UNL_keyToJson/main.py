import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_metadata():
    fn = "../Metadata/ManualEdits/KeepMetadata_002.csv"
    df = pd.read_csv(fn,  encoding= 'unicode_escape')
    df = df.fillna('')
    return df

def read_keys():
    fn = "../Metadata/ManualEdits/KeepMetadata_002_keys.csv"
    df = pd.read_csv(fn,  encoding= 'unicode_escape')
    df = df.fillna('')
    return df

def fixup(df):
    df = df.fillna(0)
    for index, row in df.iterrows():
        Magnification = str(row['Magnification']).strip()
        if Magnification.isdigit():
            Magnification = int(Magnification)
            Magnification = "{:03d}X".format(Magnification)
        df.loc[index, 'Magnification'] = Magnification
    return df

def get_Keys(adic, df):
    for index, row in df.iterrows():
        Param = str(row['Param']).strip()
        Image = str(row['Image' ]).strip()
        if len(Image) > 3:
            adic[Param] = list()
    return adic

def get_images(adic, df):
    for index, row in df.iterrows():
        Param = str(row['Param']).strip()
        Image = str(row['Image' ]).strip()
        if Param in adic :
            if len(Image) > 3:
                if Image not in adic[Param]:
                    adic[Param].append(Image)
    return adic

def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "../../../files/json/unl/UNL_Keys.json"
    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    #df = fixup(df)
    #df = read_metadata()
    df = read_keys()
    nematode_dict = SortedDict()
    nematode_dict = get_Keys(nematode_dict, df)
    nematode_dict = get_images(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)

if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

