from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time
from filesharer import FileSharer


Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def start(self):
        """Starts camera and displays it in screen"""
        self.ids.camera.play = True
        self.ids.camera_switch.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """Stops camera and cleans the screen"""
        self.ids.camera.play = False
        self.ids.camera_switch.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        """Captures a frame from camera, saves an image
        with current date and time as name in images directory
        and switches to another screen, where image is displayed
        and open access to image sharing functionality"""
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f'images/{current_time}.png'
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):

    def create_link(self):
        filepath = App.get_running_app().root.ids.camera_screen.filepath
        filesharer = FileSharer(filepath=filepath)
        url = filesharer.share()
        self.ids.link.text = url


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
