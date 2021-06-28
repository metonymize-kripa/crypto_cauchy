import matplotlib.pyplot as plt
import scipy
from scipy.stats import cauchy, norm
import numpy as np

#my_data = np.genfromtxt('ETH-USD-samples.csv', delimiter=',')
my_data = np.genfromtxt('BTC-USD-samples.csv', delimiter=',')

cauchy_params_fit  = scipy.stats.distributions.cauchy.fit(my_data)
loc, scale = cauchy_params_fit
print("Cauchy Params Estimated:", cauchy_params_fit)

norm_params_fit  = scipy.stats.distributions.norm.fit(my_data)
mean, var = norm_params_fit
print("Normal Params Estimated:", norm_params_fit)

x = np.linspace(-0.25,0.25,100)

cauchy_fitted_data = scipy.stats.distributions.cauchy.pdf(x, loc, scale)
norm_fitted_data = scipy.stats.distributions.norm.pdf(x, mean, var)

plt.hist(my_data, bins=100, range=(-0.25,0.25), density=True)
plt.plot(x,cauchy_fitted_data,'r-')
plt.plot(x,norm_fitted_data,'g-')

plt.show()


