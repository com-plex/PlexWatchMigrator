# PlexWatchMigrator

This repository contains two Python scripts that will help you migrate the watched status for your Plex server/appbox. It is written for movie and TV libraries, anime might not work depending on the setup.

This is a slightly adjusted version of [Gurky-Kronos/PlexWatchMigrator](https://github.com/Gurky-Kronos/PlexWatchMigrator).

**Windows:**

1. Install Python 3.
2. Open command prompt and enter: `pip install plexapi`
3. Either download both scripts or clone the repository.
4. Edit the two scripts in Notepad++ (or a comparable editor) and change the values:
   ```
   OLD_PLEX_TOKEN = "**YOUR OLD TOKEN**"
   OLD_PLEX_URL = "**PLEX URL INCLUDING PORT**"
   NEW_PLEX_TOKEN = "**YOUR NEW TOKEN**"
   NEW_PLEX_URL =  "**PLEX URL INCLUDING PORT**"
   ```
   Guidance as to where the tokens can be found: [see Plex Support](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/). You can use the Plex Direct URL from the same action, eg: `https://192-168-0-1.blabla.plex.direct:32400`
5. Edit the `section_sync` area with the names of your libraries.
   ```
   section_sync = {
       'Movies': 'Movies'
   }
   ```
   The format is old:new **and is case sensitive**. The libraries should be configured in the respective scripts; mixing will break stuff.
6. Run the scripts, eg, by executing:
   ```
   python3 \Users\Whatever\SyncTV.py
   ```

**macOS/Linux:**
1. Install Python 3, alongside with pip
2. Install the required plexapi moddule: `pip install plexapi`
3. Either download both scripts or clone the repository.
4. Edit the two scripts in your favorite editor and change the values:
   ```
   OLD_PLEX_TOKEN = "**YOUR OLD TOKEN**"
   OLD_PLEX_URL = "**PLEX URL INCLUDING PORT**"
   NEW_PLEX_TOKEN = "**YOUR NEW TOKEN**"
   NEW_PLEX_URL =  "**PLEX URL INCLUDING PORT**"
   ```
   Guidance as to where the tokens can be found: [see Plex Support](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/). You can use the Plex Direct URL from the same action, eg: `https://192-168-0-1.blabla.plex.direct:32400`
5. Edit the `section_sync` area with the names of your libraries.
   ```
   section_sync = {
       'Movies': 'Movies'
   }
   ```
   The format is old:new **and is case sensitive**. The libraries should be configured in the respective scripts; mixing will break stuff.
6. Run the scripts, eg, by executing:
   ```
   python3 /home/user/SyncTV.py
   ```

## Troubleshooting

**Q: I get a 401 error?**

1. Make sure the Plex token and URLs are correct within the two scripts
2. Make sure you configured the `section_sync` properly and that it matches the case.
3. Make sure all the users can access both the old and new libraries; that you've shared both with them.

**Q: The script crashes after a certain username?**

1. Make sure all the users can access both the old and new libraries; that you've shared both with them.
2. If you are not sharing anything with the respective user, [unfriend them](https://app.plex.tv/desktop/#!/friends).

**Q: I get a "not found in the library" error?**

If you get errors like this:

```
They're Watching - imdb://tt3096858 - [<Guid:imdb://tt3096858>, <Guid:tmdb://383535>, <Guid:tvdb://12172>]
NOT FOUND - They're Watching - imdb://tt3096858 - [<Guid:imdb://tt3096858>, <Guid:tmdb://383535>, <Guid:tvdb://12172>]
Guid 'imdb://tt3096858' is not found in the library
```

It means that the movie or TV show either does not exist on the destination Plex server or is matched differently. There is nothing that can be done about this, unfortunately, except manually marking them as watched.