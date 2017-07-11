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
```

Read the configuration file before starting Downloader.

```
$ downloader ~/.config/downloader/downloader.cfg
	[+] aftermath
[torrent9]           Seed:   1 File: Coheed And Cambria - The Aftermath: Ascension - 2012
[torrent9]           Seed:   3 File: Obscure : The Aftermath (PSP)
	Download ->  [torrent9]           Seed: 1917 File: Aftermath FRENCH DVDRIP 2017
	[+] into.the.badlands.vostfr S03E01
	[+] fear.the.walking.dead S01E01
[torrent9]           Seed:  89 File: Fear The Walking Dead S01E01 FRENCH HDTV
[torrent9]           Seed:  21 File: Fear The Walking Dead S01E01 FRENCH BluRay 720p HDTV
[torrent9]           Seed:   1 File: Fear The Walking Dead S01E01 VOSTFR HDTV
[torrent9]           Seed:   8 File: Fear The Walking Dead S01E01 VOSTFR BluRay 720p HDTV
[torrent9]           Seed:  15 File: Fear The Walking Dead S01E01 VOSTFR HDTV (.mp4)
	Download ->  [torrent9]           Seed:  89 File: Fear The Walking Dead S01E01 FRENCH HDTV
	[+] fear.the.walking.dead S01E02
[torrent9]           Seed: 114 File: Fear The Walking Dead S01E02 FRENCH HDTV
[torrent9]           Seed:  20 File: Fear The Walking Dead S01E02 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  32 File: Fear The Walking Dead S01E02 VOSTFR HDTV
[torrent9]           Seed:  10 File: Fear The Walking Dead S01E02 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 114 File: Fear The Walking Dead S01E02 FRENCH HDTV
	[+] fear.the.walking.dead S01E03
[torrent9]           Seed: 102 File: Fear The Walking Dead S01E03 FRENCH HDTV
[torrent9]           Seed:  16 File: Fear The Walking Dead S01E03 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  22 File: Fear The Walking Dead S01E03 VOSTFR HDTV
[torrent9]           Seed:   8 File: Fear The Walking Dead S01E03 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 102 File: Fear The Walking Dead S01E03 FRENCH HDTV
	[+] fear.the.walking.dead S01E04
[torrent9]           Seed:  97 File: Fear The Walking Dead S01E04 FRENCH HDTV
[torrent9]           Seed:   1 File: Fear The Walking Dead S01E04 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  23 File: Fear The Walking Dead S01E04 VOSTFR HDTV
[torrent9]           Seed:   8 File: Fear The Walking Dead S01E04 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  97 File: Fear The Walking Dead S01E04 FRENCH HDTV
	[+] fear.the.walking.dead S01E05
[torrent9]           Seed:  97 File: Fear The Walking Dead S01E05 FRENCH HDTV
[torrent9]           Seed:  22 File: Fear The Walking Dead S01E05 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  21 File: Fear The Walking Dead S01E05 VOSTFR HDTV
[torrent9]           Seed:   9 File: Fear The Walking Dead S01E05 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  97 File: Fear The Walking Dead S01E05 FRENCH HDTV
	[+] fear.the.walking.dead S01E06
[torrent9]           Seed:  96 File: Fear The Walking Dead S01E06 FINAL FRENCH HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S01E06 FINAL FRENCH BluRay 720p HDTV
[torrent9]           Seed:  26 File: Fear The Walking Dead S01E06 FINAL VOSTFR HDTV
[torrent9]           Seed:   7 File: Fear The Walking Dead S01E06 FINAL VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  96 File: Fear The Walking Dead S01E06 FINAL FRENCH HDTV
	[+] fear.the.walking.dead S01E07
	[+] fear.the.walking.dead S02E01
[torrent9]           Seed: 108 File: Fear The Walking Dead S02E01 FRENCH HDTV
[torrent9]           Seed:  16 File: Fear The Walking Dead S02E01 VOSTFR HDTV
[torrent9]           Seed:   9 File: Fear The Walking Dead S02E01 VOSTFR BluRay 720p HDTV
[torrent9]           Seed:  17 File: Fear The Walking Dead S02E01 FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 108 File: Fear The Walking Dead S02E01 FRENCH HDTV
	[+] fear.the.walking.dead S02E02
[torrent9]           Seed:  92 File: Fear The Walking Dead S02E02 FRENCH HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S02E02 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  24 File: Fear The Walking Dead S02E02 VOSTFR HDTV
[torrent9]           Seed:  12 File: Fear The Walking Dead S02E02 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  92 File: Fear The Walking Dead S02E02 FRENCH HDTV
	[+] fear.the.walking.dead S02E03
[torrent9]           Seed: 110 File: Fear The Walking Dead S02E03 FRENCH HDTV
[torrent9]           Seed:  14 File: Fear The Walking Dead S02E03 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S02E03 VOSTFR HDTV
[torrent9]           Seed:  13 File: Fear The Walking Dead S02E03 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 110 File: Fear The Walking Dead S02E03 FRENCH HDTV
	[+] fear.the.walking.dead S02E04
