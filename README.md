# distributed_horse_rider
An intuitive simple working example of tensorflow distributed!

In a nutshell
---



Usage
---
Launch two horse.py with task_index arguments 0 and 1 respectively, and similarly two rider.py.
Launching them in separate windows for a better demonstration.
  
    python3.5 -m distributed_horse_rider.horse 0
    python3.5 -m distributed_horse_rider.horse 1
    python3.5 -m distributed_horse_rider.rider 0
    python3.5 -m distributed_horse_rider.rider 1

Or, for more convenience, execute the [launch_distributed_horse_riders.sh](https://gist.github.com/reubenjohn/b714de7b47202a379642e30fd97e5853).