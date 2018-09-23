import sys

cluster_dict = {
	'rider': [
		'localhost:2221',
		'localhost:2222',
		'localhost:2223',
		'localhost:2224',
		'localhost:2225',
		'localhost:2226',
	],
	'horse': [
		'localhost:2231',
		'localhost:2232',
		'localhost:2233',
		'localhost:2234',
		'localhost:2235',
		'localhost:2236',
		'localhost:2237',
		'localhost:2238',
	]
}

if __name__ == '__main__':
	job_tasks = [(job_name, index) for job_name, task_list in cluster_dict.items() for index in range(len(task_list))]

	if len(sys.argv) > 1 and sys.argv[1] == 'multiwindow':
		import platform
		from subprocess import Popen

		if platform.system() == "Windows":
			new_window_command = "cmd.exe /c start".split()
		else:
			new_window_command = "x-terminal-emulator -e".split()

		[Popen(new_window_command + [sys.executable, "-m", 'distributed_horse_rider.start', job_name, str(index)])
			 .wait() for job_name, index in job_tasks]
	else:
		import multiprocessing
		from distributed_horse_rider.start import main

		handles = [multiprocessing.Process(target=main, args=(job_name, index, True)) for job_name, index in job_tasks]
		for handle in handles:
			handle.daemon = True
			handle.start()
		for handle in handles:
			handle.join(5000)
