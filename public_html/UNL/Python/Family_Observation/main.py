import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_metadata():
    fn = "../Metadata/ManualEdits/KeepMetadata_002.csv"
    df = pd.read_csv(fn)
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


def get_Family(adic, df):

    for index, row in df.iterrows():
        Family = str(row['Family']).strip()
        adic[Family] = SortedDict()
    return adic


def get_Observation(adic, df):

    for index, row in df.iterrows():
        Family = str(row['Family']).strip()
        Detail = str(row['Detail']).strip()
        adic[Family][Detail] = list()
    return adic

def get_image_file_name(adic, df):
    for index, row in df.iterrows():
        Family = str(row['Family']).strip()
        Detail = str(row['Detail']).strip()
        ImageName = str(row['ImageName']).strip()
        if ImageName not in adic[Family][Detail]:
            adic[Family][Detail].append(ImageName)
    return adic
Order_Observation
def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "../../../files/json/unl/Family_Observation.json"
    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    df = read_metadata()
    df = fixup(df)
    nematode_dict = SortedDict()
    nematode_dict = get_Family(nematode_dict, df)
    nematode_dict = get_Observation(nematode_dict, df)
    nematode_dict = get_image_file_name(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)


if __name__ == '__main__':
    print("Begin")
    main()
    print("End")
