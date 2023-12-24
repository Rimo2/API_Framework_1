
BASE_URL = "https://restful-booker.herokuapp.com/"
def base_url():
    return "https://restful-booker.herokuapp.com/"

class APIConstants(object):
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com/"

    def base_url_nonStatic(self):
        return "https://restful-booker.herokuapp.com/"
    @staticmethod
    def createToken_url():
        return "https://restful-booker.herokuapp.com/auth"

    @staticmethod
    def createBooking_url():
        return "https://restful-booker.herokuapp.com/booking"


    def patch_put_delete_url(self,bookingId):

        return "https://restful-booker.herokuapp.com/booking/" + str(self.bookingId)