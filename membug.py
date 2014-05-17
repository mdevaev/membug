import sys
import gc


# ===== Hacks =====
if not hasattr(sys, "getrefcount"): # For PyPy3
    sys.getrefcount = ( lambda obj: len(gc.get_referents(obj)) )


# ===== Public methods =====
def get_objects_by_type():
    by_type = {}
    for obj in gc.get_objects():
        by_type.setdefault(type(obj), [])
        by_type[type(obj)].append(obj)
    return by_type

def print_types_top(last_by_name=None):
    by_type = get_objects_by_type()
    obj = None
    for (obj_type, objects) in sorted(by_type.items(), key=( lambda arg: len(arg[1]) )):
        print("{} ({}) -- {}".format(obj_type, obj_type.__name__, len(objects)))
        if last_by_name is not None and obj_type.__module__ + "." + obj_type.__name__ == last_by_name:
            obj = objects[-1]
    return obj
