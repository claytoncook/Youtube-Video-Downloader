import tkinter
import os
import subprocess
import colors as c

# Example Video:
# https://www.youtube.com/watch?v=-1EPegIzD2M&list=LLgugZespId8haUhw5Wuwt5g&index=29&t=0s

def brew():
    checkIfBrewIsInstalled = str(os.system("brew -v")).split()
    if checkIfBrewIsInstalled[0] == "0":
        c.printColor(c.blue, "Brew is installed!")
    else:
        c.printColor(c.red, "Brew is not installed!")
        print("Installing now... \n")
        os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

def youtubeDL():
    chechIfYoutubeDLIsInstalled = str(os.system("youtube-dl"))
    print(chechIfYoutubeDLIsInstalled)
    if chechIfYoutubeDLIsInstalled == "0":
        c.printColor(c.blue, "Youtube-DL is installed!")
    else:
        c.printColor(c.red, "Youtube-DL is not installed!")
        print("Installing now... \n")
        os.system("brew install youtube-dl")

def downloadVideo():
    l = link.get()
    print(l)
    os.system("youtube-dl " + str(l))

window = tkinter.Tk()
window.title("Youtube Video Downloader")
link = tkinter.StringVar()
videoEntry = tkinter.Entry(window, textvariable=link)

submitButton = tkinter.Button(window, text="Submit", command=downloadVideo)

def main():
    brew()
    youtubeDL()

    tkinter.Label(window, text="Video: ").grid(row=0)
    videoEntry.grid(row=0, column=1)
    submitButton.grid(row=1)
    window.mainloop()

main()