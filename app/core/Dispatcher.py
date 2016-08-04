from importlib import import_module

class Dispatcher(object):
    """ Basic routing functionallity

    Args:
        controller: The name of the controller
                    without the 'Controller' part
        action: The method to be called from the controller
        *args: Any arguments the controller's method requires

    Returns:
        Route class with the controller as base
    """
    @staticmethod
    def dispatch(controller, action, *args):
        module = import_module("app.controllers.%sController" % controller)
        class_ = getattr(module, "%sController" % controller)

        class Route(class_):
            def __init__(self, action, *args):
                super().__init__()
                self.__getattribute__(action)(*args)

        return Route(action, *args)
