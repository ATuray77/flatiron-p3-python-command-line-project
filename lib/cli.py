from prettycli import red
from simple_term_menu import TerminalMenu
from models import Artist, Song
from banners import Banner
# if __name__ == "__main__":
#     user_input =  input("What's your name?")
#     print(user_input)

class Cli():

    def __init__(self):
        self.current_user = None
        self.current_user = None
    
    def start(self):
        self.clear(40)
        banners.welcome()
        self.clear(4)
