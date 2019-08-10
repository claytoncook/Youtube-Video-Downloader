import tkinter
import os
import colors as c

window = tkinter.Tk()
window.title("Youtube Video Downloader")

downloadType = tkinter.IntVar()
downloadType.set(1)
link = tkinter.StringVar()
title = tkinter.StringVar()

videoEntry = tkinter.Entry(window, textvariable=link)
titleEntry = tkinter.Entry(window, textvariable=title)

def downloadVideo():
    print(downloadType.get(), link.get())

    os.chdir("output")
    os.mkdir(str(title.get()))
    os.chdir("..")

    if downloadType.get() == 1 and not(link.get() == ""):
        os.chdir("output")
        os.chdir(str(title.get()))
        os.system("youtube-dl --yes-playlist -f 'bestaudio[ext=m4a]' " + str(link.get()))
    elif downloadType.get() == 2 and not(link.get() == ""):
        os.chdir("output")
        os.chdir(str(title.get()))
        os.system("youtube-dl --yes-playlist -f best " + str(link.get()))
    else:
        c.printColor(c.red, "Please choose a valid option.")

    os.chdir("..")
    os.chdir("..")

submitButton = tkinter.Button(window, text="Submit", command=downloadVideo)

#Main installation function for outside sources
def install():
    #Check to see if Brew needs to be installed
    checkIfBrewIsInstalled = str(os.system("brew -v")).split()
    if checkIfBrewIsInstalled[0] == "0":
        c.printColor(c.blue, "Brew is installed!")
    else:
        c.printColor(c.red, "Brew is not installed!")
        print("Installing now... \n")
        os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

        #Install Youtube-DL
        os.system("brew install youtube-dl")

def main():
    install()

    tkinter.Radiobutton(window, text="mp3", variable=downloadType, value=1).grid(row=0)
    tkinter.Radiobutton(window, text="mp4", variable=downloadType, value=2).grid(row=0,column=1)
    tkinter.Label(window, text="Video: ").grid(row=1)
    videoEntry.grid(row=1, column=1)
    tkinter.Label(window, text="Name of Output Folder: ").grid(row=2)
    titleEntry.grid(row=2, column=1)
    submitButton.grid(row=3)
    window.mainloop()

main()