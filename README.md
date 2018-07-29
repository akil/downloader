# Downloader

Downloader is a multiple search engine torrent downloader. It automatically detect which files to download and automatically look for next episode on torrent search engines.

# How it works

Read the configuration file and set your video/whatever files directories. Downloader, uses two modes according to file type :
* mode 1 : Means simple file
* mode 2 : Means complex file like TV shows

* For mode 1, empty directory means download the corresponding file based on the folder name.
  * Ex: Transformers.720p (Downloader will search for "Transformers 720p" on torrent search engine)
* For mode 2, if the directory is empty Downloader will download the file based on directory name beginning by S01E01. If the directory is not empty Downloader will search for the next episode.
  * Ex: Prison.break.720p (if empty Downloader will search for "prison break 720p S01E01". If not empty Downloader will search for "prison break 720p S02E03").

After downloading the torrent file, downloader can *save* the torrent file or *add* it to transmission. Check the configuration file.

# Installation

```bash
$ python setup.py install
$ mkdir ~/.config/downloader
$ cp /usr/share/downloader/downloader.cfg.example ~/.config/downloader/downloader.cfg
```

Read the configuration file before starting Downloader.


# Update

Updating Downloader is easy :
1. clone the repository again and execute *setup.py* script
2. download the archive and execute *setup.py* script
3. if you keep the repository just type the following command: *git pull*

However, more search engine will be added and I'm feeling lazy right now so to update the future search engine use one of the previous method and diff the configuration file for new settings.

# Killer setup

1. Install Plex
2. Install tranmission-daemon
3. Plug Raspberry PI on your TV and install RasPlex
4. Write a cron job for Downloader
5. Enjoy your movies and series on your TV without doing anything ;)

# Tips

- If you want to begin a TV shows after S04E11 just create that file into your directory. Downloader do not care of the file type
- If you named your directory with '720p','1080p','HDRip' Downloader will check for torrent file with that information
- I use the following structure :

```
    /opt/multimedia/videos
    ├── animes
    │   ├── trickster.vostfr
    │   └── trinity.blood.vostfr
    ├── documentary
    │   └── the.hacker.wars.doc
    ├── movies
    │   ├── Interstellar.1080p
    │   └── war.dogs.2016
    ├── series
    │   ├── narcos
    └── sports
        ├── UFC.PPV
        └── the.ultimate.tuf
```

# For developer

Adding a search engine is easy see *engines* directory and read the following steps :

1) Add your search engine filename (without .py extension) in *engines/__init__.py*
2) Check *engine.py* file in *engines/engine.py*
3) Create your search engine file (with the same name as *__init__.py*) in *engines* directory
4) Name your class with the same name of the file and capitalized (Ex: nextorrent.py -> class Nextorrent(engine.Engine))
5) *get* method must return a tuple of list and a session object:
  - list of dictionaries like the following :
     - Filename is the file from the search engine
     - Url is the download URL (can be the coresponding .torrent file or a magent link)
     - Seed is the seed for the corresponding file
```python
[{'url': 'http://foo.com/file.torrent', 'seed': 5, 'filename': 'Black list S04E22 HDTV'}]
```

   - A request session object (so you have to use it for requesting your search engine)

Do not filter the results, it's done by core Downloader program.

# Misc

- Configuration file use YAML format, use only spaces.
- Make a pull request for more search engine.
- For now Downloader use the following torrent search engine :
  - torrent9
  - ~~nextorrent~~
  - nyaa
  - yggtorrent
  - 1337x
  - ~~torrentproject~~


# ...

```
$ downloader ~/.config/downloader/downloader.cfg
	[+] aftermath
[torrent9]           Seed: 189 File: Aftermath FRENCH BluRay 1080p 2017
[torrent9]           Seed: 205 File: Aftermath FRENCH BluRay 720p 2017
[torrent9]           Seed: 1917 File: Aftermath FRENCH DVDRIP 2017
[torrent9]           Seed:  14 File: Aftermath S01E13 FINAL FRENCH HDTV
[torrent9]           Seed:  23 File: Aftermath S01E12 FRENCH HDTV
[torrent9]           Seed:  15 File: Aftermath S01E11 FRENCH HDTV
[torrent9]           Seed:  16 File: Aftermath S01E10 FRENCH HDTV
[torrent9]           Seed:  19 File: Aftermath S01E09 FRENCH HDTV
[torrent9]           Seed:  26 File: Aftermath S01E08 FRENCH HDTV
[torrent9]           Seed:  24 File: Aftermath S01E07 FRENCH HDTV
[torrent9]           Seed:  30 File: Aftermath S01E06 FRENCH HDTV
[torrent9]           Seed:  17 File: Aftermath S01E05 FRENCH HDTV
[torrent9]           Seed:  15 File: Aftermath S01E04 FRENCH HDTV
[torrent9]           Seed:  18 File: Aftermath S01E03 FRENCH HDTV
[torrent9]           Seed:  23 File: Aftermath S01E02 FRENCH HDTV
[torrent9]           Seed:  37 File: Aftermath S01E01 FRENCH HDTV
	[+] shadowhunters S02E13
[torrent9]           Seed:  18 File: Shadowhunters S02E13 VOSTFR HDTV
[torrent9]           Seed:  84 File: Shadowhunters S02E13 FRENCH HDTV
[nextorrent]         Seed:  32 File: Shadowhunters S02E13 VOSTFR HDTV
[nextorrent]         Seed: 121 File: Shadowhunters S02E13 FRENCH HDTV
[...]
```
