from kivy.uix.boxlayout import BoxLayout


class MovieList(BoxLayout):
    """Element used to display MovieListElements in a list."""
    def __init__(self, **kwargs):
        super(MovieList, self).__init__(**kwargs)
        self.orientation='vertical'
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))


