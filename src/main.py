import tkinter
import random


def shuffle_list(win : tkinter.Tk) -> list[int]:
    canvas = tkinter.Canvas(win, width=900, height=900, bg="black")
    canvas.pack(side=tkinter.LEFT)
    allLines = []
    for i in range(1, 900):
        allLines.append(i)
    random.shuffle(allLines)
    for index in range(len(allLines)):
        canvas.create_line(1 + index, 900, 1 + index, allLines[index], fill="white", width=1)
    return allLines

def selection(win : tkinter.Tk):
    win.destroy()

    selection_window = create_window("Selection Sort", "1200x900", "black")
    all_lines = shuffle_list(selection_window)
    selection_window.mainloop()


def create_window(title : str, dimensions : str, bg_color : str) -> tkinter.Tk:
    generic_window = tkinter.Tk()
    generic_window.title(title)
    generic_window.geometry(dimensions)
    generic_window.configure(bg=bg_color)
    generic_window.resizable(False, False)

    title_text = tkinter.StringVar()
    title_text.set(title)
    title_label = tkinter.Label(generic_window, textvariable=title_text, bg="black", fg="white", font=("Arial", 30))
    title_label.pack(pady=20)

    menu_button = tkinter.Button(generic_window, text="Menu", command=lambda: [generic_window.destroy(), main()])
    menu_button.place(x=10, y=10)
    return generic_window


def sorting_algo(win : tkinter.Tk):
    win.destroy()

    sorting_window = create_window('Sorting Algorithms', '1200x900', 'black')

    selection_sort_button = tkinter.Button(sorting_window, text="Selection Sort", width=20, height=5, command=lambda: selection(sorting_window))
    selection_sort_button.place(x=100, y=100)

    insertion_sort_button = tkinter.Button(sorting_window, text="Insertion Sort", width=20, height=5)
    insertion_sort_button.place(x=400, y=100)

    sorting_window.mainloop()


def pathfinding_algo(win : tkinter.Tk):
    win.destroy()

    pathfinding_window = create_window('PathFinding Algorithms', '1200x900', 'black')

    pathfinding_window.mainloop()


def main():
    main_window = create_window("Algorithm Visualisation App (made by Alex Bataille)", "1200x900", "black")


    sorting_button = tkinter.Button(main_window, text="Sorting", width=20, height=5,
                                   command=lambda: sorting_algo(main_window))
    sorting_button.place(x=100, y=100)

    path_finding_button = tkinter.Button(main_window, text="PathFinding", width=20, height=5,
                                       command=lambda: pathfinding_algo(main_window))
    path_finding_button.place(x=400, y=100)

    main_window.mainloop()

if __name__ == "__main__":
    main()
