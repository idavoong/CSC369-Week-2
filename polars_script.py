import polars as pl
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

    color = (
        pl.scan_csv("2022_place_canvas_history.csv")
        .filter((pl.col("timestamp") >= start) & (pl.col("timestamp") <= end))
        .group_by("pixel_color")
        .len()
        .max()
    )

    coord = (
        pl.scan_csv("2022_place_canvas_history.csv")
        .filter((pl.col("timestamp") >= start) & (pl.col("timestamp") <= end))
        .group_by("coordinate")
        .len()
        .max()
    )

    greatest_color = color.collect().row(0)[0]
    greatest_coord = coord.collect().row(0)[0]

    end_time = time.perf_counter_ns()

    elapsed_time_ms = (end_time - start_time) / 1000000

    print("Most placed color: \n", greatest_color)
    print("Most placed pixel location: \n", greatest_coord)
    print("Time taken: ", elapsed_time_ms, "ms")
