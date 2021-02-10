import numpy as np
from sklearn import preprocessing

# Test Functions
def f1(x,y): return np.exp(y - x**2)
def f2(x,y): return x**2 + y**2
def f3(x,y): return x**3 + y**3 + 0.2*x + 0.6*y
def f4(x,y): return np.arctan(y/x)
def uhoh(x,y): return np.sin(8*x) + np.sin(8*y)
def Squaresum(*vars):
	total = 0
	for i in range(0,len(vars)):
		total += (vars[i])**2
	return total
def cubey(x,y): return y/x**3
def loopy(x,y): return y**2/(1-x**2)

# Gradient Vectors of Test Functions
def gradf1(x,y): return [np.exp(y - x**2)*(-2.)*x, np.exp(y - x**2)]
def gradf2(x,y): return [2.*x,2.*y]
def gradf3(x,y): return [0.2 + (3.)*(x**2), 0.6 + (3.)*(y**2)]
def gradf4(x,y): return [ -y/(x**2 + y**2), x/(x**2 + y**2) ]
def graduhoh(x,y): return [8*np.cos(8*x), 8*np.cos(8*y)]
def gradSquaresum(*vars):
	grs = []
	for i in range(len(vars)):
		grs =np.concatenate( (grs, np.array([2*vars[i]])), axis = 0)
	return grs
def gcubey(x,y): return [-3*y/x**4, 1/x**3]
def gloopy(x,y): return [2*x*y**2/(1-x**2)**2,2*y/(1-x**2)]

#necessary functions for MHD stuff (defined by constantine)
coth = lambda x: 1./np.tanh(x)
sech = lambda x: 1./np.cosh(x)
csch = lambda x: 1./np.sinh(x)

#### set global variables
l = 1.0
mu0 = 1.0
# Bounds
lb = np.log(np.array([.05, 1, .5, .5, .1]))
ub = np.log(np.array([.2, 5, 3, 3, 1]))

#average velocity
def uavg(x):
	x = np.exp(x)
	return -x[:,2]*x[:,3]/x[:,4]**2*(1 - x[:,4]*l/np.sqrt(x[:,3]*x[:,0])*coth(x[:,4]*l/\
									np.sqrt(x[:,3]*x[:,0])))

#induced magnetic field
def Bind(x):
	x = np.exp(x)
	return x[:,2]*l*mu0/(2*x[:,4])*(1 - 2*np.sqrt(x[:,3]*x[:,0])/(x[:,4]*l)*np.tanh(x[:,4]*\
				l/(2*np.sqrt(x[:,3]*x[:,0]))))

#gradient of average velocity
def uavg_grad(x):
	x = np.exp(x)
	mu = x[:,0]; rho = x[:,1]; dp0 = x[:,2]; eta = x[:,3]; B0 = x[:,4]

	dudmu = -dp0*eta/B0**2*(B0*l/(2*np.sqrt(eta))*mu**(-3./2)*coth(B0*l/np.sqrt(eta*mu)) - \
			(B0*l)**2*np.sqrt(eta/mu)*csch(B0*l/np.sqrt(eta*mu))**2/(2*(eta*mu)**(3./2)))
	dudrho = 0.0*np.empty(x.shape[0])
	duddp0 = -eta/B0**2*(1 - B0*l/np.sqrt(eta*mu)*coth(B0*l/np.sqrt(eta*mu)))
	dudeta = -dp0/B0**2*(1 - B0*l/np.sqrt(eta*mu)*coth(B0*l/np.sqrt(eta*mu))) - \
		dp0*eta/B0**2*(B0*l/(2*np.sqrt(mu))*eta**(-3./2)*coth(B0*l/np.sqrt(eta*mu)) - \
			(B0*l)**2*np.sqrt(mu/eta)*csch(B0*l/np.sqrt(eta*mu))**2/(2*(eta*mu)**(3./2)))
	dudB0 = 2*dp0*eta/B0**3*(1 - B0*l/np.sqrt(eta*mu)*coth(B0*l/np.sqrt(eta*mu))) - \
		dp0*eta/B0**2*(-l/np.sqrt(eta*mu)*coth(B0*l/np.sqrt(eta*mu)) + B0*l**2/(eta*mu)*\
												csch(B0*l/np.sqrt(eta*mu))**2)

	dudmu = dudmu[:,None]; dudrho = dudrho[:,None]; duddp0 = duddp0[:,None]
	dudeta = dudeta[:,None]; dudB0 = dudB0[:,None]
	return np.hstack((dudmu, dudrho, duddp0, dudeta, dudB0))*x*(ub - lb).reshape((1, 5))/2.