[torrent9]           Seed:  86 File: Fear The Walking Dead S02E04 FRENCH HDTV
[torrent9]           Seed:  22 File: Fear The Walking Dead S02E04 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S02E04 VOSTFR HDTV
[torrent9]           Seed:  13 File: Fear The Walking Dead S02E04 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  86 File: Fear The Walking Dead S02E04 FRENCH HDTV
	[+] fear.the.walking.dead S02E05
[torrent9]           Seed:  94 File: Fear The Walking Dead S02E05 FRENCH HDTV
[torrent9]           Seed:  22 File: Fear The Walking Dead S02E05 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  16 File: Fear The Walking Dead S02E05 VOSTFR HDTV
[torrent9]           Seed:  15 File: Fear The Walking Dead S02E05 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  94 File: Fear The Walking Dead S02E05 FRENCH HDTV
	[+] fear.the.walking.dead S02E06
[torrent9]           Seed:  88 File: Fear The Walking Dead S02E06 FRENCH HDTV
[torrent9]           Seed:  12 File: Fear The Walking Dead S02E06 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  27 File: Fear The Walking Dead S02E06 VOSTFR HDTV
[torrent9]           Seed:  13 File: Fear The Walking Dead S02E06 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  88 File: Fear The Walking Dead S02E06 FRENCH HDTV
	[+] fear.the.walking.dead S02E07
[torrent9]           Seed: 103 File: Fear The Walking Dead S02E07 FRENCH HDTV
[torrent9]           Seed:   5 File: Fear The Walking Dead S02E07 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  29 File: Fear The Walking Dead S02E07 VOSTFR HDTV
[torrent9]           Seed:  10 File: Fear The Walking Dead S02E07 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 103 File: Fear The Walking Dead S02E07 FRENCH HDTV
	[+] fear.the.walking.dead S02E08
[torrent9]           Seed:  23 File: Fear The Walking Dead S02E08 VOSTFR HDTV
[torrent9]           Seed:   8 File: Fear The Walking Dead S02E08 VOSTFR BluRay 720p HDTV
[torrent9]           Seed:  70 File: Fear The Walking Dead S02E08 FRENCH HDTV
[torrent9]           Seed:  16 File: Fear The Walking Dead S02E08 FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  70 File: Fear The Walking Dead S02E08 FRENCH HDTV
	[+] fear.the.walking.dead S02E09
[torrent9]           Seed:  22 File: Fear The Walking Dead S02E09 VOSTFR HDTV
[torrent9]           Seed:   9 File: Fear The Walking Dead S02E09 VOSTFR BluRay 720p HDTV
[torrent9]           Seed:  90 File: Fear The Walking Dead S02E09 FRENCH HDTV
[torrent9]           Seed:  21 File: Fear The Walking Dead S02E09 FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  90 File: Fear The Walking Dead S02E09 FRENCH HDTV
	[+] fear.the.walking.dead S02E10
[torrent9]           Seed:  21 File: Fear The Walking Dead S02E10 VOSTFR HDTV
[torrent9]           Seed:   7 File: Fear The Walking Dead S02E10 VOSTFR BluRay 720p HDTV
[torrent9]           Seed:  63 File: Fear The Walking Dead S02E10 FRENCH HDTV
[torrent9]           Seed:  15 File: Fear The Walking Dead S02E10 FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  63 File: Fear The Walking Dead S02E10 FRENCH HDTV
	[+] fear.the.walking.dead S02E11
[torrent9]           Seed:  24 File: Fear The Walking Dead S02E11 VOSTFR HDTV
[torrent9]           Seed:  11 File: Fear The Walking Dead S02E11 VOSTFR BluRay 720p HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S02E11 FRENCH HDTV
[torrent9]           Seed:  16 File: Fear The Walking Dead S02E11 FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  24 File: Fear The Walking Dead S02E11 VOSTFR HDTV
	[+] fear.the.walking.dead S02E12
[torrent9]           Seed:  72 File: Fear The Walking Dead S02E12 FRENCH HDTV
[torrent9]           Seed:  16 File: Fear The Walking Dead S02E12 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  17 File: Fear The Walking Dead S02E12 VOSTFR HDTV
[torrent9]           Seed:   9 File: Fear The Walking Dead S02E12 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  72 File: Fear The Walking Dead S02E12 FRENCH HDTV
	[+] fear.the.walking.dead S02E13
[torrent9]           Seed:  96 File: Fear The Walking Dead S02E13 FRENCH HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S02E13 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  33 File: Fear The Walking Dead S02E13 VOSTFR HDTV
[torrent9]           Seed:   7 File: Fear The Walking Dead S02E13 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed:  96 File: Fear The Walking Dead S02E13 FRENCH HDTV
	[+] fear.the.walking.dead S02E14
