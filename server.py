import socketserver
from operator import itemgetter

with open("data.txt") as file:
    lines = file.readlines()
    all_clients = [tuple(line.strip().split("|")) for line in lines]

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        # convert bytes to string
        my_data = self.data.decode("utf-8")
        dataFromClient = my_data.split("|")
        isExist = False

        # 1. Find customer
        if(dataFromClient[0] == "1"):
            for each_client in all_clients:
                if(dataFromClient[1] == each_client[0]):
                    isExist = True
                    # convert list to string
                    result = '|'.join(each_client)
                    # convert string to byte
                    self.request.sendall(bytes(result+ "\n","utf-8"))
                    break
            if(isExist == False):
                self.request.sendall(bytes(dataFromClient[1] + " not found in database\n","utf-8"))

        # 2. Add customer
        elif(dataFromClient[0] == "2"):
            for each_client in all_clients:
                if(dataFromClient[1] == each_client[0]):
                    isExist = True
                    self.request.sendall(bytes("Customer already exist\n","utf-8"))
                    break
            if(isExist == False):
                dataFromClient = dataFromClient[1:5]
                asTuple = tuple(dataFromClient)
                all_clients.append(asTuple)
                self.request.sendall(bytes("New customer is added\n","utf-8"))

        # 3. Delete customer
        elif(dataFromClient[0] == "3"):
            for each_client in all_clients:
                if(dataFromClient[1] == each_client[0]):
                    isExist = True
                    all_clients.remove(each_client)
                    self.request.sendall(bytes("Removed successfully\n","utf-8"))
                    break
            if(isExist == False):
                self.request.sendall(bytes("Customer doesn't exist\n","utf-8"))
        
        # 4. Update age
        elif(dataFromClient[0]=="4"):
            for each_client in all_clients:
                if(dataFromClient[1] == each_client[0]):
                    isExist = True
                    i = all_clients.index(each_client)
                    #change tuple in list as list
                    all_clients[i] = list(all_clients[i])
                    asList = list(each_client)
                    asList[1] = dataFromClient[2]
                    all_clients[i] = tuple(asList)
                    # convert string to byte
                    self.request.sendall(bytes("You have updated the age\n","utf-8"))
                    break
            if(isExist == False):
                self.request.sendall(bytes(dataFromClient[1] + " not found in database\n","utf-8"))
        
        # 5.Update address
        elif(dataFromClient[0]=="5"):
            for each_client in all_clients:
                if(dataFromClient[1] == each_client[0]):
                    isExist = True
                    i = all_clients.index(each_client)
                    #change tuple in list as list
                    all_clients[i] = list(all_clients[i])
                    asList = list(each_client)
                    asList[2] = dataFromClient[2]
                    all_clients[i] = tuple(asList)

                    # convert string to byte
                    self.request.sendall(bytes("You have updated the address\n","utf-8"))
                    break
            if(isExist == False):
                self.request.sendall(bytes(dataFromClient[1] + " not found in database\n","utf-8"))

        #6. Update phone number
        elif(dataFromClient[0]=="6"):
            for each_client in all_clients:
                if(dataFromClient[1] == each_client[0]):
                    isExist = True
                    i = all_clients.index(each_client)
                    #change tuple in list as list
                    all_clients[i] = list(all_clients[i])
                    asList = list(each_client)
                    asList[3] = dataFromClient[2]
                    all_clients[i] = tuple(asList)
                    # convert string to byte
                    self.request.sendall(bytes("You have updated the phone number\n","utf-8"))
                    break
            if(isExist == False):
                self.request.sendall(bytes(dataFromClient[1] + " not found in database\n","utf-8"))

        # 7. Print report
        elif(dataFromClient[0] == "7"):
            sorted_list = sorted(all_clients, key = itemgetter(0))
            report ="\n\n** Python DB contents **\n"
            for a_list in sorted_list:
                list_to_str = '|'.join(a_list) + "\n"
                report += list_to_str
            self.request.sendall(bytes(report+ "\n","utf-8")) 

        # 8. Exit
        else:
            self.request.sendall(bytes("Good bye"+ "\n","utf-8")) 

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()