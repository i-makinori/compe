#|
# https://paiza.jp/student/challenges/183/retry


def prime_list(max):
    primes = [2]
    for i in range(2,max+1):
        if all(map(lambda n: i%n!=0, primes)):
            primes = primes + [i]

    return primes

digit = 7
primes = prime_list(10**7)

|#


(defun prime (max)
  (let ((prime-list '()))
    (loop for n from 2 to max
          do (if (every #'(lambda (num)
                            (not (= 0 (mod n num))))
                        prime-list)
                 (setq prime-list (nconc prime-list (list n)))))
    prime-list))

(defparameter *prime-list* (prime 1000000))


(defun test (primes)
  (remove-if-not #'(lambda (s)
                     (and (= (length s) 6)
                          (eq (aref s 2) #\0)
                          (eq (aref s 3) #\5)
                          (eq (aref s 4) #\1)
                          (eq (aref s 5) #\1)))
          (mapcar #'write-to-string primes)))

