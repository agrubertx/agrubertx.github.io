from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def burgers( method, nx, nt, t_max, bc, param, plot = False ):
  """
  This function solves the time-dependent inviscid Burgers equation.
  It also solves sensitivity equations for derivatives of the PDE solution
    with respect to parameters mu1 and mu2, and computes the values/gradients
    of some functions of the PDE solution.

  The code for solving Burgers' equation is ported from "BURGERS_TIME_INVISCID"
    by Mikel Landajuela and Zhu Wang.

  Discussion:

    A number of solution methods are available for the user to choose.

  Modified:

    4 February 2020

  Author:

    Anthony Gruber

  Inputs:

    Integer METHOD.
      1, Upwind nonconservative;
      2, Upwind conservative;
      3, Godunov.

    Integer NX, the number of nodes.

    Integer NT, the number of time steps.

    Real T_MAX, the maximum time.

    Integer BC, defines the boundary conditions.
      0, Dirichlet at A, Dirichlet at B.
      1, Dirichlet at A, nothing/Neumann at B.

    Array PARAM, contains two parameters:
      param(1): left-end boundary condition.
      param(2): parameter in source term.

    Bool plot (false by default), enables/disables plot of solution over time.

  Output:

    Real U(5, NT+1, NX). U[0] is the solution at each time and node.
      U[1], U[2] are solution derivatives w.r.t. mu1, mu2 at each time and node.
      U[3] is the time derivative of the solution at each time and node.
      U[4] is the spatial derivative of the solution at each time and node.

    Real Dsav(5, NT+1, NParam+1+NX), stores [parameter value, time, quantity].

    Real Q2, value of total kinetic energy, 0.5 * \int_x \int_t w(x, t, \mu)^2.

    Real gradQ2(3), gradient of Q2(t, \mu).

    Real Q3alt, value of integrated kinetic energy at right endpoint,
      0.5 * \int_t w(100, t, \mu)^2.

    Real gradQ3alt(3), gradient of Q3alt(t, \mu).

  Reference:
    Burgers equation by Mikel Landajuela
      Test problem from
        A Trajectory Piecewise-Linear Approach to Model Order Reduction
        of Nonlinear Dynamical Systems, by M. Rewienski
          and
        Model reduction of dynamcial systems on nonlinear manifolds using
        deep convolutional autoencoders by K. Lee and K. Carlberg

  Demo:
    burgers ( 2, 256, 500, 35, 1, [4.3, 0.021] );
  """

  def f(u): return 0.5 * u**2
  def df(u): return u

  def nf(u, v):
    ustar = u
    if np.ndim(u) == 0:
      u = np.array( [u] )
      ustar = u;
    if np.ndim(v) == 0:
      v = np.array( [v] );
    for i in range( len(u) ):   #i = 1:len(u)
      if u[i] >= v[i]:
        if ( u[i] + v[i] ) / 2 > 0:
          ustar[i] = u[i]
        else:
          ustar[i] = v[i]
      else:
        if u[i] > 0:
          ustar[i] = u[i]
        elif v[i] < 0:
          ustar[i] = v[i]
        else:
          ustar[i] = 0
    return 0.5 * ustar**2

  a, b = 0, 100
  dx = ( b - a ) / nx
  x = np.linspace(a, b, nx)
  dt = t_max / nt

  g = 0.02 * np.exp( param[1] * x )

# Set up the initial solution values and parameter gradient values.
  U = np.zeros( (5, nt + 1, nx) )
  Dsav = np.zeros( (5, nt + 1, nx + len(param) + 1) )
  u0 = np.ones_like(x)
  umu10 = np.zeros_like(x)
  umu20 = np.zeros_like(x)
  ut0 = np.zeros_like(x)
  ux0 = np.zeros_like(x)

# impose BC at left endpoint
  u0[0] = param[0]
  umu10[0] = 1
  umu20[0] = 0
  ut0[0] = 0
  ux0[0] = 0

