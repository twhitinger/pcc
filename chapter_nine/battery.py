class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print("This car has a {}-kWh battery.".format(self.battery_size))
        
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270 
        print("This car can go {} miles on a fully charge".format(range))
        
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            print("Upgrade to battery size {}".format(self.battery_size))
        else:
            print("Your battery cannot be upgraded past {}".format(self.battery_size))