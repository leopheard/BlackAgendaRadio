from xbmcswift2 import Plugin, xbmcgui
from resources.lib import blackagendaradio

plugin = Plugin()

URL = "https://blackagendaradio.podbean.com/feed.xml"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://popularresistance-uploads.s3.amazonaws.com/uploads/2018/12/black-agenda2.jpg"},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://popularresistance-uploads.s3.amazonaws.com/uploads/2018/12/black-agenda2.jpg"},
    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = blackagendaradio.get_soup(URL)
    
    playable_podcast = blackagendaradio.get_playable_podcast(soup)
    
    items = blackagendaradio.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = blackagendaradio.get_soup(URL)
    
    playable_podcast1 = blackagendaradio.get_playable_podcast1(soup)
    
    items = blackagendaradio.compile_playable_podcast1(playable_podcast1)

    return items


if __name__ == '__main__':
    plugin.run()