# Could vectorize this more, but I think it's more readable like this.
  U[0][0, :] = u0
  U[1][0, :] = umu10
  U[2][0, :] = umu20
  U[3][0, :] = ut0
  U[4][0, :] = ux0
  Dsav[0][0, :] = np.concatenate( (param, 0, u0), axis = None )
  Dsav[1][0, :] = np.concatenate( (param, 0, umu10), axis = None )
  Dsav[2][0, :] = np.concatenate( (param, 0, umu20), axis = None )
  Dsav[3][0, :] = np.concatenate( (param, 0, ut0), axis = None )
  Dsav[4][0, :] = np.concatenate( (param, 0, ux0), axis = None )

  u = u0
  umu1 = umu10
  umu2 = umu20
  ut = ut0
  ux = ux0

  unew = 0 * u
  umu1new = 0 * umu1
  umu2new = 0 * umu2
  utnew = 0 * ut
  uxnew = 0 * ux

# Generate plot data
  if plot:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    upperlim = 1.4 * param[0]
    ax.set_ylim( [0, upperlim] )
    line1, = ax.plot(x, u0, 'r-')

# Implementation of the numerical methods.

  irange = [ y + 1 for y in range(nt) ] # so irange starts at 1

  for i in irange:

#  Upwind nonconservative.

    if method == 1:
      if bc == 0 or bc == 1:
        unew[0] = u[0]
        umu1new[0] = umu1[0]
        umu2new[0] = umu2[0]
        utnew[0] = ut[0]

      unew[1:] = u[1:] + dt * ( -1/dx * u[1:] * ( u[1:] - u[:-1] ) + g[1:] )

    # Compute parameter derivatives
      umu1new[1:] = umu1[1:] - dt * ( umu1[1:] * ( u[1:]
        - u[:-1]) / dx + u[1:] * ( umu1[1:] - umu1[:-1] ) / dx )

      umu2new[1:] = umu2[1:] + dt * ( x[1:] * g[1:] - umu2[1:] * ( u[1:]
        - u[:-1] ) / dx - u[1:] * ( umu2[1:] - umu2[:-1] ) / dx  )

      utnew[1:] = -1/dx * u[1:] * ( u[1:] - u[:-1] ) + g[1:]

 # Upwind conservative.

    if method == 2:
      if bc == 0 or bc == 1:
        unew[0] = u[0]
        umu1new[0] = umu1[0]
        umu2new[0] = umu2[0]
        utnew[0] = ut[0]
        uxnew[0] = ux[0]


      utnew[1:] = -1/dx * ( f(u[1:]) - f(u[:-1]) ) + g[1:]

      unew[1:] = u[1:] + dt * utnew[1:]

      #unew[1:] = u[1:] + dt * ( -1/dx * ( f(u[1:]) - f(u[:-1]) ) + g[1:] )

    # Solve for parameter derivatives
      umu1new[1:] = umu1[1:] - dt * (1/dx) * ( umu1[1:] * u[1:]
        - u[:-1] * umu1[:-1] )

      umu2new[1:] = umu2[1:] + dt * x[1:] * g[1:] - dt * (1/dx) * ( umu2[1:]
        * u[1:] - u[:-1] * umu2[:-1] )

      uxnew[1:-1] = (u[2:] - u[:-2]) / (2*dx)
      uxnew[-1] = (u[-1] - u[-2]) / dx

