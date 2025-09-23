from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class CalculatorApp(App):
    def build(self):
        Window.clearcolor = (0.9, 0.9, 0.9, 1)

        main_layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

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

        buttons_layout = GridLayout(cols=4, spacing=5, size_hint_y=0.8)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '+',
            'del', '='
        ]

        for button_text in buttons:
            btn_color = (0.7, 0.7, 0.7, 1)
            text_color = (0, 0, 0, 1)

            if button_text in '+-*/C':
                btn_color = (0.8, 0.5, 0.2, 1)
            elif button_text == '=':
                btn_color = (0.2, 0.5, 0.8, 1)
                text_color = (1, 1, 1, 1)
            elif button_text == 'del':
                btn_color = (0.8, 0.5, 0.2, 1)

            btn = Button(
                text=button_text,
                font_size='30sp',
                background_normal='',
                background_color=btn_color,
                color=text_color
            )
            btn.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(btn)

        main_layout.add_widget(buttons_layout)
        return main_layout

    def on_button_press(self, instance):
        button_text = instance.text
        current_solution = self.solution.text

        if button_text == 'C':
            self.solution.text = "0"
            return
        
        if button_text == 'del':
            self.solution.text = current_solution[:-1] if len(current_solution) > 1 and current_solution != "Error" else "0"
            return

        if button_text == '=':
            if not any(op in current_solution for op in '+-*/'):
                return
            try:
                result = str(eval(current_solution))
                self.solution.text = result
            except (SyntaxError, ZeroDivisionError, NameError):
                self.solution.text = "Error"
            return

        if current_solution == "0" or current_solution == "Error":
            self.solution.text = button_text
        else:
            self.solution.text += button_text

if __name__ == '__main__':
    CalculatorApp().run()
