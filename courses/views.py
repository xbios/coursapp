from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

data = {
        "programlama": "programlama kategorisi",
        "web": "web kategorisi",
        "mobil": "mobil kategorisi",
       }


def kurslar(request):
    list_items = ""
    category_list = list(data.keys())
    
    for category in category_list:
        redirect_url = reverse('coursesByCategory', args=[category])
        list_items += f'<li><a href="{redirect_url}">{category}</a></li>'    
    
    html = f"<h1>kurs listesi</h1><br><ul>{list_items}</ul>"

    return HttpResponse(html)

def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getcoursesByCategory(request,category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(f"{category_text} Kurs listesi") 
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
