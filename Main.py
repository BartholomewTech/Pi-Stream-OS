import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex
from kivy.config import Config # Import Config early
from kivy.lang import Builder # *** NEW: Import Builder for explicit KV loading ***

# --- Kivy Configuration for Fullscreen HDMI Output (SDL2 Fallback) ---

# Reverting to the most stable window provider for minimal OS running without X server
# We use 'sdl2' as the window provider, which worked in the previous successful launch attempts.
Config.set('graphics', 'window', 'sdl2')
Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'show_mouse', '1') 

# Requesting 1080p resolution for sharpness (optional, Kivy will scale to monitor size)
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')

# Removed egl_rpi which was causing the graphics failure.

# ------------------------------------------------------------------------

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
        # *** CRITICAL FIX: Explicitly load ui.kv as the file name doesn't match the app name. ***
        Builder.load_file('app/ui.kv') 
        
        # Ensure the window has a defined background color
        Window.clearcolor = self.background_color

        # The MediaManager instance is created and its content is defined by ui.kv
        return MediaManager()

    def set_category(self, category_name):
        """Updates the top bar label when a new category is selected."""
        self.current_category = category_name
        # NOTE: We will add logic here later to switch the content grid based on category.

if __name__ == '__main__':
    
    try:
        PiStreamOSApp().run()
    except Exception as e:
        print(f"Kivy App failed to run: {e}") # Simple print for user visibility
