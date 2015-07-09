#Binary QR Thing (work in progress)

##How this started
This started out when I was solving a HackMIT2015 puzzle that gave me a decimal number with a clue that "doge loves squares" and something related to "tiles." After I looked at the binary representation of the number, I noticed that it made a perfect 21x21 square. Because the MIT puzzle last year used a QR code (ok, looking at previous puzzles might have been a tiny bit cheating), I thought maybe I could translate the binary array into a QR image. This was a quick Python program.

I thought I'd maybe expand on this and make a project (not really sure where this is going), but I did some Googling and there's a CrackMIT git repo that actually does the same thing. So I'm going to rewrite my original program in Go and see where this goes.

Update: I moved from one "whoa, it'd be cool if I made this thing" to the next and have decided to make a very inefficient and bad QR compression program.

##Current usage
* `./encode` looks for a `input.png` file (your QR code) and compresses it to a `output.txt` file. 
* `./decode` looks for a `input.txt` file and returns a `output.png`. 
* You can test this compression with `./test`, which diffs the two files.

##Compression rate
Still being reduced. 
