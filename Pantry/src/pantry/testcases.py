import APIReader

baking_soda = APIReader.APIReader("baking_soda")
canned_hash = APIReader.APIReader("hash")
canned_peas = APIReader.APIReader("peas")
coffee_container = APIReader.APIReader("coffee")
frosted_cereal = APIReader.APIReader("frosted_flakes")
heavy_cream = APIReader.APIReader("cream")
olive_oil = APIReader.APIReader("olive_oil")
sriracha = APIReader.APIReader("sriracha")
tomato_sauce = APIReader.APIReader("tomato_sauce")
whipped_cream = APIReader.APIReader("whipped")

# https://www.geeksforgeeks.org/viewing-all-defined-variables-in-python/
file_vars = dir()
for v in file_vars:
    if not v.startswith('__'):
        print(eval(v))

