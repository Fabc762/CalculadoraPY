# Importamos los módulos necesarios de Kivy para la interfaz.
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class CalculatorApp(App):
    """
    Clase principal para nuestra aplicación de calculadora.
    Hereda de kivy.app.App.
    """
    def build(self):
        """
        Este método construye y retorna la interfaz de usuario de la aplicación.
        """
        # Establecer el color de fondo de la ventana (opcional)
        Window.clearcolor = (0.9, 0.9, 0.9, 1)

        # Usamos un BoxLayout vertical como el contenedor principal.
        main_layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # Campo de texto para mostrar la entrada y el resultado.
        # Es de solo lectura para evitar que el usuario escriba.
        self.solution = TextInput(
            text="0", 
            readonly=True, 
            font_size='50sp', 
            halign="right", 
            size_hint_y=0.2,
            background_color=(0.8, 0.8, 0.8, 1),
            foreground_color=(0, 0, 0, 1),
            multiline=False
        )
        main_layout.add_widget(self.solution)

        # Un GridLayout para los botones de la calculadora.
        buttons_layout = GridLayout(cols=4, spacing=5, size_hint_y=0.8)

        # Definimos los botones que tendrá la calculadora.
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', 'C', '+',
            'del', '='
        ]

        # Iteramos sobre la lista para crear y añadir cada botón.
        for button in buttons:
            btn = Button(
                text=button, 
                font_size='30sp',
                background_normal='',
                background_color=(0.7, 0.7, 0.7, 1) if button not in '+-*/C=del' else (0.8, 0.5, 0.2, 1),
                color=(0,0,0,1)
            )
            btn.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(btn)

        # Añadimos el layout de botones al layout principal.
        main_layout.add_widget(buttons_layout)
        
        # Ajustamos el botón '=' para que ocupe 2 columnas.
        # Quitamos los últimos dos botones del grid y los añadimos manualmente
        # para que '=' ocupe el espacio de 'del' y ' ='.
        # Es una solución simple para un diseño de grid no uniforme.
        del_button = Button(
            text='del',
            font_size='30sp',
            background_color=(0.8, 0.5, 0.2, 1),
            color=(0,0,0,1)
        )
        del_button.bind(on_press=self.on_button_press)
        
        equals_button = Button(
            text='=',
            font_size='30sp',
            background_color=(0.2, 0.5, 0.8, 1),
            color=(1,1,1,1)
        )
        equals_button.bind(on_press=self.on_button_press)
        
        # Reemplazamos los últimos dos widgets para que el botón de 'del' y '=' se vean bien.
        buttons_layout.remove_widget(buttons_layout.children[1])
        buttons_layout.remove_widget(buttons_layout.children[0])
        buttons_layout.add_widget(del_button)
        buttons_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        """
        Maneja los eventos de pulsación de los botones de la calculadora.
        """
        # Obtenemos el texto del botón presionado.
        button_text = instance.text
        current_solution = self.solution.text

        # Lógica para el botón 'C' (limpiar).
        if button_text == 'C':
            self.solution.text = "0"
            return
        
        # Lógica para el botón 'del' (borrar el último carácter).
        if button_text == 'del':
            self.solution.text = current_solution[:-1] if len(current_solution) > 1 else "0"
            return

        # Lógica para el botón '=' (calcular el resultado).
        if button_text == '=':
            try:
                # Usamos la función eval() para calcular la expresión, con precauciones.
                result = str(eval(current_solution))
                self.solution.text = result
            except (SyntaxError, ZeroDivisionError, NameError):
                self.solution.text = "Error"
            return

        # Lógica para añadir el texto del botón a la pantalla.
        if current_solution == "0" or current_solution == "Error":
            self.solution.text = button_text
        else:
            self.solution.text += button_text

# Punto de entrada de la aplicación.
if __name__ == '__main__':
    CalculatorApp().run()
