from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import math

class ScientificCalculator(App):

    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        equals_button = Button(text='=', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)

        scientific_functions = [
            'sqrt', 'cos', 'sin', 'tan', 'acos', 'asin', 'atan', 'log', 'ln', 'antilog', 'antiln'
        ]

        for func in scientific_functions:
            function_button = Button(text=func, pos_hint={'center_x': 0.5, 'center_y': 0.5})
            function_button.bind(on_press=self.on_scientific_function_press)
            layout.add_widget(function_button)

        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == '' and button_text in self.operators:
                return
            else:
                self.result.text = current + button_text

        self.last_was_operator = button_text in self.operators

    def on_solution(self, instance):
        text = self.result.text
        try:
            solution = str(eval(self.result.text))
            self.result.text = solution
        except Exception:
            self.result.text = 'Error'

    def on_scientific_function_press(self, instance):
        function_name = instance.text
        current = self.result.text

        if function_name in ('sqrt', 'cos', 'sin', 'tan', 'acos', 'asin', 'atan', 'log', 'ln'):
            try:
                result = str(eval(f"math.{function_name}({current})"))
                self.result.text = result
            except Exception:
                self.result.text = 'Error'
        elif function_name == 'antilog':
            try:
                result = str(10 ** float(current))
                self.result.text = result
            except Exception:
                self.result.text = 'Error'
        elif function_name == 'antiln':
            try:
                result = str(math.e ** float(current))
                self.result.text = result
            except Exception:
                self.result.text = 'Error'

if __name__ == '__main__':
    app = ScientificCalculator()
    app.run()