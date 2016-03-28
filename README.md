#mincemeatpy hw4

- Math stats - mathstats.py -  Given a text file name on the command-line containing one number per line, print out the sum, count, and standard-deviation of all the numbers in the file.  All statistics should be found in one pass through the data.

- Palendrome prime number finder - primes.py -  Output all the prime numbers which are palindromes between 2 and 10 million.  A palindrome number is one which when read backwards is the same value.  Ex. 919 is prime and a palindrome.  

- Password cracking - passCrack.py - Given a string of characters on the command line, find what string hashes to it.  Passwords are sometimes stored in a hashed form, so if the database is breached, the passwords are not easily usable. For this assignment, assume we have a hash of a password in hex form.  Given this hash on the command line, find what password hashes to it.  Only the first 5 characters of the hash are checked.  Assume passwords are 4 or fewer characters containing only lowercase letters and numbers.  Use MapReduce to quickly look through all combinations for a match.  Print out the input hash string and the valid passwords which hash to it, if any.  Use hashlib md5 hexdigest()and use the first 5 characters.  Here are some passwords to crack: d077f, 0832c, 1a1dc, ee269, 0fe63

To genereate a list of random numbers, I used "gennumber.py". Just need to pass as parameter the amount of numbers you want to generate. 
