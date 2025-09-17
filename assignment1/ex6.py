def add_list_items(_list):
    try:
        total = _list[0]
        for item in _list[1:]:
            total += item
        return total
    except Exception:
        raise Exception("Incompatible data types")

print(add_list_items([1, 2, 3, 4]))
print(add_list_items(["a", "b", "c"]))
print(add_list_items([2, "x", 3]))
