from main import main
from link_gsid_name import link
from save_company_data import save
from find_gsid import find_gsid


'''

This file takes the data from the Dataset using the API key and compiles
all the data into a seperate .csv file for each company.

'''
find_gsid()
link()
save()
