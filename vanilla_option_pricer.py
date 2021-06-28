import math, random, numpy, scipy
from scipy.stats import cauchy, norm

def genCauchySpotPriceSample(spot,days_ahead,loc,scale):
    running_sum_spot=spot
    cauchy_returns_trace = cauchy.rvs(loc,scale,days_ahead)
    for cauchy_return_sample in cauchy_returns_trace:
        running_sum_spot += running_sum_spot*cauchy_return_sample
    return running_sum_spot

##Simple Monte Carlo Pricing Vanilla Call Option using Cauchy Distribution, and 0 interest rate
def genCauchyCallOptionPrice(days_ahead, strike, spot, loc, scale, num_traces):
    running_sum_call_payoff = 0
    ##Simulate spot price traces and corresponding pay offs
    for i in range(num_traces):
        this_spot = genCauchySpotPriceSample(spot,days_ahead,loc,scale)
        #Determine payoff of this specific path
        this_payoff = this_spot - strike
        #Value of option is zero is our price is less than the strike
        this_payoff = this_payoff if this_payoff > 0 else 0
        running_sum_call_payoff+=this_payoff
    average_payoff = running_sum_call_payoff/num_traces
    return round(average_payoff,2)

#estimated_call_option_price = genCauchyCallOptionPrice(7,2000,1850,0,0.025,10000)
estimated_call_option_price = genCauchyCallOptionPrice(7,2000,1850,0.002,0.014,10000)
print(estimated_call_option_price)

generated_samples=[genCauchyCallOptionPrice(7,42000,32150,0.002,0.014,1000) for _ in range(500)]
plt.hist(generated_samples, bins=30, range=(0,30000), density=True); plt.show()
