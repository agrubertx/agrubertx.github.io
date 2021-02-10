from __future__ import division

import numpy as np
import scipy as sy
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import model_selection
import json, codecs
import active_subspaces as ac
import burgers as bg


# function for saving objects
def jsonify(obj, out_file):
  """
  This function saves obj to the path out_file as a json file.

  Inputs:
  - obj: the object to be jsonified
  - out_file: the file path where obj will be saved
  """
  json.dump(obj, codecs.open(out_file, 'a', encoding='utf-8'),
            separators=(',', ':'), sort_keys=True, indent=4)


def make_mesh( dim, numpts ):
  """
  Create grid of uniformly sampled pts over [-1,1]^dim.

  Input:  dim -- int, dimension of space m
          numpts -- number of points to sample along each axis

  Output:  meshPoints -- list, points of mesh arranged lexicographically
  """

  # if numpts is None:
  # # Define mesh
  #     numpts = (2. // step) + 1.
  mesh = np.meshgrid( *[ np.linspace( -1., 1., numpts ) for i in range(dim) ] )

  # Make mesh into list of points
  # Order them lexicographically
  mesh = [ mesh[i].reshape( (np.prod( mesh[i].shape), )
                          ) for i in np.arange( len(mesh) ) ]

  meshPoints = np.asarray( sorted( zip(*mesh) ) )

  return meshPoints


def sample_f_on_mesh( f, meshPoints ):
  """
  Evaluate a function on a set of points.

  Input:  f -- function R^m to R
          meshPoints -- list of input values in R^m

  Output:	 array, f evaluated at elements of meshPoints
  """

  return np.array( list( map( lambda x: f(*x), meshPoints ) ), dtype=float )


def compute_paths( gradf, meshPoints ):
  """
  Evaluate and normalize the gradient of f.

  Input:	gradf -- function, gradient of f: R^m -> R
          meshPoints -- list, input values in R^m

  Output:	gradPaths -- array, \nabla f evaluated at meshPoints, normalized
          realGrads -- array, \nabla f evaluated at meshPoints
          cpIdx -- list, indices of critical points inside meshPoints
  """

  # Evaluate grad f on points of base space
  realGrads = np.asarray( list( map( lambda x: gradf(*x), meshPoints )
                              ), dtype=float )

  # Normalize
  gradPaths = preprocessing.normalize(realGrads)

  # Find critical points, save them into an index list
  cpIdx = [ i for i in range( len(gradPaths) )
            if np.linalg.norm(gradPaths[i]) == 0 ]

  return gradPaths, realGrads, cpIdx


def build_uniform_data( dim, numPoints, f, grad_f ):
  """
  Builds 'numPoints' test points uniformly distributed across [-1,1]^dim.

  Input:  dim -- integer, dimension of input space
          numPoints -- integer, number of samples
          f -- function from R^m to R
          grad_f -- function, gradient of f: R^m -> R

  Output:  mesh -- (numPoints x dim) array of sample points
           fx -- array, f evaluated at sample points
           amGrads -- array, \nabla f evaluated at sample points, normalized
           realGrads -- array, \nabla f evaluated at sample points
  """

  mesh = make_mesh( dim = dim, numpts = numPoints )
  fx = sample_f_on_mesh( f, mesh )
  amGrads, realGrads = compute_paths( grad_f, mesh )[:-1]

  return mesh, fx, amGrads, realGrads


