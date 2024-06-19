import tkinter
import random
import time

def selection_sort_algorithm(win : tkinter.Tk, numb_list : list[int], canvas, max_size : int, speed : int = 0):
    for i in range(len(numb_list)-1):
        current_minimum = i
        for j in range(i+1,len(numb_list)):
            if numb_list[j] < numb_list[current_minimum]:
                current_minimum = j
        display_list(win, numb_list, canvas, max_size, current_minimum)
        numb_list[i], numb_list[current_minimum] = numb_list[current_minimum], numb_list[i]
        win.update()
        time.sleep(speed*0.001)

def display_list(win : tkinter.Tk, numb_list : list, canvas, max_size : int, current_index=None):
    canvas.delete("all")
    n = 900/max_size if max_size != 0 else 1
    for index in range(len(numb_list)):
        color = "red" if index == current_index else "white"
        canvas.create_line(1 + round(index*n), 900, 1 + round(index*n), numb_list[index], fill=color, width=n)

def shuffle_list(win : tkinter.Tk, canvas, max_size : int) -> list[int]:
    allLines = []
    for i in range(1, max_size):
        allLines.append(i)
    random.shuffle(allLines)
    display_list(win, allLines, canvas, max_size)
    return allLines

def selection_display(win : tkinter.Tk):
    win.destroy()
    selection_window = create_window("Selection Sort", "1200x900", "black")

    canvas = tkinter.Canvas(selection_window, width=900, height=900, bg="black")
    canvas.pack(side=tkinter.LEFT)

    l_text = tkinter.StringVar()
    l_text.set("Number of lines : ")
    l_label = tkinter.Label(selection_window, textvariable=l_text)
    l_label.place(x=920, y=300)

    lines_number = tkinter.Entry(selection_window)
    lines_number.place(x=1050, y=300)

    s_text = tkinter.StringVar()
    s_text.set("Slowness : ")
    s_label = tkinter.Label(selection_window, textvariable=s_text)
    s_label.place(x=920, y=400)

    speed = tkinter.Entry(selection_window)
    speed.place(x=1050, y=400)

    selection_launch_button = tkinter.Button(selection_window, text="Launch", width=10, height=3, command=lambda:
                                            selection_sort_algorithm(selection_window, shuffle_list(selection_window,
                                            canvas, int(lines_number.get())), canvas, int(lines_number.get()), int(speed.get())))
    selection_launch_button.place(x=1000, y=100)

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

    selection_sort_button = tkinter.Button(sorting_window, text="Selection Sort", width=20, height=5, command=lambda: selection_display(sorting_window))
    selection_sort_button.place(x=100, y=100)

    insertion_sort_button = tkinter.Button(sorting_window, text="Insertion Sort", width=20, height=5)
    insertion_sort_button.place(x=400, y=100)

    sorting_window.mainloop()

def pathfinding_algo(win : tkinter.Tk):
    win.destroy()

    pathfinding_window = create_window('PathFinding Algorithms', '1200x900', 'black')

    pathfinding_window.mainloop()

def main():
    main_window = create_window("Algorithm Visualisation App (made by Alex Bataille)", "1200x900",
                                "black")


    sorting_button = tkinter.Button(main_window, text="Sorting", width=20, height=5,
                                   command=lambda: sorting_algo(main_window))
    sorting_button.place(x=100, y=100)

    path_finding_button = tkinter.Button(main_window, text="PathFinding", width=20, height=5,
                                       command=lambda: pathfinding_algo(main_window))
    path_finding_button.place(x=400, y=100)

    main_window.mainloop()


if __name__ == "__main__":
    main()