#  Godunov

    if method == 3:
      if bc == 0 or bc == 1:
        unew[0] = u[0]
        umu1new[0] = umu1[0]
        umu2new[0] = umu2[0]
        utnew[0] = ut[0]

      unew[1:-1] = u[1:-1] + dt * ( -1/dx * ( nf(u[1:-1], u[2:])
        - nf(u[:-2], u[1:-1]) ) + g[1:-1] )

      if ( bc == 0 or bc == 2 ):
        unew[-1] = u[-1]
      elif ( bc == 1 ):
        unew[-1] = u[-1] + dt * ( -1/dx * ( nf(u[-1], u[-1])
          - nf(u[-2], u[-1]) ) + g[-1] )
        # assume neumann at the rightend

    # Solve for parameter derivatives (same as method 2)
      umu1new[1:] = umu1[1:] - dt * (1/dx) * ( umu1[1:] * u[1:]
        - u[:-1] * umu1[:-1] )
        #
      umu2new[1:] = umu2[1:] + dt * x[1:] * g[1:] - dt * (1/dx) * ( umu2[1:]
        * u[1:] - u[:-1] * umu2[:-1] )

      utnew[1:] = -1/dx * ( f(u[1:]) - f(u[:-1]) ) + g[1:]

#  Save the latest result.
    u = unew
    umu1 = umu1new
    umu2 = umu2new
    ut = utnew
    ux = uxnew
    U[0][i, :] = u
    U[1][i, :] = umu1
    U[2][i, :] = umu2
    U[3][i, :] = ut
    U[4][i, :] = ux
    Dsav[0][i, :] = np.concatenate( (param, dt*i, u), axis = None )
    Dsav[1][i, :] = np.concatenate( (param, dt*i, umu1), axis = None )
    Dsav[2][i, :] = np.concatenate( (param, dt*i, umu2), axis = None )
    Dsav[3][i, :] = np.concatenate( (param, dt*i, ut), axis = None )
    Dsav[4][i, :] = np.concatenate( (param, dt*i, ux), axis = None )

#  Plot the profile curve.
    if plot:
      line1.set_ydata(u)
      fig.canvas.draw()
      fig.canvas.flush_events()
      plt.pause(0.001)

#  Generate quantity of interest Q2 (total kinetic energy) and its derivatives
#  All trapezoidal Riemann sums in space and left sums in time
  tempLeft = np.sum( U[0][:, :-1]**2, 1 ) * dx  # left row sum
  tempRight = np.sum( U[0][:, 1:]**2, 1 ) * dx  # right row sum
  Q2 = 0.25 * np.sum( tempLeft[:-1] + tempRight[:-1] ) * dt  # left time sum

  dQ2dT = 0.25 * np.sum( U[0][-1, :-1]**2 + U[0][-1, 1:]**2 ) * dx
  # derivative in the final time

  tempLeft = np.sum( U[0][:, :-1] * U[1][:, :-1], 1 ) * dx
  tempRight = np.sum( U[0][:, 1:] * U[1][:, 1:], 1 ) * dx
  dQ2dmu1 = 0.5 * np.sum( tempLeft[:-1] + tempRight[:-1] ) * dt
  # derivative in mu1

  tempLeft = np.sum( U[0][:, :-1] * U[2][:, :-1], 1 ) * dx
  tempRight = np.sum( U[0][:, 1:] * U[2][:, 1:], 1 ) * dx
  dQ2dmu2 = 0.5 * np.sum( tempLeft[:-1] + tempRight[:-1] ) * dt
  # derivative in mu2

  gradQ2 = np.array( [dQ2dT, dQ2dmu1, dQ2dmu2] )

  # Generate quantity of interest Q3alt (integrated kinetic energy density
  # at right endpoint) and its derivatives
  Q3alt = 0.5 * np.sum( U[0][:-1, -1]**2 ) * dt
  dQ3altdT = 0.5 * U[0][-1, -1]**2
  dQ3altdmu1 = np.sum( U[0][:-1, -1] * U[1][:-1, -1] ) * dt
  dQ3altdmu2 = np.sum( U[0][:-1, -1] * U[2][:-1, -1] ) * dt

  gradQ3alt = np.array( [dQ3altdT, dQ3altdmu1, dQ3altdmu2] )

  # # Generate quantity of interest Q3 (kinetic energy density at right endpoint
  # # and final time) and its derivatives  #### NO LONGER USED OR RETURNED ####
  # Q3 = 0.5 * U[0][-1, -1]**2
  # dQ3dmu1 = U[0][-1, -1] * U[1][-1, -1]
  # dQ3dmu2 = U[0][-1, -1] * U[2][-1, -1]
  # dQ3dt = U[0][-1, -1] * U[3][-1, -1]
  #
  # gradQ3 = np.array( [dQ3dt, dQ3dmu1, dQ3dmu2] )

  return U, Dsav, Q2, gradQ2, Q3alt, gradQ3alt


