def init():
    import importlib.util
    spec = importlib.util.spec_from_file_location("module.name", "test_case.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    print(foo.get_pic())


if __name__ == '__main__':
    init()
