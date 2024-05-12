# fruits=["apple","orange","banana","watermelon","peach"]

# for index, val in enumerate(fruits):
#     print (index,val)

#     a=[2,6,7,5,1]
#     b=[9,6,2,5,1]

#task one
# write a python code to multilply the numbers of first list with second list
#write a python code to multiply the numbers of first list woith reverse order of second list
def calculate_discounted_price(price):
    ds=0.20
    dps= price-(price*ds)

df=[["ID","ProductName","Price","Description"],
    ["1","Dell MOouse", "500","good reliabale mouse"],
    ["2", "LCD","21000", "trusted & efficient lcd display"],
    ["2", "Mobile", "50000","reliable phone"],
    ["3","Keyboard", "500","unbreakabale keyboard"],
    ["4","laptop","80000","futuristic laptop"],
    ["5","laptop charger","1000"," used but ok"],
    ["6","monitor","25000","new features and reliable"],
    ["7","ram","1000","increase speed 2x"],
    ["8", "usb","3000","unbreakbale and efficient"],
    ["9","watch","6000","water proof"],
    ["10","tripod","6000","good quality"]]

# for i in df:
#     print(i[1])
#     print(i[3])


for product in df:
    original_price = product["Price"]
    discounted_price = original_price * 0.8  # 20% discount

    print(f"Product: {product['name']}, Original Price: {original_price}, Discounted Price: {discounted_price}, Description: {product['description']}")