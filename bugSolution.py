def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return b / a
        else:
            return a / b
    except ZeroDivisionError:
        return float('inf')  # Handle the error gracefully and return infinity or another appropriate value
    except Exception as e:
      return f"An unexpected error occurred:{e}"