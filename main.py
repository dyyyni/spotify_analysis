from scripts import data_raw_to_interim
from scripts import data_interim_to_overview

def main():
    data_raw_to_interim.main()
    data_interim_to_overview.main()