def build_random_data( dim, numPoints, f, grad_f, seed = 0, Gaussian = False ):
  """
  Builds 'numPoints' test points randomly distributed across [-1,1]^dim.

  Input:  dim -- integer, dimension of input space
          numPoints -- integer, number of samples
          f -- function from R^m to R
          grad_f -- function, gradient of f: R^m -> R
          seed -- integer, seed for random
          Gaussian -- bool, draws points according to a Gaussian distribution.

  Output:  mesh -- (numPoints x dim) array of sample points
           fx -- array, f evaluated at sample points
           amGrads -- array, \nabla f evaluated at sample points, normalized
           realGrads -- array, \nabla f evaluated at sample points
  """

  np.random.seed(seed)

  if Gaussian:
    mesh = np.random.multivariate_normal( np.zeros(dim),
                                          np.eye(dim), (numPoints) )

  else:
    mesh = np.random.uniform( -1.0, 1.0, (numPoints, dim) )

  fx = sample_f_on_mesh( f, mesh )
  amGrads = compute_paths( grad_f, mesh )[0]
  realGrads = compute_paths( grad_f, mesh )[1]

  return mesh, fx, amGrads, realGrads


def get_random_init_pt( dim, seed = 0 ):
  """
  Get random point in [-1,1]^dim using seed 'seed'.

  Inputs:  dim -- int, dimension of domain
           seed -- int, seed for random draw (default = 0)

  Output:  1D np.array of length 'dim'
  """

  np.random.seed(seed)

  return np.ravel( 2 * np.random.rand( dim, 1 ) -1 )


def build_AM_from_data( seedPoint, meshPoints, fSamples, realGrads, stepsize ):
  """
  Build active manifold through seedPoint using data held in inputs 2-4.

  Input:  seedPoint -- array or list, random REGULAR value in [-1,1]^m (no CP)
          meshPoints -- array or list, sample points used for training.
          fSamples -- array, f evaluated at meshPoints
          gradPaths -- array, grad f evaluated at meshPoints
          stepsize -- float, increment between points along the AM

  Output: activeManifold -- array, ordered points of the active manifold
          fValues -- array, function values along the active manifold
  """

  gradPaths = preprocessing.normalize(realGrads)

  mesh_kdtree = sy.spatial.KDTree(meshPoints, 1000)

  # Define region / hypercube [-1,1]^(m+1)
  dim = len(seedPoint)
  rBound = np.ones(dim)
  #rBound = np.append(np.ones(liftDim - 1),t_0)
  Dom = sy.spatial.Rectangle( -1*rBound, rBound )

  # Define starting point
  p0 = seedPoint

  # Find closest mesh point to seedpoint (i0 is index)
  # Use d0 for first direction
  i0 = mesh_kdtree.query(p0)[1]
  c0 = mesh_kdtree.data[i0]
  d0 = gradPaths[i0]

  # Line integral to get f(p0).
  fp0 = fSamples[i0] + np.dot( realGrads[i0], p0-c0 )

  # Initialize gradient ascent
  ascentPoints = np.asarray(p0)
  aCloseVals = np.asarray(fp0)

  # Take one step
  p1 = p0 + (stepsize * d0)

  i1 = mesh_kdtree.query(p1)[1]
  c1 = mesh_kdtree.data[i1]

  fp1 = fSamples[i1] + np.dot( realGrads[i1], p1-c1 )

  ascentPoints = np.vstack( (ascentPoints,p1) )
  aCloseVals = np.append( aCloseVals, fp1 )

  cond = np.array(1)
  # Gradient ascent, computing line integrals to recover f along the AM
  while ( Dom.min_distance_point(ascentPoints[-1]) == 0
          and min(cond.flatten()) > 1*stepsize/3 ):

    iOld = mesh_kdtree.query( ascentPoints[-1] )[1]
    d = gradPaths[iOld]

    p = ascentPoints[-1] + (stepsize * d)

    i = mesh_kdtree.query(p)[1]
    c = mesh_kdtree.data[i]

    fp = fSamples[i] + np.dot( realGrads[i], p - c )

    ascentPoints = np.vstack( (ascentPoints, p) )
    aCloseVals = np.append( aCloseVals, fp )

    #update loop condition
    cond = sy.spatial.distance.cdist( [ascentPoints[-1]],
      ascentPoints[0:len(ascentPoints)-1], 'euclidean' )

  # Delete last elements (outside of hypercube)
  ascentPoints = np.delete( ascentPoints, len(ascentPoints) - 1, 0 )
  aCloseVals = np.delete( aCloseVals, len(aCloseVals) - 1, 0 )

  # Initialize gradient descent
  descentPoints = np.asarray(p0)
  dCloseVals = fp0

  # Take one step
  p1 = p0 - stepsize * d0

  c1dist, i1 = mesh_kdtree.query(p1)
  c1 = mesh_kdtree.data[i1]

  fp1 = fSamples[i1] + np.dot( realGrads[i1], p1-c1 )

  descentPoints = np.vstack( (descentPoints, p1) )
  dCloseVals = np.append( dCloseVals, fp1 )

  # cond = np.array(1)

  # Gradient descent, using line integrals to recover f along the AM
  while ( Dom.min_distance_point(descentPoints[-1]) == 0
        and min(cond.flatten()) > 1*stepsize/3 ):

    iOld = mesh_kdtree.query( descentPoints[-1] )[1]
    d = gradPaths[iOld]

    p = descentPoints[-1] - stepsize * d

    i = mesh_kdtree.query(p)[1]
    c = mesh_kdtree.data[i]

    fp = fSamples[i] + np.dot( realGrads[i], p - c )

    descentPoints = np.vstack( (descentPoints, p) )
    dCloseVals = np.append( dCloseVals, fp )

    # update loop condition
    cond = sy.spatial.distance.cdist( [descentPoints[-1]],
      descentPoints[0:len(descentPoints)-1], 'euclidean' )

  # Delete first and last element in descentpoints and fValuesdescent
  descentPoints = np.delete( descentPoints, 0, 0 )
  descentPoints = np.delete( descentPoints, len(descentPoints) - 1, 0 )
  dCloseVals = np.delete( dCloseVals, 0 )
  dCloseVals = np.delete( dCloseVals, len(dCloseVals) - 1 )

  # Flip order of descentPoints and concatenate lists
  activeManifold = np.concatenate(
                    ( np.flipud(descentPoints), ascentPoints ), axis=0 )

  fCloseVals = np.concatenate( ( np.flipud(dCloseVals), aCloseVals ) )

  return activeManifold, fCloseVals


