import os
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Spread sheet id to extract the values
SPREADSHEET_ID = '1pTqSaWbTGITZRd6hteS2DN-0I1VY2ZWf1UJdcHCXwHY'
# Credential path for the service account to get the access to the spreadsheet 
service_account_file = 'utils//credential.json'
# Scope of the spreadsheet
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Initialization of the credential using the service account creds 
credentials = Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
# Initialization of the service for the sheet api 
service = build('sheets', 'v4', credentials=credentials)


# Declaring the sheet variable for the extraction of the  to the spreadsheet  data 
sheet = service.spreadsheets()
# extracting the values withing the specified range in sheet 
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Sheet1!A2:B85').execute()
# Getting the values only from the sheet variable 
rows = result.get('values', [])


def sheet_to_dict():
    """ Saving the extracted data from google sheet to dictionary where title is stored as key and its related SEO_keyword as values """
    valid_key = None
    dict_sheet = {} #intialization of dictionary 

    for row in rows:
        if len(row) < 2: # checking if the first two columns exists or not in sheet 
            continue

        if row[0]:  # Checking if there is null values first columns 
            valid_key = row[0]  # if the first columns values is not null then set it as a valid key for dictonary
            dict_sheet[valid_key] = [row[1]] # assigning the values seo_keyword to the valid key of a dictonary

        else:  # if the first  columns values is null setting the value of its corressponding seo_keyword to previous valid key 
            if valid_key:
                dict_sheet[valid_key].append(row[1])

    return dict_sheet
dict = sheet_to_dict()
print(dict['Why a Strong Online Presence Is the Secret to Restaurant Success'])