[torrent9]           Seed:  31 File: Fear The Walking Dead S02E14 VOSTFR HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S02E14 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 112 File: Fear The Walking Dead S02E14 FRENCH HDTV
[torrent9]           Seed:  22 File: Fear The Walking Dead S02E14 FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 112 File: Fear The Walking Dead S02E14 FRENCH HDTV
	[+] fear.the.walking.dead S02E15
[torrent9]           Seed:  50 File: Fear The Walking Dead S02E15 FINAL VOSTFR HDTV
[torrent9]           Seed:  20 File: Fear The Walking Dead S02E15 FINAL VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 119 File: Fear The Walking Dead S02E15 FINAL FRENCH HDTV
[torrent9]           Seed:  44 File: Fear The Walking Dead S02E15 FINAL FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 119 File: Fear The Walking Dead S02E15 FINAL FRENCH HDTV
	[+] fear.the.walking.dead S02E16
	[+] fear.the.walking.dead S03E01
[torrent9]           Seed: 323 File: Fear The Walking Dead S03E01 FRENCH HDTV
[torrent9]           Seed:  74 File: Fear The Walking Dead S03E01 FRENCH BluRay 720p HDTV
[torrent9]           Seed: 148 File: Fear The Walking Dead S03E01 VOSTFR HDTV
[torrent9]           Seed:  74 File: Fear The Walking Dead S03E01 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 323 File: Fear The Walking Dead S03E01 FRENCH HDTV
	[+] fear.the.walking.dead S03E02
[torrent9]           Seed: 318 File: Fear The Walking Dead S03E02 FRENCH HDTV
[torrent9]           Seed:  68 File: Fear The Walking Dead S03E02 FRENCH BluRay 720p HDTV
[torrent9]           Seed: 121 File: Fear The Walking Dead S03E02 VOSTFR HDTV
[torrent9]           Seed:  61 File: Fear The Walking Dead S03E02 VOSTFR BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 318 File: Fear The Walking Dead S03E02 FRENCH HDTV
	[+] fear.the.walking.dead S03E03
[torrent9]           Seed: 123 File: Fear The Walking Dead S03E03 VOSTFR HDTV
[torrent9]           Seed:  55 File: Fear The Walking Dead S03E03 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 357 File: Fear The Walking Dead S03E03 FRENCH HDTV
[torrent9]           Seed: 103 File: Fear The Walking Dead S03E03 FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 357 File: Fear The Walking Dead S03E03 FRENCH HDTV
	[+] fear.the.walking.dead S03E04
[torrent9]           Seed: 148 File: Fear The Walking Dead S03E04 VOSTFR HDTV
[torrent9]           Seed:  81 File: Fear The Walking Dead S03E04 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 443 File: Fear The Walking Dead S03E04 FRENCH HDTV
[torrent9]           Seed: 108 File: Fear The Walking Dead S03E04 FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 443 File: Fear The Walking Dead S03E04 FRENCH HDTV
	[+] fear.the.walking.dead S03E05
[torrent9]           Seed: 240 File: Fear The Walking Dead S03E05 VOSTFR HDTV
[torrent9]           Seed: 178 File: Fear The Walking Dead S03E05 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 633 File: Fear The Walking Dead S03E05 FRENCH HDTV
[torrent9]           Seed: 230 File: Fear The Walking Dead S03E05 FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 633 File: Fear The Walking Dead S03E05 FRENCH HDTV
	[+] fear.the.walking.dead S03E06
[torrent9]           Seed: 296 File: Fear The Walking Dead S03E06 VOSTFR HDTV
[torrent9]           Seed: 230 File: Fear The Walking Dead S03E06 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 915 File: Fear The Walking Dead S03E06 FRENCH HDTV
[torrent9]           Seed: 301 File: Fear The Walking Dead S03E06 FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 915 File: Fear The Walking Dead S03E06 FRENCH HDTV
	[+] fear.the.walking.dead S03E07
[torrent9]           Seed: 497 File: Fear The Walking Dead S03E07 VOSTFR HDTV
[torrent9]           Seed: 243 File: Fear The Walking Dead S03E07 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 1366 File: Fear The Walking Dead S03E07 FRENCH HDTV
[torrent9]           Seed: 407 File: Fear The Walking Dead S03E07 FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 1366 File: Fear The Walking Dead S03E07 FRENCH HDTV
	[+] fear.the.walking.dead S03E08
[torrent9]           Seed: 433 File: Fear The Walking Dead S03E08 VOSTFR HDTV
[torrent9]           Seed: 241 File: Fear The Walking Dead S03E08 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 1375 File: Fear The Walking Dead S03E08 FRENCH HDTV
[torrent9]           Seed: 400 File: Fear The Walking Dead S03E08 FRENCH BluRay 720p HDTV
	Download ->  [torrent9]           Seed: 1375 File: Fear The Walking Dead S03E08 FRENCH HDTV
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
