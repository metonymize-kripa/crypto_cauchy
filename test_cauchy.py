import matplotlib.pyplot as plt
import scipy
from scipy.stats import cauchy, norm, t
import numpy as np
import pandas as pd

my_data = pd.read_csv('ETH-USD-samples.csv', delimiter=',')
my_data['returns']=np.log(my_data.Close) - np.log(my_data.Close.shift(1))
my_data.returns[my_data.returns == np.inf] = 0
my_data.returns[my_data.returns == -np.inf] = 0
my_data = my_data.fillna(0)
cauchy_params_fit  = scipy.stats.distributions.cauchy.fit(my_data.returns)
loc, scale = cauchy_params_fit
print("Cauchy Params Estimated:", cauchy_params_fit)

norm_params_fit  = scipy.stats.distributions.norm.fit(my_data.returns)
mean, var = norm_params_fit
print("Normal Params Estimated:", norm_params_fit)

t_params_fit  = scipy.stats.distributions.t.fit(my_data.returns)
t_df, t_loc, t_scale = t_params_fit

print("T Params Estimated:", t_params_fit)
x = np.linspace(-0.25,0.25,100)

cauchy_fitted_data = scipy.stats.distributions.cauchy.pdf(x, loc, scale)
norm_fitted_data = scipy.stats.distributions.norm.pdf(x, mean, var)
t_fitted_data = scipy.stats.distributions.t.pdf(x, t_df, t_loc, t_scale)

plt.hist(my_data.returns, bins=100, range=(-0.25,0.25), density=True)
plt.plot(x,cauchy_fitted_data,'r-')
plt.plot(x,norm_fitted_data,'g-')
plt.plot(x,t_fitted_data,'b-')

plt.show()
