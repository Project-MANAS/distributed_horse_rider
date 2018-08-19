# distributed_horse_rider
An intuitive simple working example of tensorflow distributed!

In a nutshell
---
There is a caravan with:  
**2 Drivers**: Each sends whippings of increasing intensity along a whip to a less worked up horse and then measures the distance covered  
**2 Horses**: Each receives whippings from the whip and takes steps as per that whipping intensity

Under the ~~hood~~ analogies
---
 - The `whip` is shared by all drivers and horses => Shared FIFO queue of capacity 16.
 - Each whipping of a particular intensity => An integer that is enqueued by a driver
 - `flick_intensity` => TF placeholder
 - `flick_whip` => TF op to enqueue the flick_intensity
 - `feel_whip` => TF op to dequeue the flick_intensity
 - `steps_taken` => TF variable shared by all horses and riders storing total steps taken by all horses
 - `take_step` => TF op to add the dequeued flick_intensity to the shared `steps_taken` variable
 - `measure_distance` => Just a TF op representing half the number of steps taken

![distributed_horse_rider Architecture](https://image.ibb.co/nQkHvz/distributed_horse_rider_architecture.png)

Usage
---
Launch two horse.py with task_index arguments 0 and 1 respectively, and similarly two rider.py.
Launching them in separate windows for a better demonstration.
  
    python3.5 -m distributed_horse_rider.horse 0
    python3.5 -m distributed_horse_rider.horse 1
    python3.5 -m distributed_horse_rider.rider 0
    python3.5 -m distributed_horse_rider.rider 1

Or, for more convenience, execute the [launch_distributed_horse_riders.sh](https://gist.github.com/reubenjohn/b714de7b47202a379642e30fd97e5853).

Fun Fact
---
There are almost more characters in this README than code in the project XD