# batch-subtitle-renamer
This tool renames all subtitles in a given folder to the video file names

# Usage:
python main.py "folder where the video files and subtitles are located"
e.g.:
python main.py "c:\tmp\testfolder\"

e.g.: If a folder contains the following files:
House.of.Cards.2013.S02E07.720p.BluRay.x264-DEMAND.srt
House.of.Cards.2013.S02E07.1080p.BluRay.x265-RARBG.mp4

after running to tool it will look like so:
House.of.Cards.2013.S02E07.1080p.BluRay.x265-RARBG.srt
House.of.Cards.2013.S02E07.1080p.BluRay.x265-RARBG.mp4

the matching is done by the season and episode codes, so the S01E01 will match with s01e01
though not all combinations are taken into account, so s01e01 will NOT match with s1e1 notation