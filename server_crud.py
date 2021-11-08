import Pyro4, Pyro4.naming

database = [] #inialize empty local DB

@Pyro4.expose
class FunctionsCrud():
    def create(self, data):
        id = data['id']
        try:
            info = [item for item in database if item['id'] == int(id)][0]
            resp = 'INVALID ID (' + str(id) + ')'
        except:

            database.append(data)  
            resp = 'CREATED: ' + str(data)
        return resp

    def read(self, id):
        try:
            info = [item for item in database if item['id'] == int(id)][0]
            resp = str(info)
        except:
            resp = 'INVALID ID (' +str(id) + ')'
        return resp
    
    def update(self,data):
        id = data['id']
        try:
            info = [item for item in database if item['id']== int(id)][0]
            name = data['name']
            duration = data['duration']
            director = data['director']
            info['name'] = name
            info['duration'] = duration
            info['director'] = director
            resp = 'UPDATED TO ' + str(info)
        except:
            resp = 'INVALID ID (' + str(id) + ')'
        return resp

    def delete(self, id):
        try:
            info = [item for item in database if item['id'] == int(id)][0]
            resp = 'ID ' + str(id) + ' DELETED'
            database.pop(database.index(info))
        except:
            resp = 'INVALID ID (' + str(id) + ')' 
        return resp


def main():
    
    crud = FunctionsCrud()

    daemon = Pyro4.Daemon()

    uri = daemon.register(crud)
    print("Published")

    ns = Pyro4.locateNS()
    ns.register("PedroRenan", uri) #Name utilized just for identification on class, do not replicate

    print("Registered item") 
    
    daemon.requestLoop()

if __name__ == "__main__":
    main()