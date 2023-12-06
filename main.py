from fastapi import FastAPI
import gspread
import numpy as np
import pandas as pd
from gspread_dataframe import set_with_dataframe
app = FastAPI()


def main():
    #print("Access Google Sheet via API...")
    # your code here
    sa = gspread.service_account()
    sh = sa.open("TRIAL_PROGRAM_KASIR")
    wks = sh.worksheet("KASIR")
    wks2 = sh.worksheet("DATABASE")
    #print("Upload to JIRA via API...")
    data_raw =  wks.get('D7:D10')
    data = (pd.DataFrame(data=data_raw)).transpose()
    data_values = data.values.tolist()
    sh.values_append('DATABASE',{'valueInputOption': 'RAW'},{'values': data_values})

@app.get("/")
def root():
    main()
    return {"message": "Done"}
