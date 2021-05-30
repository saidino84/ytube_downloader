from kivy.app import App
from kivy.lang import Builder
kv = """
<Scroller@BoxLayout>:
    size_hint_y: None
    height: 40
    Label:
        size_hint_x: None
        width: 100
        text: 'Grab Me'
        font_size: 20
    ScrollView:
        do_scroll_x: True
        do_scroll_y: False
        Label:
            font_size: 20
            size_hint: None, None
            size: self.texture_size
            text: 'test-TEST' * 10

ScrollView:
    do_scroll_x: False
    do_scroll_y: True
    bar_width: 20
    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        Scroller:
        Scroller:
        Scroller:
        Scroller:
        Scroller:
        Scroller:
        Scroller:
        Scroller:
        Scroller:
        Scroller:
        Scroller:
        Scroller:
        Scroller:
        Scroller:
        Scroller:
        Scroller:
"""


class Test(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    Test().run()