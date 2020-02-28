from multiprocessing import Process, Event, Queue

class Concurrent_Process:	
	# Constructor
	def __init__(self, ftn=None, name='PROC'):
	# ftn: A function pointer, called for handling queue items
	# queue: Queue instance, contains elements/inputs to process
	# signal_queue: Event instance, used to signal when queue has elements
	# signal_exit_now: Event instance, used to signal to exit process immediately
	# signal_exit: Event instance, used to exit process after queue empty
	# process: Process, spawned in start()
	# name: String, for logging/debugging purposes
		self.ftn = ftn
		self.queue = Queue()
		self.signal_queue = Event()
		self.signal_exit_now = Event()
		self.signal_exit = Event()
		self.process = Process(target=self.process_main)
		self.name = name
	
	# Push item to queue
	def push_to_queue(self, item=None):
		if item:
			self.queue.put(item)
			self.signal_queue.set() # Signal that queue has item
	
	# Start the process
	def start(self):
		print('[{}] Start'.format(self.name))
		self.process.start()
	
	# Main process loop
	# Process all items on queue
	# If queue is empty, wait for items to be pushed onto queue
	# Exit only when signaled by stop()/stop_now()
	def process_main(self):
		while True:
			if self.queue.empty():
				# Exit if exit signal true, set by stop()
				if self.signal_exit.is_set():
					return
				# Wait for queue to have item
				print('[{}] Wait for queue...'.format(self.name))
				self.signal_queue.wait()
				self.signal_queue.clear()
				
			# Exit if exit signal is true, set by stop_now() or stop()
			if self.signal_exit_now.is_set() or\
			   self.queue.empty() and self.signal_exit.is_set():
				return

			# Pop queue and process item with ftn
			if not self.queue.empty():
				item = self.queue.get()
				print('[{}] Popped queue: {}'.format(self.name, item))
				try:
					self.ftn(item, self.name)
				except Exception as e:
					print('[{}] Exception: {}'.format(self.name, e))
	
	# BLOCK for process
	def wait(self):
		self.process.join()
	
	# Exit the process only when queue is empty
	def stop(self):
		self.signal_exit.set()
		self.signal_queue.set()
	
	# Exit the process even if items still on queue
	def stop_now(self):
		self.signal_exit_now.set()
		self.signal_queue.set()
