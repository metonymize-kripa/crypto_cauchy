import math, random, numpy, scipy, sys
from scipy.stats import cauchy, norm, t
import matplotlib.pyplot as plt

def genCauchySpotPriceSample(spot,days_ahead,loc,scale):
    running_sum_spot=spot
    cauchy_returns_trace = cauchy.rvs(loc,scale,days_ahead)
    for cauchy_return_sample in cauchy_returns_trace:
        #print(f'gg-{cauchy_return_sample}')
        if cauchy_return_sample < 1:
            running_sum_spot = running_sum_spot*math.exp(cauchy_return_sample)
    #print(running_sum_spot)
    return running_sum_spot

def genNormSpotPriceSample(spot,days_ahead,loc,scale):
    running_sum_spot=spot
    norm_returns_trace = norm.rvs(loc,scale,days_ahead)
    #print(norm_returns_trace)
    for norm_return_sample in norm_returns_trace:
        #print(f'gg-{cauchy_return_sample}')
        #if norm_return_sample < 1:
        running_sum_spot = running_sum_spot*math.exp(norm_return_sample)
    #if running_sum_spot <spot:
    #    print(running_sum_spot)
    return running_sum_spot

def genStudentTSpotPriceSample(spot,days_ahead,df,loc,scale):
    running_sum_spot=spot
    t_returns_trace = t.rvs(df,loc,scale,days_ahead)
    for t_return_sample in t_returns_trace:
        #print(f'gg-{cauchy_return_sample}')
        #if t_return_sample < 1:
        running_sum_spot = running_sum_spot*math.exp(t_return_sample)
    #print(running_sum_spot)
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

def genNormCallOptionPrice(days_ahead, strike, spot, loc, scale, num_traces):
    running_sum_call_payoff = 0
    ##Simulate spot price traces and corresponding pay offs
    for i in range(num_traces):
        this_spot = genNormSpotPriceSample(spot,days_ahead,loc,scale)
        #Determine payoff of this specific path
        this_payoff = this_spot - strike
        #Value of option is zero is our price is less than the strike
        this_payoff = this_payoff if this_payoff > 0 else 0
        running_sum_call_payoff+=this_payoff
        
    average_payoff = running_sum_call_payoff/num_traces
    return round(average_payoff,2)
    
def genTCallOptionPrice(days_ahead, strike, spot,df, loc, scale, num_traces):
    running_sum_call_payoff = 0
    ##Simulate spot price traces and corresponding pay offs
    for i in range(num_traces):
        this_spot = genStudentTSpotPriceSample(spot,days_ahead,df,loc,scale)
        #Determine payoff of this specific path
        this_payoff = this_spot - strike
        #Value of option is zero is our price is less than the strike
        this_payoff = this_payoff if this_payoff > 0 else 0
        running_sum_call_payoff+=this_payoff
    average_payoff = running_sum_call_payoff/num_traces
    return round(average_payoff,2)

#estimated_call_option_price = genCauchyCallOptionPrice(7,2000,1850,0,0.025,10000)
# estimated_call_option_price = genCauchyCallOptionPrice(7,2000,1850,0.002,0.014,10000)
# print(estimated_call_option_price)
#
# generated_samples=[genCauchyCallOptionPrice(7,42000,32150,0.002,0.014,1000) for _ in range(500)]
# plt.hist(generated_samples, bins=30, range=(0,30000), density=True); plt.show()

if __name__== "__main__":
    print(sys.argv)
    strike = float(sys.argv[2])
    spot = float(sys.argv[3])
    num_traces = 100000
    loc = 0
    scale = 0
    ndays = 10
    df=1
    if sys.argv[4] == 'T':
        if sys.argv[1].upper() == 'ETH':
            df = 2.2810757
            loc = 0.001038856
            scale = 0.0337545
        if sys.argv[1].upper() == 'BTC':
            df = 2.03146
            loc = 0.002328
            scale = 0.01981
        estimated_call_option_price = genTCallOptionPrice(ndays,strike,spot,df,loc,scale,num_traces)
        print(estimated_call_option_price)
        generated_samples=[genTCallOptionPrice(ndays,strike,spot,df,loc,scale,1000) for _ in range(500)]
        plt.hist(generated_samples, bins=30, range=(0,30000), density=True)
        plt.show()
    elif sys.argv[4] == 'C':
        if sys.argv[1].upper() == 'ETH':
            loc = -0.00012
            scale = 0.02453
        if sys.argv[1].upper() == 'BTC':
            #using all available data
            #loc = 0.0021
            #scale = 0.01457
            #using data from mid 2017
            loc = 0.0020628
            scale = 0.01731177
        estimated_call_option_price = genCauchyCallOptionPrice(ndays,strike,spot,loc,scale,num_traces)
        print(estimated_call_option_price)
        generated_samples=[genCauchyCallOptionPrice(ndays,strike,spot,loc,scale,1000) for _ in range(500)]
        plt.hist(generated_samples, bins=30, range=(0,30000), density=True)
        plt.show()
    elif sys.argv[4] == 'N':
        if sys.argv[1].upper() == 'ETH':
            loc = 0.0029975
            scale = 0.0681606
        if sys.argv[1].upper() == 'BTC':
            #using all available data
            #loc = 0.0021
            #scale = 0.01457
            #using data from mid 2017
            loc = 0.00170646
            scale = 0.00170646
        estimated_call_option_price = genNormCallOptionPrice(ndays,strike,spot,loc,scale,num_traces)
        print(estimated_call_option_price)
        generated_samples=[genNormCallOptionPrice(ndays,strike,spot,loc,scale,1000) for _ in range(500)]
        plt.hist(generated_samples, bins=30, range=(0,30000), density=True)
        plt.show()

    
    
    
    
