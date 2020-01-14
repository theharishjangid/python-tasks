dict = {1:'har', 3:'xyz', 'nam':'abc'}
print(Dict)

print("Acessing a element using key:") 
print(Dict['nam']) 
  

print("Acessing a element using key:") 
print(Dict[1]) 
  

print("Acessing a element using get:") 
print(Dict.get(3)) 

del Dict[3] 
print("\nDeleting a specific key: ") 
print(Dict) 


Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict)
