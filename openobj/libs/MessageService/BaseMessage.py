class BaseMessage(object):
    to_user = ""
    from_user = ""
    subject = ""
    body = ""

    def send(self):
        raise Exception("You must override this function in subclass.")
