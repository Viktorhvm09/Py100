# TODO Найдите количество книг, которое можно разместить на дискете
size_diskette_Mb = 1.44
byte_on_diskette = 1.44 * 1024 ** 2
page_to_book = 100
line_to_page = 50
symbol_to_line = 25
size_symbol_byte = 4
size_symbol_to_one_book = size_symbol_byte * symbol_to_line * line_to_page * page_to_book
number_book = int(byte_on_diskette / size_symbol_to_one_book)
print("Количество книг, помещающихся на дискету:", number_book)
