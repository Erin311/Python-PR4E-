'''
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
'''
# Use the file name mbox-short.txt as the file name box.txt
average = 0.0
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
		continue    
    aux = line[20:27]
    aux1 = float(aux)            			
    average = average + aux1
    #print aux1
print "Average spam confidence:", float(average/27)
#X-DSPAM-Confidence: 0.6178
