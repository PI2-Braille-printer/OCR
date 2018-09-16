from tesserocr import PyTessBaseAPI, RIL, iterate_level

with PyTessBaseAPI(lang='por') as api:
    api.SetImageFile(input())
    api.SetVariable("save_blob_choices", "T")
    api.Recognize()

    ri = api.GetIterator()
    level = RIL.SYMBOL
    for r in iterate_level(ri, level):
        symbol = r.GetUTF8Text(level)  # r == ri
        conf = r.Confidence(level)
        print(symbol, end='')
