# numpy_speed_test

import numpy as np
import CB_Decorators
import CB_Module as cb


# Create a 1D List
def py_list(x):
    # Create a 1D array
    lst = list(range(x))

    def __str__(lst):
        return "py_list: " + str(lst)
        # print("list: " + str(lst))

    return lst


# Create a 1D array
def np_array(x):
    arr = np.arange(x)
    # print("np_array: " + str(arr))
    return arr


# MAIN:
def main():
    # Create a 1D List
    x = 10000000
    lst = py_list(x)
    arr = np_array(x)

    # Test: Binary Search
    import time

    # Test List
    # ------------------------------
    # start_time = time.perf_counter()    # 1 Start the timer

    # ### Execute the binary search
    # list_index_of_target_value = cb.binary_search(lst, 4)
    # end_time = time.perf_counter()      # 2 Stop the timer

    # run_time = end_time - start_time    # 3 Calculate the runtime
    # print(f"List Finished in {run_time:.4f} secs")

    # print("Index: " + str(list_index_of_target_value))

    # Test Numpy Array
    # ------------------------------
    def timer(func):
        import time

        def wrapper(*args, **kwargs):

            start_time = time.time_ns()  # 1 Start the timer
            # print("start_time: " + str(start_time) + " ns")
            result = func(*args, **kwargs)  # 2 Execute the function
            end_time = time.time_ns()  # 3 Stop the timer
            # print("end_time: " + str(end_time) + " ns")
            run_time = end_time - start_time  # 4 Calculate the runtime
            print(f"Finished in {run_time:.4f} ms")
            return result  # Return the result of the function

        return wrapper

    @timer
    def binary_search(arr, n, start=0, end=None):
        array_index_of_target_value = cb.binary_search(arr, n)
        print("Index: " + str(array_index_of_target_value))
        return array_index_of_target_value

    result = binary_search(lst, 4333)
    result = binary_search(arr, 4333)
    # print("arr: " + str(arr))
    # print("Index: " + str(result))

    # import time

    # lst_start_time = time.time_ns()
    # print("lst_start_time: " + str(lst_start_time) + " ns")

    # ### Execute the binary search
    # list_index_of_target_value = cb.binary_search(lst, 4)

    # lst_end_time = time.time_ns()
    # print("lst_end_time: " + str(lst_end_time) + " ns")

    # lst_run_time = lst_end_time - lst_start_time    # 3 Calculate the runtime
    # print("lst_run_time: " + str(lst_run_time) + " ms")

    # #print(f"listArray Finished in {lst_run_time:.4f} ms")
    # print("lst_Index: " + str(list_index_of_target_value))
    # #print("Index: " + str(array_index_of_target_value))

    # start_time = time.time_ns()
    # print("start_time: " + str(start_time) + " ns")
    # ### Execute the binary search
    # array_index_of_target_value = cb.binary_search(arr, 4)
    # end_time = time.time_ns()
    # print("end_time: " + str(end_time) + " ns")
    # run_time = end_time - start_time    # 3 Calculate the runtime
    # #run_time = run_time/1000
    # print("run_time: " + str(run_time) + " ms")
    # #print(f"npyArray Finished in {run_time:.4f} ms")
    # print("Index: " + str(array_index_of_target_value))

    # Test: Decorators
    # @timer
    # def binary_search(lst, n, start=0, end=None):
    # 	list_index_of_target_value = cb.binary_search(lst, n)
    # 	return list_index_of_target_value


if __name__ == "__main__":
    main()
