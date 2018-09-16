from PIL import Image
Image.MAX_IMAGE_PIXELS=1000000000
from tesserocr import PyTessBaseAPI, RIL
import tesserocr
import sys

image = Image.open(sys.argv[1])
with PyTessBaseAPI(lang='por') as api:
    api.SetImage(image)
    boxes = api.GetComponentImages(RIL.TEXTLINE, True)
    print(len(boxes));
    for i, (im, box, _, _) in enumerate(boxes):
        api.SetRectangle(box['x'], box['y'], box['w'], box['h'])
        it = api.AnalyseLayout()
        ocr_res = api.GetUTF8Text()
        conf = api.MeanTextConf()
        print(ocr_res)