def splinePlot( activeManifold, fValues, func, sub, pdf = False ):
  """
  Input:  activeManifold -- array, ordered points of the active manifold
          fValues -- array, function values along the active manifold
          func -- string, title of plot
          sub -- string, subscript for AM \gamma(t)
          pdf -- bool, 'true' saves plot to current directory.

  Output:  matplotlib.pyplot figure, cubic splines fit to f along the AM
  """

  numpts = len(activeManifold)

  sValues = np.linspace( 0., numpts, numpts ) / numpts
  xp = np.linspace( 0., numpts, 2 * (numpts) ) / numpts

  spline = sy.interpolate.PchipInterpolator( sValues, fValues )

  fig=plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title( r'Value of ${}$ Along $\gamma_{}(t)$'.
                  format( func, sub ), fontsize = 13 )
  ax.set_xlabel( r'Curve Parameter: $t$', fontsize = 13 )
  ax.set_ylabel( r'Function Value: ${}\,(\gamma_{}\,(t))$'.
                  format( func, sub ), fontsize = 13 )
  plt.scatter( sValues, fValues, c = '#fc8d62', s = 17 )
  plt.plot( xp, spline(xp), '-', c = '#66c2a5', lw = 3 )
  plt.xlim(0,1)
  plt.grid(True)

  if pdf:
    return plt.savefig( str(func) + str(sub) + 'FitSpline' + '.pdf' )


