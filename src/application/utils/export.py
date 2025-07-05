def export(lst: list):
    def _export(func):
        lst.append(func)
        return func

    return _export
