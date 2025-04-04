---
permalink: /
title: "About Me"
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---
<!-- ![image-center](/images/frontpage.jpg){: .align-center} -->
<!-- ![Alt Text](/files/gifs/knotFandB.gif) -->

<!-- ![image-left](/images/me.png){: width="400" } ![image-right](/files/gifs/knotFandB.gif){: width="300" } -->

<!-- ![image-left](/images/me_over_gorge.JPG){: width="280" } ![image-left](/images/me_w_sunglasses.JPG){: width="160" } ![image-left](/images/me.png){: width="320" } -->

<!-- ![image-left](/images/me_over_gorge.JPG){: width="280" } ![image-left](/images/me_in_Florence.pdf){: width="140" } ![image-left](/images/me.png){: width="320" } -->

![image-left](/images/me_over_gorge.JPG){: width="360" } ![image-left](/images/me_in_Florence.pdf){: width="182" } ![image-left](/images/me_w_sunglasses.JPG){: width="203" }

I am a mathematician interested in basic and applied research questions that arise in the contexts of geometric mechanics, data science, nonlinear PDEs, and scientific machine learning.
<!-- {: .notice--success} -->

Lately, my focus is primarily on developing structure-informed numerical methods for scientific applications.  Doing this generally involves identifying or reasoning about some abstract mathematical structure which is important for a particular physical phenomenon, formulating a smart discretization (based on, e.g., a finite element or artificial neural network backbone) which takes this structure into account, and writing mathematical software in Python or C++ which implements a proposed approach.  Over time, I've found that my preferred flavor of research problem leaves ample opportunity for geometric ideas, satisfying visuals, and punchy algebraic arguments which are characteristic of my personal style.

<details markdown="1"><summary><b>More about me</b></summary>
{: .notice--info}