def manifoldEx( inputs, fSamples, grads, stepsize, test_size, seedPoint,
  seed = 0, plot = True, outpath = None ):
  """
  Script for testing error between function and Active Manifold approximation.

  Input:  inputs -- list or array, sample points in [-1,1]^dim
          fSamples -- list or array, f evaluated at inputs
          grads -- list or array, \nabla f evaluated at inputs
          stepsize -- float, increment between points along the AM
          test_size -- float in [0,1], fraction of samples to use for testing
          seedPoint -- 1 x dim array, initial condition for AM
          seed -- integer, seed for random
          plot -- bool, 'True' runs splinePlot funcition above
          outpath -- path to file, where to save printouts

  Output:  console printout of relative L1, L2 approximation errors.
  """

  # Single-step line integral to recover function value at unknown points
  def get_f_value( startPoint, mesh_kdtree, fSamples, realGrads ):
    cdist, i = mesh_kdtree.query(startPoint)
    c = mesh_kdtree.data[i]
    fStartPoint = fSamples[i] + np.dot( realGrads[i], startPoint - c )

    return fStartPoint

  # Random Samples to Test function approximation on
  meshPoints, testPoints, fSampsTraining, fSampsTest, meshGrads, testGrads = (
  model_selection.train_test_split( inputs, fSamples, grads,
  test_size = test_size, random_state = seed ) )

  # Compute normalized gradient
  gradPaths = preprocessing.normalize(meshGrads)

  mesh_kdtree = sy.spatial.KDTree(meshPoints, 1000)

  # Build active manifold
  if plot:
    activeManifold, fValsAM = build_AM_from_data(
      seedPoint = seedPoint, meshPoints = meshPoints,
      fSamples = fSampsTraining, realGrads = meshGrads, stepsize = stepsize)

    splinePlot( activeManifold, fValsAM, "function", "{}" )

  fApproxVals = [ get_f_value( tp, mesh_kdtree, fSampsTraining, meshGrads )
                  for tp in testPoints ]

  # Average L1, L2 error of the fit
  # fitErrorL1 = np.mean( np.abs( fSampsTest - fApproxVals ) )
  # fitErrorL2 = ( np.linalg.norm( fApproxVals - fSampsTest )
  #              / float( len(testPoints) ) )

  # Relative L1, L2 errors
  relErrorL1 = ( np.sum( np.abs( fSampsTest - fApproxVals) )
               / np.sum( np.abs(fSampsTest) ) * 100 )
  relErrorL2 = ( np.linalg.norm( fApproxVals - fSampsTest )
               / np.linalg.norm(fSampsTest) * 100 )

  results = {'relative L1 error': relErrorL1, "relative L2 error": relErrorL2}
  if outpath:
    jsonify(results, outpath)

  # print 'The Average L1 Error is %f or %f%%' %(fitErrorL1, relErrorL1)
  # print 'The Average L2 Error is %f or %f%%' %(fitErrorL2, relErrorL2)

  print( 'The Relative L1 Error is %f%%' %relErrorL1 )
  print( 'The Relative L2 Error is %f%%' %relErrorL2 )


