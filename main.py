from time import time_ns

from solutions import days

if __name__ == "__main__":
    for day in range(1,26):
        if day in days:
            parsed_input = days[day]['input'](f'inputs/{day:02d}/real.txt')

            start_time = time_ns()
            result_a = days[day]['A'](parsed_input)
            end_time = time_ns()
            print(f"Day {day:02d} - A - {(end_time - start_time)/1000000:.4f}ms - {result_a}")
            
            start_time = time_ns()
            result_b = days[day]['B'](parsed_input)
            end_time = time_ns()
            print(f"Day {day:02d} - B - {(end_time - start_time)/1000000:.4f}ms - {result_b}")
