from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class ZuxQuantityConverter(App):
    def build(self):
        self.title = "Zux Quantity Converter"
        root = BoxLayout(orientation='vertical', padding=20, spacing=10)
        header_label = Label(text="Quantity Converter", font_size='24sp', size_hint_y=None, height=60)

        input_grid = GridLayout(cols=2, spacing=10)
        input_label = Label(text="Enter a value:", size_hint_y=None, height=40)
        self.input_value = TextInput(hint_text="Value", multiline=False, font_size='18sp', size_hint_y=None, height=40)
        from_unit_label = Label(text="From Unit:", size_hint_y=None, height=40)
        self.input_unit = TextInput(hint_text="Unit", multiline=False, font_size='18sp', size_hint_y=None, height=40)
        to_unit_label = Label(text="To Unit:", size_hint_y=None, height=40)
        self.output_unit = TextInput(hint_text="Unit", multiline=False, font_size='18sp', size_hint_y=None, height=40)

        input_grid.add_widget(input_label)
        input_grid.add_widget(self.input_value)
        input_grid.add_widget(from_unit_label)
        input_grid.add_widget(self.input_unit)
        input_grid.add_widget(to_unit_label)
        input_grid.add_widget(self.output_unit)

        self.convert_button = Button(text="Convert", size_hint_y=None, height=60, font_size='20sp')
        self.convert_button.bind(on_release=self.convert)
        self.output_label = Label(text="Conversion Result:", font_size='18sp', size_hint_y=None, height=60)

        root.add_widget(header_label)
        root.add_widget(input_grid)
        root.add_widget(self.convert_button)
        root.add_widget(self.output_label)

        return root

    def convert(self, instance):
        try:
            value = float(self.input_value.text)
            from_unit = self.input_unit.text.lower()
            to_unit = self.output_unit.text.lower()

            # Define conversion functions for various quantities
            conversions = {
                'meters_to_feet': lambda x: x * 3.28084,
                'feet_to_meters': lambda x: x / 3.28084,
                'celsius_to_fahrenheit': lambda x: (x * 9 / 5) + 32,
                'fahrenheit_to_celsius': lambda x: (x - 32) * 5 / 9,
                'kg_to_lb': lambda x: x * 2.20462,
                'lb_to_kg': lambda x: x / 2.20462,
                # Add more conversions here
                'liters_to_gallons': lambda x: x * 0.264172,
                'gallons_to_liters': lambda x: x / 0.264172,
            }

            conversion_key = f'{from_unit}_to_{to_unit}'
            if conversion_key in conversions:
                conversion_function = conversions[conversion_key]
                result = conversion_function(value)
                self.output_label.text = f"Conversion Result: {result:.2f} {to_unit}"
            else:
                self.output_label.text = "Invalid conversion units"
        except ValueError:
            self.output_label.text = "Invalid input value"


if __name__ == '__main__':
    ZuxQuantityConverter().run()