def burgers_witheps( method, nx, nt, t_max, bc, param,
                     eps1, eps2, plot = False ):
  """
  Same method as Burgers', but includes some epsilons to adjust the influence
  of mu1 and mu2.
  """

  def f(u): return 0.5 * u**2
  def df(u): return u

  def nf(u, v):
    ustar = u
    if np.ndim(u) == 0:
      u = np.array( [u] )
      ustar = u;
    if np.ndim(v) == 0:
      v = np.array( [v] );
    for i in range( len(u) ):   #i = 1:len(u)
      if u[i] >= v[i]:
        if ( u[i] + v[i] ) / 2 > 0:
          ustar[i] = u[i]
        else:
          ustar[i] = v[i]
      else:
        if u[i] > 0:
          ustar[i] = u[i]
        elif v[i] < 0:
          ustar[i] = v[i]
        else:
          ustar[i] = 0
    return 0.5 * ustar**2

  a, b = 0, 100
  dx = ( b - a ) / nx
  x = np.linspace(a, b, nx)
  dt = t_max / nt

  g = 0.02 * np.exp( eps2 * param[1] * x )

# Set up the initial solution values and parameter gradient values.
  U = np.zeros( (5, nt + 1, nx) )
  Dsav = np.zeros( (5, nt + 1, nx + len(param) + 1) )
  u0 = np.ones_like(x)
  umu10 = np.zeros_like(x)
  umu20 = np.zeros_like(x)
  ut0 = np.zeros_like(x)
  ux0 = np.zeros_like(x)

# impose BC at left endpoint
  u0[0] = eps1 * param[0]
  umu10[0] = eps1
  umu20[0] = 0
  ut0[0] = 0
  ux0[0] = 0

# Could vectorize this more, but I think it's more readable like this.
  U[0][0, :] = u0
  U[1][0, :] = umu10
  U[2][0, :] = umu20
  U[3][0, :] = ut0
  U[4][0, :] = ux0
  Dsav[0][0, :] = np.concatenate( (param, 0, u0), axis = None )
  Dsav[1][0, :] = np.concatenate( (param, 0, umu10), axis = None )
  Dsav[2][0, :] = np.concatenate( (param, 0, umu20), axis = None )
  Dsav[3][0, :] = np.concatenate( (param, 0, ut0), axis = None )
  Dsav[4][0, :] = np.concatenate( (param, 0, ux0), axis = None )

  u = u0
  umu1 = umu10
  umu2 = umu20
  ut = ut0
  ux = ux0

  unew = 0 * u
  umu1new = 0 * umu1
  umu2new = 0 * umu2
  utnew = 0 * ut
  uxnew = 0 * ux

# Generate plot data
  if plot:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    upperlim = 1.4 * param[0]
    ax.set_ylim( [0, upperlim] )
    line1, = ax.plot(x, u0, 'r-')

# Implementation of the numerical methods.

  irange = [ y + 1 for y in range(nt) ] # so irange starts at 1

  for i in irange:

