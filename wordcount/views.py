"""
views.py ini untuk menampilkan halaman/page
buatan kita sendri lewat function yang ada di file views.py ini

secara default views.py ini belum ada dan kita hrs menakmakan dg nama ttp 'views.py'


<!--


in Template file HTML, You can use

{% %} For sentences such as if and for or to call tags such as load, static, etc.

{{ }} To render variables in the template.
-->


"""

# import python dg return string menggunakan http response
# (krn kita menggunakan http bkn https)
from django.http import HttpResponse

# jika return-nya redirect ke folder dan file tertentu menggunakan shortcut render
from django.shortcuts import render

import operator


# request--> obeject bawaan Django koneksi request ke website kita
def home(request):
    # minimal ada 2 yg hrs di passing di sini: request dan nama file template
    # bisa passing dictionary yg nanti bisa dipanggil di 'home.html'
    return render(request, 'home.html', {'hithere':'this is me'})

# request--> obeject bawaan Django koneksi request ke website kita
def about(request):
    # minimal ada 2 yg hrs di passing di sini: request dan nama file template
    # bisa passing dictionary yg nanti bisa dipanggil di 'home.html'
    return render(request, 'about.html')

# request--> obeject bawaan Django koneksi request ke website kita
def count(request):
    #mengabil value dr link: http://localhost/count/?fulltext=
    # saat user klik tombol submit count di home page textarea
    fulltext = request.GET['fulltext']
    #print(fulltext)
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # increase
            worddictionary[word] += 1
        else:
            # add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})



def others(request):
    return HttpResponse('Hello, this is the "Others" page content...')
