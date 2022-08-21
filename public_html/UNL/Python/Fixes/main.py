import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict

def read_metadata_csv():
    fn = "../Metadata/ManualEdits/KeepMetadata_002.csv"
    df = pd.read_csv(fn)
    df = df.fillna('')
    return df


def read_metadata_xlsx_Location():
    fn = "../Metadata/ManualEdits/KeepMetadata_002.xlsx"
    df = pd.read_excel(fn, sheet_name='Location')
    df = df.fillna('')
    locDict = dict()
    for index, row in df.iterrows():
        Location = str(row['Location']).strip()
        locationAr = Location.split(',')

        locDict[Location] = (New_Location, Host)
    return locDict

def read_metadata_xlsx_KeepMetadata_003_test():
    fn = "../Metadata/ManualEdits/KeepMetadata_002.xlsx"
    df = pd.read_excel(fn, sheet_name='KeepMetadata_003_test')
    df = df.fillna('')

    return df

def fixup(df, locDict):
    df = df.fillna('')
    for index, row in df.iterrows():
        Location = str(row['Location']).strip()
        if Location in locDict:
            (New_Location, Host) = locDict[Location]
            if len(New_Location) > 2:
                df.loc[index, 'Location'] = New_Location

    fn = "../Metadata/ManualEdits/KeepMetadata_002_new.csv"
    df.to_csv(fn,  index=False)
    return df




def main():
    locDict = read_metadata_xlsx_Location()
    df = read_metadata_xlsx_KeepMetadata_003_test()
    df = fixup(df,locDict)


if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

