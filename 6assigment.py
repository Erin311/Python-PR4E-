text = "X-DSPAM-Confidence:    0.8475";
start = text.find('0')
end = text.find('5')
number = text[start : end+1]
final = float(number)

print final