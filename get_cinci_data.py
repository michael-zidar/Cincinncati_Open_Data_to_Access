# Import your libraries
import pandas as pd
from sodapy import Socrata
import os
import pyodbc

# Paste your app token here
AppToken = 'My App Token'

# Path to the MS Access data file 
AccessFile = os.getcwd()+"\\data\\data.accdb;"

# Set up the connection to the Access database
print("Connecting to the database...")
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ='+AccessFile)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

print("Fetching the last inserted Shooting rocord...")
last_inserted = cursor.execute("SELECT Max(CPD_Shootings.OID) FROM CPD_Shootings;").fetchone()[0]
print("The last record inserted into the shootings table has an id of " + str(last_inserted)+"...")

# Sending requests with your app token will allow us pull more data than if we sent it annomously
print("Connecting to the data source...")
client = Socrata('data.cincinnati-oh.gov',
                 AppToken)

results = client.get("7a3r-kxji", where="oid>"+str(last_inserted))

# Convert to pandas DataFrame
print("Converting JSON to dataframe...")
results_df = pd.DataFrame.from_records(results)

print("Inserting each row of the dataframe to the access database...")
for index, row in results_df.iterrows():
    insert_statement = "INSERT INTO CPD_Shootings ( DISTRICT, INCLOCATION_X, LONGITUDE_X, CPD_NEIGHBORHOOD, OID, RMS_NO, VICCOUNT, RACE, SEX, AGE, TYPE, DATEOCCURRED, MONTHOCCURED, TIMEOCCURED, HROCCURED, DAYOCCURRED, RMSDUP, [DATETIME], DSTFULL, COMMUNITY_COUNCIL_NEIGHBORHOOD) VALUES ("+"'"+str(row['district']) +"','"+str(row['inclocation_x']) +"','"+str(row['longitude_x']) +"','"+str(row['cpd_neighborhood']) +"','"+str(row['oid']) +"','"+str(row['rms_no']) +"','"+str(row['viccount']) +"','"+str(row['race']) +"','"+str(row['sex']) +"','"+str(row['age']) +"','"+str(row['type']) +"','"+str(row['dateoccurred']) +"','"+str(row['monthoccured']) +"','"+str(row['timeoccured']) +"','"+str(row['hroccured']) +"','"+str(row['dayoccurred']) +"','"+str(row['rmsdup']) +"','"+str(row['datetime']) +"','"+str(row['dstfull']) +"','"+str(row['community_council_neighborhood'])+"');"
    cursor.execute(insert_statement)
    cursor.commit()

print("Closing Database connection...")
conn.close()
