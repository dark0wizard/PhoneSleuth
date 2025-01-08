from googlesearch import search


def simple_google(query):
    try:
        dict_google = {}
        for i, j in enumerate(search(f'"{query}"')):
            dict_google.update({i + 1: j})
        return dict_google if dict_google != {} else False
    except:
        return "Google blocked a request"


def google_dorks(query):
    try:
        social_medias = ["instagram.com", "facebook.com", "tiktok.com", "twitter.com", "linkedin.com"]
        dict_google = {}
        for media in social_medias:
            result = simple_google(f'site:{media} intext:"{query}" | intext:"{query[1:]}"')
            if result:
                dict_google.update({media: result})
        return dict_google if dict_google != {} else False
    except:
        return "Google blocked a request"
