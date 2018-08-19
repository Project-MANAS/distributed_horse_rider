import sys

import tensorflow as tf

spec = tf.train.ClusterSpec({
	"driver": [
		"localhost:2221",
		"localhost:2222",
		# "localhost:2223",
		# "localhost:2224",
	],
	"horse": [
		"localhost:2231",
		"localhost:2232",
		# "localhost:2233",
		# "localhost:2234",
	]
})


class Horse:
	with tf.device("/job:horse/task:0"):
		whip = tf.FIFOQueue(16, tf.int32, (), name='whip', shared_name='whip')
		feel_whip_intensity = whip.dequeue('feel_whip_intensity')
		steps_taken = tf.Variable(0, False, name='steps_taken')
		take_step = tf.assign_add(steps_taken, feel_whip_intensity, True, 'take_step')


class Rider:
	with tf.device("/job:driver/task:0"):
		flick_intensity = tf.placeholder(tf.int32, (), 'flick_intensity')
		flick_whip = Horse.whip.enqueue(flick_intensity, 'flick_whip')
		measure_distance_covered = tf.divide(Horse.steps_taken, 2, 'measure_distance_covered')


if len(sys.argv) != 2:
	raise AssertionError("Task index not specified or is not an integer")
task_index = int(sys.argv[1])
