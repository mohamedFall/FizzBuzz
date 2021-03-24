class FizzbuzzChecker:

    @staticmethod
    def fizzbuzz(number):
        if(number == 0):
            raise(ValueError)
        if(number < 0):
            raise(ValueError)