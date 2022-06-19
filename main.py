import sys
from os import listdir, rename
from os.path import isfile, join, splitext
import re

def splitFilesList(fileList):
        """
        This function splits the received list into subtitles and video files list and returns them
        """
        videoExtensions = [
                "mkv",
                "mp4",
                "mov",
                "avi",
                "wmv",
                "mpeg",
                "m4v",
                "flv",
                "webm"
        ]
        
        subtitleExtensions = [
                "srt"
        ]

        videoFileList = []
        subtitleFileList = []

        for fileName in fileList:
                for extension in videoExtensions:
                        if "."+extension in fileName.lower():
                                videoFileList.append(fileName)
                                break
                for extension in subtitleExtensions:
                        if "."+extension in fileName.lower():
                                subtitleFileList.append(fileName)
                                break

        return videoFileList, subtitleFileList

def main():
        if len(sys.argv) == 1 or len(sys.argv) > 3:
                print("The number of supplied arguments are too low or too high!")
                print("---> Usage: main.py 'path to folder'")
                return
        # The argument should be the folder where the subtitles and the video files are
        print("The given folder path is: " + sys.argv[1])
        folderPath = sys.argv[1]
        onlyfiles = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]

        videoFileList, subtitleFileList = splitFilesList(onlyfiles)
        print(videoFileList)
        print(subtitleFileList)
        print("*******************")

        for videoFileName in videoFileList:
                # Get the S01E12 part from the file and search for it in the subtitle names
                # .[sS]\d{1,}[eE]\d{1,}.
                # explanation: starts with ., continues with s or S, and 1 or 2 numbers, then e or E, and 1 or 2 numbers, and then a .
                # not using lower because the video file names should be kept the same, maybe they are still being downloaded...
                seasonEpisodeIdentifier = re.search(r".[sS]\d{1,2}[eE]\d{1,2}.", videoFileName)
                print(seasonEpisodeIdentifier.group(0))
                seasonEpisodeIdentifierText = seasonEpisodeIdentifier.group(0)

                for subtitleFileName in subtitleFileList:
                        if seasonEpisodeIdentifierText.lower() in subtitleFileName.lower():
                                # Rename that subtitle file to the video file name + the original extension
                                nameWithoutExtension, subtitleExtension = splitext(subtitleFileName)
                                print(nameWithoutExtension)
                                oldSubTitleFileName = join(folderPath, subtitleFileName)
                                videoFileNameWithoutExtension, videoExtension = splitext(videoFileName)
                                newSubTitleFileName = join(folderPath, videoFileNameWithoutExtension + subtitleExtension)
                                print(oldSubTitleFileName)
                                print(newSubTitleFileName)
                                rename(oldSubTitleFileName, newSubTitleFileName)
                                break

if __name__ == '__main__':
        main()