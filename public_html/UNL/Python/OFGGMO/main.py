import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict
import mysql.connector


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
    orderSet = set()
    FamilySet = set()
    GenusSet = set()
    ImageSet = set()
    for index, row in df.iterrows():
        Order = str(row['Order']).strip()
        Family = str(row['Family']).strip()
        Genus = str(row['Genus']).strip()
        Gender = str(row['Gender']).strip()
        Magnification = str(row['Magnification']).strip()
        View = str(row['Detail']).strip()
        orderSet.add(Order)
        FamilySet.add(Family)
        GenusSet.add(Genus)

        if View == '0':
            continue

        ImageName = str(row['ImageName']).strip()
        ImageSet.add(ImageName)

        if ImageName not in adic[Order][Family][Genus][Gender][Magnification][View]:
            adic[Order][Family][Genus][Gender][Magnification][View].append(ImageName)

    print ("Order:" + str(len(orderSet)) + ", Family:" + str(len(FamilySet)) + ", Genus:" + str(len(GenusSet)) + ", Completed:" + str(len(ImageSet)) )
    # Order:12, Family:67, Genus:248
    return adic

def connetct_to_database():
    cnx = mysql.connector.connect(host="localhost", user="lperepol",
                        passwd="law715ren*117", db="nematodes")

def main():
    connetct_to_database()
    return
    df = read_metadata()
    df = fixup(df)
    nematode_dict = SortedDict()
    nematode_dict = get_image_file_name(nematode_dict, df)
    jo = writeDict2Json(nematode_dict)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

