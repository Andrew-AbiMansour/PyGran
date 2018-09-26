import PyGran.Simulator as Si
from PyGran.Params import steel
import matplotlib.pylab as plt
import numpy as np

# Create a list of contact models to analyze
models = [Si.models.SpringDashpot, Si.models.HertzMindlin]

# Set particle radius to 1 mm
steel['radius'] = 1e-3

# Compute the force-displacement curve
for model in models:
	model = model(material=steel, limitForce=True)

	time, delta, force = model.displacement()
	plt.plot(delta[:,0] * 1e6, force * 1e3)

	if hasattr(model, 'displacementAnalytical'):
		time, delta, force = model.displacementAnalytical()
		plt.plot(delta[:,0] * 1e6, force * 1e3, ':o')

plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.legend(['SpringDashpot (numerical)', 'SpringDashpot (analytical)', 'HertzMindlin'], loc='best')
plt.xlabel(r'$\delta$ $(\mu m)$')
plt.ylabel('Force (mN)')
plt.grid(linestyle=':')
plt.show()
