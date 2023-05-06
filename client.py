import socket
import sys

HOST, PORT = "localhost", 9999

do_again = True
while(do_again == True):
 
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))

        print("Python DB menu\n")
        print("1. Find customer")
        print("2. Add cusotmer")
        print("3. Delete customer")
        print("4. Update customer age")
        print("5. Update customer address")
        print("6. Update customer phone")
        print("7. Print report")
        print("8. Exit\n")
        # data = " ".join(sys.argv[1:])
        num = input("Select: ")

        if(num == "1"):
            find_name = input("Customer Name: ")
            data = num + "|" + find_name
        elif(num == "2"):
            new_name = input("New customer name: ")
            new_age = input("New customer age: ")    
            new_address = input("New customer address: ")    
            new_pnumber = input("New customer phone number: ")
            data = num + "|" +new_name + "|" + new_age + "|" + new_address + "|" + new_pnumber
        elif(num == "3"):
            delete_name = input("Customer to delete: ")
            data = num + "|" + delete_name
        elif(num == "4"):
            print("Update customer age...")
            update_name = input("Enter the name you want to update: ")
            update_age = input("Enter the new age: ")
            data = num + "|"+update_name+"|"+update_age
        elif(num == "5"):
            print("Update customer address...")
            update_name = input("Enter the name you want to update: ")
            update_address = input("Enter the new address: ")
            data = num + "|"+update_name+"|"+update_address
        elif(num == "6"):
            print("Update customer phone...")
            update_name = input("Enter the name you want to update: ")
            update_phone = input("Enter the new phone number: ")
            data = num + "|"+update_name+"|"+update_phone
        elif(num == "7"):
            data = num
        else:
            data = num
            do_again = False

        sock.sendall(bytes(data + "\n","utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("\nServer response: {}".format(received))
        print("-------------------------------------")
        
sock.close()