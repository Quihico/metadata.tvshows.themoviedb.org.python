from trakt import Trakt
from trakt.objects import Show

# get the movie info via imdb
def get_ratinginfo(imdb_id):
    __client_id = "5f2dc73b6b11c2ac212f5d8b4ec8f3dc4b727bb3f026cd254d89eda997fe64ae"
    __client_secret = "7b9ce1836d6f5c60fc78809d5455afaeb33236d86545ec860e814d3d4aae7b5c"
    # Configure
    Trakt.configuration.defaults.client(
        id=__client_id,
        secret=__client_secret
    )

    with Trakt.configuration.http(retry=True):
        show_info = Trakt['shows'].get(imdb_id, extended='full').to_dict()
        result = {}
        if(show_info):
            if 'votes' in show_info and 'rating' in show_info:
                result['ratings'] = {'trakt': {'votes': int(show_info['votes']), 'rating': float(show_info['rating'])}}
            elif 'rating' in show_info:
                result['ratings'] = {'trakt': {'rating': float(show_info['rating'])}}

        return result
