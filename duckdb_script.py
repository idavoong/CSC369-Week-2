import duckdb
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

    color = duckdb.sql(f"""SELECT pixel_color, COUNT(*) AS count 
               FROM "2022_place_canvas_history.csv"
               WHERE timestamp BETWEEN '{start}' AND '{end}'
               GROUP BY pixel_color 
               ORDER BY count DESC
               LIMIT 1""")
    
    coord = duckdb.sql(f"""SELECT coordinate, COUNT(*) AS count 
               FROM "2022_place_canvas_history.csv"
               WHERE timestamp BETWEEN '{start}' AND '{end}'
               GROUP BY coordinate 
               ORDER BY count DESC
               LIMIT 1""")
    
    '''
    calculating time here gives 100ms, seems like query is only being called in print statement?
    '''

    print("Most placed color: \n", color)
    print("Most placed pixel location: \n", coord)

    end_time = time.perf_counter_ns()
    elapsed_time_ms = (end_time - start_time) / 1000000

    print("Time taken: ", elapsed_time_ms, "ms")
