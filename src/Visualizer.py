import tkinter
import random
from song import *

class Visualizer:

    def __init__(self, selection_sort_algorithm, insertion_sort_algorithm, bubble_sort_algorithm, counting_sort_algorithm):
        self.selection_sort_algorithm = selection_sort_algorithm
        self.insertion_sort_algorithm = insertion_sort_algorithm
        self.bubble_sort_algorithm = bubble_sort_algorithm
        self.counting_sort_algorithm = counting_sort_algorithm

    sound = True

    def change_sound(self):
        if self.sound:
            self.sound = False
        else:
            self.sound = True

    def display_sorted_list(self, win: tkinter.Tk, canvas: tkinter.Canvas, numb_list: list[float], max_size: int):
        canvas.delete("all")
        n = 800 / max_size if max_size != 0 else 1
        color = "green"
        for index in range(len(numb_list)):
            canvas.create_line((index + 1) * n, 800, (index + 1) * n, 800 - numb_list[index], fill=color, width=n)
            play_sound(numb_list[index], max_size)
            if index % 5 == 0:
                win.update()

    def display_list(self, numb_list: list, canvas, max_size: int, current_index=None):
        canvas.delete("all")
        n = 800 / max_size if max_size != 0 else 1
        for index in range(len(numb_list)):
            color = "red" if index == current_index else "white"
            canvas.create_line((index + 1) * n, 800, (index + 1) * n, 800 - numb_list[index], fill=color, width=n)

    def selection_display(self, win: tkinter.Tk, selection_sort_algorithm):
        win.destroy()
        selection_window = self.create_sorting_window("Selection Sort", "1200x900",
                                                      algorithm = selection_sort_algorithm)

        complexity_text = tkinter.StringVar()
        complexity_text.set("Complexity : O(n^2)")
        complexity_label = tkinter.Label(selection_window, textvariable=complexity_text)
        complexity_label.place(x=920, y=500)

        selection_window.mainloop()

    def bubble_display(self, win: tkinter.Tk, bubble_sort_algorithm):
        win.destroy()
        bubble_window = self.create_sorting_window("Bubble Sort", "1200x900", algorithm = bubble_sort_algorithm)

        complexity_text = tkinter.StringVar()
        complexity_text.set("Complexity : O(n^2)")
        complexity_label = tkinter.Label(bubble_window, textvariable=complexity_text)
        complexity_label.place(x=920, y=500)

        bubble_window.mainloop()

    def counting_display(self, win: tkinter.Tk, counting_sort_algorithm):
        win.destroy()
        counting_window = self.create_sorting_window("Counting Sort", "1200x900", algorithm = counting_sort_algorithm)

        complexity_text = tkinter.StringVar()
        complexity_text.set("Complexity : O(n + k)")
        complexity_label = tkinter.Label(counting_window, textvariable=complexity_text)
        complexity_label.place(x=920, y=500)

        counting_window.mainloop()

    def insertion_display(self, win: tkinter.Tk, insertion_sort_algorithm):
        win.destroy()

        insertion_window = self.create_sorting_window("Insertion Sort", "1200x900",
                                                      algorithm = insertion_sort_algorithm)

        complexity_text = tkinter.StringVar()
        complexity_text.set("Complexity : O(n^2)")
        complexity_label = tkinter.Label(insertion_window, textvariable=complexity_text)
        complexity_label.place(x=920, y=500)

        insertion_window.mainloop()

    def shuffle_list(self, canvas, max_size: int) -> list[float]:
        all_lines = []
        for i in range(1, max_size + 1):
            all_lines.append(i * (800 / max_size))
        random.shuffle(all_lines)
        self.display_list(all_lines, canvas, max_size)
        return all_lines

    def create_sorting_window(self, title: str, dimensions: str, algorithm) -> tkinter.Tk:
        win = self.create_window(title, dimensions, "black")

        canvas = tkinter.Canvas(win, width=800, height=800, bg="black")
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
        launch_button.config(
            command=lambda: algorithm(win, self.shuffle_list(canvas, int(lines_number.get())),
                                        canvas, int(lines_number.get()), int(speed.get())))

        launch_button.place(x=1000, y=100)

        mute_button = tkinter.Button(win, text="Sound", width=10, height=3)
        mute_button.config(command=self.change_sound)
        mute_button.place(x=1000, y=600)

        return win

    def sorting_algo(self, win: tkinter.Tk):
        win.destroy()

        sorting_window = self.create_window('Sorting Algorithms', '1200x900', 'black')

        selection_sort_button = tkinter.Button(sorting_window, text="Selection Sort", width=20, height=5,
                                               command=lambda: self.selection_display(sorting_window, self.selection_sort_algorithm))
        selection_sort_button.place(x=100, y=100)

        insertion_sort_button = tkinter.Button(sorting_window, text="Insertion Sort", width=20, height=5,
                                               command=lambda: self.insertion_display(sorting_window, self.insertion_sort_algorithm))
        insertion_sort_button.place(x=400, y=100)

        bubble_sort_button = tkinter.Button(sorting_window, text="Bubble Sort", width=20, height=5,
                                            command=lambda: self.bubble_display(sorting_window, self.bubble_sort_algorithm))
        bubble_sort_button.place(x=700, y=100)

        counting_sort_button = tkinter.Button(sorting_window, text="Counting Sort", width=20, height=5,
                                              command=lambda: self.counting_display(sorting_window, self.counting_sort_algorithm))
        counting_sort_button.place(x=100, y=300)

        sorting_window.mainloop()

    def pathfinding_algo(self, win: tkinter.Tk):
        win.destroy()

        pathfinding_window = self.create_window('PathFinding Algorithms', '1200x900', 'black')

        pathfinding_window.mainloop()

    def create_window(self, title: str, dimensions: str, bg_color: str) -> tkinter.Tk:
        generic_window = tkinter.Tk()
        generic_window.title(title)
        generic_window.geometry(dimensions)
        generic_window.configure(bg=bg_color)
        generic_window.resizable(False, False)

        title_text = tkinter.StringVar()
        title_text.set(title)
        title_label = tkinter.Label(generic_window, textvariable=title_text, bg="black", fg="white", font=("Arial", 30))
        title_label.pack(pady=20)

        menu_button = tkinter.Button(generic_window, text="Menu",
                                     command=lambda: [generic_window.destroy(), self.main()])
        menu_button.place(x=10, y=10)
        return generic_window

    def main(self):

        main_window = self.create_window("Algorithm Visualisation (made by Alex Bataille)", "1200x900",
                                    "black")

        sorting_button = tkinter.Button(main_window, text="Sorting", width=20, height=5,
                                        command=lambda: self.sorting_algo(main_window))
        sorting_button.place(x=100, y=100)

        path_finding_button = tkinter.Button(main_window, text="PathFinding", width=20, height=5,
                                             command=lambda: self.pathfinding_algo(main_window))
        path_finding_button.place(x=400, y=100)

        main_window.mainloop()