A differential geometer by training, I received my PhD from Texas Tech University under the guidance of <a href="http://www.math.ttu.edu/~mtoda/">Magdalena Toda</a>, with co-advisors <a href="http://www.math.ttu.edu/~eaulisa/">Eugenio Aulisa</a> and <a href="https://www.math.uci.edu/~hungtt1/">Hung Tran</a>. At this time, I applied techniques from Riemannian geometry, variational calculus, and differential topology to study functionals involving surface curvature, with the ultimate goal of understanding their extrema. Moreover, I was (and still am) interested in understanding the possible immersions of a given topological space inside another, including what configurations are "preferred" (usually energy-minimizing) in this case.  I also spent quite a bit of time thinking about the computational modeling of geometric objects, sparking a standing interest in computer graphics which can be seen in the various simulation videos found on the <a href="/gallery/">Gallery</a> page.
<br><br>
Catalyzed by an NSF internship at Oak Ridge National Lab (featured [here!](https://orise.orau.gov/nsf-msgi/profiles/gruber.html)) toward the end of graduate school where I worked with <a href="https://sites.google.com/site/robertbridgeshomepage/">Robert Bridges</a>, I became involved post-PhD in scientific algorithm development for dimension reduction, function approximation, and the reduced-order modeling of PDEs.  This led to a postdoctoral appointment with <a href="https://people.sc.fsu.edu/~mgunzburger/">Max Gunzburger</a> at FSU working on data-driven strategies for predictive tasks related to ocean modeling.  At the same time as my application-driven interests were shifting, my purer "side project" work also moved in the direction of rigidity results for geometric objects constrained by curvature conditions.  Now, I maintain active interests in several areas of mathematics, computer science, and engineering.
<br><br>
Broad research keywords which tend to interest me include: scientific machine learning, computational and discrete geometry, conservation laws, reduced-order modeling, manifold learning, harmonic maps, surface immersions, and integrability problems.
{: .notice--info}

<!-- A more detailed description of my interests can be found in my <a href="/files/Research_Statement.pdf">academic research statement</a> (current as of 9/21). -->

<!-- Lately, my focus is primarily on developing structure-informed numerical methods for scientific applications.  Doing this generally involves identifying/reasoning about some abstract mathematical structure which is important for a particular phenomenon, formulating a smart discretization (based on e.g. a finite element or artificial neural network backbone) which takes this structure into account, and writing mathematical software in Python or C++ which implements the proposed discretization.  Over time, I've found that my preferred "flavor" of research problem creates ample opportunity for algebraic reasoning, flashy visuals, and short "punchy" arguments which are characteristic of my personal style.

<br><br> -->

</details>


![image-right](/files/gifs/knotFandB.gif){: .align-right}{: width="200" } <br><br> Below are some coarse categories containing (some of) my work. Some have their own page for further reading.  (This part of the website is a work-in-progress.) <br><br>


Structure-Informed Model Reduction and Function Approximation
-----
<img src="/images/GCNN_recon2.png" style="max-height: 275px; max-width: 325px; margin-right: 16px" align=left>  Due to their high computational cost, scientific studies based on large-scale simulation frequently operate at a data deficit which creates problems inverse to the issues with "big data".  Particularly, there is a need for efficient function approximation and model reduction strategies which can serve as cheap and reliable surrogates for the high-fidelity models used in practical applications.  These projects develop such technology using invariances and other structural considerations as a starting point, allowing for informed surrogates with beneficial behavior.

<details markdown="1"><summary><b>Projects</b></summary>
{: .notice}

### Tensor Parametric Hamiltonian Operator Inference  [Preprint](https://arxiv.org/abs/2502.10888#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/tensor_wave.pdf" style="max-height: 250px; max-width: 250px; margin-right: 16px; margin-bottom: 10px" align=left>  **Abstract:** TThis work presents a tensor-based approach to constructing data-driven reduced-order models corresponding to semi-discrete partial differential equations with canonical Hamiltonian structure. By expressing parameter-varying operators with affine dependence as contractions of a generalized parameter vector against a constant tensor, this method leverages the operator inference framework to capture parametric dependence in the learned reduced-order model via the solution to a convex, least-squares optimization problem. This leads to a concise and straightforward implementation which compactifies previous parametric operator inference approaches and directly extends to learning parametric operators with symmetry constraints, a key feature required for constructing structure-preserving surrogates of Hamiltonian systems. The proposed approach is demonstrated on both a (non-Hamiltonian) heat equation with variable diffusion coefficient as well as a Hamiltonian wave equation with variable wave speed.
<br><br>
(Joint with [Arjun Vijaywargia](https://arjunveejay.notion.site/Arjun-Vijaywargiya-4f155526b32e4b0a97b7f5dad4c89dde) and [Shane A. McQuarrie](https://github.com/shanemcq18).)
{: .notice--info}

### Efficiently Parameterized Neural Metriplectic Systems  [Preprint](https://arxiv.org/abs/2405.16305#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/metriplectic_diagram.pdf" style="max-height: 250px; max-width: 250px; margin-right: 16px; margin-bottom: 10px" align=left>  **Abstract:** Metriplectic systems are learned from data in a way that scales quadratically in both the size of the state and the rank of the metriplectic data. Besides being provably energy conserving and entropy stable, the proposed approach comes with approximation results demonstrating its ability to accurately learn metriplectic dynamics from data as well as an error estimate indicating its potential for generalization to unseen timescales when approximation error is low. Examples are provided which illustrate performance in the presence of both full state information as well as when entropic variables are unknown, confirming that the proposed approach exhibits superior accuracy and scalability without compromising on model expressivity.
<br><br>
(Joint with [Kookjin Lee](https://scai.engineering.asu.edu/faculty/kookjin-lee/), [Haksoo Lim](https://openreview.net/profile?id=~Haksoo_Lim1), [Noseong Park](https://sites.google.com/view/noseong), and [Nathaniel Trask](https://scholar.google.com/citations?user=6iLMZkwAAAAJ&hl=en).)
{: .notice--info}

### Variationally Consistent Hamiltonian Model Reduction  [Preprint](https://arxiv.org/abs/2404.15315#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/PlateTrajectoriesT005.pdf" style="max-height: 300px; max-width: 300px; margin-right: 16px; margin-bottom: 10px" align=left>  **Abstract:** Though ubiquitous as first-principles models for conservative phenomena, Hamiltonian systems present numerous challenges for model reduction even in relatively simple, linear cases. Here, we present a method for the projection-based model reduction of canonical Hamiltonian systems that is variationally consistent for any choice of linear reduced basis: Hamiltonian models project to Hamiltonian models. Applicable in both intrusive and nonintrusive settings, the proposed method is energy-conserving and symplectic, with error provably decomposable into a data projection term and a term measuring deviation from canonical form. Examples from linear elasticity with realistic material parameters are used to demonstrate the advantages of a variationally consistent approach, highlighting the steady convergence exhibited by consistent models where previous methods reliant on inconsistent techniques or specially designed bases exhibit unacceptably large errors.
<br><br>
(Joint with [Irina Tezaur](https://www.sandia.gov/-ikalash/staff/irina-tezaur-clone/).)
{: .notice--info}

### Reversible and Irreversible Bracket-Based Dynamics for Deep Graph Neural Networks  [Preprint](https://arxiv.org/abs/2305.15616#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/GNN-architecture-diagram-v2.pdf" style="max-height: 300px; max-width: 300px; margin-right: 16px; margin-bottom: 10px" align=left>  **Abstract:** Recent works have shown that physics-inspired architectures allow the training of deep graph neural networks (GNNs) without oversmoothing. The role of these physics is unclear, however, with successful examples of both reversible (e.g., Hamiltonian) and irreversible (e.g., diffusion) phenomena producing comparable results despite diametrically opposed mechanisms, and further complications arising due to empirical departures from mathematical theory. This work presents a series of novel GNN architectures based upon structure-preserving bracket-based dynamical systems, which are provably guaranteed to either conserve energy or generate positive dissipation with increasing depth.  It is shown that the theoretically principled framework employed here allows for inherently explainable constructions, which contextualize departures from theory in current architectures and better elucidate the roles of reversibility and irreversibility in network performance
<br><br>
(Joint with [Kookjin Lee](https://scai.engineering.asu.edu/faculty/kookjin-lee/) and [Nathaniel Trask](https://scholar.google.com/citations?user=6iLMZkwAAAAJ&hl=en).)
{: .notice--info}

### Canonical and Noncanonical Hamiltonian Operator Inference  [Preprint](https://arxiv.org/abs/2304.06262#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/hamopinf_BBMsoln.png" style="max-height: 250px; max-width: 250px; margin-right: 16px; margin-bottom: 10px" align=left>  **Abstract:** A method for the nonintrusive and structure-preserving model reduction of canonical and noncanonical Hamiltonian systems is presented.    Based on the idea of operator inference, this technique is provably convergent and reduces to a straightforward linear solve given snapshot data and gray-box knowledge of the system Hamiltonian.  Examples involving several hyperbolic partial differential equations show that the proposed method yields reduced models which, in addition to being accurate and stable with respect to the addition of basis modes, preserve conserved quantities well outside the range of their training data.
<br><br>
(Joint with [Irina Tezaur](https://www.sandia.gov/-ikalash/staff/irina-tezaur-clone/).)
{: .notice--info}

### Multifidelity Monte Carlo Estimation for Efficient Uncertainty Quantification in Climate-Related Modeling  [Preprint](https://egusphere.copernicus.org/preprints/2022/egusphere-2022-797/){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/ice_mfmc.png" style="max-height: 250px; max-width: 250px; margin-right: 16px; margin-bottom: 10px" align=left>  **Abstract:** Uncertainties in an output of interest that depends on the solution of a complex system (e.g., of partial differential equations with random inputs) are often, if not nearly ubiquitously, determined in practice using Monte Carlo (MC) estimation.  While simple to implement, MC estimation fails to provide reliable information about statistical quantities (such as the expected value of the output of interest) in application settings such as climate modeling for which obtaining a single realization of the output of interest is a costly endeavor.  Specifically, the dilemma encountered is that many samples of the output of interest have to be collected in order to obtain an MC estimator having sufficient accuracy; so many, in fact, that the available computational budget is not large enough to effect the number of samples needed. To circumvent this dilemma, we consider using multifidelity Monte Carlo (MFMC) estimation which leverages the use of less costly and less accurate surrogate models (such as coarser grids, reduced-order models, simplified physics, interpolants, etc.) to achieve, for the same computational budget, higher accuracy compared to that obtained by an MC estimator or, looking at it another way, an MFMC estimator obtains the same accuracy as the MC estimator at lower computational cost.  The key to the efficacy of MFMC estimation is the fact that most of the required computational budget is loaded onto the less costly surrogate models, so that very few samples are taken of the more expensive model of interest.  We first provide a more detailed discussion about the need to consider an alternate to MC estimation for uncertainty quantification.  Subsequently, we present a review, in an abstract setting, of the MFMC approach along with its application to three climate-related benchmark problems as a proof-of-concept exercise.
<br><br>
(Joint with [Max Gunzburger](https://people.sc.fsu.edu/~mgunzburger/), [Lili Ju](https://people.math.sc.edu/ju/), [Rihui Lan](https://scholar.google.com/citations?user=qkMD9tsAAAAJ&hl=en), and [Zhu Wang](https://people.math.sc.edu/wangzhu/).)
{: .notice--info}

### A Multifidelity Monte Carlo Method for Realistic Computational Budgets  [Preprint](http://arxiv.org/abs/2206.07572#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/mfmc_alg_pic.png" style="max-height: 250px; max-width: 250px; margin-right: 16px; margin-bottom: 10px" align=left>  **Abstract:** A method for the multifidelity Monte Carlo (MFMC) estimation of statistical quantities is proposed which is applicable to computational budgets of any size.  Based on a sequence of optimization problems each with a globally minimizing closed-form solution, this method extends the usability of a well known MFMC algorithm, recovering it when the computational budget is large enough. Theoretical results verify that the proposed approach is at least as optimal as its namesake and retains the benefits of multifidelity estimation with minimal assumptions on the budget or amount of available data, providing a notable reduction in variance over simple Monte Carlo estimation.
<br><br>
(Joint with [Max Gunzburger](https://people.sc.fsu.edu/~mgunzburger/), [Lili Ju](https://people.math.sc.edu/ju/), and [Zhu Wang](https://people.math.sc.edu/wangzhu/).)
{: .notice--info}

### Energetically Consistent Model Reduction for Metriplectic Systems  [Preprint](https://arxiv.org/abs/2204.08049#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/gas_containers_FOMs.png" style="max-height: 250px; max-width: 250px; margin-right: 16px; margin-bottom: 10px" align=left>  **Abstract:** The metriplectic formalism is useful for describing complete dynamical systems which conserve energy and produce entropy.  This creates challenges for model reduction, as the elimination of high-frequency information will generally not preserve the metriplectic structure which governs long-term stability of the system.  Based on proper orthogonal decomposition, a provably convergent metriplectic reduced-order model is formulated which is guaranteed to maintain the algebraic structure necessary for energy conservation and entropy formation.  Numerical results on benchmark problems show that the proposed method is remarkably stable, leading to improved accuracy over long time scales at a moderate increase in cost over naive methods.  
<br>
(Joint with [Max Gunzburger](https://people.sc.fsu.edu/~mgunzburger/), [Lili Ju](https://people.math.sc.edu/ju/), and [Zhu Wang](https://people.math.sc.edu/wangzhu/).)
{: .notice--info}

### Comparing Neural Architectures for Reduced-Order Modeling  [Preprint](https://arxiv.org/abs/2110.03442#){: .btn .btn--info .btn--small}{: .align-right} [Read More](/autoencoder-rom/){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/gcnnRom.pdf" style="max-height: 250px; max-width: 250px; margin-right: 16px" align=left>  **Abstract:** The popularity of deep convolutional autoencoders (CAEs) has engendered new and effective reduced-order models (ROMs) for the simulation of large-scale dynamical systems.  Despite this, it is still unknown whether deep CAEs provide superior performance over established linear techniques or other network-based methods in all modeling scenarios.  To elucidate this, the effect of autoencoder architecture on its associated ROM is studied through the comparison of deep CAEs against two alternatives: a simple fully connected autoencoder, and a novel graph convolutional autoencoder.  Through benchmark experiments, it is shown that the superior autoencoder architecture for a given ROM application is highly dependent on the size of the latent space and the structure of the snapshot data, with the proposed architecture demonstrating benefits on data with irregular connectivity when the latent space is sufficiently large.
<br><br>
(Joint with [Max Gunzburger](https://people.sc.fsu.edu/~mgunzburger/), [Lili Ju](https://people.math.sc.edu/ju/), and [Zhu Wang](https://people.math.sc.edu/wangzhu/).)<br>
{: .notice--info}

### Learning the Structure of Level Sets from Sparse Data  [Preprint](https://arxiv.org/abs/2104.14072#){: .btn .btn--info .btn--small}{: .align-right} [Read More](/nll/){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/levset_cartoon.pdf" style="max-height: 250px; width: 250px; margin-right: 16px; margin-bottom: 10px" align=left>  **Abstract:** A dimension reduction method based on the ``Nonlinear Level set Learning'' (NLL) approach is presented for the pointwise prediction of functions which have been sparsely sampled.  Leveraging geometric information provided by the Implicit Function Theorem, the proposed algorithm effectively reduces the input dimension to the theoretical lower bound with minor accuracy loss, providing a one-dimensional representation of the function which can be used for regression and sensitivity analysis.  Experiments and applications are presented which compare this modified NLL with the original NLL and the Active Subspaces (AS) method.  While accommodating sparse input data, the proposed algorithm is shown to train quickly and provide a much more accurate and informative reduction than either AS or the original NLL on two example functions with high-dimensional domains, as well as two state-dependent quantities depending on the solutions to parametric differential equations. 
<br><br>
(Joint with [Max Gunzburger](https://people.sc.fsu.edu/~mgunzburger/), [Lili Ju](https://people.math.sc.edu/ju/), [Yuankai Teng](https://slooowtyk.github.io/), and [Zhu Wang](https://people.math.sc.edu/wangzhu/).)
{: .notice--info}

### Pseudo-Reversible Neural Networks  [Preprint](https://arxiv.org/abs/2112.01438#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/prnn.png" style="max-height: 250px; max-width: 250px; margin-right: 16px" align=left>  **Abstract:** Due to the curse of dimensionality and limitations on training data, approximating high-dimensional functions is a very challenging task even for powerful deep neural networks. Inspired by the Nonlinear Level set Learning (NLL) method that uses the reversible residual network (RevNet), in this paper we propose a new method for function approximation called Dimension Reduction via Learning Level Sets (DRiLLS). Our method contains two major components: one is the pseudo-reversible neural network (PRNN) module that effectively transforms high-dimensional input variables to low-dimensional active variables, and the other is the synthesized regression module for approximating function values based on the transformed data in the low-dimensional space.  Extensive experimental results demonstrate that DRiLLS outperforms both the NLL and Active Subspace methods, especially when the target function possesses critical points in the interior of its input domain.
<br><br>
(Joint with [Lili Ju](https://people.math.sc.edu/ju/), [Yuankai Teng](https://slooowtyk.github.io/), [Zhu Wang](https://people.math.sc.edu/wangzhu/), and [Guannan Zhang](https://sites.google.com/view/guannan-zhang/home).)
{: .notice--info}

### Active Manifolds: Geometric Data Analysis for Dimension Reduction  [Here](http://proceedings.mlr.press/v97/bridges19a/bridges19a.pdf){: .btn .btn--info .btn--small}{: .align-right} [Read More.](/am/){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/AMstuff.png" style="max-height: 300px; max-width: 300px; margin-right: 16px" align=left>  **Abstract:** We present an approach to analyze $$C^1(\mathbb{R}^m)$$ functions that addresses limitations present in the Active Subspaces (AS) method of Constantine et al.  Under appropriate hypotheses, our Active Manifolds (AM) method identifies a 1-D curve in the domain (the active manifold) on which nearly all values of the unknown function are attained, and which can be exploited for approximation or analysis, especially when $$m$$ is large (high-dimensional input space).  We provide theorems justifying our AM technique and an algorithm permitting functional approximation and sensitivity analysis. 
Using accessible, low-dimensional functions as initial examples, we show AM reduces approximation error by an order of magnitude compared to AS, at the expense of more computation.  Following this, we revisit the sensitivity analysis by Glaws et al. who apply AS to analyze a magnetohydrodynamic power generator model, and compare the performance of AM on the same data.  Our analysis provides detailed information not captured by AS, exhibiting the influence of each parameter individually along an active manifold.  Overall, AM represents a novel technique for analyzing functional models with benefits including: reducing $$m$$-dimensional analysis to a 1-D analogue, permitting more accurate regression than AS (at more computational expense), enabling more informative sensitivity analysis, and granting accessible visualizations (2-D plots) of parameter sensitivity along the AM. 
<br><br>
(Joint with [Robert Bridges](https://sites.google.com/site/robertbridgeshomepage/), [Christopher Felder](https://www.math.wustl.edu/~cfelder/), and [Miki Verma](https://scholar.google.com/citations?user=1jUa6nwAAAAJ&hl=en).) <br>
{: .notice--info}

</details>


Rigidity Results for Immersed Submanifolds
-----
<img src="/images/Willmore-Hopf-5-1.jpeg" style="max-height: 225px; max-width: 325px; margin-right: 16px" align=left>  Many practical problems involving shape deformation can be understood in the context of "allowable" mappings between Riemannan spaces.  When these mappings are constrained by natural geometric conditions on e.g. curvature, their existence is governed by overdetermined PDEs which are difficult to approach using classical analytic techniques.  These projects establish characterization results in my preferred style for certain classes of mappings which I have encountered in applications.  
<br>
(Hopf torus courtesy of [Álvaro Pámpano](https://www.math.ttu.edu/~apampano/index.html).)

<details markdown="1"><summary><b>Projects</b></summary>
{: .notice}

### Planar Immersions with Prescribed Curl and Jacobian Determinant are Unique  [Preprint](https://arxiv.org/abs/2107.13707#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/phiJphi.png" style="max-height: 225px; max-width: 250px; margin-right: 16px" align=left>  **Abstract:** We prove that immersions of planar domains are uniquely specified by their Jacobian determinant, curl function, and boundary values. This settles the two-dimensional version of an outstanding conjecture related to a particular grid generation method in computer graphics. <br><br><br>
{: .notice--info}

### Parallel Codazzi Tensors with Submanifold Applications  [Preprint](https://arxiv.org/abs/2004.03103#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/equations.png" style="max-height: 225px; max-width: 250px; margin-right: 16px" align=left>  **Abstract:** A decomposition theorem is established for a class of closed Riemannian submanifolds immersed in a space form of constant sectional curvature. In particular, it is shown that if $$M$$ has nonnegative sectional curvature and admits a Codazzi tensor with “parallel mean curvature”, then $$M$$ is locally isometric to a direct product of irreducible factors determined by the spectrum of that tensor. This decomposition is global when $$M$$ is simply connected, and generalizes what is known for immersed submanifolds with parallel mean curvature vector.
{: .notice--info}

</details>


Quaternionic Surface Theory for Graphics and Meshing
-----
<img src="/images/torus_dots.png" style="max-height: 275px; max-width: 325px; margin-right: 16px" align=left>  Just as classical complex analysis facilitates study of the conformal geometry of planar domains, the rich algebraic structure of the quaternions enables a useful framework for describing the conformal geometry of surfaces in Euclidean space.  These projects develop and use quaternionic surface theory for graphics and meshing applications.

<details markdown="1"><summary><b>Projects</b></summary>
{: .notice}

### Quasiconformal Mappings with Surface Domains [Preprint](/files/preprints/QC_paper.pdf){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/torus_checkerboard.png" style="max-height: 225px; max-width: 225px; margin-right: 16px" align=left> **Abstract:** Quasiconformal mappings from surfaces immersed in Euclidean space are discussed for the purposes of computing dilatation-optimal surface meshes with prescribed connectivity and Dirichlet boundary data.  In particular, a quaternionic formulation of quasiconformality is proposed which leads to a linear algorithm for computing least-squares quasiconformal maps from surfaces given as extrinsic mesh data.  This facilitates an iterative procedure which computes optimal quasiconformal mappings with optional constraints on surface area and extrinsic geometry.  Based on the established Quasiconformal Iteration method, the proposed algorithm produces high quality surface mappings which correctly capture boundary information while eliminating undesirable folds which appear during least-squares conformal mapping procedures.
<br><br>
(Joint with [Eugenio Aulisa](http://www.math.ttu.edu/~eaulisa/).)
{: .notice--info}

### Modeling the p-Willmore Flow of Surfaces  [Here](https://dl.acm.org/doi/10.1145/3369387?cid=99659571076){: .btn .btn--info .btn--small}{: .align-right} [Read More](/surfaceFlow/){: .btn .btn--info .btn--small}{: .align-right} 
<img src="/images/cows.pdf" style="max-height: 225px; max-width: 225px; margin-right: 16px" align=left>  **Abstract:** The unsigned p-Willmore functional generalizes important geometric functionals which measure the area and Willmore energy of immersed surfaces.  Presently, techniques of Dziuk are adapted to compute the first variation of this functional as a weak-form system of equations, which are subsequently used to develop a model for the p-Willmore flow of closed surfaces in $$\mathbb{R}^3$$.  This model is amenable to constraints on surface area and enclosed volume, and is shown to decrease the p-Willmore energy monotonically.  In addition, a penalty-based regularization procedure is formulated to prevent artificial mesh degeneration along the flow; inspired by a conformality condition derived by Kamberov et al., this procedure encourages angle-preservation in a closed and oriented surface immersion as it evolves.  Following this, a finite-element discretization of both procedures is discussed, an algorithm for running the flow is given, and an application to mesh editing is presented.
<br><br>
(Joint with [Eugenio Aulisa](http://www.math.ttu.edu/~eaulisa/).)
{: .notice--info}

</details>


Curvature Functionals and p-Willmore Energy
------
<img src="/images/dogs.pdf" style="max-height: 225px; max-width: 325px; margin-right: 16px" align=left> Functionals involving surface curvature are widely used as models for elastic phenomena, and their critical points are frequently representative of physically relevant structures such as biomembranes or material interfaces.  These projects involve a variational characterization of curvature functionals and their critical surfaces, both from a general perspective and in multiple specific cases of interest.

<details markdown="1"><summary><b>Projects</b></summary>
{: .notice}

### Instability of Closed $$p$$-Elastic Curves in $$\mathcal{S}^2$$  [Preprint](https://arxiv.org/abs/2110.14778#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/spherical_curve_3-5.jpg" style="max-height: 180px; max-width: 180px; margin-right: 16px" align=left> **Abstract:** For $$p \in \mathbb{R}$$, we show that non-circular closed p-elastic curves in $$\mathbb{S}^2$$ exist only when $$p=2$$, in which case they are classical elastic curves, or when $$p\in(0,1)$$. In the latter case, we prove that for every pair of relatively prime natural numbers $$n$$ and $$m$$ satisfying $$m<2n<2\sqrt{m}$$, there exists a closed spherical $$p$$-elastic curve with non-constant curvature which winds around a pole $$n$$ times and closes up in m periods of its curvature. Further, we show that all closed spherical $$p$$-elastic curves for $$p\in(0,1)$$ are unstable as critical points of the p-elastic energy.
<br><br>
(Joint with [Magdalena Toda](http://www.math.ttu.edu/~mtoda/) and [Álvaro Pámpano](https://www.math.ttu.edu/~apampano/index.html).)
{: .notice--info}

### On p-Willmore Disks with Boundary Energies  [Preprint](https://arxiv.org/abs/2110.14778#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/bubble.jpg" style="max-height: 180px; max-width: 180px; margin-right: 16px" align=left> **Abstract:** We consider an energy functional on surface immersions which includes contributions from both boundary and interior. Inspired by physical examples, the boundary is modeled as the center line of a generalized Kirchhoff elastic rod, while the interior term is arbitrarily dependent on the mean curvature and linearly dependent on the Gaussian curvature. We study equilibrium configurations for this energy in general among topological disks, as well as specifically for the class of examples known as p-Willmore energies.
<br><br>
(Joint with [Magdalena Toda](http://www.math.ttu.edu/~mtoda/) and [Álvaro Pámpano](https://www.math.ttu.edu/~apampano/index.html).)
{: .notice--info}

### Regarding the Euler-Plateau Problem with Elastic Modulus  [Preprint](https://arxiv.org/abs/2010.00149#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/elastic_modulus.png" style="max-height: 180px; max-width: 180px; margin-right: 16px; margin-bottom: 10px" align=left>  **Abstract:** We study equilibrium configurations for the Euler-Plateau energy with elastic modulus, which couples an energy functional of Euler-Plateau type with a total curvature term often present in models for the free energy of biomembranes. It is shown that the potential minimizers of this energy are highly dependent on the choice of physical rigidity parameters, and that the area of critical surfaces can be computed entirely from their boundary data. When the elastic modulus does not vanish, it is shown that axially symmetric critical immersions and critical immersions of disk type are necessarily planar domains bounded by area-constrained elasticae. The cases of topological genus zero with multiple boundary components and unrestricted genus with control on the geodesic torsion are also discussed, and sufficient conditions are given which establish the same conclusion in these cases.
<br><br>
(Joint with [Magdalena Toda](http://www.math.ttu.edu/~mtoda/) and [Álvaro Pámpano](https://www.math.ttu.edu/~apampano/index.html).)
{: .notice--info}

### Stationary Surfaces with Boundaries  [Preprint](https://arxiv.org/abs/1912.07103#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/sswb_visual2.pdf" style="max-height: 225px; max-width: 225px; margin-right: 16px; margin-bottom: 10px" align=left>  **Abstract:** This article investigates stationary surfaces with boundaries, which arise as the critical points of functionals dependent on curvature. Precisely, a generalized "bending energy" functional $$\mathcal{W}$$ is considered which involves a Lagrangian that is symmetric in the principal curvatures. The first variation of $$\mathcal{W}$$ is computed, and a stress tensor is extracted whose divergence quantifies deviation from $$\mathcal{W}$$-criticality. Boundary-value problems are then examined, and a characterization of free-boundary $$\mathcal{W}$$-surfaces with rotational symmetry is given for scaling-invariant $$\mathcal{W}$$-functionals. In case the functional is not scaling-invariant, certain boundary-to-interior consequences are discussed. Finally, some applications to the conformal Willmore energy and the p-Willmore energy of surfaces are presented.
<br><br>
(Joint with [Magdalena Toda](http://www.math.ttu.edu/~mtoda/) and [Hung Tran](https://www.math.uci.edu/~hungtt1/).)
{: .notice--info}

### On the Variation of Curvature Functionals in a Space Form with Applications to a Generalized Willmore Energy  [Preprint](https://arxiv.org/abs/1905.01759#){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/variationfig.pdf" style="max-height: 200px; max-width: 200px; margin-right: 16px" align=left>  **Abstract:** Functionals involving surface curvature are important across a range of scientific disciplines, and their extrema are representative of physically meaningful objects such as atomic lattices and biomembranes. Inspired in particular by the relationship of the Willmore energy to lipid bilayers, we consider a general functional depending on a surface and a symmetric combination of its principal curvatures, provided the surface is immersed in a 3-D space form. We compute the first and second variations of this functional, leading to expressions given entirely in terms of the surface fundamental forms. We then apply the stability criteria afforded by our calculations to a generalization of the Willmore functional, proving a result regarding the stability of spheres.
<br><br>
(Joint with [Magdalena Toda](http://www.math.ttu.edu/~mtoda/) and [Hung Tran](https://www.math.uci.edu/~hungtt1/).)
{: .notice--info}

### Curvature Functionals and p-Willmore Energy  [Here](https://ttu-ir.tdl.org/handle/2346/85351#){: .btn .btn--info .btn--small}{: .align-right} [Read More](/cf/){: .btn .btn--info .btn--small}{: .align-right}
<img src="/images/virus_end.png" style="max-height: 225px; max-width: 225px; margin-right: 16px" align=left>  My PhD thesis, which investigates many aspects of general curvature functionals in the abstract, and applies some of them to the particular case of the p-Willmore energy. 
<br><br>
**Abstract:** Functionals involving surface curvature are frequently
encountered when modeling the behavior of important biological structures such
as lipid membranes. To better understand these objects, we consider a general
functional on surface immersions which is dependent on the surface mean and
Gauss curvatures. Variations of this functional are presented, and stability
criteria are given in terms of basic geometric invariants coming from the surface
fundamental forms. These results are then applied to a particular curvature
functional which generalizes the Willmore energy, and a nonexistence result is
presented. A constrained minimization problem is then considered, leading to
a stability result involving round spheres. Further study is done on a generalization of the Willmore flow of surfaces in $\mathbb{R}^3$ -- a geometric tool known for its aesthetic beauty. In particular, two finite-element formulations of this problem are presented: one which is applicable to surfaces presented graphically, and the other which models closed immersed (possibly self-intersecting) surfaces and is amenable to constraints on surface area and enclosed volume. It is shown in both cases that the energy decreases along the flow. Moreover, stability and consistency results are obtained in the closed surface model, and examples of the implementation are discussed. Inspired by conformal geometry, a post-processing procedure is also presented, which ensures that a given surface mesh remains nearly conformal along the Willmore flow despite its initial regularity. This abolishes the mesh degeneration that usually accompanies position-based surface flows, and leads to a robust model that can accommodate variable time steps as well as surface genera.
{: .notice--info}

</details>
