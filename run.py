from config.bootstrap import MAIN_ROUTE
from app.core.Dispatcher import Dispatcher

def main():
    app = Dispatcher.dispatch(*MAIN_ROUTE)
if __name__ == "__main__":
    main()
