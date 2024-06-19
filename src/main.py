import tkinter

if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Algorithm Visualisation App")
    window.geometry("1200x900")
    window.resizable(False, False)
    window.configure(background="black")

    sortingFrame = tkinter.Frame(window, bg="red")
    sortingFrame.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

    sortingButton = tkinter.Button(sortingFrame, text="Sorting")
    sortingButton.pack(side=tkinter.TOP)

    window.mainloop()
