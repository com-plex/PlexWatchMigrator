# PlexWatchMigrator

This repo contains two scripts that will migrate the watched status for TV shows (by episode) and Movies between Plex servers.  These scripts should migrate the watched statuses for all users including the owner/admin.

> **NOTE**: This may or may not work for Anime shares depending on how the shows are setup.

I do not take credit for this as I did not make it originally.  I did add some logic to sync the owner/admin data and split it into a script for TV Shows and a script for Movies, and I am just uploading it here with instructions so others can use it as well.

**Windows:**
1. Install python (open command prompt and type python)
2. `pip install plexapi`
3. Download each script from the repo.
4. Edit the file in notepad++ or another editor with your values below:
```
    OLD_PLEX_TOKEN = "**YOUR OLD TOKEN**"

    OLD_PLEX_URL = "**PLEX URL INCLUDING PORT**"

    NEW_PLEX_TOKEN = "**YOUR NEW TOKEN**"

    NEW_PLEX_URL =  "**PLEX URL INCLUDING PORT**"
```
5. Edit the `section_sync` area with the names of your libraries.  TV show libraries should be in the TV script and Movie libraries should be in the Movie script.  These values are case sensitive and must match what is on each Plex server. (see note below)

6. `python your\directory\tree\plexTVwatchedlist.py` (for TV Shows)

7. `python your\directory\tree\plexMoviewatchedlist.py` (for Movies)

**macOS/Linux:**
1. Install python
2. Install pip
3. `pip3 install plexapi`
4. Download each script from the repo.
5. Edit the file in the editor of your choice with your values below:
```
    OLD_PLEX_TOKEN = "YOUR OLD TOKEN"

    OLD_PLEX_URL = "PLEX URL INCLUDING PORT"

    NEW_PLEX_TOKEN = "YOUR NEW TOKEN"

    NEW_PLEX_URL =  "PLEX URL INCLUDING PORT"
```
6. Edit the `section_sync` area with the names of your libraries.  TV show libraries should be in the TV script and Movie libraries should be in the Movies script.  These values are case sensitive and must match what is on each Plex server. (see note below)

7. `python3 your/directory/tree/plexTVwatchedlist.py` (for TV Shows)

8. `python3 your/directory/tree/plexMoviewatchedlist.py` (for Movies)

> **NOTE**: If you don't know how to get the token or url/port use Google.  I may add instructions for this in the future.

**No support will be offered with this.**

> **NOTE**: In order for this to work the libraries must be named exactly the same in the scripts as they are in Plex and the users must have the libraries toggled on in Plex.

```
section_sync = {
    'TV Shows': 'TV Shows', 
    'Kids TV': 'Kids Tv', 
    'Anime': 'Anime',
}
```

```
section_sync = {
    'Movies': 'Movies'
}
```

**ISSUES:**

---
If you see messages like this, it means that the Movie or TV Show either doesn't exist on the destination Plex server or is matched differently.  There's really nothing you can do about this besides manually marking them as watched:

```
They're Watching - imdb://tt3096858 - [<Guid:imdb://tt3096858>, <Guid:tmdb://383535>, <Guid:tvdb://12172>]
NOT FOUND - They're Watching - imdb://tt3096858 - [<Guid:imdb://tt3096858>, <Guid:tmdb://383535>, <Guid:tvdb://12172>]
Guid 'imdb://tt3096858' is not found in the library
```
---
If you see 401 errors, it can mean a few things:

* The token and/or URL isn't correct for one or both of the Plex servers
* The libraries don't exist on one or both of the Plex servers, or you have a typo in `section_sync`
* The users don't have the libraries shared with them on one or both of the Plex servers

