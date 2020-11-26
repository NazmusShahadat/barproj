from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import *
from django.views.decorators.csrf import csrf_exempt
import barcode
from barcode.writer import ImageWriter
from barcode import Code128
from pyzbar.pyzbar import decode
import PIL
from PIL import Image
from pdf417 import encode, render_image, render_svg
import sys
import math
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def showlist(request):
    if request.method == "POST":
        try:
            brand = request.POST['brand']
            category = request.POST['category']
            model = request.POST['model']
            type = request.POST['type']
            size = request.POST['size']      
            b_id = '00' + brand
            b = (b_id[-2:])
            print(b)
            c_id = '000' + category
            c = (c_id[-3:])
            print(c)
            m_id = '00' + model
            m = (m_id[-2:])
            print(m)
            t_id = '000' + type
            t = (t_id[-3:])
            print(t)
            s_id = '000' + size
            s = (s_id[-2:])
            print(s)
            out = b + c + m + t + s 
            """ print(out) """
            """ a = barcode.get_barcode_class('code128')
            b = a(out, writer=ImageWriter())
            c = b.save('filename') """
            EAN = barcode.get_barcode_class('ean13')
            ean = EAN(f'{b}{c}{m}{t}{s}', writer=ImageWriter())
            d = ean.save('bar')
        except ObjectDoesNotExist:
            print('Field cannot be blank')

        """ newSize = (300, 200) # new size will be 500 by 300 pixels, for example
        resized = to_be_resized.resize(newSize, resample=PIL.Image.NEAREST)
        resized.save('bar_resized.png') """
        """ to_be_resized = Image.open('bar.png')
        images = [Image.open(x) for x in ['bar1.png', 'bar2.png', 'bar3.png']]
        widths, heights = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(heights) 
        new_im = Image.new('RGB', (total_width, max_height))
        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset, 0))
            x_offset += im.size[0]
        new_im.save('test.png') """

        """ img = Image.open('bar.png')
        result = decode(img)
        for i in result:
            num = []
            print(i.data.decode("utf-8"))
            num.append(i.data.decode("utf-8"))

        string = (num[0])
        print(string)
        brand_match = int(string[0:2])
        category_match = int(string[2:5])
        model_match = int(string[5:7])
        type_match = int(string[7:10])
        size_match = int(string[10:12])
        print(brand_match)
        print(category_match)
        print(model_match)
        print(type_match)
        print(size_match) 
        br = Brand.objects.get(pk=brand_match)
        print(br.brand)
        ca = Category.objects.get(pk=category_match)
        print(ca.category)
        mo = Model.objects.get(pk=model_match)
        print(mo.model)
        ty = Type.objects.get(pk=type_match)
        print(ty.type)
        si = Size.objects.get(pk=size_match)
        print(si.size) """

        
        """ buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('bar.png', File(buffer), save=False) """
        return redirect('showlist')
        return render(request, 'templates/home.html')
        return brand, category, model, type, size
 
    results = Brand.objects.all()
    category = Category.objects.all()
    model = Model.objects.all()
    type = Type.objects.all()
    size = Size.objects.all()
    context = {'results':results, 'category':category, 'model':model, 'type':type, 'size':size}
    return render(request, 'templates/home.html', context)

    """ def readlist(request):
        img = Image.open('barcode.png'
        result = decode(img)
        print(result)
        for i in result:
            print(i.data.decode("utf-8")) """


def multiple(request):
    global y
    global inp 
    global imglist
    y = 1
    imglist = []
    y = int(y)
    inp = request.POST.get('input')
    print(inp)
    print(y)
    inp = int(inp or 0)   
    context = {'y':y, 'inp':inp}
    return render(request, 'templates/multiple.html', context) 
    return y, inp, imglist 


