#Increase/maintain after if or for
#decrease to indicate end of block
'''
x = 5
if x > 2:
	print "Bigger than 2"
	print "Still bigger"
print "Done with 2"
for i in range(5):
	print i 
	if i > 2:
		print "Bigger than 2"
	print ("Done with i",i)
print "All Done"
'''
#Example increase
#---igger than 2
#   Still bigger
#   Done with 2
#   0
#   ('Done with i', 0)
#   1
#   ('Done with i', 1)
#   2
#   ('Done with i', 2)
#    3
#   Bigger than 2
#   ('Done with i', 3)
#   4
#   Bigger than 2
#   ('Done with i', 4)
#    All Done
#--------------------------------------------------
#Nested Decisions/Desiciones anidadas
'''
x = 42
if x > 1:
	print "More than one"
	if x < 100:
		print "Less than 100"
print "All Done"
'''
#---More than one
#   Less than 100
#   All Done
#------------------------------------
#Two-way using else:/Dos caminos usando else
'''
x = 4
if x > 2 :
	print 'Bigger'
else :
	print 'Smaller'
print 'All done'
'''
#Example
#Bigger
#All done
#------------------------------------
#Multi-way/Multiples caminos 
x = 20
if x < 2 :
	print 'small'
elif x < 10 :
	print 'Medium'
else :
	print 'LARGE'
print 'All done'
#Example for x = 5
#---Medium
#   All done
#Example for x = 0
#small
#All done
#x = 20 
#small 
#All done
#-----------------------------------