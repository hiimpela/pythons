def count_down(day):
    if day != 0:
        count_down(day - 1)
        print("Day", day)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_down(days)
    print("Harvest time!")
