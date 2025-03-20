def split_data(lines, interval, start_interval, time_sorted, data_sorted, mid_sorted_time, mid_sorted_data, orig_interval):
    while interval <= (lines[-1])[0]:
        for j in range(len(lines)):
            if (lines[j])[0] > start_interval and round((lines[j])[0]) <= interval:
                mid_sorted_time.append((lines[j])[0])
                mid_sorted_data.append((lines[j])[1])
        time_sorted.append(mid_sorted_time)
        data_sorted.append(mid_sorted_data)
        mid_sorted_time = []
        mid_sorted_data = []
        start_interval += orig_interval
        interval += orig_interval
    if (lines[-1])[0] > (time_sorted[-1])[-1]:
        last_int_t = []
        last_int_d = []
        last_t = (time_sorted[-1])[-1]
        last_d = (data_sorted[-1])[-1]
        index = lines.index([last_t, last_d]) + 1
        while index != (lines.index(lines[-1]) + 1):
            last_int_t.append((lines[index])[0])
            last_int_d.append((lines[index])[1])
            index += 1
        time_sorted.append(last_int_t)
        data_sorted.append(last_int_d)

