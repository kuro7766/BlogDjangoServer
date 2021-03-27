if __name__ == '__main__':
    from library import ml as ml

    f = [ml.path_to_filename(i) for i in ml.getAllFiles('s')]
    print(f)
