import pytz, datetime, argparse

print('')
print("buffering")
print('')
print('live music coding experiments')
print('max for live / norns / c')
print('')

ap = argparse.ArgumentParser()

ap.add_argument('heretime')

ar = ap.parse_args()

here = 'America/Chicago'
heretime = ar.heretime  #'8/27/2020 15:00'
us_fm = '%I%p %Z'
fm = '%H:%M %Z'
  
utc = pytz.timezone(here).localize(datetime.datetime.strptime(heretime, '%m/%d/%Y %H:%M')).astimezone(pytz.utc)
  
print(utc.astimezone(pytz.timezone(here)).strftime('%A').lower() + ' ' + utc.astimezone(pytz.timezone(here)).strftime('%m/%d'))
#print('')


tc = [] 

# the US gets it's own loop for our silly 12-hour clocks 
for c in ['us']:
  for tz in ['America/Los_Angeles', 'America/Phoenix', 'America/Chicago', 'America/New_York']:
    tc.append(utc.astimezone(pytz.timezone(tz)).strftime(us_fm))

tc = list(dict.fromkeys(tc))
tc.sort()

str1 = tc[0]
for tz in tc[1:]:
  str1 = str1 + ' | ' + tz

tc = []

for c in ['gb', 'no', 'de', 'se', 'it', 'fi']: #europe
  for tz in pytz.country_timezones[c]:
    tc.append(utc.astimezone(pytz.timezone(tz)).strftime(fm))

tc = list(dict.fromkeys(tc))
tc.sort()

for tz in tc:
   str1 = str1 + ' | ' + tz

print(str1)
print('')

print('( ' + utc.astimezone(pytz.timezone('Australia/Melbourne')).strftime('%A').lower() + ' ' + utc.astimezone(pytz.timezone('Australia/Melbourne')).strftime('%m/%d') + ' )')
#print('')

tc = []

for c in ['jp', 'au', 'ph']: #asia / au
  for tz in pytz.country_timezones[c]:
    tc.append(utc.astimezone(pytz.timezone(tz)).strftime(fm))

tc = list(dict.fromkeys(tc))
tc.sort()

str1 = tc[0]
for tz in tc[1:]:
  str1 = str1 + ' | ' + tz

print(str1)

print('\nhttps://www.twitch.tv/a__ndrew\n\n\n')
