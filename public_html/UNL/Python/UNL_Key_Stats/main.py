import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict



def read_metadata_xlsx_Location():
    fn = "../Metadata/ManualEdits/KeepMetadata_002_keys_update.xlsx"
    df = pd.read_excel(fn, sheet_name='Keyed')
    df = df.fillna('')
    keyedSet = set()
    baseSet = set()
    for index, row in df.iterrows():
        Keyed = str(row['Genera Keyed']).strip()
        base = str(row['Genera on UNL']).strip()
        keyedSet.add(Keyed)
        baseSet.add(base)
    print("Keyed ==> " + str(len(keyedSet)))
    print("base ==> " + str(len(baseSet)))

    return




def main():
    locDict = read_metadata_xlsx_Location()

if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

