import psutil
import os
import datetime
import argparse
import json
import time
from collections import Counter


class SystemMonitor:
    #initializes the object that holds parsed argument values
    def __init__(self, args):
        self.args = args
        self.args.i = int(self.args.i)
        self.args.n = int(self.args.n)
    
    #counts the number of processes running on a system and collects them based on their current status
    def processes_stats(self):
        status_count = Counter()
        for proc in psutil.process_iter(['status']):
            try:
                status = proc.info['status']
                status_count[status] += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        mapped = {
            "running": int(status_count.get(psutil.STATUS_RUNNING, 0)),
            "sleeping": (
                int(status_count.get(psutil.STATUS_SLEEPING, 0)) + 
                int(status_count.get(psutil.STATUS_IDLE, 0)) + 
                int(status_count.get(psutil.STATUS_WAITING, 0))
            ),
            "stopped": int(status_count.get(psutil.STATUS_STOPPED, 0)),
            "zombie": int(status_count.get(psutil.STATUS_ZOMBIE, 0))
        }

        total = sum(mapped.values())
        return  {
                "total": total,
                "running": mapped["running"],
                "sleeping": mapped["sleeping"],
                "stopped": mapped["stopped"],
                "zombie": mapped["zombie"]
                }
    
    #calculates the workload of the cpu
    def cpu_stats(self):
        cpu_load = psutil.cpu_times_percent(interval=0, percpu=False)
        return {
            "user": cpu_load.user,
            "system": cpu_load.system,
            "idle": cpu_load.idle
        }
    
    #calculates the workload of the virtual memory
    def mem_stats(self):
        mem = psutil.virtual_memory()
        return{
            "total": mem.total,
            "free": mem.free,
            "used": mem.used
        }

    #calculates the workload of the swap memory
    def swap_stats(self):
        swap = psutil.swap_memory()
        return{
            "total": swap.total,
            "free": swap.free,
            "used": swap.used
        }
    
    #calculates the timestamp of the current timestamp
    def make_timestamp(self):
        current_datetime = datetime.datetime.now()
        timestamp = current_datetime.timestamp()
        return int(timestamp)
    
    #groups collected data in the dictionary
    def collect_snapshot(self):
        snapshot = {}
        snapshot["Tasks"] = self.processes_stats()
        snapshot["%CPU"] = self.cpu_stats()
        snapshot["KiB Mem"] = self.mem_stats()
        snapshot["KiB Swap"] = self.swap_stats()
        snapshot["Timestamp"] = self.make_timestamp()

        return snapshot
        
    #runs the system and writes its performance data to both json file and stdout
    def run(self):
        with open(self.args.f, "w") as file:
            pass

        for _ in range(self.args.n):
            current_snapshot = self.collect_snapshot()

            os.system('clear')
            print(json.dumps(current_snapshot, indent=2))

            with open(self.args.f, "a") as file:
                json.dump(current_snapshot, file, indent=2)
                file.write("\n")
            
            time.sleep(self.args.i)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=30)
    parser.add_argument("-f", help="Output file name", default="snapshot.json")
    parser.add_argument("-n", help="Quantity of snapshot to output", default=20)

    args = parser.parse_args()

    sm = SystemMonitor(args)
    sm.run()



    

