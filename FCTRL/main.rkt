#lang racket



(define (input)
    (read-line (current-input-port) 'any)
)

(define (factorial n)
    (define zeros 0)

    (for ([power (in-range 1 13)]) (
        (let ([f (expt 5 power)]))

        (if (<= f n) (
            (set! power (add1 power))
            (set! zeros (floor (/ n f)))
        ) (
            (set! nEnd #f)
        ))
    ))

    zeros
)



(define testsCount (string->number (input)))

(for ([test (in-range testsCount)])
    (define n (string->number (input)))
    (display (factorial n))
    (display "\n")
)