#  Upwind nonconservative.

    if method == 1:
      if bc == 0 or bc == 1:
        unew[0] = u[0]
        umu1new[0] = umu1[0]
        umu2new[0] = umu2[0]
        utnew[0] = ut[0]

      unew[1:] = u[1:] + dt * ( -1/dx * u[1:] * ( u[1:] - u[:-1] ) + g[1:] )

    # Compute parameter derivatives
      umu1new[1:] = umu1[1:] - dt * ( umu1[1:] * ( u[1:]
        - u[:-1]) / dx + u[1:] * ( umu1[1:] - umu1[:-1] ) / dx )

      umu2new[1:] = umu2[1:] + dt * (eps2 * x[1:] * g[1:] - umu2[1:] * ( u[1:]
        - u[:-1] ) / dx - u[1:] * ( umu2[1:] - umu2[:-1] ) / dx  )

      utnew[1:] = -1/dx * u[1:] * ( u[1:] - u[:-1] ) + g[1:]

 # Upwind conservative.

    if method == 2:
      if bc == 0 or bc == 1:
        unew[0] = u[0]
        umu1new[0] = umu1[0]
        umu2new[0] = umu2[0]
        utnew[0] = ut[0]
        uxnew[0] = ux[0]


      utnew[1:] = -1/dx * ( f(u[1:]) - f(u[:-1]) ) + g[1:]

      unew[1:] = u[1:] + dt * utnew[1:]

    # Solve for parameter derivatives
      umu1new[1:] = umu1[1:] - dt * (1/dx) * ( umu1[1:] * u[1:]
        - u[:-1] * umu1[:-1] )

      umu2new[1:] = umu2[1:] + dt * eps2 * x[1:] * g[1:] - dt * (1/dx) * (
        umu2[1:] * u[1:] - u[:-1] * umu2[:-1] )

      uxnew[1:-1] = (u[2:] - u[:-2]) / (2*dx)
      uxnew[-1] = (u[-1] - u[-2]) / dx

#  Godunov

    if method == 3:
      if bc == 0 or bc == 1:
        unew[0] = u[0]
        umu1new[0] = umu1[0]
        umu2new[0] = umu2[0]
        utnew[0] = ut[0]

      unew[1:-1] = u[1:-1] + dt * ( -1/dx * ( nf(u[1:-1], u[2:])
        - nf(u[:-2], u[1:-1]) ) + g[1:-1] )

      if ( bc == 0 or bc == 2 ):
        unew[-1] = u[-1]
      elif ( bc == 1 ):
        unew[-1] = u[-1] + dt * ( -1/dx * ( nf(u[-1], u[-1])
          - nf(u[-2], u[-1]) ) + g[-1] )
        # assume neumann at the rightend

    # Solve for parameter derivatives (same as method 2)
      umu1new[1:] = umu1[1:] - dt * (1/dx) * ( umu1[1:] * u[1:]
        - u[:-1] * umu1[:-1] )
        #
      umu2new[1:] = umu2[1:] + dt * eps2 * x[1:] * g[1:] - dt * (1/dx) * (
        umu2[1:] * u[1:] - u[:-1] * umu2[:-1] )

      utnew[1:] = -1/dx * ( f(u[1:]) - f(u[:-1]) ) + g[1:]

#  Save the latest result.
    u = unew
    umu1 = umu1new
    umu2 = umu2new
    ut = utnew
    ux = uxnew
    U[0][i, :] = u
    U[1][i, :] = umu1
    U[2][i, :] = umu2
    U[3][i, :] = ut
    U[4][i, :] = ux
    Dsav[0][i, :] = np.concatenate( (param, dt*i, u), axis = None )
    Dsav[1][i, :] = np.concatenate( (param, dt*i, umu1), axis = None )
    Dsav[2][i, :] = np.concatenate( (param, dt*i, umu2), axis = None )
    Dsav[3][i, :] = np.concatenate( (param, dt*i, ut), axis = None )
    Dsav[4][i, :] = np.concatenate( (param, dt*i, ux), axis = None )

#  Plot the profile curve.
    if plot:
      line1.set_ydata(u)
      fig.canvas.draw()
      fig.canvas.flush_events()
      plt.pause(0.001)

