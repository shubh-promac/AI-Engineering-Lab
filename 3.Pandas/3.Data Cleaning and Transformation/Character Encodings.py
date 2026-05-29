# modules we'll use
import pandas as pd
import numpy as np
import charset_normalizer # helpful character encoding module

np.random.seed(0)

# A character encoding is a standardized system that assigns unique numeric values to human-readable characters,
# allowing computers to store, process, and transmit text.
# example like ASCII

before = "This is the euro symbol: €"
print(type(before))

after = before.encode("utf-8", errors="replace") # encoding text using UTF-8
# errors="replace", replacing characters that raise errors
print(type(after))
print(after)
print(after.decode("utf-8")) # decoding text using UTF-8
# we have to use the same encoding standards for decoding as well otherwise it won't functions
# print(after.decode("ascii")) # this will throw an error as we tried to use a different decoding standard to my encoding one

# Using ASCII
before = "This is the euro symbol: €"

# encode it to a different encoding, replacing characters that raise errors
after = before.encode("ascii", errors = "replace")
print(after.decode("ascii")) # convert it back to utf-8
# this will throw a question mark instead of a € symbol, as ASCII doesn't include that symbol so it has been replaced

df = pd.read_csv("3.Pandas/Datasets/encoding file.csv")

# look at the first ten thousand bytes to guess the character encoding
with open("3.Pandas/Datasets/encoding file.csv", 'rb') as rawdata:
    result = charset_normalizer.detect(rawdata.read(10000))

# check what the character encoding might be
print(result)

# read in the file with the encoding detected by charset_normalizer
df = pd.read_csv("3.Pandas/Datasets/encoding file.csv", encoding='utf-8')

# look at the first few lines
df.head()

df.to_csv("3.Pandas/Datasets/encoding file.csv") # saving the file's progress