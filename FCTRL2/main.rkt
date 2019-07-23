#lang racket

(define (input)
    (read-line (current-input-port) 'any)
)

(define (factorial n)
    (if (equal? n 1) 1 (* n (factorial (- n 1))))
)



(define testsCount (string->number (input)))

(for ([test (in-range testsCount)])
    (define n (string->number (input)))
    (display (factorial n))
    (display "\n")
)