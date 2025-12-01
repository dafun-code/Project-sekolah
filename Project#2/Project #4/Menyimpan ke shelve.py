import shelve
berkas = open("L200250028", "r")
data = berkas.readlines()
berkas.close()

s = shelve.open("data.s")
s["data"] = data
s.close()