def subspEx( inputs, fSamples, grads, dim, seed = 0,
  test_size = .2, plot = True, poly = False, outpath = None ):
  """
  Script for testing error between function and Active Subspace approximation.

  Input:  inputs -- list or array, sample points in domain
          fSamples -- list or array, f evaluated at inputs
          grads -- list or array, \nabla f evaluated at inputs
          dim -- integer, desired dimension of the AS
          test_size -- float in [0,1], fraction of samples to use for testing
          seedPoint -- 1 x dim array, initial condition for AM
          plot -- bool, 'True' runs Constantine's plot functions
          poly -- bool, 'True' trains a degree 2 poly approximation on the AS
                        'False' trains a degree 2 radial basis approximation
          outpath -- path to file, where to save error printouts

  Output:  console printout of relative L1, L2 approximation errors.
  """

  # Generate training/testing points based on partNum
  X_train, X_test, y_train, y_test, grad_train, grad_test = ( model_selection
  .train_test_split( inputs, fSamples, grads,
  test_size = test_size, random_state = seed ) )

  # Build active subspace from training points
  # ss = ac.subspaces.Subspaces()
  # ss.compute( df=grad_train, sstype='AS' )

  ss = ac.subspaces.Subspaces()
  ss.compute( df=grad_train, nboot=100 )
  ss.partition(dim)
  xRed = np.dot( X_train, ss.W1 )

  # Plot Eigenvals
  if plot:
    ac.utils.plotters.eigenvalues(ss.eigenvals)

  # Determine AS dimension
  dimension = len(ss.W1[0])
  print( 'The dimension of the Active Subspace is %i' %dimension )

  # reshape f values for traing
  fTrainVals = y_train.reshape( ( len(y_train), 1 ) )

  if poly:
    # Build polynomial approximation to the data, using Constantine functions
    rs = ac.subspaces.PolynomialApproximation(2)
    rs.train( xRed, fTrainVals )
    print( 'The R^2 value of the response surface is {:.4f}'.format(rs.Rsqr) )

    #Compute approximate fVals
    xTestRed = np.dot( X_test, ss.W1 )
    fApproxVals = rs.predict(xTestRed)[0]
    fTestVals = y_test.reshape( (len(y_test), 1) )

  else:
    # set up the active variable domain
    avd = ac.domains.BoundedActiveVariableDomain(ss)
    # set up the maps between active and full variables
    avm = ac.domains.BoundedActiveVariableMap(avd)
    #Build and train response surface
    rs = ac.response_surfaces.ActiveSubspaceResponseSurface(avm)
    rs.train_with_data( X_train, fTrainVals )

    #Compute approximate fVals
    fApproxVals = rs.predict(X_test)[0]
    fTestVals = y_test.reshape( (len(y_test), 1) )

  # Plot it (only works for dimensions 1 and 2)
  if plot:
    xRed = np.dot( X_train, ss.W1 )

    if dim == 1:
      plt.figure( figsize=(7, 7) )
      y0 = np.linspace( -1, 1, 200 )
      plt.scatter( xRed, y_train, c = '#66c2a5' )

      if poly:
        plt.plot( y0, rs.predict(y0[:, None])[0],
                  c = '#fc8d62', ls='-', linewidth=2 )

      else:
        plt.plot( y0, rs.predict_av(y0[:, None])[0],
                  c = '#fc8d62', ls='-', linewidth=2 )

      plt.grid(True)
      plt.xlabel( 'Active Variable Value', fontsize=18 )
      plt.ylabel( 'Output', fontsize=18 )

    if dimension == 2:
      if not poly:
        ac.utils.plotters.sufficient_summary( xRed, y_train )

  # Average L1, L2 errors
  # fitErrorL1 = np.mean( np.abs( fTestVals - fApproxVals ) )
  # fitErrorL2 = ( np.linalg.norm( fTestVals - fApproxVals )
  #                / float( len(fTestVals) ) )

  # Relative L1, L2 errors
  relErrorL1 = ( np.sum( np.abs( fTestVals - fApproxVals) )
               / np.sum( np.abs(fTestVals) ) * 100 )
  relErrorL2 = ( np.linalg.norm( fTestVals - fApproxVals )
               / np.linalg.norm(fTestVals) * 100 )

  results = {'relative L1 error': relErrorL1, "relative L2 error": relErrorL2}
  if outpath:
    jsonify( results, outpath )

  # print 'The Average L1 Error is %f or %f%%' %(fitErrorL1, relErrorL1)
  # print 'The Average L2 Error is %f or %f%%' %(fitErrorL2, relErrorL2)
  print( 'The Relative L1 Error is %f%%' %relErrorL1 )
  print( 'The Relative L2 Error is %f%%' %relErrorL2 )


# Single-step line integral to recover function value at unknown points
def get_f_value( startPoint, mesh_kdtree, fSamples, realGrads ):
  """
  Same method implemented in manifoldEx.
  """

  cdist, i = mesh_kdtree.query(startPoint)
  c = mesh_kdtree.data[i]
  fStartPoint = fSamples[i] + np.dot( realGrads[i], startPoint - c )

  return fStartPoint


