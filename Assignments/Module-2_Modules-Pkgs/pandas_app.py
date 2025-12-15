import pandas


data={
    "id":[1,2,3,4,5],
    "name":["sanket","ashok","hitesh","darshan","gopal"],
    "city":["rajkot","baroda","surat","ahmedabad","navsari"]
}

#print(data)
dt=pandas.DataFrame(data)
print(dt)
