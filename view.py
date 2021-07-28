# view.py
import tkinter as tk
from functools import partial


class View():
    def __init__(self):
        self.window = tk.Tk()
        self.series = ''
        self.saved = []
        self.file_name = ''

    def get_series(self):
        # Asks the user to enter a series name and
        # has the user hit submit to get the entry
        canvas = tk.Canvas(self.window, width=500, height=500)
        tk.Label(self.window, text='Enter a series name').grid(row=0)
        entry = tk.Entry(self.window)
        entry.grid(row=0, column=1)

        def get_entry():
            self.series = entry.get()
            if self.series != '':
                self.window.destroy()

        button = tk.Button(self.window, text='Submit',
                           command=get_entry)

        button.grid(row=2, column=1)
        self.window.mainloop()

    def display_episodes(self, objects: [dict]):
        # Takes information from the model and displays the episodes
        # for the user to select

        def on_configure(event):
            canvas2.configure(scrollregion=canvas2.bbox('all'))

        self.window = tk.Tk()
        canvas2 = tk.Canvas(self.window, width=600, height=600)
        canvas2.pack(side=tk.LEFT)
        # Creates a scrollbar so that the user can scroll through
        # episodes
        scrollbar = tk.Scrollbar(self.window, command=canvas2.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        canvas2.configure(yscrollcommand=scrollbar.set)
        canvas2.bind('<Configure>', on_configure)
        frame = tk.Frame(canvas2)
        canvas2.create_window((0, 0), window=frame, anchor='nw')
        formatted_episodes = []
        for items in objects:
            for x in items['Episodes']:
                ep = (x['Title'] +
                      ' :--:  Season ' + items['Season'] +
                      '  |  Episode ' + x['Episode'])
                formatted_episodes.append(ep)
        saved_episodes = []

        def callback(value):
            # callback is used to index episodes in formatted_episodes.
            # It's a command for when the button has been pressed
            # and it saves the episode selected to saved_episodes
            if formatted_episodes[value] in saved_episodes:
                pass
            elif formatted_episodes[value] not in saved_episodes:
                saved_episodes.append(formatted_episodes[value])

            if len(saved_episodes) == 5:
                self.saved = saved_episodes
                self.window.destroy()
        label = tk.Label(frame, text='SELECT 5 EPISODES')
        label.pack()
        for i in range(len(formatted_episodes)):
            action = partial(callback, i)
            b = tk.Button(frame, text=formatted_episodes[i],
                          command=action)
            b.pack(fill='both')
        frame.mainloop()

    def get_filename(self):
        # Opens tkinter and allows the user to enter a file
        # name to save the desired episodes to
        self.window = tk.Tk()
        canvas = tk.Canvas(self.window, width=500, height=500)
        tk.Label(self.window,
                 text='Enter a file name. (Include .csv) ').grid(row=0)
        entry = tk.Entry(self.window)
        entry.grid(row=0, column=1)

        # get_entry is the command for the submission button and it checks
        # if the filename entered contains .csv at the end.
        def get_entry():
            self.file_name = entry.get()
            self.file_name = self.file_name.replace(' ', '')
            if self.file_name[-4:] == '.csv':
                self.window.destroy()
        button = tk.Button(self.window, text='submit', command=get_entry)
        button.grid(row=2, column=1)
        self.window.mainloop()

    def display_saved_info(self, info: [dict]):
        # Has tkinter display the title, season number, episode number,
        # and plot of every selected episode.
        self.window = tk.Tk()
        canvas = tk.Canvas(self.window, width=500, height=500)

        for x in info:
            a1 = tk.Label(self.window,
                          text=('Title = ' + x['Title'] + ' | ' +
                                'Season = ' + x['Season'] + ' | ' +
                                'Episode = ' + x['Episode']))
            a2 = tk.Label(self.window, text='Plot: ' + x['Plot'])
            a1.pack()
            a2.pack()

    def return_file(self):
        # returns the file name for the model to use
        return self.file_name

    def return_saved(self):
        # returns the saved episodes to pass to the model
        return self.saved

    def return_series(self):
        # returns the user-entered series
        return self.series