def test_local_linear(meshPoints, fVals, meshGrads, numx, numt, mu1, mu2, t, numplots):
  """
  Script for testing the reconstruction error of solutions to the 1-D inviscid
  Burgers equation.  Computes a linear interpolant from mu1 and mu2 and
  compares the error at some times

  Input:  meshPoints -- list or array, sample points in domain
          fVals -- list or array, f evaluated at inputs
          meshGrads -- list or array, \nabla f evaluated at inputs
          numx -- integer, number of spatial nodes
          numt -- integer, number of time steps
          mu1 -- 1x2 array of first \mu coordinates
          mu2 -- 1x2, array of second \mu coordinates
          t -- float in [0,1], parameter for linear interpolation
          numplots -- integer in [0,10], number of times at which to plot soln.

  Output:  plot comparing exact solution, AM approx., and LL approx.
           console printout of relative L1, L2 approximation errors.
  """

  # Parameters for Burgers simulations
  xx = np.linspace(0, 100, numx)
  dx = (100-0) / numx
  dt = 35 / numt
  tt = np.array( [dt * i for i in range(numt+1)] )

  UBs = np.array( [100, 35, 5.5, 0.03], dtype=float )
  LBs = np.array( [0, 0, 4.25, 0.015], dtype=float )

  # Exact solutions at mu1, mu2
  Utrain1 = bg.burgers(2, numx, numt, 35, 1, mu1, False)[0]
  Utrain2 = bg.burgers(2, numx, numt, 35, 1, mu2, False)[0]

  tree = sy.spatial.KDTree(meshPoints, 3000)

  # Interpolated mu
  interpmu = t * mu2 + (1-t) * mu1

  # Exact solution at interpmu
  trueU = bg.burgers(2, numx, numt, 35, 1, interpmu, False)[0]

  # Interpolated solution
  interpU = [ t * Utrain2[0][i] + (1-t) * Utrain1[0][i]
              for i in range(len(Utrain1[0])) ]

  # Points for AM approximation
  test = np.array( [ np.concatenate( [[xx[j], tt[k]], interpmu] )
                  for k in range(len(tt)) for j in range(len(xx)) ] )

  nuTest = 2 / (UBs - LBs) * (test - LBs) - 1

  vals = [0,0,0,0,0,0,0,0,0,0]

  # Computing AM approximation
  for i in range(numplots):
    idx = int(numx / 10 * numt)
    vals[i] = np.array( [ get_f_value( nuTest[idx*(i+1) + j],
                       tree, fVals, meshGrads ) for j in range(numx) ] )

  # Error printouts
  print("Errors in AM approximation")
  for i in range(numplots):
    k = int(0.1 * numt * (i+1))

    relErrorL1 = ( np.sum( np.abs( vals[i] - trueU[0][k]) )
                  / np.sum( np.abs(trueU[0][k]) ) * 100 )
    print("The relative L1 error for t = %f is %f" %( 3.5*(i+1), relErrorL1 ))

    relErrorL2 = ( np.linalg.norm( vals[i] - trueU[0][k] )
                  / np.linalg.norm(trueU[0][k]) * 100 )
    print("The relative L2 error for t = %f is %f" % ( 3.5*(i+1), relErrorL2 ))

  print(" ")

  print("Errors in local linear approximation")
  for i in range(numplots):
    k = int(0.1 * numt * (i+1))

    relErrorL1 = ( np.sum( np.abs( interpU[k] - trueU[0][k]) )
                  / np.sum( np.abs(trueU[0][k]) ) * 100 )
    print("The relative L1 error for t = %f is %f" %( 3.5*(i+1), relErrorL1 ))

    relErrorL2 = ( np.linalg.norm( interpU[k] - trueU[0][k] )
                  / np.linalg.norm(trueU[0][k]) * 100 )
    print("The relative L2 error for t = %f is %f" % ( 3.5*(i+1), relErrorL2 ))

  # Plots.
  fig = plt.figure(figsize = (8, 6))
  ax = fig.add_subplot(111)
  for i in range(numplots):
    k = int(0.1 * numt * (i+1))

    plt.plot(test[:numx][:,0], trueU[0][k], '-', c = 'darkslategrey',
             label = 'FOM' if i == 0 else "", markersize=2, linewidth=2)

    plt.plot(test[:numx][:,0], interpU[k], linestyle = 'dotted', c = 'orange',
             label = 'linear' if i == 0 else "", markersize=3, linewidth=3)

    plt.plot(test[:numx][:,0], vals[i], '-.', c = 'lightseagreen',
             label = 'AM' if i == 0 else "", markersize=2, linewidth=2)

  plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
  plt.show()


