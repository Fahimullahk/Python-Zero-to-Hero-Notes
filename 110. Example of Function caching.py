from functools import lru_cache
import time

@lru_cache(maxsize=None)
def ln(f):
    time.sleep(5)
    return f * 2

a = ln(10)
print(f"Done for 10 which is equal to {a}")
b = ln(20)
print(f"Done for 20 which is equal to {b}")
c = ln(30)
print(f"Done for 30 which is equal to {c}")
print ("---------------------------------------")
d = ln(10)
print(f"Done for 10 which is equal to {d}")
e = ln(20)
print(f"Done for 20 which is equal to {e}")
f = ln(30)
print(f"Done for 30 which is equal to {f}")
g = ln(40)
print(f"Done for 40 which is equal to {g}")

"""As in the above example we used the Function caching module in 
which the caching stores in our memory and the repeated objects executes 
without delaying 5 sec, however on reaching to the new object it again 
starts waiting for 5 sec."""