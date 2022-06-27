


from enum import unique
from itertools import count
from operator import ne


list_of_dic = [
{'Pallet ID': '3822-153-08-S04-B', 'USCS PID': '3822-15', 'Lot Number': '88469', 'Quantity': '20'}, 
{'Pallet ID': '6622-153-13-S02-F', 'USCS PID': '6622-15', 'Lot Number': '89102', 'Quantity': '13'}, 
{'Pallet ID': '6622-153-13-S03-C', 'USCS PID': '6622-15', 'Lot Number': '89102', 'Quantity': '14'}, 
{'Pallet ID': '6622-153-13-S04-B', 'USCS PID': '6622-15', 'Lot Number': '89102', 'Quantity': '15'}, 
{'Pallet ID': '6622-154-13-S05-E', 'USCS PID': '6622-15', 'Lot Number': '90348', 'Quantity': '16'},
{'Pallet ID': '3822-150-05-S01-D', 'USCS PID': '3822-15', 'Lot Number': '00259', 'Quantity': '17'}, 
{'Pallet ID': '3822-156-02-S03-E', 'USCS PID': '3822-15', 'Lot Number': '91584', 'Quantity': '18'}, 
{'Pallet ID': '3822-156-02-S03-F', 'USCS PID': '3822-15', 'Lot Number': '91365', 'Quantity': '19'}, 
{'Pallet ID': '3822-156-05-S01-A', 'USCS PID': '3822-15', 'Lot Number': '96200', 'Quantity': '12'}, 
{'Pallet ID': '3822-156-05-S01-B', 'USCS PID': '3822-15', 'Lot Number': '96200', 'Quantity': '15'}]


def prod_combine():
    combine_list = []

    for items in list_of_dic:
        lot = items.get("Lot Number")
        qty = items.get("Quantity")
       
        combine_list.append((lot, qty))
    print(combine_list)
    
    merged_list = {}
    
    for key, val in combine_list:
        #merged_list = {}
        #print(key)
        #print(val)
        #print(type(key))
        #print(type(val))        
        
        if len(merged_list) == 0:
            merged_list[key] = val

            print(merged_list)
            

        elif merged_list.get(key) == None:
            #print("Key not Found")
            #print(merged_list.get(key))
            merged_list[key] = val
            
        
        elif merged_list.get(key):
            print("Already in list")
            print(merged_list.get(key))
            current = merged_list.get(key)
            former = combine_list.get(key)

            print(former)
            print(current)
            



        #elif merged_list.get(lot_num):
            #new = merged_list.get(lot_num)
            #new = int(new + value)

            #old_val = lot_num.get(lot_num)
            #print("This is the old Value: " + str(old_val))
            #merged_list[lot_num] = merged_list.update(merged_list.items() + value)
            


        print(merged_list)
        #print(new_list)
        #if items[0] == 


prod_combine()

#print(list_of_dic[1])