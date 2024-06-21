import tkinter
from Visualizer import Visualizer
from song import *
import time


def insertion_sort_algorithm(win: tkinter.Tk, numb_list: list[float], canvas, max_size: int, speed: int = 0):
    for i in range(1, len(numb_list)):
        save = numb_list[i]
        j = i - 1
        while j >= 0 and numb_list[j] > save:
            numb_list[j + 1] = numb_list[j]
            j -= 1
        numb_list[j + 1] = save
        if visualizer.sound:
            play_sound(numb_list[j], max_size)
        visualizer.display_list(numb_list, canvas, max_size, j + 1)
        win.update()
        time.sleep(speed * 0.001)
    visualizer.display_sorted_list(win, canvas, numb_list, max_size)


def selection_sort_algorithm(win: tkinter.Tk, numb_list: list[float], canvas, max_size: int, speed: int = 0):
    for i in range(len(numb_list)):
        current_minimum = i
        for j in range(i + 1, len(numb_list)):
            if numb_list[j] < numb_list[current_minimum]:
                current_minimum = j
                if visualizer.sound and j%3 == 0:
                    play_sound(numb_list[j], max_size)
        visualizer.display_list(numb_list, canvas, max_size, current_minimum)
        numb_list[i], numb_list[current_minimum] = numb_list[current_minimum], numb_list[i]
        win.update()
        time.sleep(speed * 0.001)
    visualizer.display_sorted_list(win, canvas, numb_list, max_size)


def bubble_sort_algorithm(win: tkinter.Tk, numb_list: list[float], canvas, max_size: int, speed: int = 0):
    for i in range(len(numb_list), 0, -1):
        current_min = i
        for j in range(i - 1):
            if numb_list[j] > numb_list[j + 1]:
                numb_list[j], numb_list[j + 1] = numb_list[j + 1], numb_list[j]
                current_min = j
                if visualizer.sound:
                    play_sound(numb_list[current_min], max_size)
        visualizer.display_list(numb_list, canvas, max_size, current_min)
        win.update()
        time.sleep(speed * 0.001)
    visualizer.display_sorted_list(win, canvas, numb_list, max_size)


def counting_sort_algorithm(win: tkinter.Tk, numb_list: list[float], canvas, max_size: int, speed: int = 0):
    max_val = int(max(numb_list))
    counts = [0] * (max_val + 1)
    for num in numb_list:
        counts[int(num)] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    output = [0] * len(numb_list)
    for num in reversed(numb_list):
        output[counts[int(num)] - 1] = num
        counts[int(num)] -= 1
        if visualizer.sound:
            play_sound(output[counts[int(num)]], max_size)
        visualizer.display_list(output + [0] * (len(numb_list) - len(output)), canvas, max_size, counts[int(num)])
        win.update()
        time.sleep(speed * 0.001)
    visualizer.display_sorted_list(win, canvas, output, max_size)


if __name__ == "__main__":
    visualizer = Visualizer(selection_sort_algorithm, insertion_sort_algorithm, bubble_sort_algorithm, counting_sort_algorithm)
    visualizer.main()
