from scripts import data_raw_to_interim
from scripts import data_interim_to_overview
from scripts import data_by_year_month

def main():
    data_raw_to_interim.main()
    data_interim_to_overview.main()
    data_by_year_month.main()
