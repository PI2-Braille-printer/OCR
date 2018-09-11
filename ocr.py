from PIL import Image, ImageEnhance
import pytesseract
import os

#image = Image.open('f_test.jpg')
#enhance = ImageEnhance.Contrast(image)
#new_image = enhance.enhance(1.5)
#new_image.save('f_test__c_2.jpg')

for x in range(0,3):
	os.system('./textcleaner -g -s 2 -a 1 ./Images/test_crop_'+str(x)+'.jpg ./Images/test_crop_'+str(x)+'_r.jpg')

	result_string = pytesseract.image_to_string(Image.open('./Images/test_crop_'+str(x)+'_r.jpg'),lang='por')
	print(result_string)
#result_string = result_string.split()
#print(result_string)
