#!/usr/bin/env python

import random
import string as s

options ={
    "length":16,
    "lowercase":True,
    "uppercase":True,
    "digits":True,
    "punctuation":True
}
        
def rnd_string(str_in, len_out):
    str_out = ""
    for i in range(len_out-1):
        str_out += random.choice(str_in)
    return str_out

def stp_str_in(options):
    chars = s.printable[:-6]
    for key, value in options.iteritems():
        if key == "length":
            #print "Key was %s. Skipping!" % (key) 
            continue
        else:
            if not value:
                #print "Key %s has value %s" % (key, value) 
                chars = chars.replace(getattr(s, key), "")
                #print "Removed %s from string. String: %s" % (key, chars)
    return chars

def main():
    options["length"] = int(raw_input("Choose a length for your password: "))
    options["lowercase"] = True if raw_input("Do you want lowercase characters? (y/n): ") == "y" else False
    options["uppercase"] = True if raw_input("Do you want uppercase characters? (y/n): ") == "y" else False
    options["digits"] = True if raw_input("Do you want digits? (y/n): ") == "y" else False
    options["punctuation"] = True if raw_input("Do you want special characters? (y/n): ") == "y" else False
    print options
    print "Your password is: %s" % rnd_string(stp_str_in(options), options["length"])

if __name__ == "__main__":
    main()
