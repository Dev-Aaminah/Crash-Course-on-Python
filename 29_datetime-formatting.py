import datetime

my_date = datetime.datetime(2024,11,17,11,34,40)
print(my_date)

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

sentence_date = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence_date)