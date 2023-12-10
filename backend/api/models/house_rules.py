class HouseRules():
    columns = [
               'host_name', 'listing_id','house_rules',
 ]

    def __init__(self,values):
        self.__dict__ = dict(zip(self.columns,values))
