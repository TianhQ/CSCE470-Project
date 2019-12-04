import request

def search_string():
    url = ""
    r = request.get(url)
    data = r.json()
    return (
                data[0].name, data[0].address, data[0].city, data[0].city,
                data[0].state, data[0].postal_code, data[0].review_count,
                data[0].stars
           )