#gradient of induced magnetic field
def Bind_grad(x):
	x = np.exp(x)
	mu = x[:,0]; rho = x[:,1]; dp0 = x[:,2]; eta = x[:,3]; B0 = x[:,4]

	dBdmu = dp0*l*mu0/(2*B0)*(-(B0*l)**-1*np.sqrt(eta/mu)*np.tanh(B0*l/(2*np.sqrt(eta*mu))) +\
				eta*np.sqrt(eta*mu)*sech(B0*l/(2*np.sqrt(eta*mu)))**2/(2*(eta*mu)**(3./2)))
	dBdrho = 0.0*np.empty(x.shape[0])
	dBddp0 = l*mu0/(2*B0)*(1 - 2*np.sqrt(eta*mu)/(B0*l)*np.tanh(B0*l/(2*np.sqrt(eta*mu))))
	dBdeta = dp0*l*mu0/(2*B0)*(-(B0*l)**-1*np.sqrt(mu/eta)*np.tanh(B0*l/(2*np.sqrt(eta*mu)))+\
				mu*np.sqrt(eta*mu)*sech(B0*l/(2*np.sqrt(eta*mu)))**2/(2*(eta*mu)**(3./2)))
	dBdB0 = -dp0*l*mu0/(2*B0**2)*(1 - 2*np.sqrt(eta*mu)/(B0*l)*np.tanh(B0*l/\
		(2*np.sqrt(eta*mu)))) + dp0*l*mu0/(2*B0)*(2*np.sqrt(eta*mu)/(B0**2*l)*np.tanh(\
		B0*l/(2*np.sqrt(eta*mu))) - B0**-1*sech(B0*l/(2*np.sqrt(eta*mu)))**2)

	dBdmu = dBdmu[:,None]; dBdrho = dBdrho[:,None]; dBddp0 = dBddp0[:,None]
	dBdeta = dBdeta[:,None]; dBdB0 = dBdB0[:,None]
	return np.hstack((dBdmu, dBdrho, dBddp0, dBdeta, dBdB0))*x*(ub - lb).reshape((1, 5))/2.

def get_u_avg_data(meshy):

    # Un-normalized log-inputs
    xu = lb + 2./(ub-lb)*(np.array(meshy) + 1)

    # Function values and gradients at exponentiated (non-log) inputs (np.exp in Constantine's stuff)
    u = uavg(xu)
    du = uavg_grad(xu)

    m = [(ub[i]-1)/(lb[i]+1) for i in range(5)]
    m = np.array(m)
    m = np.diagflat(m)

    # Normalized, unit-length grads for AM
    gradsu = preprocessing.normalize(np.matmul(du,m))

    return u, gradsu, du

def get_b_ind_data(meshy):
    # Un-normalized log-inputs
    xu = lb + 2./(ub-lb)*(np.array(meshy) + 1)

    # Function values and gradients at exponentiated (non-log) inputs (np.exp in Constantine's stuff)
    B = Bind(xu)
    dB = Bind_grad(xu)

    m = [(ub[i]-1)/(lb[i]+1) for i in range(5)]
    m = np.array(m)
    m = np.diagflat(m)

    # Normalized, unit-length grads for AM
    gradsB = preprocessing.normalize(np.matmul(dB,m))

    return B, gradsB, dB
