import sys
import csv
from split import split_data
import statistics

def read_data_from_file(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            lines = []
            raw_data = csv.reader(csvfile, delimiter= ',', quotechar=' ')
            next(raw_data)
            for i in raw_data:
                i[0] = float(i[0])
                i[1] = int(i[1])
                lines.append(i)
            return lines
    except FileNotFoundError:
        print("Файл не найден")
        return []

def calculate_statistic(data_sorted, final_stat):
    stats = []
    for s in range(len(data_sorted)):
        lenght = len(data_sorted[s])
        stats.append(lenght)
        mean = statistics.mean(data_sorted[s])
        stats.append(mean)
        mode = statistics.mode(data_sorted[s])
        stats.append(mode)
        median = statistics.median(data_sorted[s])
        stats.append(median)
        final_stat.append(stats)
        stats = []
    return final_stat


def main():
    time_sorted = []
    data_sorted = []
    mid_sorted_time = []
    mid_sorted_data = []
    final_stat = []
    start_interval = 0
    if len(sys.argv) > 2:
        file_path = sys.argv[1]
        try:
            interval = int(sys.argv[2])
            if interval <= 0:
                print("Недопустимый интервал")
                exit()
        except ValueError:
            print("Неверный формат интервала")
            exit()
    else:
        file_path = input("Введите имя файла: ")
        try:
            interval = int(input("Введите интервал: "))
            if interval <= 0:
                print("Недопустимый интервал")
                exit()
        except ValueError:
            print("Неверный формат интервала")
            exit()
        
    lines = read_data_from_file(file_path)
    if interval > (lines[-1])[0]:
        interval = (lines[-1])[0]
    orig_interval = interval - start_interval
    split_data(lines, interval, start_interval, time_sorted, data_sorted, mid_sorted_time, mid_sorted_data, orig_interval)
    final_stat = calculate_statistic(data_sorted, final_stat)
    for p in range(len(final_stat)):
        print(
            "Вот что получилось:\n"
            f"Для отрезка от {(time_sorted[p])[0]} до {(time_sorted[p])[-1]}:\n"
            f"Кол-во значений: {(final_stat[p])[0]}\n"
            f"Среднее значение: {(final_stat[p])[1]}\n"
            f"Мода: {(final_stat[p])[2]}\n"
            f"Медиана {(final_stat[p])[3]}\n"
        )
if __name__ == "__main__":
    main()