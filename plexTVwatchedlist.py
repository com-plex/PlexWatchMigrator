#pip install plexapi
#
import json
import requests
import time
from plexapi.server import PlexServer
import os

# Change the next four lines

OLD_PLEX_TOKEN = "YOUR OLD TOKEN"
OLD_PLEX_URL = "PLEX URL INCLUDING PORT"
NEW_PLEX_TOKEN = "YOUR NEW TOKEN"
NEW_PLEX_URL =  "PLEX URL INCLUDING PORT"

old_plex = PlexServer(OLD_PLEX_URL, OLD_PLEX_TOKEN)
old_account = old_plex.myPlexAccount()
new_plex = PlexServer(NEW_PLEX_URL, NEW_PLEX_TOKEN)
new_account = new_plex.myPlexAccount()


#old:new library names. need to be exact. note "Kids Tv" vs "Kids TV"
#make sure you share libraries on the new server before. otherwise it will error.
#
#If you get a 401 error it's usually either due to these settings not matching the Plex servers or
#the users don't have access to the libraries
#
section_sync = {
    'TV Shows': 'TV Shows', 
    'Kids TV': 'Kids Tv', 
    'Anime': 'Anime'
}

def mark_watched_tv(old_section, new_section):
    print("Checking: " + old_section.title)
    for ep in old_section.watched():
        for ep2 in new_section.episodes():
            if ep.title == ep2.title:
                if ep.isWatched:
                    ep2.markWatched()
                    print(f'Episode marked watched - {ep2.seasonEpisode} - {ep2.title}')
                    break
                else:
                    ep2.markUnwatched()
                    print(f'Episode marked unwatched - {ep2.seasonEpisode} - {ep2.title}')
                    break

def get_user_list(): 
    user_list = {x.title: x.email if x.email else x.title for x in old_plex.myPlexAccount().users() if x.title}
    return user_list
 
def parse_guid(guid, guids): 
    x = guid
    if(guids): 
        for i in guids: 
            if(i.id.find('imdb') != -1):
                x = i.id
 
    # if guid[0:2] == "tt" and guid[2:].isnumeric():
    #     return "imdb"
    # x = guid.split("://")[0]
    x = x.replace("com.plexapp.agents.", "")
    x = x.replace("tv.plex.agents.", "")
    x = x.replace("themoviedb", "tmdb")
    x = x.replace("thetvdb", "tvdb")
    x = x.replace("?lang=en", "")
    return (x)


if __name__ == "__main__":

    user_list = get_user_list()
    for user_id in user_list: 
    # if(True): 
        print (user_id)
 
        old_user_account = old_account.user(user_id)
        new_user_account = new_account.user(user_id)
 
        old_user_plex = PlexServer(OLD_PLEX_URL, old_user_account.get_token(old_plex.machineIdentifier))
        new_user_plex = PlexServer(NEW_PLEX_URL, new_user_account.get_token(new_plex.machineIdentifier))
 
        sections = old_user_plex.library.sections()
        for old_section in sections: 
            print(old_section.title)
            if old_section.title in section_sync:
                new_section = new_user_plex.library.section(section_sync[old_section.title]) 
                admin_section = new_plex.library.section(new_section.title)
 
                for media in old_section.search(unwatched=False):
                    guid = parse_guid(media.guid, media.guids)
                    print(f'{media.title} - {guid} - {media.guids}')
                    try: 
                        #for the search, we have to use the admin account, otherwise 403
                        result = admin_section.getGuid(guid)
                        if(not result):
                            raise 
                        #take the MediaItem key returned, pass it into the local user's fetch
                        found_item = new_section.fetchItem(result.key)
                        mark_watched_tv(media, found_item)
                    except Exception as e: 
                        print(f'NOT FOUND - {media.title} - {guid} - {media.guids}')
                        print(e)
                        pass

#Sync the owner's watched status as well -- There is probably a better way to do this, but here's what worked for me.
#This is required because plexapi's users() function doesn't return the admin/owner user for some reason.

    owner_user_id = old_plex.myPlexAccount().username
    print (owner_user_id)

    old_user_plex = PlexServer(OLD_PLEX_URL, OLD_PLEX_TOKEN)
    new_user_plex = PlexServer(NEW_PLEX_URL, NEW_PLEX_TOKEN)

    sections = old_user_plex.library.sections()
    for old_section in sections: 
        print(old_section.title)
        if old_section.title in section_sync:
            new_section = new_user_plex.library.section(section_sync[old_section.title]) 
            admin_section = new_plex.library.section(new_section.title)

            for media in old_section.search(unwatched=False):
                guid = parse_guid(media.guid, media.guids)
                print(f'{media.title} - {guid} - {media.guids}')
                try: 
                    #for the search, we have to use the admin account, otherwise 403
                    result = admin_section.getGuid(guid)
                    if(not result):
                        raise 
                    #take the MediaItem key returned, pass it into the local user's fetch
                    found_item = new_section.fetchItem(result.key)
                    mark_watched_tv(media, found_item)
                except Exception as e: 
                    print(f'NOT FOUND - {media.title} - {guid} - {media.guids}')
                    print(e)
                    pass
