my_dict={1:"apel",2:"jeruk",3:"rambutan",4:"semangka",10:"jeruk"}
print("Data original dictionary:\n",my_dict)



def tambah(dictionary, key, value):
    dictionary[key] = value



tambah(my_dict,5,"manggis")
print("Data baru dictionary adalah:\n",my_dict)
#function to remove key_value
def hapuskey(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    else:
        print(f"The key '{key}' does not exist in the dictionary.")
        
hapuskey(my_dict, 2)
print("Data baru dictionary adalah:\n",my_dict)
hapuskey(my_dict, 2)
print("Data baru dictionary adalah:\n",my_dict)