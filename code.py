# Importation des modules nécessaires
from time import strftime
from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# Définition de la classe principale de l'application Kivy
class clockApp(App):
    # Variables de classe
    sw_started = False   # Indique si le chronomètre est en cours d'exécution
    sw_seconds = 0       # Le nombre total de secondes écoulées depuis le démarrage du chronomètre

    # Méthode appelée à intervalles réguliers pour mettre à jour le temps
    def update_time(self, nap):
        # Si le chronomètre est en cours d'exécution, incrémenter le temps écoulé
        if self.sw_started:
            self.sw_seconds += nap

        # Convertir le temps total en minutes, secondes et centièmes de seconde
        minutes, seconds = divmod(self.sw_seconds, 60)

        # Mettre à jour le texte du chronomètre avec le temps formaté
        self.root.ids.stopwatch.text = (
            '%02d:%02d.[size=40]%02d[/size]' %
            (int(minutes), int(seconds), int(seconds * 100 % 100))
        )

        # Mettre à jour le texte de l'horloge avec l'heure actuelle formatée
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')

    # Méthode appelée au démarrage de l'application
    def on_start(self):
        # Planifier la mise à jour régulière du temps en utilisant Clock
        Clock.schedule_interval(self.update_time, 0)

    # Méthode appelée lorsqu'on appuie sur le bouton "Start/Stop"
    def start_stop(self):
        # Changer le texte du bouton en fonction de l'état du chronomètre
        self.root.ids.start_stop.text = (
            'Start' if self.sw_started else 'Stop'
        )

        # Inverser l'état du chronomètre
        self.sw_started = not self.sw_started

    # Méthode appelée lorsqu'on appuie sur le bouton "Reset"
    def reset(self):
        # Si le chronomètre est en cours d'exécution, le stopper
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False

        # Réinitialiser le temps du chronomètre
        self.sw_seconds = 0

# Point d'entrée pour l'exécution de l'application
if __name__ == '__main__':
    # Définir la couleur de fond de la fenêtre
    Window.clearcolor = get_color_from_hex('#101216')

    # Enregistrer la police de caractères Roboto avec les fichiers correspondants
    LabelBase.register(
        name='Roboto',
        fn_regular='Roboto-Thin.ttf',
        fn_bold='Roboto-Medium.ttf'
    )

    # Lancer l'application Kivy
    clockApp().run()