#### DEPRECATED FUNCTION ####
def subspExOld( inputs, fSamples, grads, dim, test_train_split_seed = 0, test_size = .2, outpath = None ):
  """
  Function for building active subspace using Constantines method (Deprecated)
  """

  # Generate training/testing points based on partNum
  X_train, X_test, y_train, y_test, grad_train, grad_test= model_selection.train_test_split(
      inputs, fSamples, grads, test_size = test_size, random_state = test_train_split_seed )

  # Build active subspace from trainingPoints with 100 bootstrap replicates
  ss = ac.subspaces.Subspaces()
  ss.compute( df=grad_train, nboot=100 )
  ss.partition(dim)
  xRed = np.dot( X_train, ss.W1 )

  # Build polynomial approximation to the data, using Constantine functions
  rs = ac.subspaces.PolynomialApproximation(4)
  #RS = ac.utils.response_surfaces.RadialBasisApproximation(2)
  y_train = y_train.reshape( ( len(y_train), 1 ) )
  rs.train( xRed, y_train )
  print( 'The R^2 value of the response surface is {:.4f}'.format(rs.Rsqr) )

  # Plot it
  if dim == 1:
      plt.figure( figsize=(7, 7) )
      y0 = np.linspace( -1, 1, 200 )
      plt.scatter( xRed, y_train, c = '#66c2a5' )
      plt.plot( y0, rs.predict(y0[:, None])[0], c = '#fc8d62', ls='-', linewidth=2 )
      plt.grid(True)
      plt.xlabel( 'Active Variable Value', fontsize=18 )
      plt.ylabel( 'Output', fontsize=18 )

  #Compute approximate fVals
  xTestRed = np.dot( X_test, ss.W1 )
  fApproxVals = rs.predict(xTestRed)[0]
  fTestVals = y_test.reshape( (len(y_test), 1) )

  # # Average L1, L2 errors
  # fitErrorL1 = np.mean( np.abs( fTestVals - fApproxVals ) )
  # fitErrorL2 = np.linalg.norm( fTestVals - fApproxVals ) / float( len(fTestVals) )

  # Relative L1, L2 errors
  relErrorL1 = np.sum( np.abs( fTestVals - fApproxVals) ) / np.sum( np.abs(fTestVals) ) * 100
  relErrorL2 = np.linalg.norm( fTestVals - fApproxVals ) / np.linalg.norm(fTestVals) * 100

  results = { 'fit L1 error': fitErrorL1, "fit L2 error": fitErrorL2 }
  if outpath:
      jsonify( results, outpath )

  # print 'The Average L1 Error is %f or %f%%' %(fitErrorL1, relErrorL1)
  # print 'The Average L2 Error is %f or %f%%' %(fitErrorL2, relErrorL2)
  print( 'The Relative L1 Error is %f%%' %relErrorL1 )
  print( 'The Relative L2 Error is %f%%' %relErrorL2 )

# def closest_node(node, nodes):
#     return nodes[sy.spatial.distance.cdist([node], nodes).argmin()]
