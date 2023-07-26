from scripts import data_raw_to_interim
from scripts import data_interim_to_overview
from scripts import data_by_year_month
from scripts import data_by_weekday
from scripts import data_by_hour
from scripts import top_lists

def main():
    data_raw_to_interim.main()
    data_interim_to_overview.main()
    data_by_year_month.main()
    data_by_weekday.main()
    data_by_hour.main()
    top_lists.main()
