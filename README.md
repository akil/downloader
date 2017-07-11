# Downloader

Downloader is a multiple engine torrent downloader. It automatically detect which files to download and automatically look for next episode on torrent engines.

# How it works

Read the configuration file and set your video/whatever files directories. Downloader, uses two modes according to file type :
* mode 1 : Means simple file
* mode 2 : Means complex file like TV shows

* For mode 1, empty directory means download the corresponding file based on the folder name.
  * Ex: Transformers.720p (Downloader will search for "Transformers 720p" on torrent engine)
* For mode 2, if the directory is empty Downloader will download the file based on directory name beginning by S01E01. If the directory is not empty Downloader will search for the next episode.
  * Ex: Prison.break.720p (if empty Downloader will search for "prison break 720p S01E01". If not empty Downloader will search for "prison break 720p S02E03").

After downloading the torrent file, downloader can *save* the torrent file or *add* it to transmission. Check the configuration file.

# Installation

```bash
$ python setup.py install
$ mkdir ~/.config/downloader
$ cp /usr/share/downloader/downloader.cfg.example ~/.config/downloader/downloader.cfg
$ downloader ~/.config/downloader/downloader.cfg
```

# Update

Updating Downloader is easy :
1. clone the repository again and execute *setup.py* script
2. download the archive and execute *setup.py* script
3. if you keep the repository just type the following command: *git pull*

However, more engine will be added and I'm feeling lazy right now so to update the future engine use one of the previous method and diff the configuration file for new settings.

# For developer

Adding an engine is easy see *engines* directory and read the following steps :

1) Add your engine filename (without .py extension) in *engines/__init__.py*
2) Check *engine.py* file in *engines/engine.py*
3) Create your engine file (with the same name as *__init__.py*) in *engines* directory
4) Name your class with the same name of the file and capitalized (Ex: nextorrent.py -> class Nextorrent(engine.Engine))
5) *get* method must return a list of dictionaries like the following :
```python
[{'url': 'http://foo.com/file.torrent', 'seed': 5, 'filename': 'Black list S04E22 HDTV'}]
```
- Filename is the file from the engine
- Url is the download URL (can be the corresponding .torrent file or a magent link)
- Seed is the seed for the corresponding file

Do not filter the results, it's done by core Downloader program.

# Misc

- Configuration file use YAML format, use only spaces.
- Make a pull request for more engine.
- For now Downloader use the following torrent engine :
  - torrent9
  - nextorrent
  - nyaa
  - t411
  - 1337x
