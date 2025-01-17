import pandas as pd
import sys
import time

if __name__ == "__main__":
    start = sys.argv[1] + " " + sys.argv[2]
    end = sys.argv[3] + " " + sys.argv[4]

    if start >= end:
        print("Start date must be before end date")
        exit()

    start = start + ":00:00"
    end = end + ":00:00"

    start_time = time.perf_counter_ns()

    data = pd.read_csv("2022_place_canvas_history.csv", usecols=["timestamp", "pixel_color", "coordinate"])
    filter = data[(data['timestamp'] > start) & (data['timestamp'] <= end)]
    color = filter['pixel_color'].value_counts().head(1)
    coord = filter['coordinate'].value_counts().head(1)

    end_time = time.perf_counter_ns()
    elapsed_time_ms = (end_time - start_time) / 1000000

    print("Most placed color: \n", color)
    print("Most placed pixel location: \n", coord)
    print("Time taken: ", elapsed_time_ms, "ms")
