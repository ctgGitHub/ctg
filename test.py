#test.py
#!/usr/bin/python

val = 0
def test2():
	global val
	print "test begin"
	while val < 12:
		val = val + 1
		print val
	print "test end"	
	
test2()
def test1( b ):
	print b
test1(val)	