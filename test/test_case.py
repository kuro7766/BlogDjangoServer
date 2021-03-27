from library import ml

a = [
    'http://img.netbian.com/file/20101206/0ab6bc5ad6c993f438712fd73b85cbc8.jpg',
    'http://img.netbian.com/file/20101208/a0419b480a10e45239e434157697dab4.jpg',
    'http://img.netbian.com/file/20101208/7f8110a822d1bc3890b6edbba103883e.jpg',
    'http://img.netbian.com/file/20101209/47fc33f195d1dff52b0a66a5e45b8d03.jpg',
    'http://img.netbian.com/file/20101214/4a0c1fa9f4235870233ce4722ae2cf8f.jpg',
    'http://img.netbian.com/file/20101214/3561f9d5fd20dd81531318f934c66881.jpg',
    'http://img.netbian.com/file/20101215/544cfde339de02d89b9b573f4aaa6600.jpg',
    'http://img.netbian.com/file/20101215/d7ef259da7ba6fdc89cba4ae76a93978.jpg',
    'http://img.netbian.com/file/20101218/d441b9aa5c953d219161ac41e07450a7.jpg',
    'http://img.netbian.com/file/20101218/46f6306f58488a5c27e498332384a69e.jpg',
    'http://img.netbian.com/file/20101218/3758f328fd63a5ea1b36e4b6b30ba1fd.jpg'
]


def get_pic():
    return ml.random_pick(a, 1)[0]
