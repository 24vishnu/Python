#Program for read the data from json file and print all data

import InventryDataManagementBL as IFM_obj

data = IFM_obj.read_File()
IFM_obj.print_data(data)
# IFM_obj.print_toal_price(data)