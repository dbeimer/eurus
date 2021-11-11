import gi

gi.require_version("Gtk","3.0")
gi.require_version("Handy","1")

from gi.repository import Gtk,Gdk
from gi.repository import Handy as hdy

# recognition
import speech_recognition as sr


hdy.init()
gtk_settings=Gtk.Settings.get_default ()
gtk_settings.props.gtk_application_prefer_dark_theme=True
# print(dir(gtk_settings.props))

css_provider =Gtk.CssProvider()
css_provider.load_from_path("style.css")
Gtk.StyleContext.add_provider_for_screen (Gdk.Screen.get_default (), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

win = hdy.Window(default_width=300)
win.connect("destroy", Gtk.main_quit)

grid=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
first_row=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, margin=20)
# print(dir(win.props))

# for index,name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name {} found for Microphone(device_index{})".format(name,index))

mic=sr.Microphone()
recog=sr.Recognizer()
# print(sr.Microphone.list_microphone_names())


def activa_reconocimiento(button):
    with mic as audio_file:

        label.set_text("Escuchando ...")
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)

        # print("Converting Speech to Text...")
        reconocio= recog.recognize_google(audio,language='es-PE')
        label.set_text(reconocio)

header=hdy.HeaderBar(show_close_button=True)
button=Gtk.Button(label="Escucha")
button.connect("clicked",activa_reconocimiento)
label= Gtk.Label("Active el reconocimiento")
label.set_line_wrap(True)
label.set_max_width_chars(30)
label.set_margin_bottom(20)

first_row.add(label)
first_row.add(button)

header_context=header.get_style_context()
header_context.add_class("default-decoration")
header_context.add_class(Gtk.STYLE_CLASS_FLAT)

grid.add(header)
grid.add(first_row)

win.add(grid)

win.show_all()
Gtk.main()

