from datetime import date
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import TemplateDoesNotExist
from django.urls import reverse

data = {
        "programlama": "programlama kategorisi",
        "web": "web kategorisi",
        "mobil": "mobil kategorisi",
        "mobil2": "mobil kategorisi",
       }

db = { 
    "courses" : [
        {             
            "title": "javascript kursu", 
            "description": "javascript kurs açıklaması", 
            "iamgeUrl": "https://img-c.udemycdn.com/course/750x422/1662526_fc1c_3.jpg",
            "slug": "javascript-kursu",
            "date": date(2025, 10, 10),
            "isActive": True,
            "isUpdated": False
        },
        {             
            "title": "python kursu", 
            "description": "python kurs açıklaması", 
            "iamgeUrl": "https://img-c.udemycdn.com/course/750x422/2463492_8344_3.jpg",
            "slug": "python-kursu",
            "date": date(2025, 9, 10),
            "isActive": False,
            "isUpdated": False
        },
        {             
            "title": "web geliştirme kursu", 
            "description": "web geliştirme kurs açıklaması", 
            "iamgeUrl": "https://img-c.udemycdn.com/course/750x422/1258436_2dc3_4.jpg",
            "slug": "web-gelistirme-kursu",
            "date": date(2025, 8, 10),
            "isActive": True,
            "isUpdated": True
        }
    ],
    "categories": [
        {"id":1, "name":"programlama","slug":"programlama"},
        {"id":2, "name":"web programalama","slug":"web"},
        {"id":3, "name":"mobil uygulama","slug":"mobil"},        
    ]   
}

# def index(request):
#     try:
#         return render(request, 'courses/index.html')
#     except TemplateDoesNotExist:
#         return HttpResponse("Template not found")
    #return HttpResponse("index")
    
def index(request):
    # list_items = ""
    #category_list = list(data.keys())    
    
    #kurslar = db["courses"]
    #kurslar = []
    # list comprehension
    kurslar = [course for course in db["courses"] if course["isActive"]]
    kategoriler = db["categories"]

    # for kurs in db["courses"]:
    #     if kurs["isActive"]:
    #         kurslar.append(kurs)       
    
    return render(request, 'courses/index.html',{ 
        #'categories': category_list 
        'categories': kategoriler,
        'courses': kurslar,
        })

    # for category in category_list:
    #     redirect_url = reverse('courses_by_category', args=[category])
    #     list_items += f'<li><a href="{redirect_url}">{category}</a></li>'    
    
    # html = f"<h1>kurs listesi</h1><br><ul>{list_items}</ul>"

    # return HttpResponse(html)

def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getcoursesByCategory(request,category_name):
    try:
        category_text = data[category_name]
        #return HttpResponse(f"{category_text} Kurs listesi") 
        return render(request, 'courses/kurslar.html', {
            'category': category_name,
            'category_text': category_text
            })    
    except:
        return HttpResponseNotFound("yanlış Kategori Seçimi")

       
    # text=""
    # if category_name == "python":
    #     text="Python Programlama"
    # elif category_name == "java":
    #     text="Java Programlama"
    # else:
    #     text="Kategori Bulunamadı"
    # return HttpResponse(f'{text} Kurs listesi')

def getcoursesByCategoryId(request,category_id):
    #return HttpResponse(category_id)

    category_list = list(data.keys())

    if(category_id > len(category_list)):
        return HttpResponseNotFound("yanlış Kategori Seçimi")
    
    category_name = category_list[category_id-1]
    redirect_url = reverse('coursesByCategory', args=[category_name])

    #return redirect('/kurs/kategory/'+category_name)
    return redirect(redirect_url)
