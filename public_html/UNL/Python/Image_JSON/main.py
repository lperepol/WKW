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


def get_image_file_name(adic, df):
    for index, row in df.iterrows():
        ImageName = str(row['ImageName']).strip()
        ImageText = str(row['ImageText']).strip()
        Gender = str(row['Gender']).strip()
        General = str(row['General']).strip()
        Descr = str(row['Descr']).strip()
        Detail = str(row['Detail']).strip()
        Magnification = str(row['Magnification']).strip()
        Location = str(row['Location']).strip()
        Host = str(row['Host']).strip()
        Species = str(row['Species']).strip()
        ScientificName_accepted = str(row['ScientificName_accepted']).strip()
        ScientificName = str(row['ScientificName']).strip()
        Class = str(row['Class']).strip()
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        Species = str(row['Species']).strip()
        lst = [
            ImageName,
            ImageText,
            Gender,
            General,
            Descr,
            Detail,
            Magnification,
            Location,
            Host,
            Species,
            ScientificName_accepted,
            ScientificName,
            Class,
            Order,
            Family,
            Genus,
            Species
        ]
        adic[ImageName] = lst
    return adic

def writeDict2Json(adict):
    json_object = json.dumps(adict, indent=4)
    fn = "../../../files/json/unl/UNL_Flat_Images.json"

    with open(fn, "w") as outfile:
        json.dump(adict, outfile,indent=4)
    return json_object

def main():
    df = read_metadata()
    df = fixup(df)
    nematode_dict = SortedDict()
    nematode_dict = get_image_file_name(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

