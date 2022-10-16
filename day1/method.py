class Phone:
    color = 'black'
    features = ['camera', 'waterproof', 'foldable', 'dual-sim']

    """ In python class if we need to create a method then we should always give an argument even if we don't need one for the method. This is a convention, developers usually call it self for consistency. 
    Self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python."""

    def call(self):
        print("Call Function Called")

    def send_sms(self, text, number):
        sms = f'Sending SMS --> {text} to {number}'
        return sms


my_phone = Phone()
my_phone.call()

sms = my_phone.send_sms("How's it going mate?", 9999999999)
print(sms)
