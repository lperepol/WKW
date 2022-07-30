import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_metadata():
    fn = "../ManualEdits/KeepMetadata_002.csv"
    df = pd.read_csv(fn,encoding = "ISO-8859-1")
    return df


def get_detail(adic, df):
    for index, row in df.iterrows():
        Detail = str(row['Detail']).strip()
        adic[Detail] = SortedDict()
    return adic

def get_mag(adic, df):
    for index, row in df.iterrows():
        Detail = str(row['Detail']).strip()
        Mag = str(row['Mag']).strip()
        adic[Detail][Mag] = SortedDict()
    return adic

def get_family(adic, df):
    for index, row in df.iterrows():
        Detail = str(row['Detail']).strip()
        Mag = str(row['Mag']).strip()
        Family = str(row['Family']).strip()
        adic[Detail][Mag][Family] = SortedDict()
    return adic

def get_genus(adic, df):
    for index, row in df.iterrows():
        Detail = str(row['Detail']).strip()
        Mag = str(row['Mag']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        adic[Detail][Mag][Family][Genus] = SortedDict()
    return adic

def get_nid(adic, df):
    for index, row in df.iterrows():
        Detail = str(row['Detail']).strip()
        Mag = str(row['Mag']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        NID = str(row['NID']).strip()
        adic[Detail][Mag][Family][Genus][NID] = list()
    return adic

def get_image_file_name(adic, df):
    for index, row in df.iterrows():
        Detail = str(row['Detail']).strip()
        Mag = str(row['Mag']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        NID = str(row['NID']).strip()
        GitHub_Image_URL = str(row['GitHub_Image_URL']).strip()

        if GitHub_Image_URL not in adic[Detail][Mag][Family][Genus][NID]:
            adic[Detail][Mag][Family][Genus][NID].append(GitHub_Image_URL)

    return adic



def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "../../../files/json/wkw/NDMFG.json"

    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    df = read_metadata()

    nematode_dict = SortedDict()
    nematode_dict = get_detail(nematode_dict, df)
    nematode_dict = get_mag(nematode_dict, df)
    nematode_dict = get_family(nematode_dict, df)
    nematode_dict = get_genus(nematode_dict, df)
    nematode_dict = get_nid(nematode_dict, df)
    nematode_dict = get_image_file_name(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

