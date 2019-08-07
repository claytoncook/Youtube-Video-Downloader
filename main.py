import tkinter
import os
import colors as c

window = tkinter.Tk()
window.title("Youtube Video Downloader")

downloadType = tkinter.IntVar()
downloadType.set(1)
link = tkinter.StringVar()

videoEntry = tkinter.Entry(window, textvariable=link)

def downloadVideo():
    print(downloadType.get(), link.get())

    if downloadType.get() == 1 and not(link.get() == ""):
        os.chdir("output")
        os.system("youtube-dl -f best " + str(link.get()))
    elif downloadType.get() == 2 and not(link.get() == ""):
        os.chdir("output")
        os.system("youtube-dl --yes-playlist -f best " + str(link.get()))
    else:
        c.printColor(c.red, "Please choose a valid option.")

    os.chdir("..")

submitButton = tkinter.Button(window, text="Submit", command=downloadVideo)

def install():
    checkIfBrewIsInstalled = str(os.system("brew -v")).split()
    if checkIfBrewIsInstalled[0] == "0":
        c.printColor(c.blue, "Brew is installed!")
    else:
        c.printColor(c.red, "Brew is not installed!")
        print("Installing now... \n")
        os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

    checkIfYoutubeDLIsInstalled = str(os.system("youtube-dl"))
    if checkIfYoutubeDLIsInstalled == "0":
        c.printColor(c.blue, "Youtube-DL is installed!")
    else:
        c.printColor(c.red, "Youtube-DL is not installed!")
        print("Installing now... \n")
        os.system("brew install youtube-dl")

def main():
    install()

    tkinter.Radiobutton(window, text="Video", variable=downloadType, value=1).grid(row=0)
    tkinter.Radiobutton(window, text="Playlist", variable=downloadType, value=2).grid(row=0,column=1)
    tkinter.Label(window, text="Video: ").grid(row=1)
    videoEntry.grid(row=1, column=1)
    submitButton.grid(row=2)
    window.mainloop()

main()