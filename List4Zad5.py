from enum import Enum

class Status(Enum):
    ACTIVE =0
    STOPPED = 1
    FINISHED = 2


class Proces() :
    def __init__(self, id: int, cpu_usage: int, status: Status):
        self.id = id
        self.cpu_usage = cpu_usage
        self.status = status
    
    def set_status(self,s: Status) ->None:
        self.status = s
    
    def get_status(self) ->Status:
        return self.status
    
    def get_cpu_usage(self) -> int:
        return self.cpu_usage
    
    def get_id(self) -> int:
        return self.id



class ProcessManager():
    def __init__(self):
        self.list_of_processes = []

    def add_new_process(self,p: Proces) ->None:
        self.list_of_processes.append(p)
    
    def delete_process(p: Proces) ->None:
        self.list_of_processes.remove(p)

    def get_process_by_id(id: int) -> Proces:
        for i in self.list_of_processes:
            if i.get_id() == id :
                return i

    def stop_process(id: int) ->None:
        for i in self.list_of_processes:
            if i.get_id() == id:
                i.set_status(Status(1))

    def kill_process(id: int) ->None:
        for i in self.list_of_processes:
            if i.get_id() == id:
                i.set_status(Status(2))
    
    def run_process(id: int) ->None:
        for i in self.list_of_processes:
            if i.get_id() == id:
                i.set_status(Status(0))
    
    def print_all_process(self) ->None:
        for i in self.list_of_processes :
            status =""
            if i.get_status() == Status(0):
                status = "ACTIVE"
            elif i.get_status() == Status(1):
                status = "STOPPED"
            else:
                status = "FINISHED"
            print("Proces id: " + str(i.get_id()) + ", proces status: " + status +", cpu usage: " + str(i.get_cpu_usage()))

pm = ProcessManager()
for i in range(0,10):
    p = Proces(i,2*i,Status(i%3 ))
    pm.add_new_process(p)
pm.print_all_process()