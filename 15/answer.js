let factors = {
  a: 16807,
  b: 48271
}

let current = {
  a: 116,
  b: 299
}

let divisor = Math.pow(2, 31) - 1

let count = 0

/*for (let _ = 0; _ < 40000000; _++) {
  current.a = (Factors.a*current.a)%divisor
  current.b = (Factors.b*current.b)%divisor

  let a = current.a.toString(2).slice(-16)
    , b = current.a.toString(2).slice(-16)
  if (a === b) count++
}
console.log(count)*/

count = 0

for (let _ = 0; _ < 5000000; _++) {
  while (true) {
    current.a = (factors.a*current.a)%divisor
    if (current.a % 4 !== 0) break;
  }
  while (true) {
    current.b = (factors.b*current.b)%divisor
    if (current.b % 8 !== 0) break;
  }
  let a = current.a.toString(2).slice(-16)
    , b = current.b.toString(2).slice(-16)
  if (a === b) count++
}
console.log(count)