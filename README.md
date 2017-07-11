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
	[+] the.mummy
[nyaa]               Seed:   2 File: The Mummy 2017 1080p KORSUB HDRip x264 AAC 5.1 ESub - NextBit
[nyaa]               Seed: 520 File: The.Mummy.2017.1080p.KORSUB.HDRip.x264.AAC2.0-STUTTERSHIT
[1337x]              Seed: 12529 File: The.Mummy.2017.1080p.KORSUB.HDRip.x264.AAC2.0-STUTTERSHIT[rarbg]
[1337x]              Seed: 4918 File: The Mummy 2017 HD-TS x264-CPG
[1337x]              Seed: 3631 File: The.Mummy.2017.KORSUB.HDRip.x264-STUTTERSHIT[rarbg]
[1337x]              Seed: 3545 File: The.Mummy.2017.720p.KORSUB.HDRip.x264.AAC2.0-STUTTERSHIT[rarbg]
[1337x]              Seed: 2353 File: The.Mummy.2017.1080p.HC.HDRip.X264.AC3-EVO
[1337x]              Seed: 2057 File: The.Mummy.2017.KORSUB.HDRip.XviD.MP3-STUTTERSHIT[rarbg]
[1337x]              Seed: 1962 File: The Mummy 2017 720p HD-TS x264-CPG
[1337x]              Seed: 1606 File: The.Mummy.2017.1080p.HC.HDRip.X264.AC3-EVO
[1337x]              Seed: 1435 File: The Mummy (2017) - HDCAM - x264 - ENG - 800MB - Makintos13
[1337x]              Seed: 1361 File: The.Mummy.2017.720p.KORSUB.HDRip.XviD.MP3-STUTTERSHIT[rarbg]
[1337x]              Seed: 1318 File: The.Mummy.2017.720p.HC.HDRip.X264.AC3-EVO
[1337x]              Seed: 1178 File: The Mummy (2017) 720p Uncut HD-TS [Dual Audio] [Hindi+Rus] 980Mb [DiCT]
[1337x]              Seed: 1102 File: The Mummy (2017) 1080p KORSUB HDRip 1.8GB - MkvCage
[1337x]              Seed: 1014 File: The Mummy 2017 FULL HDCAM x264-JiMMY
[1337x]              Seed: 983 File: The Mummy (2017) 720p HC HDRip x264 AAC - Downloadhub.in
[1337x]              Seed: 981 File: The Mummy (2017) [720p - HC HDRip - [English + (Tamil + Telugu (TC Audios)] - x264 - 1GB] - Team TR
[1337x]              Seed: 789 File: The Mummy (2017) 720p HC HDRip 850MB - MkvCage
[1337x]              Seed: 683 File: The.Mummy.2017.1080p.HC.HDRip.X264.AC3-EVO[EtHD]
[1337x]              Seed: 613 File: The Mummy 2017 Movies HD TS XviD Clean Audio AAC New Source with Sample &#226;&#152;&#187;rDX&#226;&#152;&#187;
[1337x]              Seed: 610 File: The Mummy 2017 480p HDTS Rip x264 AAC ESub - NextBit
	Download ->  [1337x]              Seed: 12529 File: The.Mummy.2017.1080p.KORSUB.HDRip.x264.AAC2.0-STUTTERSHIT[rarbg]
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
[torrent9]           Seed:   4 File: Aftermath S01E13 VOSTFR HDTV
[torrent9]           Seed:   3 File: Aftermath S01E12 VOSTFR HDTV
[torrent9]           Seed:   6 File: Aftermath S01E11 VOSTFR HDTV
[torrent9]           Seed:   5 File: Aftermath S01E10 VOSTFR HDTV
[torrent9]           Seed:   6 File: Aftermath S01E09 VOSTFR HDTV
[torrent9]           Seed:   4 File: Aftermath S01E08 VOSTFR HDTV
[torrent9]           Seed:   3 File: Aftermath S01E07 VOSTFR HDTV
[torrent9]           Seed:   8 File: Aftermath S01E06 VOSTFR HDTV
[torrent9]           Seed:   5 File: Aftermath S01E05 VOSTFR HDTV
[torrent9]           Seed:   5 File: Aftermath S01E04 VOSTFR HDTV
[torrent9]           Seed:   7 File: Aftermath S01E03 VOSTFR HDTV
[torrent9]           Seed:   9 File: Aftermath S01E02 VOSTFR HDTV
[torrent9]           Seed:  11 File: Aftermath S01E01 VOSTFR HDTV
[torrent9]           Seed:   1 File: Coheed And Cambria - The Aftermath: Ascension - 2012
[torrent9]           Seed:   3 File: Obscure : The Aftermath (PSP)
[nextorrent]         Seed: 742 File: Aftermath VOSTFR DVDRiP 2017
[nextorrent]         Seed: 912 File: Aftermath MULTI BluRay 1080p 2017
[nextorrent]         Seed: 703 File: Aftermath FRENCH BluRay 720p 2017
[nextorrent]         Seed: 7851 File: Aftermath FRENCH DVDRiP 2017
[nextorrent]         Seed:  82 File: Aftermath FRENCH DVDRiP x264 2017
[nextorrent]         Seed:  59 File: Aftermath S01E13 FINAL FRENCH HDTV
[nextorrent]         Seed:  39 File: Aftermath S01E12 FRENCH HDTV
[nextorrent]         Seed:  39 File: Aftermath S01E11 FRENCH HDTV
[nextorrent]         Seed:  14 File: Aftermath S01E10 FRENCH HDTV
[nextorrent]         Seed:  70 File: Aftermath S01E09 FRENCH HDTV
[nextorrent]         Seed:  40 File: Aftermath S01E08 FRENCH HDTV
[nextorrent]         Seed:  24 File: Aftermath S01E07 FRENCH HDTV
[nextorrent]         Seed:  74 File: Aftermath S01E06 FRENCH HDTV
[nextorrent]         Seed:  89 File: Aftermath S01E05 FRENCH HDTV
[nextorrent]         Seed:  57 File: Aftermath S01E04 FRENCH HDTV
[nextorrent]         Seed: 101 File: Aftermath S01E03 FRENCH HDTV
[nextorrent]         Seed: 131 File: Aftermath S01E02 FRENCH HDTV
[nextorrent]         Seed: 333 File: Aftermath S01E01 FRENCH HDTV
[1337x]              Seed: 2290 File: Aftermath.2017.HDRip.XViD-ETRG
[1337x]              Seed: 2235 File: Aftermath (2017) [720p] [YTS] [YIFY]
[1337x]              Seed: 1841 File: Aftermath (2017) [1080p] [YTS] [YIFY]
[1337x]              Seed: 1203 File: Aftermath.2017.1080p.WEB-DL.DD5.1.H264-FGT[EtHD]
[1337x]              Seed: 1185 File: Aftermath (2017) 720p WEB-DL 750MB - MkvCage
[1337x]              Seed: 686 File: [Tushy] Moka Mora (Drunk Dial Aftermath - 26.04.2017) rq (2k).mp4
[1337x]              Seed: 650 File: Aftermath 2017 HDRip XviD AC3-EVO
[1337x]              Seed: 422 File: Aftermath.2017.1080p.BluRay.x264-ROVERS
[1337x]              Seed: 352 File: Aftermath &#226;&#128;&#147; La vendetta (2017 ITA)
[1337x]              Seed: 335 File: [Tushy] Moka Mora (Drunk Dial Aftermath - 26.04.2017) (1k).mp4
[1337x]              Seed: 263 File: Aftermath.2017.1080p.BluRay.H264.AAC-RARBG
[1337x]              Seed: 205 File: Aftermath 2017 1080p WEBRip 1.3 GB - iExTV
[1337x]              Seed: 200 File: Aftermath (2017) 720p BRRip 850MB - MkvCage
[1337x]              Seed: 179 File: Tushy - Drunk Dial Aftermath - Moka Mora [720p].mp4 torrent
[1337x]              Seed: 159 File: Aftermath.La.Vendetta.2017.iTALiAN.AC3.BDRip.XviD-DDNCREW.avi
[1337x]              Seed: 150 File: Aftermath.2017.HDRip.XviD.AC3-EVO[PRiME]
[1337x]              Seed: 146 File: Keeping.Up.With.the.Kardashians.S13E03.The.Aftermath.HDTV.x264-CRiMSON[eztv]
[1337x]              Seed: 138 File: Aftermath.2017.720p.BluRay.H264.AAC-RARBG
[1337x]              Seed: 111 File: Aftermath.2017.BDRip.x264-ROVERS
[1337x]              Seed: 104 File: Leah.Remini.Scientology.and.the.Aftermath.S02E00.Merchants.of.Fear.HDTV.x264-W4F[eztv]
	Download ->  [nextorrent]         Seed: 7851 File: Aftermath FRENCH DVDRiP 2017
	[+] the.wizard.of.lies
[torrent9]           Seed: 1936 File: The Wizard Of Lies FRENCH WEBRIP 2017
[nextorrent]         Seed: 1662 File: The Wizard Of Lies FRENCH HDRiP 2017
[1337x]              Seed: 2053 File: The.Wizard.Of.Lies.2017.FRENCH.HDRiP.XViD-STVFRV &#226;&#151;&#143;Shadow&#226;&#151;&#143;
[1337x]              Seed: 510 File: The.Wizard.of.Lies.2017.HDRip.XviD.AC3-EVO
[1337x]              Seed: 388 File: The Wizard of Lies (2017) 720p WEB-DL 1GB - MkvCage
[1337x]              Seed: 376 File: The.Wizard.of.Lies.2017.1080p.WEBRip.DD5.1.x264-monkee [HDSector]
[1337x]              Seed: 122 File: The.Wizard.of.Lies.2017.WEBRip.x264-FGT [HDSector]
[1337x]              Seed: 104 File: The.Wizard.of.Lies.2017.1080p.WEBRip.DD5.1.x264-monkee[EtHD]
[1337x]              Seed:  86 File: The.Wizard.of.Lies.2017.HDRip.HBO.700MB
[1337x]              Seed:  85 File: The.Wizard.of.Lies.2017.HDRip.XViD.AC3-juggs
[1337x]              Seed:  49 File: The Wizard of Lies 2017 720p WEBRip 950 MB - iExTV
[1337x]              Seed:  39 File: The.Wizard.of.Lies.2017.HDRip.XviD.AC3-EVO
[1337x]              Seed:  31 File: The Wizard Of Lies 2017 Movies HDRip XviD AAC New Source with Sample &#226;&#152;&#187;rDX&#226;&#152;&#187;
[1337x]              Seed:  24 File: The.Wizard.of.Lies.2017.1080p.WEB-DL.x264-M2Tv
[1337x]              Seed:  18 File: The.Wizard.of.Lies.2017.HDTV.x264-aAF[ettv]
[1337x]              Seed:  16 File: The.Wizard.of.Lies.2017.HDTV.1080p.x264.[By ExYu-Subs HC]
[1337x]              Seed:   9 File: The.Wizard.of.Lies.2017.REPACK.720p.HBO.WEB-DL.AAC2.0.H.264-monkee[EtHD]
[1337x]              Seed:   9 File: The.Wizard.of.Lies.2017.HDRip.XviD.AC3-EVO
[1337x]              Seed:   5 File: The.Wizard.of.Lies.2017.REPACK.720p.WEBRip.H.264-monkee
[1337x]              Seed:   4 File: The.Wizard.of.Lies.2017.REPACK.720p.HBO.WEB-DL.AAC2.0.H.264-monkee[PRiME]
[1337x]              Seed:   3 File: The.Wizard.of.Lies.2017.HDRip.XviD.AC3-EVO[PRiME]
[1337x]              Seed:   1 File: The.Wizard.of.Lies.2017.REPACK.720p.HBO.WEB.DL.HEVC.2CH.x265[PRiME]
	Download ->  [1337x]              Seed: 2053 File: The.Wizard.Of.Lies.2017.FRENCH.HDRiP.XViD-STVFRV &#226;&#151;&#143;Shadow&#226;&#151;&#143;
	[+] fear.the.walking.dead S01E01
[torrent9]           Seed:  89 File: Fear The Walking Dead S01E01 FRENCH HDTV
[torrent9]           Seed:  21 File: Fear The Walking Dead S01E01 FRENCH BluRay 720p HDTV
[torrent9]           Seed:   1 File: Fear The Walking Dead S01E01 VOSTFR HDTV
[torrent9]           Seed:   8 File: Fear The Walking Dead S01E01 VOSTFR BluRay 720p HDTV
[torrent9]           Seed:  15 File: Fear The Walking Dead S01E01 VOSTFR HDTV (.mp4)
[1337x]              Seed:   0 File: Fear the Walking Dead S01E01 Pilot 1080p WEB-DL DD5.1 x264-NTb
[1337x]              Seed:   0 File: Fear The Walking Dead S01e01-06, [Mux - XviD - Ita Eng Mp3 - Sub Ita Eng] WEB-DLRip by sp_54321 COMP...
[1337x]              Seed:   0 File: AgusiQ TorrentS pl Fear the Walking Dead S01E01 PL 480p Ralf AgusiQ
[1337x]              Seed:   0 File: Fear The Walking Dead S01e01[BDmux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng]By GiuseppeTnT.Littleli...
[1337x]              Seed:   0 File: AgusiQ TorrentS pl Fear The Walking Dead S01E01 PL SUBBED KiT 676kowal
[1337x]              Seed:   0 File: Fear The Walking Dead S01E01 720p HDTV x264 KILLERS
[1337x]              Seed:   0 File: Fear The Walking Dead S01E01 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear the Walking Dead S01e01-02, [XviD - Eng Mp3 - Sub Ita Eng] DLRip
[1337x]              Seed:   0 File: Fear The Walking Dead S01E01,02 1080p AC3 5.1 Web Dl
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S01E01.720p.HDTV.x265-MRSK [CTTV]
[1337x]              Seed:   0 File: Fear The Walking Dead S01E01 Pilot 1080p WEB-DL Dual-Audio
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E01.HDTV.480p.x264.AAC-VYTO [P2PDL]
[1337x]              Seed:   0 File: Fear the Walking Dead S01E01 Pilot 1080p WEB-DL 2CH x264 - MZABI
[1337x]              Seed:   0 File: Fear the Walking Dead S01E01 Pilot 720p WEB-DL 2CH x264 - MZABI
[1337x]              Seed:   0 File: Fear The Walking Dead s01e01[720p]x265_lucifer22
[1337x]              Seed:   0 File: Fear The Walking Dead S01E01 HDTV 1080p {KNIX}
[1337x]              Seed:   0 File: Fear the Walking Dead S01e01, [XviD - Eng Mp3 - Sub Ita Eng] HDTVRip - Pilot
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E01.Xvid-AJAXEN
[1337x]              Seed:   0 File: Fear The Walking Dead S01E01 HDTV XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear The Walking Dead S01E01 720p HDTV x264-KILLERS
	Download ->  [torrent9]           Seed:  89 File: Fear The Walking Dead S01E01 FRENCH HDTV
	[+] fear.the.walking.dead S01E02
[torrent9]           Seed: 114 File: Fear The Walking Dead S01E02 FRENCH HDTV
[torrent9]           Seed:  20 File: Fear The Walking Dead S01E02 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  32 File: Fear The Walking Dead S01E02 VOSTFR HDTV
[torrent9]           Seed:  10 File: Fear The Walking Dead S01E02 VOSTFR BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S01E02 So Close, Yet So Far 720p WEB-DL DD5.1 x264-NTb
[1337x]              Seed:   0 File: Fear the Walking Dead S01E02 So Close, Yet So Far 1080p WEB-DL DD5.1 x264
[1337x]              Seed:   0 File: Fear The Walking Dead S01e02[BDmux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng]By GiuseppeTnT.Littleli...
[1337x]              Seed:   0 File: Fear The Walking Dead S01E02 720p HDTV x264 KILLERS Dublado Coveiro
[1337x]              Seed:   0 File: Fear The Walking Dead S01E02 1080p HDTV x264 G2G DUAL RK
[1337x]              Seed:   0 File: Fear The Walking Dead S01E02 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S01E02.720p.HDTV.x265-MRSK [CTTV]
[1337x]              Seed:   0 File: Fear The Walking Dead S01E02 So Close, Yet So Far 720p
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E02.720p.HDTV.x264-KILLERS [CTTV]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E02.Xvid-AJAXEN
[1337x]              Seed:   0 File: Fear The Walking Dead S01E02 REPACK 720p HDTV x264-KILLERS
[1337x]              Seed:   0 File: Fear the Walking Dead S01e02, [XviD - Eng Mp3 - Sub Ita Eng] HDTVRip - So Close, Yet So Far [TNT Vil...
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E02.HDTV.480p.x264.AAC-VYTO [P2PDL]
[1337x]              Seed:   0 File: Fear The Walking Dead S01E02 HDTV XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear The Walking Dead S01E02 720p HDTV x264-KILLERS
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E02.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E02.720p.HDTV.x264-KILLERS[EtHD]
	Download ->  [torrent9]           Seed: 114 File: Fear The Walking Dead S01E02 FRENCH HDTV
	[+] fear.the.walking.dead S01E03
[torrent9]           Seed: 102 File: Fear The Walking Dead S01E03 FRENCH HDTV
[torrent9]           Seed:  16 File: Fear The Walking Dead S01E03 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  22 File: Fear The Walking Dead S01E03 VOSTFR HDTV
[torrent9]           Seed:   8 File: Fear The Walking Dead S01E03 VOSTFR BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S01E03 720p HDTV x264-KILLERS
[1337x]              Seed:   0 File: Fear The Walking Dead S01e03[BDmux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng]By GiuseppeTnT.Littleli...
[1337x]              Seed:   0 File: Fear The Walking Dead S01E03 HDTV x264 KILLERS
[1337x]              Seed:   0 File: Fear the Walking Dead S01E03 1080p WEB DL DD5 1 H 264 NTb DUAL RK
[1337x]              Seed:   0 File: Fear The Walking Dead S01E03 The Dog 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear The Walking Dead S01E03 The Dog 720p Dual
[1337x]              Seed:   0 File: Fear the Walking Dead S01e03, [XviD - Eng Mp3 - Sub Ita Eng] DLRip
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E03.Xvid-AJAXEN
[1337x]              Seed:   0 File: Fear The Walking Dead S01E03 HDTV XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E03.720p.HDTV.x264-KILLERS[EtHD]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E03.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Fear The Walking Dead S01E03 720p HDTV x264-KILLERS
	Download ->  [torrent9]           Seed: 102 File: Fear The Walking Dead S01E03 FRENCH HDTV
	[+] fear.the.walking.dead S01E04
[torrent9]           Seed:  97 File: Fear The Walking Dead S01E04 FRENCH HDTV
[torrent9]           Seed:   1 File: Fear The Walking Dead S01E04 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  23 File: Fear The Walking Dead S01E04 VOSTFR HDTV
[torrent9]           Seed:   8 File: Fear The Walking Dead S01E04 VOSTFR BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S01E04.Not.Fade.Away.1080p.WEB-DL.DD.5.1.H.264-SRS
[1337x]              Seed:   0 File: Fear The Walking Dead S01e04[BDmux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng]By GiuseppeTnT.Littleli...
[1337x]              Seed:   0 File: FileTracker pl Fear The Walking Dead S01E04 wilu75
[1337x]              Seed:   0 File: Fear the Walking Dead S01E04 rus LostFilm TV
[1337x]              Seed:   0 File: Fear The Walking Dead S01E04 Not Fade Away 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear The Walking Dead S01E04 Not Fade Away 720p
[1337x]              Seed:   0 File: Fear the Walking Dead S01e04, [XviD - Eng Mp3 - Sub Ita Eng] WEB-DLRip [TNT Village]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E04.Xvid-AJAXEN
[1337x]              Seed:   0 File: Fear The Walking Dead S01E04 HDTV XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear The Walking Dead S01E04 720p HDTV x264-KILLERS
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E04.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E04.720p.HDTV.x264-KILLERS[EtHD]
	Download ->  [torrent9]           Seed:  97 File: Fear The Walking Dead S01E04 FRENCH HDTV
	[+] fear.the.walking.dead S01E05
[torrent9]           Seed:  97 File: Fear The Walking Dead S01E05 FRENCH HDTV
[torrent9]           Seed:  22 File: Fear The Walking Dead S01E05 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  21 File: Fear The Walking Dead S01E05 VOSTFR HDTV
[torrent9]           Seed:   9 File: Fear The Walking Dead S01E05 VOSTFR BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S01E05 HDTV x264 KILLERS
[1337x]              Seed:   0 File: Fear The Walking Dead S01E05 HDTV x264 KILLERS ettv
[1337x]              Seed:   0 File: Fear The Walking Dead S01E05 Cobalt 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear The Walking Dead S01E05 Cobalt 720p Dual
[1337x]              Seed:   0 File: Fear the Walking Dead S01e05, [XviD - Eng Mp3 - Sub Ita Eng] WEB-DLRip [TNT Village]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E05.Xvid-AJAXEN
[1337x]              Seed:   0 File: Fear The Walking Dead S01E05 HDTV XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear The Walking Dead S01E05 720p HDTV x264-KILLERS
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E05.720p.HDTV.x264-KILLERS[EtHD]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E05.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed:  97 File: Fear The Walking Dead S01E05 FRENCH HDTV
	[+] fear.the.walking.dead S01E06
[torrent9]           Seed:  96 File: Fear The Walking Dead S01E06 FINAL FRENCH HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S01E06 FINAL FRENCH BluRay 720p HDTV
[torrent9]           Seed:  26 File: Fear The Walking Dead S01E06 FINAL VOSTFR HDTV
[torrent9]           Seed:   7 File: Fear The Walking Dead S01E06 FINAL VOSTFR BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S01e06[BDmux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng]By GiuseppeTnT.Littleli...
[1337x]              Seed:   0 File: Fear The Walking Dead S01E06 720p HDTV x264 KILLERS
[1337x]              Seed:   0 File: Fear The Walking Dead S01E06 The Good Man 720p Blu-Ray Dual
[1337x]              Seed:   0 File: Fear the Walking Dead S01e06, [XviD - Eng Mp3 - Sub Ita Eng] WEB-DLRip Final Season
[1337x]              Seed:   0 File: Fear The Walking Dead S01E06 The Good Man 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E06.Xvid-AJAXEN
[1337x]              Seed:   0 File: Fear The Walking Dead S01E06 HDTV XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E06.720p.HDTV.x264-KILLERS[EtHD]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S01E06.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed:  96 File: Fear The Walking Dead S01E06 FINAL FRENCH HDTV
	[+] fear.the.walking.dead S01E07
	[+] fear.the.walking.dead S02E01
[torrent9]           Seed: 108 File: Fear The Walking Dead S02E01 FRENCH HDTV
[torrent9]           Seed:  16 File: Fear The Walking Dead S02E01 VOSTFR HDTV
[torrent9]           Seed:   9 File: Fear The Walking Dead S02E01 VOSTFR BluRay 720p HDTV
[torrent9]           Seed:  17 File: Fear The Walking Dead S02E01 FRENCH BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S02E01 1080p WEBDL DD5 1 x265 opus bluury
[1337x]              Seed:   0 File: Fear The Walking Dead S02e01-07, [Mux - XviD - Ita Eng Mp3 - Sub Ita Eng] WEB-DLRip by sp_54321
[1337x]              Seed:   0 File: Fear the Walking Dead S02E01 Monster 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear The Walking Dead S02e01[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT Little...
[1337x]              Seed:   0 File: Fear The Walking Dead S02E01 SWESUB 720p HDTV x264
[1337x]              Seed:   0 File: FileTracker pl Fear The Walking Dead S02E01 wilu75
[1337x]              Seed:   0 File: fear the walking dead s02e01 1080p web dl 6ch hevc x265 rmteam mkv
[1337x]              Seed:   0 File: ELECTRO TORRENT PL Fear The Walking Dead S02E01 PL SUBBED HDTV XviD KiT
[1337x]              Seed:   0 File: Fear The Walking Dead S02E01 480p 232mb HDTV x264 Monster 11 Apr 2016
[1337x]              Seed:   0 File: fear the walking dead s02e01 720p hdtv hevc x265 rmteam mkv
[1337x]              Seed:   0 File: Fear The Walking Dead S02E01 HDTV x264 KILLERS eztv mkv
[1337x]              Seed:   0 File: Fear The Walking Dead S02E01 720p HDTV x265 ShAaNiG mkv
[1337x]              Seed:   0 File: Fear The Walking Dead S02E01 720p HDTV x264 SVA eztv mkv
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E01.WEB-DL.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear The Walking Dead S02E01 HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S02E01.720p.WEB-DL.x264-FUM[ettv]
[1337x]              Seed:   0 File: Fear The Walking Dead S02E01 HDTV XviD-AFG
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S02E01.HDTV.x264-KILLERS
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S02E01.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed: 108 File: Fear The Walking Dead S02E01 FRENCH HDTV
	[+] fear.the.walking.dead S02E02
[torrent9]           Seed:  92 File: Fear The Walking Dead S02E02 FRENCH HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S02E02 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  24 File: Fear The Walking Dead S02E02 VOSTFR HDTV
[torrent9]           Seed:  12 File: Fear The Walking Dead S02E02 VOSTFR BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S02E02 1080p WEBDL DD5 1 x265 opus bluury
[1337x]              Seed:   0 File: Fear the Walking Dead S02E02 We All Fall Down 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear The Walking Dead S02e02 Repack[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT...
[1337x]              Seed:   0 File: Fear The Walking Dead S02e02[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT Little...
[1337x]              Seed:   0 File: Fear the Walking Dead S02E02 We All Fall Down 1080p WEB DL H 264 DD5 1 Napisy PL
[1337x]              Seed:   0 File: Fear The Walking Dead S02E02 HDTV x264 KILLERS
[1337x]              Seed:   0 File: Fear The Walking Dead s02e02 WEBDLRip NewStudio TV
[1337x]              Seed:   0 File: Fear The Walking Dead S02E02 720p HDTV x264 AVS eztv mkv
[1337x]              Seed:   0 File: Fear The Walking Dead S02E02 720p HDTV x265 ShAaNiG mkv
[1337x]              Seed:   0 File: Fear The Walking Dead S02E02 HQ480p 280mb hdtv x264 We All Fall Down 18 Apr 2016
[1337x]              Seed:   0 File: Fear The Walking Dead S02E02 HDTV x264 KILLERS eztv mkv
[1337x]              Seed:   0 File: Fear The Walking Dead S02E02 HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Fear The Walking Dead S02E02 720p HDTV x264 AVS rarbg
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E02.720p.WEB-DL.H.264-NTb[ettv]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S02E02.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear The Walking Dead S02E02 1080p HDTV X264-DIMENSION
[1337x]              Seed:   0 File: Fear The Walking Dead S02E02 HDTV XviD-AFG
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S02E02.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed:  92 File: Fear The Walking Dead S02E02 FRENCH HDTV
	[+] fear.the.walking.dead S02E03
[torrent9]           Seed: 110 File: Fear The Walking Dead S02E03 FRENCH HDTV
[torrent9]           Seed:  14 File: Fear The Walking Dead S02E03 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S02E03 VOSTFR HDTV
[torrent9]           Seed:  13 File: Fear The Walking Dead S02E03 VOSTFR BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S02E03 1080p WEBDL DD5 1 x265 opus bluury
[1337x]              Seed:   0 File: Fear the Walking Dead S02E03 Ouroboros 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear The Walking Dead S02E03 HDTV XviD AFG Pawulon
[1337x]              Seed:   0 File: Fear the Walking Dead S02E03 Ouroboros 1080p WEB DL H 264 DD5 1 Napisy PL
[1337x]              Seed:   0 File: Fear the Walking Dead S02E03 HDTV x264 KILLERS
[1337x]              Seed:   0 File: Fear The Walking Dead s02e03 WEBDLRip NewStudio TV
[1337x]              Seed:   0 File: Fear the Walking Dead S02E03 720p HDTV x264 SVA
[1337x]              Seed:   0 File: Fear the Walking Dead S02E03 HDTV x264 KILLERS eztv mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E03 Ouroboros 720p WEB-DL 325MB - MkvCage
[1337x]              Seed:   0 File: Fear the Walking Dead S02E03 HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E03.720p.WEB-DL.x264-FUM[ettv]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S02E03.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear the Walking Dead S02E03 720p HDTV 350MB - MkvCage
[1337x]              Seed:   0 File: Fear the Walking Dead S02E03 HDTV XviD-AFG
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E03.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed: 110 File: Fear The Walking Dead S02E03 FRENCH HDTV
	[+] fear.the.walking.dead S02E04
[torrent9]           Seed:  86 File: Fear The Walking Dead S02E04 FRENCH HDTV
[torrent9]           Seed:  22 File: Fear The Walking Dead S02E04 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S02E04 VOSTFR HDTV
[torrent9]           Seed:  13 File: Fear The Walking Dead S02E04 VOSTFR BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S02E04 1080p WEBDL DD5 1 x265 aac bluury
[1337x]              Seed:   0 File: Fear The Walking Dead S02E04 1080p WEBDL DD5 1 x265 opus bluury
[1337x]              Seed:   0 File: Fear the Walking Dead S02E04 Blood in the Streets 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear The Walking Dead S02e04[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT Little...
[1337x]              Seed:   0 File: Fear the Walking Dead S02E04 HDTV x264 FUM eztv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E04 PROPER 720p HDTV x264 KILLERS
[1337x]              Seed:   0 File: Fear the Walking Dead S02E04 HDTV x264 FLEET
[1337x]              Seed:   0 File: FileTracker pl Fear The Walking Dead S02E04 wilu75
[1337x]              Seed:   0 File: Fear the Walking Dead S02E04 PROPER HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Fear the Walking Dead S02E04 PROPER 720p HDTV x265 ShAaNiG mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E04 HDTV x264 FLEET eztv mkv
[1337x]              Seed:   0 File: Fear The Walking Dead S02E04 720p WEB DL DD5 1 H264 RARBG
[1337x]              Seed:   0 File: Fear the Walking Dead S02E04 HDTV x264 FLEET rarbg
[1337x]              Seed:   0 File: Fear the Walking Dead S02E04 PROPER 720p HDTV x264 KILLERS VTV mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E04 720p WEB-DL HEVC 200MB - MkvCage
[1337x]              Seed:   0 File: Fear the Walking Dead S02E04 PROPER 720p HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E04.PROPER.HDTV.x264-KILLERS
[1337x]              Seed:   0 File: Fear the Walking Dead S02E04 PROPER 720p HDTV HEVC 200MB - MkvCage
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E04.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E04.HDTV.x264-FUM[ettv]
	Download ->  [torrent9]           Seed:  86 File: Fear The Walking Dead S02E04 FRENCH HDTV
	[+] fear.the.walking.dead S02E05
[torrent9]           Seed:  94 File: Fear The Walking Dead S02E05 FRENCH HDTV
[torrent9]           Seed:  22 File: Fear The Walking Dead S02E05 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  16 File: Fear The Walking Dead S02E05 VOSTFR HDTV
[torrent9]           Seed:  15 File: Fear The Walking Dead S02E05 VOSTFR BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S02E05 1080p WEBDL DD5 1 x265 opus bluury
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 Captive 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 Captive 1080p DD5 1 x265 EmEm
[1337x]              Seed:   0 File: FileTracker pl Fear The Walking Dead S02E05 wilu75
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 SWESUB 720p HDTV x264
[1337x]              Seed:   0 File: Fear The Walking Dead S02E05 1080p WEB DL HEVC DD5 1 x265 mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 HDTV x264 FLEET
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 720p HDTV x264 AVS
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 720p HDTV x265 ShAaNiG mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 HDTV x264 FUM eztv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 720p HDTV x264 AVS eztv mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 HDTV x264 FLEET rarbg
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 720p HDTV x264 AVS rarbg
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 720p WEB-DL HEVC 200MB - MkvCage
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 720p WEB-DL 320MB - MkvCage
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S02E05.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E05.HDTV.x264-FUM[ettv]
[1337x]              Seed:   0 File: Fear the Walking Dead S02E05 HDTV XviD-AFG
	Download ->  [torrent9]           Seed:  94 File: Fear The Walking Dead S02E05 FRENCH HDTV
	[+] fear.the.walking.dead S02E06
[torrent9]           Seed:  88 File: Fear The Walking Dead S02E06 FRENCH HDTV
[torrent9]           Seed:  12 File: Fear The Walking Dead S02E06 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  27 File: Fear The Walking Dead S02E06 VOSTFR HDTV
[torrent9]           Seed:  13 File: Fear The Walking Dead S02E06 VOSTFR BluRay 720p HDTV
[1337x]              Seed:  30 File: Fear The Walking Dead S02e06[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT Little
[1337x]              Seed:   0 File: Fear The Walking Dead S02E06 1080p WEBDL DD5 1 x265 opus bluury
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E06.720p.HDTV.x264.CLEANED.mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E06 Sicut Cervus 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: FileTracker pl Fear The Walking Dead S02E06 wilu75
[1337x]              Seed:   0 File: Fear the Walking Dead S02E06 720p HDTV x264 AVS
[1337x]              Seed:   0 File: Fear The Walking Dead S02E06 720p HDTV x265 ShAaNiG mkv
[1337x]              Seed:   0 File: Fear The Walking Dead S02E06 HDTV x264 FUM eztv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E06 HDTV x264 FLEET eztv mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E06 720p HDTV x264 AVS eztv mkv
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S02E06.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S02E06.HDTV.x264-FUM[ettv]
[1337x]              Seed:   0 File: Fear The Walking Dead S02E06 1080p HDTV X264-DIMENSION
[1337x]              Seed:   0 File: Fear the Walking Dead S02E06 720p WEB-DL HEVC 215MB - MkvCage
[1337x]              Seed:   0 File: Fear the Walking Dead S02E06 720p HDTV x264-AVS
[1337x]              Seed:   0 File: Fear the Walking Dead S02E06 HDTV x264-FLEET
[1337x]              Seed:   0 File: Fear the Walking Dead S02E06 HDTV XviD-AFG
	Download ->  [torrent9]           Seed:  88 File: Fear The Walking Dead S02E06 FRENCH HDTV
	[+] fear.the.walking.dead S02E07
[torrent9]           Seed: 103 File: Fear The Walking Dead S02E07 FRENCH HDTV
[torrent9]           Seed:   5 File: Fear The Walking Dead S02E07 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  29 File: Fear The Walking Dead S02E07 VOSTFR HDTV
[torrent9]           Seed:  10 File: Fear The Walking Dead S02E07 VOSTFR BluRay 720p HDTV
[1337x]              Seed:  24 File: fear the walking dead s02e07 shiva 1080p web dl 6ch hevc x265 rmteam mkv
[1337x]              Seed:   0 File: Fear The Walking Dead S02E07 1080p WEBDL DD5 1 x265 opus bluury
[1337x]              Seed:   0 File: Fear the Walking Dead S02E07 Shiva 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: FileTracker pl Fear The Walking Dead S02E07 wilu75
[1337x]              Seed:   0 File: FileTracker pl Fear The Walking Dead S02E07 wilu75
[1337x]              Seed:   0 File: Fear The Walking Dead s02e07 WEBDLRip NewStudio TV
[1337x]              Seed:   0 File: Fear the Walking Dead S02E07 720p HDTV x264 FLEET eztv mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E07 720p HDTV x264 AVS
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S02E07.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear The Walking Dead S02E07 720p HDTV x265 ShAaNiG mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E07 720p HDTV x264 AVS VTV mkv
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E07.1080p.HDTV.X264-DIMENSION [WOP]
[1337x]              Seed:   0 File: Fear the Walking Dead S02E07 HDTV x264 FLEET eztv mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E07 HDTV x264 FLEET mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E07 720p WEB-DL HEVC 200MB - MkvCage
[1337x]              Seed:   0 File: Fear the Walking Dead S02E07 720p HDTV x264 AVS eztv mkv
[1337x]              Seed:   0 File: Fear the Walking Dead S02E07 720p HDTV x264 AVS rarbg
[1337x]              Seed:   0 File: Fear the Walking Dead S02E07 720p HDTV x264 FLEET rarbg
[1337x]              Seed:   0 File: Fear the Walking Dead S02E07 HDTV x264 FLEET rarbg
[1337x]              Seed:   0 File: Fear the Walking Dead S02E07 720p HDTV x264-FLEET [WOP]
	Download ->  [torrent9]           Seed: 103 File: Fear The Walking Dead S02E07 FRENCH HDTV
	[+] fear.the.walking.dead S02E08
[torrent9]           Seed:  23 File: Fear The Walking Dead S02E08 VOSTFR HDTV
[torrent9]           Seed:   8 File: Fear The Walking Dead S02E08 VOSTFR BluRay 720p HDTV
[torrent9]           Seed:  70 File: Fear The Walking Dead S02E08 FRENCH HDTV
[torrent9]           Seed:  16 File: Fear The Walking Dead S02E08 FRENCH BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E08.720p.ARSUB.HDTV.x264.AAC-SHOWSCEN &#217;&#133;&#216;&#170;&#216;&#177;&#216;&#172;&#217;&#133;&#216;&#169;
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E08.720p.WEB-DL.DD5.1.H264-RARBG
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E08.1080p.HDTV.x264-BRISK
[1337x]              Seed:   0 File: Fear The Walking Dead S02e08-15 [Mux - 1080p - H264 - Ita Mp3 Eng Ac3 5.1 - Sub Ita Eng] WEB-DLMux b...
[1337x]              Seed:   0 File: Fear The Walking Dead S02e08-15 [Mux - XviD - Ita Eng Mp3 - Sub Ita Eng] WEB-DLMux by sp_54321
[1337x]              Seed:   0 File: Fear The Walking Dead S02e08, [720p - H264 - Eng Ac3 5.1 - Sub Eng Ita] WEB-DLRip by sp_54321
[1337x]              Seed:   0 File: Fear The Walking Dead S02e08-09, [Mux - XviD - Ita Eng Mp3 - Sub Ita Eng] WEB-DLRip by sp_54321
[1337x]              Seed:   0 File: Fear The Walking Dead S02e08[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT Little
[1337x]              Seed:   0 File: Fear the Walking Dead S02E08 Grotesque 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear.The.Walking.Dead.S02E08.WEB-DL.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E08.WEB-DL.x264-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E08.720p.WEB-DL.x264-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E08.1080p.HDTV.x264-BRISK[PRiME]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E08.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E08.720p.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E08.720p.HDTV.x264-AVS[PRiME]
	Download ->  [torrent9]           Seed:  70 File: Fear The Walking Dead S02E08 FRENCH HDTV
	[+] fear.the.walking.dead S02E09
[torrent9]           Seed:  22 File: Fear The Walking Dead S02E09 VOSTFR HDTV
[torrent9]           Seed:   9 File: Fear The Walking Dead S02E09 VOSTFR BluRay 720p HDTV
[torrent9]           Seed:  90 File: Fear The Walking Dead S02E09 FRENCH HDTV
[torrent9]           Seed:  21 File: Fear The Walking Dead S02E09 FRENCH BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E09.1080p.WEB-DL.DD5.1.H264-RARBG
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E09.720p.HDTV.x264-AVS
[1337x]              Seed:   0 File: Fear The Walking Dead S02e09, [720p - H264 - Eng Ac3 5.1 - Sub Eng Ita] WEB-DLRip by sp_54321
[1337x]              Seed:   0 File: Fear The Walking Dead S02e09[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT Little
[1337x]              Seed:   0 File: Fear the Walking Dead S02E09 Los Muertos 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E09.1080p.HDTV.x264-BRISK[PRiME]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E09.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E09.HDTV.x264-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E09.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E09.720p.HDTV.x264-AVS[PRiME]
	Download ->  [torrent9]           Seed:  90 File: Fear The Walking Dead S02E09 FRENCH HDTV
	[+] fear.the.walking.dead S02E10
[torrent9]           Seed:  21 File: Fear The Walking Dead S02E10 VOSTFR HDTV
[torrent9]           Seed:   7 File: Fear The Walking Dead S02E10 VOSTFR BluRay 720p HDTV
[torrent9]           Seed:  63 File: Fear The Walking Dead S02E10 FRENCH HDTV
[torrent9]           Seed:  15 File: Fear The Walking Dead S02E10 FRENCH BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E10.720p.ARSUB.HC.HDTV.x264.AAC-SHOWSCEN &#217;&#133;&#216;&#170;&#216;&#177;&#216;&#172;&#217;&#133;&#216;&#169;
[1337x]              Seed:   0 File: Fear The Walking Dead S02e10 REPACK [Mux - XviD - Ita Eng Mp3 - Sub Ita Eng] WEB-DLRip by sp_54321
[1337x]              Seed:   0 File: Fear The Walking Dead S02e10[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT Little
[1337x]              Seed:   0 File: Fear The Walking Dead S02e10, [720p - H264 - Eng Ac3 5.1 - Sub Eng Ita] WEB-DLRip by sp_54321
[1337x]              Seed:   0 File: Fear the Walking Dead S02E10 Do Not Disturb 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E10.1080p.HDTV.x264-BRISK[PRiME]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E10.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E10.HDTV.x264-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E10.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E10.720p.HDTV.x264-AVS[PRiME]
	Download ->  [torrent9]           Seed:  63 File: Fear The Walking Dead S02E10 FRENCH HDTV
	[+] fear.the.walking.dead S02E11
[torrent9]           Seed:  24 File: Fear The Walking Dead S02E11 VOSTFR HDTV
[torrent9]           Seed:  11 File: Fear The Walking Dead S02E11 VOSTFR BluRay 720p HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S02E11 FRENCH HDTV
[torrent9]           Seed:  16 File: Fear The Walking Dead S02E11 FRENCH BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S02e11, [720p - H264 - Eng Ac3 5.1 - Sub Eng Ita] WEB-DLRip
[1337x]              Seed:   0 File: Fear The Walking Dead S02e11 [Mux - XviD - Ita Eng Mp3 - Sub Ita Eng] WEB-DLRip by sp_54321
[1337x]              Seed:   0 File: Fear The Walking Dead S02e11[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT Little
[1337x]              Seed:   0 File: Fear the Walking Dead S02E11 Pablo and Jessica 720p WebRip EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E11.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear the Walking Dead S02E11 PROPER 720p HDTV x264-KILLERS
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E11.PROPER.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E11.PROPER.720p.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E11.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E11.720p.HDTV.x264-FLEET[PRiME]
	Download ->  [torrent9]           Seed:  24 File: Fear The Walking Dead S02E11 VOSTFR HDTV
	[+] fear.the.walking.dead S02E12
[torrent9]           Seed:  72 File: Fear The Walking Dead S02E12 FRENCH HDTV
[torrent9]           Seed:  16 File: Fear The Walking Dead S02E12 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  17 File: Fear The Walking Dead S02E12 VOSTFR HDTV
[torrent9]           Seed:   9 File: Fear The Walking Dead S02E12 VOSTFR BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E12.HDTV.x264-DEFiNE[eztv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E12.HDTV.x264-FUM[eztv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E12.720p.HDTV.x264-AVS[eztv]
[1337x]              Seed:   0 File: Fear The Walking Dead S02e12 Repack[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT...
[1337x]              Seed:   0 File: Fear The Walking Dead S02e12, [Mux - XviD - Ita Eng Mp3 - Sub Ita Eng] WEB-DLRip by sp_54321
[1337x]              Seed:   0 File: Fear The Walking Dead S02e12, [720p - H264 - Eng Ac3 5.1 - Sub Eng Ita] WEB-DLRip
[1337x]              Seed:   0 File: Fear the Walking Dead S02E12 Pillar of Salt 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E12.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E12.HDTV.x264-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E12.720p.HDTV.x264-AVS[PRiME]
	Download ->  [torrent9]           Seed:  72 File: Fear The Walking Dead S02E12 FRENCH HDTV
	[+] fear.the.walking.dead S02E13
[torrent9]           Seed:  96 File: Fear The Walking Dead S02E13 FRENCH HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S02E13 FRENCH BluRay 720p HDTV
[torrent9]           Seed:  33 File: Fear The Walking Dead S02E13 VOSTFR HDTV
[torrent9]           Seed:   7 File: Fear The Walking Dead S02E13 VOSTFR BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S02e13, [Mux - XviD - Ita Eng Mp3 - Sub Ita Eng] WEB-DLMux by sp_54321
[1337x]              Seed:   0 File: Fear The Walking Dead S02e13[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT Little
[1337x]              Seed:   0 File: Fear The Walking Dead S02e13, [720p - H264 - Eng Ac3 5.1 - Sub Eng Ita] WEB-DLRip
[1337x]              Seed:   0 File: Fear the Walking Dead S02E13 Date of Death 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E13.WEB-DL.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear the Walking Dead S02E13 720p HDTV 325MB - NBY
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E13.REPACK.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E13.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E13.720p.HDTV.x264-AVS[PRiME]
	Download ->  [torrent9]           Seed:  96 File: Fear The Walking Dead S02E13 FRENCH HDTV
	[+] fear.the.walking.dead S02E14
[torrent9]           Seed:  31 File: Fear The Walking Dead S02E14 VOSTFR HDTV
[torrent9]           Seed:  18 File: Fear The Walking Dead S02E14 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 112 File: Fear The Walking Dead S02E14 FRENCH HDTV
[torrent9]           Seed:  22 File: Fear The Walking Dead S02E14 FRENCH BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S02e14[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT Little
[1337x]              Seed:   0 File: Fear the Walking Dead S02E14 Wrath 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E14.WEB-DL.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E14.PROPER.720p.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E14.PROPER.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E14.720p.HDTV.x264-FLEET[PRiME]
	Download ->  [torrent9]           Seed: 112 File: Fear The Walking Dead S02E14 FRENCH HDTV
	[+] fear.the.walking.dead S02E15
[torrent9]           Seed:  50 File: Fear The Walking Dead S02E15 FINAL VOSTFR HDTV
[torrent9]           Seed:  20 File: Fear The Walking Dead S02E15 FINAL VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 119 File: Fear The Walking Dead S02E15 FINAL FRENCH HDTV
[torrent9]           Seed:  44 File: Fear The Walking Dead S02E15 FINAL FRENCH BluRay 720p HDTV
[1337x]              Seed:   0 File: Fear The Walking Dead S02e15[Mux - 720p - H264 - Ita Eng Ac3 - Sub Ita Eng] DLMux GiuseppeTnT Little
[1337x]              Seed:   0 File: Fear the Walking Dead S02E15 North 720p WEB-DL EN-SUB x264-[MULVAcoded]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E15.WEB-DL.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E15.HDTV.x264-FUM[ettv]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E15.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Fear.the.Walking.Dead.S02E15.720p.HDTV.x264-AVS[PRiME]
	Download ->  [torrent9]           Seed: 119 File: Fear The Walking Dead S02E15 FINAL FRENCH HDTV
	[+] fear.the.walking.dead S02E16
	[+] fear.the.walking.dead S03E01
[torrent9]           Seed: 323 File: Fear The Walking Dead S03E01 FRENCH HDTV
[torrent9]           Seed:  74 File: Fear The Walking Dead S03E01 FRENCH BluRay 720p HDTV
[torrent9]           Seed: 148 File: Fear The Walking Dead S03E01 VOSTFR HDTV
[torrent9]           Seed:  74 File: Fear The Walking Dead S03E01 VOSTFR BluRay 720p HDTV
[nextorrent]         Seed: 796 File: Fear The Walking Dead S03E01 FRENCH HDTV
[nextorrent]         Seed: 434 File: Fear The Walking Dead S03E01 VOSTFR HDTV
[1337x]              Seed: 1136 File: Fear.the.Walking.Dead.S03E01.HDTV.x264-SVA
[1337x]              Seed: 1006 File: Fear.the.Walking.Dead.S03E01.HDTV.x264-SVA[eztv]
[1337x]              Seed: 653 File: Fear.the.Walking.Dead.S03E01.HDTV.x264-SVA[ettv]
[1337x]              Seed: 367 File: Fear.the.Walking.Dead.S03E01.720p.HDTV.x264-AVS[eztv]
[1337x]              Seed: 344 File: Fear.the.Walking.Dead.S03E01.720p.HDTV.x264-AVS[ettv]
[1337x]              Seed: 270 File: Fear.The.Walking.Dead.S03E01.CONVERT.720p.WEB.h264-TBS
[1337x]              Seed: 176 File: Fear.the.Walking.Dead.S03E01.1080p.WEB-DL.DD5.1.H264-RARBG
[1337x]              Seed: 154 File: Fear.the.Walking.Dead.S03E01.WEB-DL.x264-RARBG
[1337x]              Seed: 109 File: Fear.The.Walking.Dead.S03E01.CONVERT.WEB.h264-TBS
[1337x]              Seed: 101 File: Fear.The.Walking.Dead.S03E01.CONVERT.WEB.h264-TBS[eztv]
[1337x]              Seed:  76 File: Fear.the.Walking.Dead.S03E01.720p.WEB-DL.DD5.1.H264-RARBG
[1337x]              Seed:  32 File: Fear.The.Walking.Dead.S03E01.CONVERT.720p.WEB.h264-TBS[eztv]
[1337x]              Seed:  23 File: Fear.The.Walking.Dead.S03E01.PROPER.1080p.WEBRip.x264-iNSPiRiT[rarbg]-[1337x]
[1337x]              Seed:  20 File: Fear.the.Walking.Dead.S03E01.720p.AMZN.WEBRip.DD5.1.x264-VLAD [SD]
[1337x]              Seed:  19 File: Fear the Walking Dead S03E01 720p HDTV HEVC x265-RMTeam (224MB)
[1337x]              Seed:  14 File: Fear the Walking Dead S03E01 720p WEB-DL 380MB - MkvCage
	Download ->  [1337x]              Seed: 1136 File: Fear.the.Walking.Dead.S03E01.HDTV.x264-SVA
	[+] fear.the.walking.dead S03E02
[torrent9]           Seed: 318 File: Fear The Walking Dead S03E02 FRENCH HDTV
[torrent9]           Seed:  68 File: Fear The Walking Dead S03E02 FRENCH BluRay 720p HDTV
[torrent9]           Seed: 121 File: Fear The Walking Dead S03E02 VOSTFR HDTV
[torrent9]           Seed:  61 File: Fear The Walking Dead S03E02 VOSTFR BluRay 720p HDTV
[nextorrent]         Seed: 717 File: Fear The Walking Dead S03E02 FRENCH HDTV
[nextorrent]         Seed: 368 File: Fear The Walking Dead S03E02 VOSTFR HDTV
[1337x]              Seed: 1232 File: Fear.the.Walking.Dead.S03E02.HDTV.x264-SVA
[1337x]              Seed: 885 File: Fear.the.Walking.Dead.S03E02.HDTV.x264-SVA[eztv]
[1337x]              Seed: 541 File: Fear.the.Walking.Dead.S03E02.720p.HDTV.x264-AVS
[1337x]              Seed: 538 File: Fear.the.Walking.Dead.S03E02.HDTV.x264-SVA[ettv]
[1337x]              Seed: 329 File: Fear.the.Walking.Dead.S03E02.720p.HDTV.x264-AVS[ettv]
[1337x]              Seed: 321 File: Fear.the.Walking.Dead.S03E02.720p.HDTV.x264-AVS[eztv]
[1337x]              Seed: 189 File: Fear.The.Walking.Dead.S03E02.CONVERT.1080p.WEB.h264-TBS
[1337x]              Seed: 175 File: Fear.the.Walking.Dead.S03E02.1080p.WEB-DL.DD5.1.H264-RARBG
[1337x]              Seed: 170 File: Fear.the.Walking.Dead.S03E02.WEB-DL.x264-RARBG
[1337x]              Seed: 169 File: Fear.The.Walking.Dead.S03E02.CONVERT.720p.WEB.h264-TBS
[1337x]              Seed: 123 File: Fear.The.Walking.Dead.S03E02.PROPER.1080p.WEBRip.x264-iNSPiRiT[rarbg]-[1337x]
[1337x]              Seed: 108 File: Fear.The.Walking.Dead.S03E02.CONVERT.WEB.h264-TBS
[1337x]              Seed:  96 File: Fear.The.Walking.Dead.S03E02.CONVERT.WEB.h264-TBS[eztv]
[1337x]              Seed:  71 File: Fear.The.Walking.Dead.S03E02.CONVERT.720p.WEB.h264-TBS[eztv]
[1337x]              Seed:  69 File: Fear.the.Walking.Dead.S03E02.720p.WEB-DL.DD5.1.H264-RARBG
[1337x]              Seed:  18 File: Fear the Walking Dead S03E02 720p HDTV HEVC x265-RMTeam (208MB)
[1337x]              Seed:  16 File: Fear the Walking Dead S03E02 720p WEB-DL 390MB - MkvCage
	Download ->  [1337x]              Seed: 1232 File: Fear.the.Walking.Dead.S03E02.HDTV.x264-SVA
	[+] fear.the.walking.dead S03E03
[torrent9]           Seed: 123 File: Fear The Walking Dead S03E03 VOSTFR HDTV
[torrent9]           Seed:  55 File: Fear The Walking Dead S03E03 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 357 File: Fear The Walking Dead S03E03 FRENCH HDTV
[torrent9]           Seed: 103 File: Fear The Walking Dead S03E03 FRENCH BluRay 720p HDTV
[nextorrent]         Seed: 366 File: Fear The Walking Dead S03E03 VOSTFR HDTV
[nextorrent]         Seed: 893 File: Fear The Walking Dead S03E03 FRENCH HDTV
[1337x]              Seed: 1353 File: Fear.the.Walking.Dead.S03E03.HDTV.x264-SVA[ettv]
[1337x]              Seed: 634 File: Fear.the.Walking.Dead.S03E03.HDTV.x264-SVA[eztv]
[1337x]              Seed: 581 File: Fear.the.Walking.Dead.S03E03.720p.HDTV.x264-AVS [rarbg] [SD]
[1337x]              Seed: 540 File: Fear.the.Walking.Dead.S03E03.HDTV.x264-SVA [rarbg] [SD]
[1337x]              Seed: 422 File: Fear.the.Walking.Dead.S03E03.HDTV.x264-FLEET[eztv]
[1337x]              Seed: 205 File: Fear.the.Walking.Dead.S03E03.1080p.WEB-DL.DD5.1.H264-RARBG [SD]
[1337x]              Seed: 182 File: Fear.the.Walking.Dead.S03E03.720p.HDTV.x264-AVS[ettv]
[1337x]              Seed: 163 File: Fear.The.Walking.Dead.S03E03.CONVERT.1080p.WEB.h264-TBS [rarbg] [SD]
[1337x]              Seed: 162 File: Fear.the.Walking.Dead.S03E03.720p.HDTV.x264-AVS[eztv]
[1337x]              Seed: 138 File: Fear.the.Walking.Dead.S03E03.WEB-DL.x264-RARBG [SD]
[1337x]              Seed: 131 File: Fear.The.Walking.Dead.S03E03.CONVERT.720p.WEB.h264-TBS [rarbg] [SD]
[1337x]              Seed: 103 File: Fear.The.Walking.Dead.S03E03.CONVERT.WEB.h264-TBS[eztv]
[1337x]              Seed:  90 File: Fear.the.Walking.Dead.S03E03.WEBRip.x264-RARBG
[1337x]              Seed:  90 File: Fear.The.Walking.Dead.S03E03.CONVERT.WEB.h264-TBS [rarbg] [SD]
[1337x]              Seed:  86 File: Fear.the.Walking.Dead.S03E03.720p.HDTV.x264-FLEET [rarbg] [SD]
[1337x]              Seed:  75 File: Fear.the.Walking.Dead.S03E03.720p.WEB-DL.DD5.1.H264-RARBG [SD]
[1337x]              Seed:  53 File: Fear.the.Walking.Dead.S03E03.1080p.AMZN.WEBRip.DD5.1.x264-VLAD[rarbg]
[1337x]              Seed:  41 File: Fear.the.Walking.Dead.S03E03.HDTV.x264-FLEET [rarbg] [SD]
[1337x]              Seed:  38 File: Fear.the.Walking.Dead.S03E03.1080p.HDTV.x264-BRISK [rarbg] [SD]
[1337x]              Seed:  32 File: Fear.the.Walking.Dead.S03E03.720p.HDTV.x264-FLEET[eztv]
	Download ->  [1337x]              Seed: 1353 File: Fear.the.Walking.Dead.S03E03.HDTV.x264-SVA[ettv]
	[+] fear.the.walking.dead S03E04
[torrent9]           Seed: 148 File: Fear The Walking Dead S03E04 VOSTFR HDTV
[torrent9]           Seed:  81 File: Fear The Walking Dead S03E04 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 443 File: Fear The Walking Dead S03E04 FRENCH HDTV
[torrent9]           Seed: 108 File: Fear The Walking Dead S03E04 FRENCH BluRay 720p HDTV
[nextorrent]         Seed: 429 File: Fear The Walking Dead S03E04 VOSTFR HDTV
[nextorrent]         Seed: 1105 File: Fear The Walking Dead S03E04 FRENCH HDTV
[1337x]              Seed: 1768 File: Fear.the.Walking.Dead.S03E04.HDTV.x264-FLEET[eztv]
[1337x]              Seed: 810 File: Fear.the.Walking.Dead.S03E04.HDTV.x264-SVA[ettv]
[1337x]              Seed: 534 File: Fear.the.Walking.Dead.S03E04.HDTV.x264-SVA[rarbg]
[1337x]              Seed: 507 File: Fear.the.Walking.Dead.S03E04.720p.HDTV.x264-AVS[rarbg]
[1337x]              Seed: 409 File: Fear.the.Walking.Dead.S03E04.720p.HDTV.x264-FLEET[rarbg]
[1337x]              Seed: 350 File: Fear.the.Walking.Dead.S03E04.720p.HDTV.x264-FLEET[eztv]
[1337x]              Seed: 280 File: Fear.the.Walking.Dead.S03E04.HDTV.x264-SVA[eztv]
[1337x]              Seed: 190 File: Fear.the.Walking.Dead.S03E04.HDTV.x264-FLEET[rarbg]
[1337x]              Seed: 181 File: Fear.The.Walking.Dead.S03E04.1080p.WEB-DL.DD5.1.H264-RARBG
[1337x]              Seed: 146 File: Fear.The.Walking.Dead.S03E04.WEB-DL.x264-RARBG
[1337x]              Seed: 121 File: Fear.The.Walking.Dead.S03E04.CONVERT.1080p.WEB.h264-TBS [rarbg] [SD]
[1337x]              Seed:  66 File: Fear.The.Walking.Dead.S03E04.720p.WEB-DL.DD5.1.H264-RARBG
[1337x]              Seed:  55 File: Fear.the.Walking.Dead.S03E04.720p.HDTV.x264-AVS[ettv]
[1337x]              Seed:  43 File: Fear.the.Walking.Dead.S03E04.720p.HDTV.x264-AVS[eztv]
[1337x]              Seed:  22 File: Fear The Walking Dead S03E04 720p WEB-DL HEVC x265-RMTeam (199MB) &#226;&#151;&#143;Shadow&#226;&#151;&#143;
[1337x]              Seed:  12 File: Fear the Walking Dead S03E04 720p WEB-DL 335MB - MkvCage
	Download ->  [1337x]              Seed: 1768 File: Fear.the.Walking.Dead.S03E04.HDTV.x264-FLEET[eztv]
	[+] fear.the.walking.dead S03E05
[torrent9]           Seed: 240 File: Fear The Walking Dead S03E05 VOSTFR HDTV
[torrent9]           Seed: 178 File: Fear The Walking Dead S03E05 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 633 File: Fear The Walking Dead S03E05 FRENCH HDTV
[torrent9]           Seed: 230 File: Fear The Walking Dead S03E05 FRENCH BluRay 720p HDTV
[nextorrent]         Seed: 1241 File: Fear The Walking Dead S03E05 VOSTFR HDTV
[nextorrent]         Seed: 1710 File: Fear The Walking Dead S03E05 FRENCH HDTV
[1337x]              Seed: 2501 File: Fear.the.Walking.Dead.S03E05.HDTV.x264-SVA[ettv]
[1337x]              Seed: 974 File: Fear.the.Walking.Dead.S03E05.720p.HDTV.x264-AVS [rarbg] [SD]
[1337x]              Seed: 755 File: Fear.the.Walking.Dead.S03E05.HDTV.x264-SVA [rarbg] [SD]
[1337x]              Seed: 219 File: Fear.The.Walking.Dead.S03E05.1080p.WEB-DL.DD5.1.H264-RARBG
[1337x]              Seed: 214 File: Fear.The.Walking.Dead.S03E05.WEB-DL.x264-RARBG [SD]
[1337x]              Seed: 171 File: Fear.The.Walking.Dead.S03E05.CONVERT.1080p.WEB.h264-TBS [rarbg] [SD]
[1337x]              Seed:  99 File: Fear.The.Walking.Dead.S03E05.720p.WEB-DL.DD5.1.H264-RARBG
[1337x]              Seed:  93 File: Fear.the.Walking.Dead.S03E05.720p.HDTV.x264-AVS[ettv]
[1337x]              Seed:  17 File: Fear The Walking Dead S03E05 720p WEB-DL HEVC x265-RMTeam (193MB) &#226;&#151;&#143;Shadow&#226;&#151;&#143;
[1337x]              Seed:  13 File: Fear the Walking Dead S03E05 720p WEB-DL 335MB - MkvCage
[1337x]              Seed:   9 File: Fear.the.Walking.Dead.S03E05.HDTV.x264-SVA-[theAmresh]
[1337x]              Seed:   7 File: Fear.the.Walking.Dead.S03E05.720p.HDTV.x264-AVS
[1337x]              Seed:   6 File: Fear.the.Walking.Dead.S03E05.HDTV.x264-SVA
	Download ->  [1337x]              Seed: 2501 File: Fear.the.Walking.Dead.S03E05.HDTV.x264-SVA[ettv]
	[+] fear.the.walking.dead S03E06
[torrent9]           Seed: 296 File: Fear The Walking Dead S03E06 VOSTFR HDTV
[torrent9]           Seed: 230 File: Fear The Walking Dead S03E06 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 915 File: Fear The Walking Dead S03E06 FRENCH HDTV
[torrent9]           Seed: 301 File: Fear The Walking Dead S03E06 FRENCH BluRay 720p HDTV
[nextorrent]         Seed: 945 File: Fear The Walking Dead S03E06 VOSTFR HDTV
[nextorrent]         Seed: 1966 File: Fear The Walking Dead S03E06 FRENCH HDTV
[1337x]              Seed: 2117 File: Fear.the.Walking.Dead.S03E06.REPACK.HDTV.x264-SVA[eztv]
[1337x]              Seed: 506 File: Fear.the.Walking.Dead.S03E06.720p.HDTV.x264-SVA [rarbg] [SD]
[1337x]              Seed: 483 File: Fear.the.Walking.Dead.S03E06.REPACK.HDTV.x264-SVA [rarbg] [SD]
[1337x]              Seed: 366 File: Fear.the.Walking.Dead.S03E06.PROPER.720p.HDTV.x264-AVS [rarbg] [SD]
[1337x]              Seed: 318 File: Fear.the.Walking.Dead.S03E06.REPACK.HDTV.x264-SVA[ettv]
[1337x]              Seed: 266 File: Fear.the.Walking.Dead.S03E06.PROPER.720p.HDTV.x264-AVS[eztv]
[1337x]              Seed: 211 File: Fear.the.Walking.Dead.S03E06.HDTV.x264-SVA[eztv]
[1337x]              Seed: 194 File: Fear.the.Walking.Dead.S03E06.HDTV.x264-SVA [rarbg] [SD]
[1337x]              Seed: 183 File: Fear.the.Walking.Dead.S03E06.WEBRip.x264-RARBG [SD]
[1337x]              Seed: 178 File: Fear.The.Walking.Dead.S03E06.CONVERT.1080p.WEB.h264-TBS [rarbg] [SD]
[1337x]              Seed: 139 File: Fear.the.Walking.Dead.S03E06.HDTV.x264-SVA[ettv]
[1337x]              Seed:  82 File: Fear.The.Walking.Dead.S03E06.CONVERT.WEB.h264-TBS [rarbg] [SD]
[1337x]              Seed:  73 File: Fear.the.Walking.Dead.S03E06.720p.HDTV.x264-SVA[eztv]
[1337x]              Seed:  70 File: Fear.the.Walking.Dead.S03E06.720p.HDTV.x264-SVA[ettv]
[1337x]              Seed:  44 File: Fear.The.Walking.Dead.S03E06.CONVERT.720p.WEB.h264-TBS[eztv]
[1337x]              Seed:  42 File: Fear.the.Walking.Dead.S03E06.PROPER.720p.HDTV.x264-AVS[ettv]
[1337x]              Seed:  28 File: Fear.The.Walking.Dead.S03E06.CONVERT.WEB.h264-TBS[eztv]
[1337x]              Seed:  19 File: Fear the Walking Dead S03E06 720p WEB-DL HEVC x265-RMTeam (180MB) &#226;&#151;&#143;Shadow&#226;&#151;&#143;
[1337x]              Seed:  14 File: Fear.the.Walking.Dead.S03E06.720p.HDTV.x264-SVA - [LD]
[1337x]              Seed:  11 File: Fear the Walking Dead S03E06 720p WEB-DL 335MB - MkvCage
	Download ->  [1337x]              Seed: 2117 File: Fear.the.Walking.Dead.S03E06.REPACK.HDTV.x264-SVA[eztv]
	[+] fear.the.walking.dead S03E07
[torrent9]           Seed: 497 File: Fear The Walking Dead S03E07 VOSTFR HDTV
[torrent9]           Seed: 243 File: Fear The Walking Dead S03E07 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 1366 File: Fear The Walking Dead S03E07 FRENCH HDTV
[torrent9]           Seed: 407 File: Fear The Walking Dead S03E07 FRENCH BluRay 720p HDTV
[nextorrent]         Seed: 453 File: Fear The Walking Dead S03E07 VOSTFR HDTV
[nextorrent]         Seed: 2533 File: Fear The Walking Dead S03E07 FRENCH HDTV
[1337x]              Seed: 2033 File: Fear.the.Walking.Dead.S03E07.PROPER.HDTV.x264-KILLERS[eztv]
[1337x]              Seed: 1231 File: Fear.the.Walking.Dead.S03E07.PROPER.720p.HDTV.x264-KILLERS [rarbg] [SD]
[1337x]              Seed: 1113 File: Fear.the.Walking.Dead.S03E07.PROPER.HDTV.x264-KILLERS [rarbg] [SD]
[1337x]              Seed: 1029 File: Fear.the.Walking.Dead.S03E07.PROPER.HDTV.x264-KILLERS[ettv]
[1337x]              Seed: 620 File: Fear.the.Walking.Dead.S03E07.720p.HDTV.x264-FLEET [rarbg] [SD]
[1337x]              Seed: 550 File: Fear.the.Walking.Dead.S03E07.HDTV.x264-FLEET [rarbg] [SD]
[1337x]              Seed: 417 File: Fear.the.Walking.Dead.S03E07.HDTV.x264-FLEET[eztv]
[1337x]              Seed: 371 File: Fear.the.Walking.Dead.S03E07.1080p.WEB-DL.DD5.1.H264-RARBG [SD]
[1337x]              Seed: 367 File: Fear.the.Walking.Dead.S03E07.PROPER.720p.HDTV.x264-KILLERS[eztv]
[1337x]              Seed: 358 File: Fear.The.Walking.Dead.S03E07.CONVERT.1080p.WEB.h264-TBS [rarbg] [SD]
[1337x]              Seed: 331 File: Fear.the.Walking.Dead.S03E07.WEBRip.x264-RARBG [SD]
[1337x]              Seed: 242 File: Fear.the.Walking.Dead.S03E07.720p.HDTV.x264-FLEET[eztv]
[1337x]              Seed: 133 File: Fear.the.Walking.Dead.S03E07.720p.WEB-DL.DD5.1.H264-RARBG [SD]
[1337x]              Seed: 125 File: Fear.the.Walking.Dead.S03E07.WEB-DL.x264-RARBG [SD]
[1337x]              Seed: 104 File: Fear.the.Walking.Dead.S03E07.1080p.AMZN.WEBRip.DD5.1.x264-VLAD [rarbg] [SD]
[1337x]              Seed:  78 File: Fear.the.Walking.Dead.S03E07.PROPER.720p.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:  45 File: Fear.The.Walking.Dead.S03E07.1080p.HDTV.x264-BRISK [rarbg] [SD]
[1337x]              Seed:  25 File: Fear the Walking Dead S03E07 720p WEB-DL 335MB - MkvCage
[1337x]              Seed:  25 File: Fear.the.Walking.Dead.S03E07.HDTV.x264-FLEET
[1337x]              Seed:  23 File: Fear.the.Walking.Dead.S03E07.720p.HDTV.x264-FLEET
	Download ->  [nextorrent]         Seed: 2533 File: Fear The Walking Dead S03E07 FRENCH HDTV
	[+] fear.the.walking.dead S03E08
[torrent9]           Seed: 433 File: Fear The Walking Dead S03E08 VOSTFR HDTV
[torrent9]           Seed: 241 File: Fear The Walking Dead S03E08 VOSTFR BluRay 720p HDTV
[torrent9]           Seed: 1375 File: Fear The Walking Dead S03E08 FRENCH HDTV
[torrent9]           Seed: 400 File: Fear The Walking Dead S03E08 FRENCH BluRay 720p HDTV
[nextorrent]         Seed: 618 File: Fear The Walking Dead S03E08 VOSTFR HDTV
[nextorrent]         Seed: 2072 File: Fear The Walking Dead S03E08 FRENCH HDTV
[1337x]              Seed: 2626 File: Fear.the.Walking.Dead.S03E08.HDTV.x264-FLEET[eztv]
[1337x]              Seed: 849 File: Fear.the.Walking.Dead.S03E08.HDTV.x264-SVA [rarbg] [SD]
[1337x]              Seed: 672 File: Fear.the.Walking.Dead.S03E08.HDTV.x264-SVA[ettv]
[1337x]              Seed: 669 File: Fear.the.Walking.Dead.S03E08.720p.HDTV.x264-AVS [rarbg] [SD]
[1337x]              Seed: 630 File: Fear.the.Walking.Dead.S03E08.720p.HDTV.x264-FLEET [rarbg] [SD]
[1337x]              Seed: 509 File: Fear.the.Walking.Dead.S03E08.HDTV.x264-SVA[eztv]
[1337x]              Seed: 452 File: Fear.the.Walking.Dead.S03E08.720p.HDTV.x264-FLEET[eztv]
[1337x]              Seed: 418 File: Fear.the.Walking.Dead.S03E08.1080p.WEB-DL.DD5.1.H264-RARBG [SD]
[1337x]              Seed: 341 File: Fear.the.Walking.Dead.S03E08.WEBRip.x264-RARBG [SD]
[1337x]              Seed: 286 File: Fear.The.Walking.Dead.S03E08.CONVERT.1080p.WEB.h264-TBS [rarbg] [SD]
[1337x]              Seed: 232 File: Fear.the.Walking.Dead.S03E08.720p.HDTV.x264-AVS[ettv]
[1337x]              Seed: 191 File: Fear.the.Walking.Dead.S03E08.720p.WEB-DL.DD5.1.H264-RARBG [SD]
[1337x]              Seed: 184 File: Fear.the.Walking.Dead.S03E08.WEB-DL.x264-RARBG [SD]
[1337x]              Seed: 179 File: Fear.The.Walking.Dead.S03E08.CONVERT.WEB.h264-TBS [rarbg] [SD]
[1337x]              Seed: 171 File: Fear.the.Walking.Dead.S03E08.HDTV.x264-FLEET [rarbg] [SD]
[1337x]              Seed: 161 File: Fear.the.Walking.Dead.S03E08.720p.HDTV.x264-AVS[eztv]
[1337x]              Seed: 130 File: Fear.the.Walking.Dead.S03E08.1080p.AMZN.WEBRip.DD5.1.x264-VLAD [rarbg] [SD]
[1337x]              Seed:  67 File: Fear.The.Walking.Dead.S03E08.CONVERT.WEB.h264-TBS[eztv]
[1337x]              Seed:  48 File: Fear.the.Walking.Dead.S03E08.1080p.HDTV.x264-BRISK [rarbg] [SD]
[1337x]              Seed:  23 File: Fear the Walking Dead S03E08 720p WEB-DL 400MB - MkvCage
	Download ->  [1337x]              Seed: 2626 File: Fear.the.Walking.Dead.S03E08.HDTV.x264-FLEET[eztv]
	[+] shadowhunters S01E01
[torrent9]           Seed:  37 File: Shadowhunters S01E01 FRENCH HDTV
[torrent9]           Seed:  13 File: Shadowhunters S01E01 VOSTFR HDTV
[1337x]              Seed:   0 File: Shadowhunters S01e01-13[Mux - 720p - H264 - Ita Eng Ac3 5.1 - Sub Ita Eng] GiuseppeTnT Littlelinx By...
[1337x]              Seed:   0 File: Shadowhunters S01e01-03[Mux - 720p - H264 - Ita Eng Ac3 5.1 - Sub Ita Eng] DLMux By Novarip
[1337x]              Seed:   0 File: Shadowhunters s01e01 WEB DLRip BaibaKo
[1337x]              Seed:   0 File: Shadowhunters.S01E01.720p.HDTV.x264.AAC-SS -={SPARROW}=-
[1337x]              Seed:   0 File: Shadowhunters.S01E01.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E01.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed:  37 File: Shadowhunters S01E01 FRENCH HDTV
	[+] shadowhunters S01E02
[torrent9]           Seed:  52 File: Shadowhunters S01E02 FRENCH HDTV
[torrent9]           Seed:   7 File: Shadowhunters S01E02 VOSTFR HDTV
[1337x]              Seed:   0 File: Shadowhunters S01E02 720p HDTV x264 BATV
[1337x]              Seed:   0 File: Shadowhunters.S01E02.HDTV.x264-BATV[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E02.720p.HDTV.x264-BATV[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E02.WEBRip.XviD-FUM[ettv]
	Download ->  [torrent9]           Seed:  52 File: Shadowhunters S01E02 FRENCH HDTV
	[+] shadowhunters S01E03
[torrent9]           Seed:  15 File: Shadowhunters S01E03 VOSTFR HDTV
[torrent9]           Seed:  27 File: Shadowhunters S01E03 FRENCH HDTV
[1337x]              Seed:   0 File: AgusiQ TorrentS pl Shadowhunters S01E03 NAPISY PL AX2 AgusiQ
[1337x]              Seed:   0 File: Shadowhunters S01E03 (2015) HDTV x264 AFG
[1337x]              Seed:   0 File: Shadowhunters S01E03 720p HDTV x264 KILLERS eztv mkv
[1337x]              Seed:   0 File: Shadowhunters S01E03 HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Shadowhunters S01E03 HDTV x264 KILLERS
[1337x]              Seed:   0 File: Shadowhunters S01E03 720p HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Shadowhunters S01E03 HDTV x264 KILLERS eztv
[1337x]              Seed:   0 File: Shadowhunters.S01E03.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters S01E03 720p HDTV x264-KILLERS
[1337x]              Seed:   0 File: Shadowhunters.S01E03.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E03.720p.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed:  27 File: Shadowhunters S01E03 FRENCH HDTV
	[+] shadowhunters S01E04
[torrent9]           Seed:   7 File: Shadowhunters S01E04 VOSTFR HDTV
[torrent9]           Seed:  40 File: Shadowhunters S01E04 FRENCH HDTV
[1337x]              Seed:   0 File: Shadowhunters s01e04 WEBDLRip NewStudio TV
[1337x]              Seed:   0 File: shadowhunters s01e04 raising hell 1080p webrip hevc x265 rmteam mkv
[1337x]              Seed:   0 File: AgusiQ TorrentS pl Shadowhunters S01E04 NAPISY PL AX2 AgusiQ
[1337x]              Seed:   0 File: Shadowhunters S01E04 720p HDTV x264 KILLERS
[1337x]              Seed:   0 File: Shadowhunters S01E04 HDTV x264 KILLERS
[1337x]              Seed:   0 File: Shadowhunters S01E04 720p HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Shadowhunters S01E04 720p HDTV x264 KILLERS eztv mkv
[1337x]              Seed:   0 File: Shadowhunters S01E04 HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Shadowhunters.S01E04.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E04.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E04.720p.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed:  40 File: Shadowhunters S01E04 FRENCH HDTV
	[+] shadowhunters S01E05
[torrent9]           Seed:   9 File: Shadowhunters S01E05 VOSTFR HDTV
[torrent9]           Seed:  31 File: Shadowhunters S01E05 FRENCH HDTV
[1337x]              Seed:   0 File: Shadowhunters.S01E05.Moo.Shu.to.Go.720p.HDTV.DD5.1.MPEG2-JiTB-={SPARROW}=-
[1337x]              Seed:   0 File: AgusiQ TorrentS pl Shadowhunters S01E05 NAPISY PL AX2 AgusiQ
[1337x]              Seed:   0 File: Shadowhunters S01E05 REPACK 720p HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Shadowhunters S01E05 HDTV x264 KILLERS
[1337x]              Seed:   0 File: Shadowhunters S01E05 REPACK 720p HDTV x264 KILLERS eztv mkv
[1337x]              Seed:   0 File: Shadowhunters S01E05 HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Shadowhunters S01E05 HDTV x264 KILLERS eztv
[1337x]              Seed:   0 File: Shadowhunters.S01E05.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E05.REPACK.720p.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E05.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed:  31 File: Shadowhunters S01E05 FRENCH HDTV
	[+] shadowhunters S01E06
[torrent9]           Seed:   7 File: Shadowhunters S01E06 VOSTFR HDTV
[torrent9]           Seed:  31 File: Shadowhunters S01E06 FRENCH HDTV
[1337x]              Seed:   0 File: Shadowhunters S01E06 Of Men and Angels 1080p NF WEBRip DD5.1 x264-LiebeIst
[1337x]              Seed:   0 File: Shadowhunters s01e06 WEBDLRip NewStudio TV
[1337x]              Seed:   0 File: Shadowhunters.S01E06.Of.Men.and.Angels.720p.HDTV.DD5.1.MPEG2-JiTB-={SPARROW}=-
[1337x]              Seed:   0 File: Shadowhunters S01E06 INTERNAL 720p HDTV x264 KILLERS eztv mkv
[1337x]              Seed:   0 File: Shadowhunters S01E06 HDTV x264 FLEET eztv
[1337x]              Seed:   0 File: Shadowhunters S01E06 INTERNAL HDTV x264 KILLERS eztv
[1337x]              Seed:   0 File: Shadowhunters S01E06 720p HDTV x264 FLEET rarbg
[1337x]              Seed:   0 File: Shadowhunters S01E06 HDTV x264 FLEET
[1337x]              Seed:   0 File: Shadowhunters S01E06 720p HDTV x264 FLEET eztv mkv
[1337x]              Seed:   0 File: Shadowhunters S01E06 HDTV x264 FLEET rarbg
[1337x]              Seed:   0 File: Shadowhunters S01E06 INTERNAL HDTV x264 KILLERS
[1337x]              Seed:   0 File: Shadowhunters.S01E06.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters S01E06 INTERNAL 720p HDTV x264-KILLERS
[1337x]              Seed:   0 File: Shadowhunters.S01E06.INTERNAL.720p.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E06.INTERNAL.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed:  31 File: Shadowhunters S01E06 FRENCH HDTV
	[+] shadowhunters S01E07
[torrent9]           Seed:  24 File: Shadowhunters S01E07 FRENCH HDTV
[torrent9]           Seed:   9 File: Shadowhunters S01E07 VOSTFR HDTV
[1337x]              Seed:   0 File: Shadowhunters.S01E07.HDTV.x264-Prt CreW!
[1337x]              Seed:   0 File: AgusiQ TorrentS pl Shadowhunters S01E07 NAPISY PL AX2 AgusiQ
[1337x]              Seed:   0 File: Shadowhunters S01E07 HDTV x264 KILLERS eztv
[1337x]              Seed:   0 File: Shadowhunters S01E07 720p HDTV x264 KILLERS eztv mkv
[1337x]              Seed:   0 File: Shadowhunters S01E07 720p HDTV x264 KILLERS
[1337x]              Seed:   0 File: Shadowhunters S01E07 HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Shadowhunters S01E07 HDTV x264 KILLERS
[1337x]              Seed:   0 File: Shadowhunters S01E07 720p HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Shadowhunters.S01E07.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E07.720p.HDTV.x264-KILLERS [GloDLS]
[1337x]              Seed:   0 File: Shadowhunters.S01E07.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Shadowhunters S01E07 720p HDTV x264-KILLERS
[1337x]              Seed:   0 File: Shadowhunters S01E07 HDTV XviD-AFG
[1337x]              Seed:   0 File: Shadowhunters.S01E07.720p.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed:  24 File: Shadowhunters S01E07 FRENCH HDTV
	[+] shadowhunters S01E08
[torrent9]           Seed:   5 File: Shadowhunters S01E08 VOSTFR HDTV
[torrent9]           Seed:  22 File: Shadowhunters S01E08 FRENCH HDTV
[1337x]              Seed:   0 File: Shadowhunters S01E08.HDTV.x264-Prt CreW!
[1337x]              Seed:   0 File: AgusiQ TorrentS pl Shadowhunters S01E08 NAPISY PL AX2 AgusiQ
[1337x]              Seed:   0 File: Shadowhunters S01E08 1080p WEB-DL DD 5.1 H.264-VietHD
[1337x]              Seed:   0 File: Shadowhunters.S01E08.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters S01E08 INTERNAL HDTV x264 KILLERS eztv
[1337x]              Seed:   0 File: Shadowhunters S01E08 INTERNAL 720p HDTV x264-KILLERS
[1337x]              Seed:   0 File: Shadowhunters.S01E08.INTERNAL.720p.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E08.INTERNAL.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Shadowhunters The Mortal Instruments S01E08 720p HDTV x264 FLEET
[1337x]              Seed:   0 File: Shadowhunters The Mortal Instruments S01E08 HDTV x264 FLEET rarbg
[1337x]              Seed:   0 File: Shadowhunters The Mortal Instruments S01E08 HDTV x264 FLEET
[1337x]              Seed:   0 File: Shadowhunters The Mortal Instruments S01E08 720p HDTV x264 FLEET eztv mkv
[1337x]              Seed:   0 File: Shadowhunters The Mortal Instruments S01E08 HDTV x264 FLEET eztv
	Download ->  [torrent9]           Seed:  22 File: Shadowhunters S01E08 FRENCH HDTV
	[+] shadowhunters S01E09
[torrent9]           Seed:   6 File: Shadowhunters S01E09 VOSTFR HDTV
[torrent9]           Seed:  23 File: Shadowhunters S01E09 FRENCH HDTV
[1337x]              Seed:   0 File: Shadowhunters.S01E09
[1337x]              Seed:   0 File: Shadowhunters S01E09 HDTV x264 KILLERS
[1337x]              Seed:   0 File: Shadowhunters S01E09 720p HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Shadowhunters S01E09 HDTV x264 KILLERS eztv
[1337x]              Seed:   0 File: Shadowhunters S01E09 HDTV x264-KILLERS [TV4Me].mp4
[1337x]              Seed:   0 File: Shadowhunters.S01E09.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters S01E09 720p HDTV x264-KILLERS
[1337x]              Seed:   0 File: Shadowhunters.S01E09.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E09.720p.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed:  23 File: Shadowhunters S01E09 FRENCH HDTV
	[+] shadowhunters S01E10
[torrent9]           Seed:  20 File: Shadowhunters S01E10 FRENCH HDTV
[torrent9]           Seed:   5 File: Shadowhunters S01E10 VOSTFR HDTV
[1337x]              Seed:   0 File: Shadowhunters S01E10 HDTV x264-Prt CreW!
[1337x]              Seed:   0 File: Shadowhunters S01E10 HDTV x264 KILLERS rarbg
[1337x]              Seed:   0 File: Shadowhunters S01E10 HDTV x264 KILLERS
[1337x]              Seed:   0 File: Shadowhunters S01E10 HDTV x264 KILLERS eztv
[1337x]              Seed:   0 File: Shadowhunters.S01E10.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E10.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E10.720p.HDTV.x264-KILLERS[ettv]
	Download ->  [torrent9]           Seed:  20 File: Shadowhunters S01E10 FRENCH HDTV
	[+] shadowhunters S01E11
[torrent9]           Seed:  21 File: Shadowhunters S01E11 FRENCH HDTV
[torrent9]           Seed:   4 File: Shadowhunters S01E11 VOSTFR HDTV
[1337x]              Seed:   0 File: Shadowhunters S01E11 HDTV x264-Prt CreW!
[1337x]              Seed:   0 File: Shadowhunters.S01E11.HDTV.x264
[1337x]              Seed:   0 File: Shadowhunters S01E11 iNTERNAL 720p HDTV x264 ALTEREGO eztv mkv
[1337x]              Seed:   0 File: Shadowhunters S01E11 iNTERNAL HDTV x264 ALTEREGO eztv mkv
[1337x]              Seed:   0 File: Shadowhunters.S01E11.WEBRip.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E11.WEBRip.x264-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters S01E11 720p HDTV x264 FLEET eztv mkv
[1337x]              Seed:   0 File: Shadowhunters S01E11 HDTV x264 FLEET eztv
[1337x]              Seed:   0 File: Shadowhunters S01E11 HDTV x264 FLEET
[1337x]              Seed:   0 File: Shadowhunters S01E11 HDTV x264 FLEET rarbg
[1337x]              Seed:   0 File: Shadowhunters S01E11 HDTV XviD-AFG
	Download ->  [torrent9]           Seed:  21 File: Shadowhunters S01E11 FRENCH HDTV
	[+] shadowhunters S01E12
[torrent9]           Seed:   4 File: Shadowhunters S01E12 VOSTFR HDTV
[torrent9]           Seed:  20 File: Shadowhunters S01E12 FRENCH HDTV
[1337x]              Seed:   0 File: Shadowhunters S01E12 HDTV x264 2HD
[1337x]              Seed:   0 File: Shadowhunters S01E12 720p HDTV x264 2HD rarbg
[1337x]              Seed:   0 File: Shadowhunters S01E12 HDTV x264 2HD eztv
[1337x]              Seed:   0 File: Shadowhunters S01E12 720p HDTV x264 2HD eztv mkv
[1337x]              Seed:   0 File: Shadowhunters S01E12 HDTV x264 2HD rarbg
[1337x]              Seed:   0 File: Shadowhunters.S01E12.HDTV.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E12.720p.HDTV.x264-2HD[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E12.HDTV.x264-2HD[ettv]
	Download ->  [torrent9]           Seed:  20 File: Shadowhunters S01E12 FRENCH HDTV
	[+] shadowhunters S01E13
[torrent9]           Seed:  22 File: Shadowhunters S01E13 FINAL FRENCH HDTV
[torrent9]           Seed:   3 File: Shadowhunters S01E13 FINAL VOSTFR HDTV
[1337x]              Seed:   0 File: Shadowhunters S01E13 iNTERNAL 720p HDTV x264 ALTEREGO eztv mkv
[1337x]              Seed:   0 File: Shadowhunters.S01E13.WEBRip.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.S01E13.WEBRip.x264-FUM[ettv]
	Download ->  [torrent9]           Seed:  22 File: Shadowhunters S01E13 FINAL FRENCH HDTV
	[+] shadowhunters S01E14
	[+] shadowhunters S02E01
[torrent9]           Seed:  38 File: Shadowhunters S02E01 FRENCH HDTV
[torrent9]           Seed:   6 File: Shadowhunters S02E01 VOSTFR HDTV
[nextorrent]         Seed:  58 File: Shadowhunters S02E01 VOSTFR HDTV
[nextorrent]         Seed:  75 File: Shadowhunters S02E01 FRENCH HDTV
[1337x]              Seed:   0 File: Shadowhunters.S02E01.WEBRip.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E01.720p.HDTV.x264-FLEET[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E01.720p.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E01.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E01.HDTV.x264-FLEET[eztv]
	Download ->  [nextorrent]         Seed:  75 File: Shadowhunters S02E01 FRENCH HDTV
	[+] shadowhunters S02E02
[torrent9]           Seed:  26 File: Shadowhunters S02E02 FRENCH HDTV
[torrent9]           Seed:   6 File: Shadowhunters S02E02 VOSTFR HDTV
[nextorrent]         Seed:  75 File: Shadowhunters S02E02 FRENCH HDTV
[1337x]              Seed:   0 File: Shadowhunters S02e02-03[Mux - 1080p - H264 - Ita Eng Ac3 - Sub Ita Eng] Novarip
[1337x]              Seed:   0 File: Shadowhunters.S02E02.WEB-DL.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters S02E02 HDTV 480p MKVTV
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E02.HDTV.x264-FLEET[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E02.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E02.720p.HDTV.x264-SVA[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E02.720p.HDTV.x264-SVA[eztv]
	Download ->  [nextorrent]         Seed:  75 File: Shadowhunters S02E02 FRENCH HDTV
	[+] shadowhunters S02E03
[torrent9]           Seed:  38 File: Shadowhunters S02E03 FRENCH HDTV
[torrent9]           Seed:  10 File: Shadowhunters S02E03 VOSTFR HDTV
[nextorrent]         Seed:  60 File: Shadowhunters S02E03 FRENCH HDTV
[nextorrent]         Seed:  58 File: Shadowhunters S02E03 VOSTFR HDTV
[1337x]              Seed:   0 File: Shadowhunters.S02E03.WEBRip.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E03.720p.HDTV.x264-FLEET[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E03.720p.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E03.720p.HDTV.x264-SVA[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E03.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E03.HDTV.x264-FLEET[eztv]
	Download ->  [nextorrent]         Seed:  60 File: Shadowhunters S02E03 FRENCH HDTV
	[+] shadowhunters S02E04
[torrent9]           Seed:  50 File: Shadowhunters S02E04 PROPER FRENCH HDTV
[torrent9]           Seed:   3 File: Shadowhunters S02E04 VOSTFR HDTV
[nextorrent]         Seed:  52 File: Shadowhunters S02E04 PROPER FRENCH HDTV
[nextorrent]         Seed:  26 File: Shadowhunters S02E04 VOSTFR HDTV
[1337x]              Seed:   0 File: Shadowhunters.S02E04.WEBRip.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters S02E04 HDTV 480p MKVTV
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E04.720p.HDTV.x264-FLEET[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E04.HDTV.x264-FLEET[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E04.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E04.720p.HDTV.x264-FLEET[PRiME]
	Download ->  [nextorrent]         Seed:  52 File: Shadowhunters S02E04 PROPER FRENCH HDTV
	[+] shadowhunters S02E05
[torrent9]           Seed:   6 File: Shadowhunters S02E05 VOSTFR HDTV
[torrent9]           Seed:  32 File: Shadowhunters S02E05 FRENCH HDTV
[nextorrent]         Seed:  17 File: Shadowhunters S02E05 VOSTFR HDTV
[nextorrent]         Seed:  33 File: Shadowhunters S02E05 FRENCH HDTV
[1337x]              Seed:   0 File: Shadowhunters.S02E05.WEBRip.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E05.720p.HDTV.x264-FLEET[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E05.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E05.720p.HDTV.x264-SVA[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E05.720p.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E05.720p.HDTV.x264-SVA[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E05.HDTV.x264-FLEET[eztv]
	Download ->  [nextorrent]         Seed:  33 File: Shadowhunters S02E05 FRENCH HDTV
	[+] shadowhunters S02E06
[torrent9]           Seed:  18 File: Shadowhunters S02E06 FRENCH HDTV
[torrent9]           Seed:  12 File: Shadowhunters S02E06 VOSTFR HDTV
[nextorrent]         Seed:  54 File: Shadowhunters S02E06 VOSTFR HDTV
[nextorrent]         Seed: 204 File: Shadowhunters S02E06 FRENCH HDTV
[1337x]              Seed:   0 File: Shadowhunters.S02E06.WEBRip.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E06.HDTV.x264-FLEET[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E06.720p.HDTV.x264-FLEET[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E06.720p.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E06.HDTV.x264-FLEET[PRiME]
	Download ->  [nextorrent]         Seed: 204 File: Shadowhunters S02E06 FRENCH HDTV
	[+] shadowhunters S02E07
[torrent9]           Seed:  40 File: Shadowhunters S02E07 FRENCH HDTV
[torrent9]           Seed:   6 File: Shadowhunters S02E07 VOSTFR HDTV
[nextorrent]         Seed:  45 File: Shadowhunters S02E07 FRENCH HDTV
[nextorrent]         Seed:  33 File: Shadowhunters S02E07 VOSTFR HDTV
[1337x]              Seed:   0 File: Shadowhunters.S02E07.WEBRip.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters S02E07 HDTV 480p MKVTV
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E07.HDTV.x264-SVA[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E07.720p.HDTV.x264-SVA[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E07.720p.HDTV.x264-SVA[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E07.HDTV.x264-SVA[PRiME]
	Download ->  [nextorrent]         Seed:  45 File: Shadowhunters S02E07 FRENCH HDTV
	[+] shadowhunters S02E08
[torrent9]           Seed:  38 File: Shadowhunters S02E08 FRENCH HDTV
[torrent9]           Seed:   7 File: Shadowhunters S02E08 VOSTFR HDTV
[nextorrent]         Seed:  16 File: Shadowhunters S02E08 FRENCH HDTV
[nextorrent]         Seed:  40 File: Shadowhunters S02E08 VOSTFR HDTV
[1337x]              Seed:   0 File: Shadowhunters S02E08 HDTV 480p MKVTV
[1337x]              Seed:   0 File: Shadowhunters.S02E08.WEBRip.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.MULTi.1080p.WEBRip.x264-BRiNK[xwarez]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.HDTV.x264-SVA[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.REAL.PROPER.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.REAL.PROPER.HDTV.x264-KILLERS[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.REAL.PROPER.720p.HDTV.x264-KILLERS[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.REAL.PROPER.720p.HDTV.x264-KILLERS[ettv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.PROPER.HDTV.x264-FLEET[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.720p.HDTV.x264-SVA[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.PROPER.720p.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.720p.HDTV.x264-SVA[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.PROPER.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.HDTV.x264-SVA[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E08.PROPER.720p.HDTV.x264-FLEET[eztv]
	Download ->  [nextorrent]         Seed:  40 File: Shadowhunters S02E08 VOSTFR HDTV
	[+] shadowhunters S02E09
[torrent9]           Seed:  11 File: Shadowhunters S02E09 VOSTFR HDTV
[torrent9]           Seed:  29 File: Shadowhunters S02E09 FRENCH HDTV
[nextorrent]         Seed:  40 File: Shadowhunters S02E09 FRENCH HDTV
[1337x]              Seed:   0 File: Shadowhunters.S02E09.WEBRip.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters S02E09 HDTV 480p MKVTV
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E09.720p.HDTV.x264-SVA[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E09.720p.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E09.HDTV.x264-SVA[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E09.720p.HDTV.x264-SVA[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E09.720p.HDTV.x264-FLEET[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E09.HDTV.x264-SVA[eztv]
	Download ->  [nextorrent]         Seed:  40 File: Shadowhunters S02E09 FRENCH HDTV
	[+] shadowhunters S02E10
[torrent9]           Seed:  40 File: Shadowhunters S02E10 FRENCH HDTV
[torrent9]           Seed:   7 File: Shadowhunters S02E10 VOSTFR HDTV
[nextorrent]         Seed:  91 File: Shadowhunters S02E10 FRENCH HDTV
[1337x]              Seed:   0 File: Shadowhunters.S02E10.WEBRip.XviD-FUM[ettv]
[1337x]              Seed:   0 File: Shadowhunters S02E10 1080p WEBRip HEVC x265-RMTeam
[1337x]              Seed:   0 File: Shadowhunters S02E10 HDTV 480p MKVTV
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E10.REAL.PROPER.720p.HDTV.x264-SVA[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E10.REAL.PROPER.720p.HDTV.x264-SVA[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E10.PROPER.720p.HDTV.x264-FLEET[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E10.PROPER.HDTV.x264-FLEET[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E10.PROPER.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E10.PROPER.720p.HDTV.x264-FLEET[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E10.720p.HDTV.x264-SVA[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E10.720p.HDTV.x264-SVA[PRiME]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E10.HDTV.x264-SVA[eztv]
[1337x]              Seed:   0 File: Shadowhunters.The.Mortal.Instruments.S02E10.HDTV.x264-SVA[PRiME]
	Download ->  [nextorrent]         Seed:  91 File: Shadowhunters S02E10 FRENCH HDTV
	[+] shadowhunters S02E11
[torrent9]           Seed:  68 File: Shadowhunters S02E11 FRENCH HDTV
[torrent9]           Seed:  22 File: Shadowhunters S02E11 VOSTFR HDTV
[nextorrent]         Seed: 102 File: Shadowhunters S02E11 FRENCH HDTV
[1337x]              Seed: 255 File: Shadowhunters.The.Mortal.Instruments.S02E11.HDTV.x264-FLEET[eztv]
[1337x]              Seed: 124 File: Shadowhunters.The.Mortal.Instruments.S02E11.WEB.x264-TBS[eztv]
[1337x]              Seed: 117 File: Shadowhunters.The.Mortal.Instruments.S02E11.WEB.x264-TBS[rarbg]-[1337x]
[1337x]              Seed:  66 File: Shadowhunters.The.Mortal.Instruments.S02E11.720p.WEB.x264-TBS[rarbg]-[1337x]
[1337x]              Seed:  47 File: Shadowhunters.The.Mortal.Instruments.S02E11.720p.WEB.x264-TBS[ettv]
[1337x]              Seed:  36 File: Shadowhunters.The.Mortal.Instruments.S02E11.720p.WEB.x264-TBS[eztv]
[1337x]              Seed:  22 File: Shadowhunters.The.Mortal.Instruments.S02E11.720p.HDTV.x264-FLEET[eztv]
[1337x]              Seed:  18 File: Shadowhunters.S02E11.WEB-DL.x264-RARBG
[1337x]              Seed:  14 File: Shadowhunters.S02E11.1080p.WEB-DL.DD5.1.H264-NOGRP[rarbg]
	Download ->  [1337x]              Seed: 255 File: Shadowhunters.The.Mortal.Instruments.S02E11.HDTV.x264-FLEET[eztv]
	[+] shadowhunters S02E12
[torrent9]           Seed:  52 File: Shadowhunters S02E12 FRENCH HDTV
[torrent9]           Seed:  15 File: Shadowhunters S02E12 VOSTFR HDTV
[nextorrent]         Seed: 101 File: Shadowhunters S02E12 FRENCH HDTV
[1337x]              Seed: 390 File: Shadowhunters.The.Mortal.Instruments.S02E12.HDTV.x264-FLEET[eztv]
[1337x]              Seed: 174 File: Shadowhunters.The.Mortal.Instruments.S02E12.HDTV.x264-FLEET[rarbg]
[1337x]              Seed:  74 File: Shadowhunters.The.Mortal.Instruments.S02E12.720p.HDTV.x264-FLEET[rarbg]
[1337x]              Seed:  64 File: Shadowhunters.The.Mortal.Instruments.S02E12.WEB.x264-TBS[rarbg]
[1337x]              Seed:  54 File: Shadowhunters.The.Mortal.Instruments.S02E12.720p.WEB.x264-TBS[rarbg]
[1337x]              Seed:  41 File: Shadowhunters.S02E12.WEB-DL.x264-RARBG
[1337x]              Seed:  40 File: Shadowhunters.The.Mortal.Instruments.S02E12.720p.WEB.x264-TBS[eztv]
[1337x]              Seed:  23 File: Shadowhunters.The.Mortal.Instruments.S02E12.WEB.x264-TBS[ettv]
[1337x]              Seed:  19 File: Shadowhunters.The.Mortal.Instruments.S02E12.720p.HDTV.x264-FLEET[eztv]
[1337x]              Seed:  18 File: Shadowhunters.S02E12.1080p.NF.WEBRip.DD5.1.x264-ViSUM[rarbg]
[1337x]              Seed:  16 File: Shadowhunters.The.Mortal.Instruments.S02E12.1080p.WEB.h264-TBS[rarbg]
[1337x]              Seed:  15 File: Shadowhunters.The.Mortal.Instruments.S02E12.WEB.x264-TBS[eztv]
[1337x]              Seed:  14 File: Shadowhunters.S02E12.1080p.WEB-DL.DD5.1.H264-NOGRP[rarbg]
[1337x]              Seed:   7 File: Shadowhunters.The.Mortal.Instruments.S02E12.720p.WEB.x264-TBS[ettv]
	Download ->  [1337x]              Seed: 390 File: Shadowhunters.The.Mortal.Instruments.S02E12.HDTV.x264-FLEET[eztv]
	[+] shadowhunters S02E13
[torrent9]           Seed:  18 File: Shadowhunters S02E13 VOSTFR HDTV
[torrent9]           Seed:  84 File: Shadowhunters S02E13 FRENCH HDTV
[nextorrent]         Seed:  32 File: Shadowhunters S02E13 VOSTFR HDTV
[nextorrent]         Seed: 121 File: Shadowhunters S02E13 FRENCH HDTV
[1337x]              Seed: 389 File: Shadowhunters.The.Mortal.Instruments.S02E13.WEB.x264-TBS[eztv]
[1337x]              Seed: 361 File: Shadowhunters.The.Mortal.Instruments.S02E13.WEB.x264-TBS[ettv]
[1337x]              Seed: 178 File: Shadowhunters.The.Mortal.Instruments.S02E13.WEB.x264-TBS [rarbg] [SD]
[1337x]              Seed:  87 File: Shadowhunters.S02E13.WEBRip.x264-RARBG
[1337x]              Seed:  48 File: Shadowhunters.S02E13.720p.NF.WEBRip.DD5.1.x264-ViSUM[rarbg]
[1337x]              Seed:  40 File: Shadowhunters.S02E13.1080p.NF.WEBRip.DD5.1.x264-ViSUM[rarbg]
[1337x]              Seed:  35 File: Shadowhunters.The.Mortal.Instruments.S02E13.1080p.WEBRip.x264-STRiFE [rarbg] [SD]
	Download ->  [1337x]              Seed: 389 File: Shadowhunters.The.Mortal.Instruments.S02E13.WEB.x264-TBS[eztv]
	[+] shadowhunters S02E14
[torrent9]           Seed:  46 File: Shadowhunters S02E14 VOSTFR HDTV
[torrent9]           Seed: 132 File: Shadowhunters S02E14 FRENCH HDTV
[nextorrent]         Seed: 124 File: Shadowhunters S02E14 VOSTFR HDTV
[nextorrent]         Seed: 166 File: Shadowhunters S02E14 FRENCH HDTV
[1337x]              Seed: 412 File: Shadowhunters.The.Mortal.Instruments.S02E14.WEB.x264-TBS[eztv]
[1337x]              Seed: 155 File: Shadowhunters.The.Mortal.Instruments.S02E14.HDTV.x264-MiNDTHEGAP[eztv]
[1337x]              Seed: 135 File: Shadowhunters.S02E14.WEBRip.x264-RARBG
[1337x]              Seed: 107 File: Shadowhunters.The.Mortal.Instruments.S02E14.WEB.x264-TBS[ettv]
[1337x]              Seed:  86 File: Shadowhunters.The.Mortal.Instruments.S02E14.WEB.x264-TBS [rarbg] [SD]
[1337x]              Seed:  82 File: Shadowhunters.The.Mortal.Instruments.S02E14.720p.WEB.x264-TBS [rarbg] [SD]
[1337x]              Seed:  51 File: Shadowhunters.S02E14.The.Fair.Folk.720p.NF.WEBRip.DD5.1.x264-NTb [rarbg] [SD]
[1337x]              Seed:  43 File: Shadowhunters.S02E14.The.Fair.Folk.1080p.NF.WEBRip.DD5.1.x264-NTb [rarbg] [SD]
[1337x]              Seed:  35 File: Shadowhunters.The.Mortal.Instruments.S02E14.720p.WEB.x264-TBS[ettv]
[1337x]              Seed:  32 File: Shadowhunters.The.Mortal.Instruments.S02E14.720p.HDTV.x264-MiNDTHEGAP[eztv]
[1337x]              Seed:  18 File: Shadowhunters.The.Mortal.Instruments.S02E14.720p.WEB.x264-TBS[eztv]
	Download ->  [1337x]              Seed: 412 File: Shadowhunters.The.Mortal.Instruments.S02E14.WEB.x264-TBS[eztv]
	[+] shadowhunters S02E15
[torrent9]           Seed:   5 File: Shadowhunters S02E15 FRENCH HDTV
[torrent9]           Seed: 164 File: Shadowhunters S02E15 VOSTFR HDTV
[nextorrent]         Seed: 109 File: Shadowhunters S02E15 VOSTFR HDTV
[1337x]              Seed: 1062 File: Shadowhunters.The.Mortal.Instruments.S02E15.WEB.x264-TBS[eztv]
[1337x]              Seed: 539 File: Shadowhunters.The.Mortal.Instruments.S02E15.XviD-AFG
[1337x]              Seed: 455 File: Shadowhunters.The.Mortal.Instruments.S02E15.WEBRip.x264-RARBG [SD]
[1337x]              Seed: 273 File: Shadowhunters.The.Mortal.Instruments.S02E15.WEB.x264-TBS[ettv]
[1337x]              Seed: 257 File: Shadowhunters.The.Mortal.Instruments.S02E15.720p.WEB.x264-TBS[eztv]
[1337x]              Seed: 109 File: Shadowhunters.The.Mortal.Instruments.S02E15.1080p.WEBRip.x264-STRiFE [rarbg] [SD]
[1337x]              Seed:  65 File: Shadowhunters.The.Mortal.Instruments.S02E15.480p.x264-mSD
[1337x]              Seed:  56 File: Shadowhunters.The.Mortal.Instruments.S02E15.720p.WEB.x264-TBS[ettv]
[1337x]              Seed:  36 File: Shadowhunters The Mortal Instruments S02E15 720p WEB&#194;&#160;x265-YST
	Download ->  [1337x]              Seed: 1062 File: Shadowhunters.The.Mortal.Instruments.S02E15.WEB.x264-TBS[eztv]
	[+] UFC.PPV 213
[1337x]              Seed: 2937 File: UFC 213 Romero vs Whittaker PPV HDTV x264-Ebi [TJET]
[1337x]              Seed: 544 File: UFC 213 Romero vs Whittaker PPV 720p HDTV x264-Ebi [TJET]
[1337x]              Seed:  76 File: UFC.213.Romero.vs.Whittaker.PPV.HDTV.x264-NoGrp
	Download ->  [1337x]              Seed: 2937 File: UFC 213 Romero vs Whittaker PPV HDTV x264-Ebi [TJET]

```

# Update

Updating Downloader is easy :
1. clone the repository again and execute *setup.py* script
2. download the archive and execute *setup.py* script
3. if you keep the repository just type the following command: *git pull*

However, more engine will be added and I'm feeling lazy right now so to update the future engine use one of the previous method and diff the configuration file for new settings.

# Killer setup

1. Install Plex
2. Install tranmission-daemon
3. Plug Raspberry PI on your TV and install RasPlex
4. Write a cron job for downloader
5. Enjoy your movies and series on your TV without doing anything ;)

# Tips

- If you want to begin a TV shows after S04E11 just create that file into your directory. Downloader do not care of the file type
- I use the following structure :
```
```

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