#  Generate quantity of interest Q2 (total kinetic energy) and its derivatives
#  All trapezoidal Riemann sums in space and left sums in time
  tempLeft = np.sum( U[0][:, :-1]**2, 1 ) * dx  # left row sum
  tempRight = np.sum( U[0][:, 1:]**2, 1 ) * dx  # right row sum
  Q2 = 0.25 * np.sum( tempLeft[:-1] + tempRight[:-1] ) * dt  # left time sum

  dQ2dT = 0.25 * np.sum( U[0][-1, :-1]**2 + U[0][-1, 1:]**2 ) * dx
  # derivative in the final time

  tempLeft = np.sum( U[0][:, :-1] * U[1][:, :-1], 1 ) * dx
  tempRight = np.sum( U[0][:, 1:] * U[1][:, 1:], 1 ) * dx
  dQ2dmu1 = 0.5 * np.sum( tempLeft[:-1] + tempRight[:-1] ) * dt
  # derivative in mu1

  tempLeft = np.sum( U[0][:, :-1] * U[2][:, :-1], 1 ) * dx
  tempRight = np.sum( U[0][:, 1:] * U[2][:, 1:], 1 ) * dx
  dQ2dmu2 = 0.5 * np.sum( tempLeft[:-1] + tempRight[:-1] ) * dt
  # derivative in mu2

  gradQ2 = np.array( [dQ2dT, dQ2dmu1, dQ2dmu2] )

  # Generate quantity of interest Q3alt (integrated kinetic energy density
  # at right endpoint) and its derivatives
  Q3alt = 0.5 * np.sum( U[0][:-1, -1]**2 ) * dt
  dQ3altdT = 0.5 * U[0][-1, -1]**2
  dQ3altdmu1 = np.sum( U[0][:-1, -1] * U[1][:-1, -1] ) * dt
  dQ3altdmu2 = np.sum( U[0][:-1, -1] * U[2][:-1, -1] ) * dt

  gradQ3alt = np.array( [dQ3altdT, dQ3altdmu1, dQ3altdmu2] )

  return U, Dsav, Q2, gradQ2, Q3alt, gradQ3alt


def burgers_vanilla( method, nx, nt, t_max, bc, param, plot = True ):
  """
  This function solves the time-dependent inviscid Burgers equation.

  This implementation is basically ported from "BURGERS_TIME_INVISCID" by
  Mikel Landajuela and Zhu Wang

  Discussion:

    Three solution methods are available for the user to choose.

    A function u(x,0) representing the initial condition is required.
      Some are provided, but others can easily be written.
      The default is the constant function 1.

  Modified:

    26 January 2020

  Author:

    Anthony Gruber (original authors Mikel Landajuela and Zhu Wang)

  Parameters:

    Input, integer METHOD.
      1, Upwind nonconservative;
      2, Upwind conservative;
      3, Godunov.

    Input, integer NX, the number of nodes.

    Input, integer NT, the number of time steps.

    Input, real T_MAX, the maximum time.

    Input, integer BC, defines the boundary conditions.
      0, Dirichlet at A, Dirichlet at B.
      1, Dirichlet at A, nothing/Neumann at B.
      4, Periodic, U(A) = U(B).

    Input, array PARAM, contains two parameters:
      param(1): left-end boundary condition.
      param(2): parameter in source term.

    Input, bool plot (default true), enables/disables solution plot over time.

  Output:

    real U(3, NT+1, NX). U[0] is the solution at each time and node.
      U[1], U[2] are solution derivatives w.r.t. mu1, mu2 at each time and node.
    real Dsav(3, NT+1,NParam+1+NX), stores [parameter value, time, solution].

  Reference:
    Burgers equation by Mikel Landajuela
      Test problem from
        A Trajectory Piecewise-Linear Approach to Model Order Reduction
        of Nonlinear Dynamical Systems, by M. Rewienski
          and
        Model reduction of dynamcial systems on nonlinear manifolds using
        deep convolutional autoencoders by K. Lee and K. Carlberg

  Demo:
    burgers_vanilla ( 2, 256, 500, 35, 1, [4.3, 0.021] );
  """

  def f(u): return 0.5 * u**2
  def df(u): return u

  def nf(u, v):
    ustar = u
    if np.ndim(u) == 0:
      u = np.array( [u] )
      ustar = u;
    if np.ndim(v) == 0:
      v = np.array( [v] );
    for i in range( len(u) ):   #i = 1:len(u)
      if u[i] >= v[i]:
        if ( u[i] + v[i] ) / 2 > 0:
          ustar[i] = u[i]
        else:
          ustar[i] = v[i]
      else:
        if u[i] > 0:
          ustar[i] = u[i]
        elif v[i] < 0:
          ustar[i] = v[i]
        else:
          ustar[i] = 0
    return 0.5 * ustar**2

  def ic_expansion(x, s): return s * ( 1.0 - 0.5 * x )
  def ic_shock (x, s): return s * x
  def ic_gaussian(x, s): return s * np.exp( -2 * (x - 1)**2 )
  def ic_ones(x): return np.ones_like(x)

  a, b = 0, 100
  dx = ( b - a ) / nx
  x = np.linspace(a, b, nx)
  dt = t_max / nt

  g = 0.02 * np.exp( param[1] * x )

