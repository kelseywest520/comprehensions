str= ("List Comprehensions are the Greatest!")
str= str.replace("i"," ")
str= str.replace("e"," ")
str= str.replace("o"," ")
str= str.replace("a"," ")

print(str)
test = ['26.5', '26.2', '26.2', '26.2', '26.5', '26.7', '27.0', '26.9', '27.1',
'27.0', '26.9', '26.8', '26.9', '27.1', '27.1', '27.2', '27.5', '27.6',
'28.1','27.5', '27.7', '27.4', '27.4', '28.0', '28.7', '28.9', '28.5',
'28.1', '27.8']

converted_to_float = []
for item in test:
    change = float(item)
    converted_to_float.append(change)
print(converted_to_float)


farenheit = []

for item in converted_to_float:
    farenheit_temperature= int(item * 1.8 + 32)
    farenheit.append(farenheit_temperature)
print(farenheit)


date= ["2015-08-01, 2015-08-02, 2015-08-03, 2015-08-04, 2015-08-05, 2015-08-06, 2015-08-07, 2015-08-08, 2015-08-09, 2015-08-10, 2015-08-11, 2015-08-12, 2015-08-13, 2015-08-14, 2015-08-15, 2015-08-16, 2015-08-17, 2015-08-18, 2015-08-19, 2015-08-20, 2015-08-21, 2015-08-22, 2015-08-23, 2015-08-25, 2015-08-26, 2015-08-27, 2015-08-28, 2015-08-29, 2015-08-30, 2015-08-31"]

wave_height= ["1.55, 1.97, 1.5, 1.72, 2.14, 2.2, 1.8, 1.99, 1.81, 1.8, 1.75, 1.6, 1.43, 1.51, 1.54, 1.52, 1.47, 1.71, 2.02, 0.98, 0.8, 0.64, 0.89, 1.42, 1.7, 1.83"]

dictionary = dict(zip(date, wave_height))
print (dictionary)
