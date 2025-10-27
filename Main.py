import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex

# We are forcing Kivy to use the GLES backend which is optimized for the Raspberry Pi GPU.
# This should be done before importing any other Kivy modules.
kivy.require('1.11.1') 

# Define Theme Colors (Centralized for easy changing)
THEME_COLORS = {
    'background': get_color_from_hex('#1A1A1A'), # Dark Charcoal Grey
    'primary': get_color_from_hex('#50C878'),    # Seafoam Green
    'accent': get_color_from_hex('#000000'),     # Black
    'text': get_color_from_hex('#FFFFFF'),       # White
    'dim_text': get_color_from_hex('#888888'),   # Light Grey
}

# --- Screen Definitions ---

class MainScreen(Screen):
    """The main screen displaying media content and navigation."""
    pass

class MediaManager(ScreenManager):
    """The root ScreenManager to handle different application views."""
    pass

# --- Main Application Class ---

class PiStreamOSApp(App):
    # Public properties for theme access in .kv file
    background_color = THEME_COLORS['background']
    primary_color = THEME_COLORS['primary']
    accent_color = THEME_COLORS['accent']
    text_color = THEME_COLORS['text']
    dim_text_color = THEME_COLORS['dim_text']

    # Current main category for the top bar
    current_category = StringProperty("Movies")

    def build(self):
        # Configure Window for Raspberry Pi TV display
        # We start in a maximized state for VNC, but will be fullscreen for the final OS image
        Window.maximize()
        # Window.fullscreen = 'auto' # Uncomment this for final Kiosk mode

        # Load the KV file (Kivy will look for 'pistreamos.kv' or 'ui.kv' based on app name)
        # Since we use self.root_manager, we load the ui.kv explicitly
        return MediaManager()

    def set_category(self, category_name):
        """Updates the top bar label when a new category is selected."""
        self.current_category = category_name
        # NOTE: We will add logic here later to switch the content grid based on category.

if __name__ == '__main__':
    # Set Kivy configuration to use GLES2 for Raspberry Pi
    from kivy.config import Config
    Config.set('graphics', 'fullscreen', '0') # Start in windowed mode for VNC testing
    Config.set('graphics', 'width', '1280')
    Config.set('graphics', 'height', '720')
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand') # Better touch/mouse input
    
    PiStreamOSApp().run()
