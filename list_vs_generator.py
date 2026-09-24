import time
import tracemalloc


N = 1_000_000


def list_processing():
    start = time.perf_counter()
    tracemalloc.start()

    result = [x * x for x in range(N)]
    total = sum(result)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time = time.perf_counter() - start

    return total, execution_time, peak / (1024 * 1024)


def generator_processing():
    start = time.perf_counter()
    tracemalloc.start()

    result = (x * x for x in range(N))
    total = sum(result)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time = time.perf_counter() - start

    return total, execution_time, peak / (1024 * 1024)


list_total, list_time, list_memory = list_processing()
generator_total, generator_time, generator_memory = generator_processing()

print("LIST-BASED PROCESSING")
print("Result:", list_total)
print("Execution Time:", list_time, "seconds")
print("Peak Memory:", list_memory, "MB")

print("\nGENERATOR-BASED PROCESSING")
print("Result:", generator_total)
print("Execution Time:", generator_time, "seconds")
print("Peak Memory:", generator_memory, "MB")

print("\nCOMPARISON")

if list_time < generator_time:
    print("List processing is faster.")
else:
    print("Generator processing is faster.")

if list_memory < generator_memory:
    print("List processing uses less memory.")
else:
    print("Generator processing uses less memory.")