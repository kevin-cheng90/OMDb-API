# controller.py
import model as m
import view as v


class Controller():
    def __init__(self):
        self.connection = m.Connect()
        self.view = v.View()
        self.saved_ep = []

    def gui_episodes(self):
        # Uses tkinter to get an input from the user
        # specifying the series name, then gathers information
        # about every episode in the series
        self.view.get_series()
        self.connection.take_input(self.view.return_series())
        self.connection.get_total_seasons()
        self.connection.get_episodes()

    def gui_display_ep(self):
        # Displays episodes on the screen and
        # allows users to select the ones they want saved
        self.view.display_episodes(self.connection.return_episodes())
        self.saved_ep = self.view.return_saved()
        self.connection.gather_info(self.saved_ep)

    def gui_print_selected(self):
        # Prints the title, episode number, season number, and plot in
        # tkinter
        self.view.display_saved_info(self.connection.return_saved_info())

    def gui_file_handling(self):
        # Uses tkinter to get a file from the user and passes it to
        # the model. The model then saves the file in the desired location.
        self.view.get_filename()
        self.connection.handle_saved(self.view.return_file())


if __name__ == '__main__':
    a = Controller()
    a.gui_episodes()
    a.gui_display_ep()
    a.gui_file_handling()
    a.gui_print_selected()
