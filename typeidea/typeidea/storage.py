from io import BytesIO

from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadeFile

from PIL import Image, ImageDraw, ImageFont


class WatermarkStorage(FileSystemStorage):
    def save(self, name, content, max_length=None):
        #处理逻辑
        if 'image' in content.content_type:
            image = self.Watermark_with_text(content, 'zpz.com', 'red')
            content = self.convert_image_to_file(image, name)
        
        return super().save(name, content, max_length=max_length)
    
    def convert_image_to_file(self, image, name):
         temp = BytesIO()
         image.save(temp, format='PNG')
         files_size = temp.tell()
         return InMemoryUploadeFile(temp, None, 'image/png', files_size, None)
     
    def Watermark_with_text(self, file_obj, text, color, fontfamily=None):
        image = Image.open(file_obj).convert('RGBA')
        draw = ImageDraw.Draw(image)
        margin = 10
        if fontfamily:
            font = ImageFont.truetype(fontfamily, int(height / 20))
        else:
            font = None
        textWidth, textHight = draw.textsize(text, font)
        x = (width - textWidth - margin) / 2    #计算横轴位置
        y = height - textHight - margin    #计算纵轴位置
        draw.text((x,y), text, color, font)
        return image