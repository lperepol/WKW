import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_metadata():
    fn = "../Metadata/ManualEdits/KeepMetadata_002.csv"
    df = pd.read_csv(fn )
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


def merge(df_keys,df_meta):
    df_keys['ImageDetail'] = ''
    df_keys['Genus'] = ''
    for index, row in df_keys.iterrows():
        Image = str(row['Image' ]).strip()
        for df_meta_index, df_meta_row in df_meta.iterrows():
            Image1 = str(df_meta_row['ImageName']).strip()
            Detail = str(df_meta_row['Detail']).strip()
            Genus = str(df_meta_row['Genus']).strip()
            if Image == Image1:
                df_keys.loc[index, 'ImageDetail'] = Detail
                df_keys.loc[index, 'Genus'] = Genus
                break

    fn = "../Metadata/ManualEdits/KeepMetadata_002_keys_update.csv"
    df_keys.to_csv(fn, sep=',', encoding='utf-8', index=False)
    return


def main():
    #df = fixup(df)
    df_meta = read_metadata()
    df_keys = read_keys()
    merge(df_keys,df_meta)

if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

