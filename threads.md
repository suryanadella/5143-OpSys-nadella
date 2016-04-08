## name : shanmukh surya pratap nadella
## date : 04/08/2016
## mustang id : m20221807

## 1) Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation ?
 In Threads1.py all the instructions are atomic.An atomic operation is an operation that is carried out in a single execution step, without any chance that another thread gets control.
 In Threads2.py similar to Threads1.py except that it has a shared resource. The run() function keeps incrementing using the sharedcounter+=1
 There is a possibility of missing a change to value attribute when one thread tries to have a control on another thread.
 
## 2) After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?
 yes it fixes the problems that occured in Threads2.py as lock() has been used. in order to have control on threads during execution, Threads have to be synchronized. This is what exactly happened with Threads3.py
 when one thread acquires a lock() another thread will be waiting until lock() is released and once one thread gets executed self.lock.release() will be called and another thread can be executed.
 
## 3) Comment out the join statements at the bottom of the program and describe what happens?
 when we comment join statements, the main thread gets terminated before thread A and thread B gets terminated. The main importance of join is that when a join is being called in a function the parent thread has to wait until the child threads gets terminated.
 
## 4) What happens if you try to Ctrl-C out of the program before it terminates?
  The program gets terminated if Ctrl-C is used during execution of the program. It is known as KeyboardInterrupt. If there is any exception handler function block to handle the interrupt,thenThe program executes as usual.
  
## 5) Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation?
      global sharedNumber
      for k in xrange(10000000):
      #self.lock.acquire()
      sharedNumber = 1
        if sharedNumber != 1:
                print 'A: that was weird'
            #self.lock.release()
        print 'Goodbye from thread A'
The weird behavior is because of the lockforsharedcounter and acquire method is not being called on both the threads so the resource can be used randomly resulting in bizarre situation. 
          
          lockForSharedCounter = threading.Lock()
          threadA = ThreadClassA(lockForSharedCounter)
          threadB = ThreadClassB(lockForSharedCounter)
          
## 6) Does uncommenting the lock operations clear up the problem in question 5?
  Surely, The problem gets resolved if we uncomment the acquire lock() in both the threads so that thread A can execute first using resources and release once its done so that thread B can acquire lock and use the resources. Thus the bizarre condition gets resolved.
  The code-snippet looks like 
      
      def run(self):
        global sharedNumber
        for k in xrange(10000000):
            self.lock.acquire()
            sharedNumber = 1
            if sharedNumber != 1:
                print 'A: that was weird'
            self.lock.release()
        print 'Goodbye from thread A'



    def run(self):
        global sharedNumber
        for k in xrange(10000000):
            self.lock.acquire()
            sharedNumber = 2
            if sharedNumber != 2:
                print 'B: that was weird'
            self.lock.release()
        print 'Goodbye from thread B'

  
