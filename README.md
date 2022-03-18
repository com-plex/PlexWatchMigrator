# PlexWatchMigrator
Migrates Plex watch history for TV show episodes from one server to another for all users including the owner/admin.

NOTE: This script will only work for TV shows (including Anime, I assume), and will mark shows watched down to the episode level.

I do not take credit for this as I did not make it, I am just uploading it here with instructions so others can use it as well.

**Windows:**
1. Install python (open command prompt and type python)
2. pip install plexapi
3. Download this: https://raw.githubusercontent.com/eiddor/PlexWatchMigrator/main/plexwatchlist.py
4. Edit the file in notepad++ or something with your values below:

    OLD_PLEX_TOKEN = "**YOUR OLD TOKEN**"

    OLD_PLEX_URL = "**PLEX URL INCLUDING PORT**"

    NEW_PLEX_TOKEN = "**YOUR NEW TOKEN**"

    NEW_PLEX_URL =  "**PLEX URL INCLUDING PORT**"

5. python your/directory/tree/plexwatchlist.py

**macOS/Linux:**
1. Install python
2. Install pip
3. pip3 install plexapi
4. Download this: https://raw.githubusercontent.com/eiddor/PlexWatchMigrator/main/plexwatchlist.py
Edit the file in the editor of your choice with your values below:

    OLD_PLEX_TOKEN = "**YOUR OLD TOKEN**"

    OLD_PLEX_URL = "**PLEX URL INCLUDING PORT**"

    NEW_PLEX_TOKEN = "**YOUR NEW TOKEN**"

    NEW_PLEX_URL =  "**PLEX URL INCLUDING PORT**"

5. python3 your/directory/tree/plexwatchlist.py

**Note:** if you don't know how to get the token or url/port use google.

**No support will be offered with this.**

p.s. in order for this to work the libraries must be named exactly the same in the .py file as they are in Plex and the users have to have the libraries toggled on in Plex.

```
section_sync = {
    'TV Shows': 'TV Shows', 
    'Kids TV': 'Kids Tv', 
    'Anime': 'Anime',
}
```