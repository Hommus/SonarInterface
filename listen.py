import subprocess as sub
import re

global packet

# Line buffers the tcpdump output
def awaitREDYFX():
	packet = 0
	p = sub.Popen(('sudo', 'tcpdump', '-l', 'udp', '-X'), stdout=sub.PIPE)
	for row in iter(p.stdout.readline, b''):
		# Process the data here
		#print (row.rstrip())
		if re.search(b'length 340', row.rstrip()):
			packet = 1
			continue

		if packet == 1 and re.search(b'x0030', row.rstrip()):
			depth 	= str(int(str(row.rstrip()[17:19], 'utf-8'), 16))
			dep_f 	= str(int(str(row.rstrip()[22:24], 'utf-8'), 16))
			temp 	= str(int(str(row.rstrip()[25:27], 'utf-8'), 16))
			batt	= int(str(row.rstrip()[35:37], 'utf-8'), 16)
			batt_f	= int(str(row.rstrip()[37:39], 'utf-8'), 16)

			print ("Depth: " + depth + "." + dep_f)
			print ("Temperature: " + temp)

			batt_volt = batt + batt_f * 0.01
			batt_life = ((batt_volt-2.4)/1.8)*100

			print ("Battery Voltage: %.2f" % batt_volt)
			#print ("Battery Life: " + str(batt_life) + "%\n")
			print ("Battery Life: %.2f%%\n" % batt_life)

			packet = 0

awaitREDYFX()
