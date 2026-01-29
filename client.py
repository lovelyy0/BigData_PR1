import requests


servers = [
"http://127.0.0.1:5000",
"http://127.0.0.1:5001",
"http://127.0.0.1:5002"
]

def write_value(key, value):
ok_count = 0

for s in servers:
try:
res = requests.put(f"{s}/put", json={"key": key, "value": value}, timeout=2)
if res.status_code == 200:
ok_count += 1
except:
continue

print(f"Write succeeded on {ok_count} out of {len(servers)} nodes")

def read_value(key):
for s in servers:
try:
res = requests.get(f"{s}/get", params={"key": key}, timeout=2)
if res.status_code == 200:
print("Value:", res.json()['value'])
return
except:
continue

print("Value not found on any node")

if __name__ == '__main__':
while True:
choice = input("Command (put/get/exit): ").strip().lower()

if choice == 'put':
k = input("Enter key: ")
v = input("Enter value: ")
write_value(k, v)

elif choice == 'get':
k = input("Enter key: ")
read_value(k)

elif choice == 'exit':
break