# Set up the initial solution values and parameter gradient values.
  U = np.zeros( (nt + 1, nx) )
  Dsav = np.zeros( (nt + 1, nx + len(param) + 1) )
  u0 = ic_ones(x)

# impose BC at left endpoint
  u0[0] = param[0]

# Store initial data
  U[0, :] = u0
  Dsav[0, :] = np.concatenate( (param, 0, u0), axis = None )

  u = u0
  unew = 0 * u

# Generate plot data
  if plot:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    upperlim = 1.4 * param[0]
    ax.set_ylim( [0, upperlim] )
    line1, = ax.plot(x, u0, 'r-')

# Implementation of the numerical methods.

  irange = [ y + 1 for y in range(nt) ]

  for i in irange:

# Upwind nonconservative.

    if method == 1:
      if bc == 0 or bc == 1:
        unew[0] = u[0]
      elif bc == 4:
        unew[0] = u[0] + dt * ( -1/dx * u[0] * ( u[0] - u[-1] ) + g[0] )

      unew[1:] = u[1:] + dt * ( -1/dx * u[1:] * ( u[1:] - u[:-1] ) + g[1:] )

# Upwind conservative.

    if method == 2:
      if bc == 0 or bc == 1:
        unew[0] = u[0]
      elif ( bc == 4 ):
        unew[0] = u[0] + dt * ( -1/dx * ( f(u[0]) - f(u[-1]) ) + g[0] )

      unew[1:] = u[1:] + dt * ( -1/dx * ( f(u[1:]) - f(u[:-1]) ) + g[1:] )

# Godunov

    if method == 3:
      if bc == 0 or bc == 1:
        unew[0] = u[0]
      elif ( bc == 4 ):
        unew[0] = u[0] + dt * ( -1/dx * ( nf(u[0], u[1])
          - nf(u[nx-1], u[0]) ) + g[0] )

      unew[1:-1] = u[1:-1] + dt * ( -1/dx * ( nf(u[1:-1], u[2:])
        - nf(u[:-2], u[1:-1]) ) + g[1:-1] )

      if ( bc == 0 or bc == 2 ):
        unew[-1] = u[-1]
      elif ( bc == 1 ):
        unew[-1] = u[-1] + dt * ( -1/dx * ( nf(u[-1], u[-1])
          - nf(u[-2], u[-1]) ) + g[-1] )
        # assume neumann at the rightend
      elif ( bc == 4 ):
        unew[-1] = u[-1] - dt / dx * ( nf(u[-1], u[0]) - nf(u[-2], u[-1]) )

#  Save the latest result.
    u = unew
    U[i, :] = u
    Dsav[i, :] = np.concatenate( (param, dt*i, u), axis = None )

