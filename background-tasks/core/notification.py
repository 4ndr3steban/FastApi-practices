from winotify import Notification

def notify(title: str, body: str):
    toast = Notification(
        app_id="test task",
        title=title,
        msg=body,
        duration="short"
    )
    
    toast.show()
    print("test")