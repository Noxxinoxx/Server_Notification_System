#router_notification Docs
# - Handles all the server notification calls.

class Notification_Router:
    def __init__(self, app):
        self.app = app
        self.load_routes()

    def load_routes(self):

        @self.app.get("/Noti/root")
        def read_root():
            return {"status" : "Noti route is working!"}

        @self.app.get("/Noti/WindowsData")
        def get_data_for_windows():
            #make the data and return the obj

            return 0            





