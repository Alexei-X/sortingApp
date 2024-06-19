import tkinter
import random
import time


def selection_sort_algorithm(win: tkinter.Tk, numb_list: list[int], canvas, max_size: int, speed: int = 0):
    for i in range(len(numb_list) - 1):
        current_minimum = i
        for j in range(i + 1, len(numb_list)):
            if numb_list[j] < numb_list[current_minimum]:
                current_minimum = j
        display_list(numb_list, canvas, max_size, current_minimum)
        numb_list[i], numb_list[current_minimum] = numb_list[current_minimum], numb_list[i]
        win.update()
        time.sleep(speed * 0.001)


def insertion_sort_algorithm(win: tkinter.Tk, numb_list: list[int], canvas, max_size: int, speed: int = 0):
    for i in range(1, len(numb_list)):
        save = numb_list[i]
        j = i - 1
        while j >= 0 and numb_list[j] > save:
            numb_list[j + 1] = numb_list[j]
            j -= 1
        numb_list[j + 1] = save
        display_list(numb_list, canvas, max_size, j + 1)
        win.update()
        time.sleep(speed * 0.001)


def create_sorting_window(title: str, dimensions: str, sort_type: str) -> tkinter.Tk:
    win = create_window(title, dimensions, "black")

    canvas = tkinter.Canvas(win, width=900, height=900, bg="black")
    canvas.pack(side=tkinter.LEFT)

    l_text = tkinter.StringVar()
    l_text.set("Number of lines : ")
    l_label = tkinter.Label(win, textvariable=l_text)
    l_label.place(x=920, y=300)

    lines_number = tkinter.Entry(win)
    lines_number.place(x=1050, y=300)

    s_text = tkinter.StringVar()
    s_text.set("Slowness : ")
    s_label = tkinter.Label(win, textvariable=s_text)
    s_label.place(x=920, y=400)

    speed = tkinter.Entry(win)
    speed.place(x=1050, y=400)

    launch_button = tkinter.Button(win, text="Launch", width=10, height=3)
    if sort_type == "selection":
        launch_button.config(
            command=lambda: selection_sort_algorithm(win, shuffle_list(canvas, int(lines_number.get())),
                                                     canvas, int(lines_number.get()), int(speed.get())))
    elif sort_type == "insertion":
        launch_button.config(
            command=lambda: insertion_sort_algorithm(win, shuffle_list(canvas, int(lines_number.get())),
                                                     canvas, int(lines_number.get()), int(speed.get())))
    else:
        pass
    launch_button.place(x=1000, y=100)

    return win


def display_list(numb_list: list, canvas, max_size: int, current_index=None):
    canvas.delete("all")
    n = 900 / max_size if max_size != 0 else 1
    for index in range(len(numb_list)):
        color = "red" if index == current_index else "white"
        canvas.create_line(1 + round(index * n), 900, 1 + round(index * n), numb_list[index], fill=color, width=n)


def shuffle_list(canvas, max_size: int) -> list[int]:
    all_lines = []
    for i in range(1, max_size):
        all_lines.append(i)
    random.shuffle(all_lines)
    display_list(all_lines, canvas, max_size)
    return all_lines


def selection_display(win: tkinter.Tk):
    win.destroy()
    selection_window = create_sorting_window("Selection Sort", "1200x900", "selection")

    complexity_text = tkinter.StringVar()
    complexity_text.set("Complexity : O(n^2)")
    complexity_label = tkinter.Label(selection_window, textvariable=complexity_text)
    complexity_label.place(x=920, y=500)

    selection_window.mainloop()


def insertion_display(win: tkinter.Tk):
    win.destroy()

    insertion_window = create_sorting_window("Insertion Sort", "1200x900", "insertion")

    complexity_text = tkinter.StringVar()
    complexity_text.set("Complexity : O(n^2)")
    complexity_label = tkinter.Label(insertion_window, textvariable=complexity_text)
    complexity_label.place(x=920, y=500)

    insertion_window.mainloop()


def create_window(title: str, dimensions: str, bg_color: str) -> tkinter.Tk:
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


def sorting_algo(win: tkinter.Tk):
    win.destroy()

    sorting_window = create_window('Sorting Algorithms', '1200x900', 'black')

    selection_sort_button = tkinter.Button(sorting_window, text="Selection Sort", width=20, height=5,
                                           command=lambda: selection_display(sorting_window))
    selection_sort_button.place(x=100, y=100)

    insertion_sort_button = tkinter.Button(sorting_window, text="Insertion Sort", width=20, height=5,
                                           command=lambda: insertion_display(sorting_window))
    insertion_sort_button.place(x=400, y=100)

    sorting_window.mainloop()


def pathfinding_algo(win: tkinter.Tk):
    win.destroy()

    pathfinding_window = create_window('PathFinding Algorithms', '1200x900', 'black')

    pathfinding_window.mainloop()


def main():
    main_window = create_window("Algorithm Visualisation (made by Alex Bataille)", "1200x900",
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
