def main(job_name: str, task_index: int, daemon):
	from distributed_horse_rider import horse, rider

	log = lambda message: print('%s%d\t' % (job_name[0], task_index), end='', flush=True)

	def daemon_prompt(message):
		log(message + ', waiting 1s')

	def user_prompt(message):
		input(message + ' (Press any key)')

	prompt = daemon_prompt if daemon else user_prompt
	{
		"horse": horse.main,
		"rider": rider.main
	}[job_name](task_index, log, prompt)


if __name__ == '__main__':
	import sys

	job_name_arg, task_index_arg = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else None
	main(job_name_arg, task_index_arg, False)
