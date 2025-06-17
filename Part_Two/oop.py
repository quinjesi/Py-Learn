class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Phone created: {self.brand} {self.model}")
        print('The phone brand is {} and the model is {}'.format(self.brand, self.model))
    def special_feature(self, ram, storage):
        print(f"Special feature: {self.brand} {self.model} with {ram}GB RAM and {storage}GB storage")
        print('The {} {} phone has {} gb ram and {} gb storage'.format(self.brand, self.model, ram, storage))
    def os(self, os_name):
        print(f"Operating System: {self.brand} {self.model} runs on {os_name}")
        print('The {} {} phone runs on {}'.format(self.brand, self.model, os_name))

phone = Phone('Tecno', 'Camon 20')
phone.special_feature(8, 128)
phone.os('Android 14')
