from django_unicorn.components import UnicornView

class HelloWorldView(UnicornView):
    name = f'teste {1+2}'
