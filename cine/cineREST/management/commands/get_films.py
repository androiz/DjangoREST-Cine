from django.core.management.base import BaseCommand, CommandError

from cineREST.models import Film
import cine.settings as settings

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import re
import json

class Command(BaseCommand):
    help = 'Get films from elpuntvalles.org'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        file = urllib2.urlopen(settings.EL_PUNT_VALLES+'index.php?lang=es')
        data = file.read()
        data.replace(" ", "")
        data.replace("\t", "")
        file.close()

        urls = self.get_urls_from_mainpage(data)
        res = self.get_data_from_urlfilm(urls)

        Film.objects.all().update(on_screen=False)

        for key in res:
            if not Film.objects.filter(url=key):
                f = Film(url=key, url_img=res[key]["url_img"], title=res[key]["title"], on_screen=True)
                f.save()
            else:
                f = Film.objects.get(url=key)
                f.on_screen = True
                f.save()


    def get_urls_from_mainpage(self, data):
        index_ref = [m.start() for m in re.finditer('mix 2', data)]

        res = list()

        for i in index_ref:
            str =  data[i:i+200]
            cad_i = "href="
            cad_j = "><img"
            i = str.index(cad_i)
            j = str.index(cad_j)
            res.append(str[i+len(cad_i)+1:j-1])

        return res

    def get_data_from_urlfilm(self, urls):

        res = dict()
        for url in urls:
            film = dict()
            data = self.get_data_from_url(settings.EL_PUNT_VALLES+url)

            #Get Img
            img_url_index = data.index("art-fullimg span2")
            img_url_1 = data[img_url_index:img_url_index+300]
            sub_index = img_url_1.index("<img")
            img_url_2 = img_url_1[sub_index:sub_index+250]
            img_url_i = img_url_2.index("src=")
            img_url_j = img_url_2.index("alt=")
            img_url = img_url_2[img_url_i+5:img_url_j-2]
            #print img_url

            #Get Title
            title_index = [m.start() for m in re.finditer('page-header', data)][1]
            title_1 = data[title_index:title_index+500]
            sub_index = title_1.index("<a")
            title_2 = title_1[sub_index:sub_index+300]
            title_i = title_2.index(">")
            title_j = title_2.index("</a>")
            title = title_2[title_i+1:title_j]
            #print title

            film["title"] = title.lstrip()
            film["url_img"] = settings.EL_PUNT_VALLES+img_url

            res[url] = film

        return res

    def get_data_from_url(self, url):
        file = urllib2.urlopen(url)
        data = file.read()
        data.replace(" ", "")
        data.replace("\t", "")
        file.close()

        return data