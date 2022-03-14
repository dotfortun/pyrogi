import arcade


class Game(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, screen_width, screen_height, screen_title):
        # Call the parent class and set up the window
        super().__init__(screen_width, screen_height, screen_title)
        arcade.set_background_color((125, 125, 125))

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""
        self.clear()
        # Code to draw the screen goes here

    def set_mouse_platform_visible(self, platform_visible=None):
        pass
