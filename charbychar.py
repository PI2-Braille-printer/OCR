from tesserocr import PyTessBaseAPI, RIL, iterate_level
import sys

with PyTessBaseAPI(lang='por') as api:
    api.SetImageFile(sys.argv[1])
    api.SetVariable("save_blob_choices", "T")
    api.Recognize()
    
    print(' '.join(word for word in api.AllWords()))
    ri = api.GetIterator()
    level = RIL.SYMBOL
    for r in iterate_level(ri, level):
        symbol = r.GetUTF8Text(level)  # r == ri
        conf = r.Confidence(level)
    print(api.GetUTF8Text())
