from functools import wraps
import time

# --- Zaman ölçen dekoratör ---
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"[timer] {func._name_}: {elapsed:.4f}s")
        return result
    return wrapper

# --- Zorunlu kolon kontrolü ---
def required_columns(required: set[str]):
    def decorator(func):
        @wraps(func)
        def wrapper(rows, *args, **kwargs):
            if not rows:
                raise ValueError("Boş veri seti")
            keys = set(rows[0].keys())
            missing = required - keys
            if missing:
                raise ValueError(f"Eksik kolonlar: {missing}")
            return func(rows, *args, **kwargs)
        return wrapper
    return decorator