#  Plot the profile curve.
    if plot:
      line1.set_ydata(u)
      fig.canvas.draw()
      fig.canvas.flush_events()
      plt.pause(0.001)

  return U, Dsav


def compute_dudmu_FD ( mu, h=0.0000001, numx=50, numt=100 ):
  """
  Function for computing central difference derivatives of the solution u with
  respect to the parameters \mu.

  Input:   mu -- 1x2 list or array, \mu parameters for simulation
           h -- float, difference parameter (optional).
           numx -- int, number of spatial nodes (optional)
           numt -- int, number of time steps (optional)

  Output:  dudmu1 -- list of \mu1 derivatives at each time and node
           dudmu2 -- list of \mu2 derivatives at each time and node
  """

  # Forward and Backward solutions with central difference
  Uf = burgers( 2, numx, numt, 35, 1, [mu[0] + h, mu[1]] , False )[0][0]
  Ub = burgers( 2, numx, numt, 35, 1, [mu[0] - h, mu[1]] , False )[0][0]
  dudmu1 = [ (Uf[i] - Ub[i]) / (2*h) for i in range(len(Uf)) ]

  Uf = burgers( 2, numx, numt, 35, 1, [mu[0], mu[1] + h] , False )[0][0]
  Ub = burgers( 2, numx, numt, 35, 1, [mu[0], mu[1] - h] , False )[0][0]
  dudmu2 = [ (Uf[i] - Ub[i]) / (2*h) for i in range(len(Uf)) ]

  return dudmu1, dudmu2


def generate_FD_gradients( q, h, T, mu ):
  """
  Simple script for generating gradients of Q2, Q3alt
    using second-order finite differences.
  Default values for Burgers' are 256 spatial nodes and 2k time steps.

  Input:  q -- integer, 2 or 3
          h -- float, difference parameter.
          T -- int or float, final simulation time.
          mu -- 1x2 list or array, \mu parameters for simulation

  Output:  Q -- float, function value
           gradQ -- 1x3 numpy array, derivatives of Q w.r.t. (t, \mu).
  """

  if q == 2:
    Q = burgers( 2, 256, 2000, T, 1, mu, False )[2]

    Qf = burgers( 2, 256, 2000, T + h, 1, mu, False )[2]
    Qb = burgers( 2, 256, 2000, T - h, 1, mu, False )[2]
    dQdT = (Qf - Qb) / (2*h)

    Qf = burgers( 2, 256, 2000, T, 1, [mu[0] + h, mu[1]], False )[2]
    Qb = burgers( 2, 256, 2000, T, 1, [mu[0] - h, mu[1]], False )[2]
    dQdmu1 = (Qf - Qb) / (2*h)

    Qf = burgers( 2, 256, 2000, T, 1, [mu[0], mu[1] + h], False )[2]
    Qb = burgers( 2, 256, 2000, T, 1, [mu[0], mu[1] - h], False )[2]
    dQdmu2 = (Qf - Qb) / (2*h)

  elif q == 3:
    Q = burgers( 2, 256, 2000, T, 1, mu, False )[4]

    Qf = burgers( 2, 256, 2000, T + h, 1, mu, False )[4]
    Qb = burgers( 2, 256, 2000, T - h, 1, mu, False )[4]
    dQdT = (Qf - Qb) / (2*h)

    Qf = burgers( 2, 256, 2000, T, 1, [mu[0] + h, mu[1]], False )[4]
    Qb = burgers( 2, 256, 2000, T, 1, [mu[0] - h, mu[1]], False )[4]
    dQdmu1 = (Qf - Qb) / (2*h)

    Qf = burgers( 2, 256, 2000, T, 1, [mu[0], mu[1] + h], False )[4]
    Qb = burgers( 2, 256, 2000, T, 1, [mu[0], mu[1] - h], False )[4]
    dQdmu2 = (Qf - Qb) / (2*h)

  else:
    print("not a valid choice!")

  gradQ = np.array( [dQdT, dQdmu1, dQdmu2] )

  return Q, gradQ
