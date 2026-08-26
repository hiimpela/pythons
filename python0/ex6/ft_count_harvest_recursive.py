def count_up(day, max_day):
    if day <= max_day:
        print("Day", day)
        count_up(day + 1, max_day)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_up(1, days)
    print("Harvest time!")
