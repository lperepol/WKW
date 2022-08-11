import pandas as pd
#import xlrd
import openpyxl
import json
from sortedcontainers import SortedList, SortedSet, SortedDict
import mysql.connector as msql
from mysql.connector import Error

def read_metadata():
    fn = "../Metadata/ManualEdits/KeepMetadata_002_MySql_Import.csv"
    df = pd.read_csv(fn)
    return df

def push_table_data_to_mysql(df):
    try:
        conn = msql.connect(host='localhost', user='lperepol',
                            password='law715ren*117', database='nematodes')#give ur username, password
        cursor = conn.cursor()
        for i, row in df.iterrows():
            ImageName = row['ImageName']
            print (ImageName)
            #here %S means string values          # 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17
            sql = "INSERT INTO nematodes.unl_metadata VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()



    except Error as e:
        print("Error while connecting to MySQL", e)

def main():
    df = read_metadata()
    push_table_data_to_mysql(df)



if __name__ == '__main__':
    print("Begin")
    main()
    print("End")