def mult(request):
    print(inp)
    global y
    k = 0
    if (y<=inp):
        if request.method == "POST":
            brand = request.POST['brand']
            category = request.POST['category']
            model = request.POST['model']
            type = request.POST['type']
            size = request.POST['size']
            print(brand)
            print(category)
            print(model)
            print(type)
            print(size)
            print(y)
            b_id = '00' + brand
            b = (b_id[-2:])
            print(b)
            c_id = '000' + category
            c = (c_id[-3:])
            print(c)
            m_id = '00' + model
            m = (m_id[-2:])
            print(m)
            t_id = '000' + type
            t = (t_id[-3:])
            print(t)
            s_id = '000' + size
            s = (s_id[-2:])
            print(s)
            out = b + c + m + t + s
            print(out)
            EAN = barcode.get_barcode_class('ean13')
            ean = EAN(f'{b}{c}{m}{t}{s}', writer=ImageWriter())
            d = ean.save(f'bar{y}')
            to_be_resized = Image.open(f'bar{y}.png')
            newSize = (250, 150)
            resized = to_be_resized.resize(newSize, resample=PIL.Image.NEAREST)
            resized.save(f'bar{y}_resized.png')
            fit_img = Image.open(f'bar{y}.png')
            imglist.append(fit_img)
            y += 1 
            k += 1      
        else: 
            print('loop ended')
    else:
        print(imglist)
        z = len(imglist)
        if z%10 == 0:
            d = int(z/10)
            for x in range(d):
                f= open(f"test{x}.png","w+")
                x = x + 1
            i = 0
            for x in range(d):
                images = [Image.open(x) for x in [f'bar{i+1}.png', f'bar{i+2}.png', f'bar{i+3}.png',f'bar{i+4}.png', f'bar{i+5}.png', f'bar{i+6}.png',f'bar{i+7}.png',f'bar{i+8}.png',f'bar{i+9}.png',f'bar{i+10}.png']]
                widths, heights = zip(*(i.size for i in images))
                total_width = sum(widths)
                max_height = max(heights)
                new_im = Image.new('RGB', (total_width, max_height))
                x_offset = 0
                for im in images:
                    new_im.paste(im, (x_offset,0))
                    x_offset += im.size[0]
                new_im.save(f'test{x+1}.png') 
                i = i + 10
        else:
            c = z/10
            d = math.ceil(c)
            m = z%10
            i = 0
            for x in range(d):
                f= open(f"test{x}.png","w+")
                x = x + 1
            for y in range(d-1):
                images = [Image.open(x) for x in [f'bar{i+1}.png', f'bar{i+2}.png', f'bar{i+3}.png',f'bar{i+4}.png', f'bar{i+5}.png', f'bar{i+6}.png',f'bar{i+7}.png',f'bar{i+8}.png',f'bar{i+9}.png',f'bar{i+10}.png']]
                widths, heights = zip(*(i.size for i in images))
                total_width = sum(widths)
                max_height = max(heights)
                new_im = Image.new('RGB', (total_width, max_height))
                x_offset = 0
                for im in images:
                    new_im.paste(im, (x_offset,0))
                    x_offset += im.size[0]
                new_im.save(f'test{y+1}.png') 
                i = i + 10
            if (x==d):
                if(m == 1):
                    images = [Image.open(x) for x in [f'bar{i+1}.png']]
                    widths, heights = zip(*(i.size for i in images))
                    total_width = sum(widths)
                    max_height = max(heights)
                    new_im = Image.new('RGB', (total_width, max_height))
                    x_offset = 0
                    for im in images:
                        new_im.paste(im, (x_offset,0))
                        x_offset += im.size[0]
                    new_im.save(f'test{x}.png') 
                elif(m==2):
                    images = [Image.open(x) for x in [f'bar{i+1}.png', f'bar{i+2}.png']]
                    widths, heights = zip(*(i.size for i in images))
                    total_width = sum(widths)
                    max_height = max(heights)
                    new_im = Image.new('RGB', (total_width, max_height))
                    x_offset = 0
                    for im in images:
                        new_im.paste(im, (x_offset,0))
                        x_offset += im.size[0]
                    new_im.save(f'test{x}.png')
                elif(m==3):
                    images = [Image.open(x) for x in [f'bar{i+1}.png', f'bar{i+2}.png', f'bar{i+3}.png']]
                    widths, heights = zip(*(i.size for i in images))
                    total_width = sum(widths)
                    max_height = max(heights)
                    new_im = Image.new('RGB', (total_width, max_height))
                    x_offset = 0
                    for im in images:
                        new_im.paste(im, (x_offset,0))
                        x_offset += im.size[0]
                    new_im.save(f'test{x}.png')
                elif(m==4):
                    images = [Image.open(x) for x in [f'bar{i+1}.png', f'bar{i+2}.png', f'bar{i+3}.png',f'bar{i+4}.png']]
                    widths, heights = zip(*(i.size for i in images))
                    total_width = sum(widths)
                    max_height = max(heights)
                    new_im = Image.new('RGB', (total_width, max_height))
                    x_offset = 0
                    for im in images:
                        new_im.paste(im, (x_offset,0))
                        x_offset += im.size[0]
                    new_im.save(f'test{x}.png')
                elif(m==5):
                    images = [Image.open(x) for x in [f'bar{i+1}.png', f'bar{i+2}.png', f'bar{i+3}.png',f'bar{i+4}.png', f'bar{i+5}.png']]
                    widths, heights = zip(*(i.size for i in images))
                    total_width = sum(widths)
                    max_height = max(heights)
                    new_im = Image.new('RGB', (total_width, max_height))
                    x_offset = 0
                    for im in images:
                        new_im.paste(im, (x_offset,0))
                        x_offset += im.size[0]
                    new_im.save(f'test{x}.png')
                elif(m==6):
                    images = [Image.open(x) for x in [f'bar{i+1}.png', f'bar{i+2}.png', f'bar{i+3}.png',f'bar{i+4}.png', f'bar{i+5}.png', f'bar{i+6}.png']]
                    widths, heights = zip(*(i.size for i in images))
                    total_width = sum(widths)
                    max_height = max(heights)
                    new_im = Image.new('RGB', (total_width, max_height))
                    x_offset = 0
                    for im in images:
                        new_im.paste(im, (x_offset,0))
                        x_offset += im.size[0]
                    new_im.save(f'test{x}.png')
                elif(m==7):
                    images = [Image.open(x) for x in [f'bar{i+1}.png', f'bar{i+2}.png', f'bar{i+3}.png',f'bar{i+4}.png', f'bar{i+5}.png', f'bar{i+6}.png',f'bar{i+7}.png']]
                    widths, heights = zip(*(i.size for i in images))
                    total_width = sum(widths)
                    max_height = max(heights)
                    new_im = Image.new('RGB', (total_width, max_height))
                    x_offset = 0
                    for im in images:
                        new_im.paste(im, (x_offset,0))
                        x_offset += im.size[0]
                    new_im.save(f'test{x}.png')
                elif(m==8):
                    images = [Image.open(x) for x in [f'bar{i+1}.png', f'bar{i+2}.png', f'bar{i+3}.png',f'bar{i+4}.png', f'bar{i+5}.png', f'bar{i+6}.png',f'bar{i+7}.png',f'bar{i+8}.png']]
                    widths, heights = zip(*(i.size for i in images))
                    total_width = sum(widths)
                    max_height = max(heights)
                    new_im = Image.new('RGB', (total_width, max_height))
                    x_offset = 0
                    for im in images:
                        new_im.paste(im, (x_offset,0))
                        x_offset += im.size[0]
                    new_im.save(f'test{x}.png')
                else:
                    images = [Image.open(x) for x in [f'bar{i+1}.png', f'bar{i+2}.png', f'bar{i+3}.png',f'bar{i+4}.png', f'bar{i+5}.png', f'bar{i+6}.png',f'bar{i+7}.png',f'bar{i+8}.png',f'bar{i+9}.png']]
                    widths, heights = zip(*(i.size for i in images))
                    total_width = sum(widths)
                    max_height = max(heights)
                    new_im = Image.new('RGB', (total_width, max_height))
                    x_offset = 0
                    for im in images:
                        new_im.paste(im, (x_offset,0))
                        x_offset += im.size[0]
                    new_im.save(f'test{x}.png')                
            else:
                print(d)


         
        """ for x in range(d):
            f= open(f"test{x}.png","w+")
            x = x + 1
        i = 0
        for x in range(d):
            images = [Image.open(x) for x in [f'bar{i+1}_resized.png', f'bar{i+2}_resized.png', f'bar{i+3}_resized.png',f'bar{i+4}_resized.png', f'bar{i+5}_resized.png', f'bar{i+6}_resized.png',f'bar{i+7}_resized.png',f'bar{i+8}_resized.png',f'bar{i+9}_resized.png',f'bar{i+10}_resized.png']]
            widths, heights = zip(*(i.size for i in images))
            total_width = sum(widths)
            max_height = max(heights)
            new_im = Image.new('RGB', (total_width, max_height))
            x_offset = 0
            for im in images:
                new_im.paste(im, (x_offset,0))
                x_offset += im.size[0]
            new_im.save(f'test{x}.png') 
            i = i + 10 """


        """ i = 0
        images = [Image.open(x) for x in [f'bar{i+1}_resized.png', f'bar{i+2}_resized.png', f'bar{i+3}_resized.png',f'bar{i+4}_resized.png', f'bar{i+5}_resized.png', f'bar{i+6}_resized.png',f'bar{i+7}_resized.png',f'bar{i+8}_resized.png',f'bar{i+9}_resized.png',f'bar{i+10}_resized.png']]
        widths, heights = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(heights)
        new_im = Image.new('RGB', (total_width, max_height)) 

        x_offset = 0
        for im in images:
            new_im.paste(im, (x_offset,0))
            x_offset += im.size[0]

        new_im.save('test.jpg') """
        return redirect('multiple')
 

    results = Brand.objects.all()
    category = Category.objects.all()
    model = Model.objects.all()
    type = Type.objects.all()
    size = Size.objects.all()
    context = {'results':results, 'category':category, 'model':model, 'type':type, 'size':size}
    return render(request, 'templates/mult_sub.html', context)