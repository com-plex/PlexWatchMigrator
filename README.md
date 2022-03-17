# PlexWatchMigrator
Migrates Plex watch history from one server to another for all users.

**Windows:**
1. Install python (open command prompt and type python)
2. pip install plexapi
3. Download this: https://raw.githubusercontent.com/Gurky-Kronos/PlexWatchMigrator/main/plexwatchlist.py
4. Edit the file in notepad++ or something with your values below:

    OLD_PLEX_TOKEN = "**YOUR OLD TOKEN**"

    OLD_PLEX_URL = "**PLEX URL INCLUDING PORT**"

    NEW_PLEX_TOKEN = "**YOUR NEW TOKEN**"

    NEW_PLEX_URL =  "**PLEX URL INCLUDING PORT**"

5. python your/directory/tree/plexwatchlist.py

**macOS:**
1. Install python
2. Install pip
3. pip3 install plexapi
4. Download this: https://raw.githubusercontent.com/Gurky-Kronos/PlexWatchMigrator/main/plexwatchlist.py
Edit the file in notepad++ or something with your values below:

    OLD_PLEX_TOKEN = "**YOUR OLD TOKEN**"

    OLD_PLEX_URL = "**PLEX URL INCLUDING PORT**"

    NEW_PLEX_TOKEN = "**YOUR NEW TOKEN**"

    NEW_PLEX_URL =  "**PLEX URL INCLUDING PORT**"

5. python3 your/directory/tree/plexwatchlist.py

**Note:** if you don't know how to get the token or url/port use google.

**No support will be offered with this.**

p.s. in order for this to work the libraries must be named exactly the same in the .py file as they are in plex and the users have to have the libraries toggled on in plex.

section_sync = {
    'Movies': 'Movies',
    'TV Shows': 'TV Shows', 
    'Kids TV': 'Kids Tv', 
    'Anime': 'Anime',
}
