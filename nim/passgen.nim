##Passgen 0.1 for Nim 0.18.0
import os, strutils, hashes, random, sequtils, typeinfo
#Compiler options
{.deadCodeElim:on, checks:off, hints:off, warnings:off.}

var
  asciiLow = @["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  asciiUp = @["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  digitGen = @["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
  hashGen = newSeq[string](0)
  asciiGen: seq[string]
  asciiCat: seq[string]
let hashLen = commandlineParams()

asciiGen = @[]
asciiCat = @[]

proc cmdArgs() =
  if hashLen.len() > 2:
    echo "Invalid argument detected"
    quit()
  elif hashLen.len() != 2:
    echo "Invalid argument detected"
    quit()
  else:
    let charGen = commandLineParams()
    if charGen[0] == "-u":
      for i in asciiUp:
        asciiGen.add(i)
    elif charGen[0] == "-l":
      for i in asciiLow:
        asciiGen.add(i)
    elif charGen[0] == "-d":
      for i in digitGen:
        asciiGen.add(i)
    elif charGen[0] == "-ul":
      asciiCat = concat(asciiLow, asciiUp)
      for i in asciiCat:
        asciiGen.add(i)
    elif charGen[0] == "-ud":
      asciiCat = concat(asciiUp, digitGen)
      for i in asciiCat:
        asciiGen.add(i)
    elif charGen[0] == "-ld":
      asciiCat = concat(asciiLow, digitGen)
      for i in asciiCat:
        asciiGen.add(i)
    elif charGen[0] == "-uld":
      asciiCat = concat(asciiLow, asciiUp, digitGen)
      for i in asciiCat:
        asciiGen.add(i)
    else:
      echo "command unknown"
      echo "Valid commands: -u, -l, -d, -ul, -ud, -ld, -uld"
      quit()
    if parseInt(hashLen[1]) <= 0:
      echo "Invalid hash length"
      quit()
    else:
      echo ""

proc delHash =
  while hashGen.len != 0:
    for i, x in hashGen:
      hashGen.delete(i)
      break

proc genHash(): string {.discardable.} =
  randomize()
  var v = 0
  for v in countup(0, parseInt(hashLen[1]) - 1):
    shuffle(asciiGen)
    hashGen.add(asciiGen[v])
  let hashString = join(hashGen)
  echo hashString
  delHash()

proc main {.discardable.} =
  cmdArgs()
  while true:
    type KeyboardInterrupt = object of Exception
    proc handler() {.noconv.} =
      echo "Ctrl + C detected quitting...\n"
      quit()
    setControlCHook(handler)
    genHash()
main()
