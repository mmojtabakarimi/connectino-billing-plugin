from wazo_confd import bus, sysconfd


class RatingNotifier:
    def __init__(self, bus, sysconfd):
        self.bus = bus
        self.sysconfd = sysconfd

    def send_sysconfd_handlers(self):
        pass

    def created(self, rating):
        pass

    def edited(self, rating):
        pass

    def deleted(self, rating):
        pass

def build_rating_notifier():
    return RatingNotifier(bus, sysconfd)
