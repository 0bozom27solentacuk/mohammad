print("type your size (small / big / medium) : ")
size = input().lower()
print("what is weight of parcel ? (light / medium / heavy): ")
weight = input().lower()

if (size == "big") and (weight == "heavy" ):
    print("this parcel will be expensive to deliver ")
else:
    print("this parcel will be inexpensive to deliver")