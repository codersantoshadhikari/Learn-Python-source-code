## 


friends = ["Santosh", "Manish", "Hari", "Sari", "Bishwa", "Mina", "Rita", "Sachin", "Gita", "Rina"]

address = ["Pokhara", "Pokhara", "Kathmandu", "Parbat", "Baglung", "India", "Lisbon", "UK", "Australia", "Japan"]

for friend, addr in zip(friends, address):
    print(f"{friend}: {addr}")

