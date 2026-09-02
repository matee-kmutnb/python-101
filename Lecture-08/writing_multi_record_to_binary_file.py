import struct

 # Get the number of records to write
num_records = int(input("How many records do you want to create? "))
 # Open a binary file for writing
with open("records.bin", "wb") as file:
 # Loop to get each record's data
 for _ in range(num_records):
 # Get data from the user
    id_num = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gpa = float(input("Enter GPA: "))
 # Pack the record into binary format
    data = struct.pack('i20sif', id_num , name.encode(), age, gpa)
 # Write the packed data to the file
    file.write(data)

print(f"{num_records} records have been written to records.bin")