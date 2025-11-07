from datetime import datetime, timedelta


def is_working_day():
    return current_date.weekday() < 5


if __name__ == '__main__':

    print("Simple program to calculate the week days of a given month in a given year")

    date_input = input("What's date that you want to work on (YYYY-MM)? ")
    base_date = datetime.strptime(date_input, "%Y-%m")

    current_date = base_date
    while current_date.month == base_date.month:
        if is_working_day():
            print(current_date.date())
        current_date += timedelta(days=1)

    print("\n\tGet to work!")
