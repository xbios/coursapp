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
            "category": "javascript kurs açıklaması", 
            "iamgeUrl": "javascript.jpg",
            "slug": "javascript-kursu",
            "date": date(2025, 10, 10)
        },
        {             
            "title": "python kursu", 
            "category": "python kurs açıklaması", 
            "iamgeUrl": "python.jpg",
            "slug": "python-kursu",
            "date": date(2025, 10, 10)
        },
        {             
            "title": "web geliştirme kursu", 
            "category": "web geliştirme kurs açıklaması", 
            "iamgeUrl": "web-geliştirme.jpg",
            "slug": "web-gelistirme-kursu",
            "date": date(2025, 10, 10)
        }
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
    category_list = list(data.keys())
    
    return render(request, 'courses/index.html',{ 
        'categories': category_list 
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
