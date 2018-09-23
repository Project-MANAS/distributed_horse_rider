import tensorflow as tf

from distributed_horse_rider.start_cluster import cluster_dict

spec = tf.train.ClusterSpec(cluster_dict)

config = tf.ConfigProto()
config.gpu_options.allow_growth = True


class Horse:
	with tf.device("/job:horse/task:0"):
		whip = tf.FIFOQueue(16, tf.int32, (), name='whip', shared_name='whip')
		feel_whip_intensity = whip.dequeue('feel_whip_intensity')
		steps_taken = tf.Variable(0, False, name='steps_taken')
		take_step = tf.assign_add(steps_taken, feel_whip_intensity, True, 'take_step')


class Rider:
	with tf.device("/job:rider/task:0"):
		flick_intensity = tf.placeholder(tf.int32, (), 'flick_intensity')
		flick_whip = Horse.whip.enqueue(flick_intensity, 'flick_whip')
		measure_distance_covered = tf.divide(Horse.steps_taken, 2, 'measure_distance_covered')
