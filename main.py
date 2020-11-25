import pyvisa
import time

from datetime import date
resourceManager = pyvisa.ResourceManager()
resources = resourceManager.list_resources()
print(resources)

freq_counter = resourceManager.open_resource('GPIB0::21::INSTR')
pressure_gauge_turbo = resourceManager.open_resource('ASRL4::INSTR')
pressure_gauge_evap = resourceManager.open_resource('ASRL3::INSTR')

for device in [freq_counter, pressure_gauge_turbo, pressure_gauge_evap]:
	device.timeout = 2000
	device.write_termination = '\n'
	device.read_termination ='\n'
	device.baud_rate = 9600 

	print('{} : {}.'.format(str(device), device.query('*IDN?')))


# material = 'Diamantane-10-3mbar-60C'
material = 'QuartzAbove-Ambient-None'
amount = ''
date = date.today().strftime("%d-%m-%Y")		
filename = "data\\" + date + '_' + material + '_' + amount + '.txt'

freq_counter.write(':EVENT1:LEVEL -.05')
time_start = time.time()
with open(filename, "a") as file:
		file.write('Time (s)' + '\t' + 'Pressure Turbo (mbar)' + '\t' + 'Pressure Evap (mbar)' + '\t' + 'Frequency (Hz)' '\n')
while True:
	u_turbo = float(pressure_gauge_turbo.query('READ?').split(",")[0])
	p_turbo = pow(10, 1.667*u_turbo-11.33)
	if p_turbo > 1000:
		p_turbo = 1000

	u_evap = float(pressure_gauge_evap.query('READ?').split(",")[0])
	p_evap = pow(10, 1.667*u_evap-11.33)
	if p_evap > 1000:
		p_evap = 1000

	f = float(freq_counter.query('READ?'))

	time_passed = time.time() - time_start
	with open(filename, "a") as file:
		line = str(time_passed) + '\t' + str(p_turbo) + '\t' + str(p_evap) + '\t' +str(f) +  '\n'
		print(line)
		file.write(line)

	time.sleep(1)

 