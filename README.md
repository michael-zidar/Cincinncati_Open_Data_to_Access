# Cincinncati_Open_Data_to_Access
Import Cincinnati open police data into Microsoft Access

Created by Michael Zidar - mikezidar@gmail.com
Created: 12/12/2021
License: MIT

## Set Up

You will need to acquire an API key from the Cincinnati Open Data Portal 

You can view all datasets and acquire an API key from https://data.cincinnati-oh.gov/

Steps to acquire an API Key

- [ ] Sign up for a developer account https://data.cincinnati-oh.gov/signup
- [ ] Once logged in, select the "Edit Profile" button or navigate this URL https://data.cincinnati-oh.gov/profile/edit/developer_settings
- [ ] Select the "Create new API Key" button 
- [ ] Copy your new API key and secret key (Store in a safe place)
- [ ] Select "Create New App Token", fill out the required information, and copy your app token to a safe place

### Useful Links
Police Open Data API Reference - https://dev.socrata.com/foundry/data.cincinnati-oh.gov/k59e-2pvf
Police Shooting Data API Reference - https://dev.socrata.com/foundry/data.cincinnati-oh.gov/7a3r-kxji


## Python Environment
Make sure that you understand with python environment you are using to access the API. You will get error messages if the environment you are using does not contain the proper libraries.

### Required Packages
You will need to make sure the following packages are installed in your working python environment. 

pip install pandas
pip install sodapy

## Access Database
In the "data/" directory you will find a Microsoft Access Database with a table labeled CPD_Shootings. This contains shooting data at the time of the initial commit, and is the data source that the script will access and update.

## Requirements
- Must have MS Office 64bit installed 
- Must have MS Access installed
