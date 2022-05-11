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

![image-left](/images/me_over_gorge.jpg){: width="280" } ![image-left](/images/me_w_sunglasses.jpg){: width="160" } ![image-left](/images/me.png){: width="320" }

<!-- ![image-left](/images/me.png){: width="300" } ![image-left](/images/me_w_sunglasses.jpg){: width="200" } ![image-right](/files/gifs/knotFandB.gif){: width="200" } -->

I am a mathematician interested in basic and applied research questions that arise in the contexts of data science, nonlinear partial differential equations (PDEs), and scientific machine learning.
<!-- {: .notice--success} -->

Lately, my focus is primarily on developing structure-informed numerical methods for scientific applications.  Doing this generally involves identifying or reasoning about some abstract mathematical structure which is important for a particular phenomenon, formulating a smart discretization (based on e.g. a finite element or artificial neural network backbone) which takes this structure into account, and writing mathematical software in Python or C++ which implements a proposed approach.  Over time, I've found that my preferred flavor of research problem leaves ample opportunity for geometric ideas, satisfying visuals, and punchy algebraic arguments which are characteristic of my personal style.

<details markdown="1"><summary><b>More about me</b></summary>
{: .notice--info}

A differential geometer by training, I received my PhD from Texas Tech University under the guidance of <a href="http://www.math.ttu.edu/~mtoda/">Magdalena Toda</a>, with co-advisors <a href="http://www.math.ttu.edu/~eaulisa/">Eugenio Aulisa</a> and <a href="https://www.math.uci.edu/~hungtt1/">Hung Tran</a>. At this time, I applied techniques from Riemannian geometry, variational calculus, and differential topology to study functionals involving surface curvature, with the ultimate goal of understanding their extrema. Moreover, I was (and still am) interested in understanding the possible immersions of a given topological space inside another, including what configurations are "preferred" (usually energy-minimizing) in this case.  I also spent quite a bit of time thinking about the computational modeling of geometric objects, sparking a standing interest in computer graphics which can be seen in the various simulation videos found on the <a href="/gallery/">Gallery</a> page.

Catalyzed by an NSF internship at Oak Ridge National Lab (featured [here!](https://orise.orau.gov/nsf-msgi/profiles/gruber.html)) toward the end of graduate school where I worked with <a href="https://sites.google.com/site/robertbridgeshomepage/">Robert Bridges</a>, I became involved post-PhD in scientific algorithm development for dimension reduction, function approximation, and the reduced-order modeling of PDEs.  This led to a postdoctoral appointment with <a href="https://people.sc.fsu.edu/~mgunzburger/">Max Gunzburger</a> at FSU working on data-driven strategies for predictive tasks related to ocean modeling.  At the same time as my application-driven interests were shifting, my purer "side project" work also moved in the direction of rigidity results for geometric objects constrained by curvature conditions.  Now, I maintain active interests in several areas of mathematics, computer science, and engineering.

<!-- Lately, my focus is primarily on developing structure-informed numerical methods for scientific applications.  Doing this generally involves identifying/reasoning about some abstract mathematical structure which is important for a particular phenomenon, formulating a smart discretization (based on e.g. a finite element or artificial neural network backbone) which takes this structure into account, and writing mathematical software in Python or C++ which implements the proposed discretization.  Over time, I've found that my preferred "flavor" of research problem creates ample opportunity for algebraic reasoning, flashy visuals, and short "punchy" arguments which are characteristic of my personal style.

<br><br> -->

Broad research keywords which tend to interest me include: scientific machine learning, computational and discrete geometry, conservation laws, reduced-order modeling, manifold learning, harmonic maps, surface immersions, and integrability problems.  A more detailed description of my interests can be found in my <a href="/files/Research_Statement.pdf">academic research statement</a> (current as of 9/21).

</details>


![image-right](/files/gifs/knotFandB.gif){: .align-right}{: width="200" } <br><br> Below are some coarse categories containing (some of) my work. Some have their own page for further reading.  (This part of the website is a work-in-progress.) <br><br>


Structure-Informed Function Approximation and Model Reduction
-----
![image-left](/images/GCNN_recon2.png){: .align-left}{: width="300" } Due to their high computational cost, scientific studies based on large-scale simulation frequently operate at a data deficit which creates problems inverse to the issues with "big data".  Particularly, there is a need for efficient function approximation and model reduction strategies which can serve as cheap and reliable surrogates for the high-fidelity models used in practical applications.  These projects develop such technology using invariances and other structural considerations as a starting point, allowing for informed surrogates with beneficial behavior.

<details markdown="1"><summary><b>Projects</b></summary>
{: .notice}

### Energetically Consistent Model Reduction for Metriplectic Systems  [Preprint](https://arxiv.org/abs/2204.08049#){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/gas_containers_FOMs.png){: .align-left}{: width="275" } **Abstract:** The metriplectic formalism is useful for describing complete dynamical systems which conserve energy and produce entropy.  This creates challenges for model reduction, as the elimination of high-frequency information will generally not preserve the metriplectic structure which governs long-term stability of the system.  Based on proper orthogonal decomposition, a provably convergent metriplectic reduced-order model is formulated which is guaranteed to maintain the algebraic structure necessary for energy conservation and entropy formation.  Numerical results on benchmark problems show that the proposed method is remarkably stable, leading to improved accuracy over long time scales at a moderate increase in cost over naive methods.  
<br>
(Joint with [Max Gunzburger](https://people.sc.fsu.edu/~mgunzburger/), [Lili Ju](https://people.math.sc.edu/ju/), and [Zhu Wang](https://people.math.sc.edu/wangzhu/).)
{: .notice--info}

### Comparing Neural Architectures for Reduced-Order Modeling  [Read More.](/autoencoder-rom/){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/gcnnRom.pdf){: .align-left}{: width="300" }  Advances in artificial neural network technology have let to recent breakthroughs in the reduced-order modeling of parameterized PDEs. Crucial to this is the idea of the autoencoder, a network archetype which learns a nonlinear projection-expansion that enables low-dimensional methods of solution.  This project compares popular autoencoder architectures against a novel design based on graph convolution.  
<br>
(Joint with [Max Gunzburger](https://people.sc.fsu.edu/~mgunzburger/), [Lili Ju](https://people.math.sc.edu/ju/), and [Zhu Wang](https://people.math.sc.edu/wangzhu/).)<br>
{: .notice--info}

### Learning the Structure of Level Sets from Sparse Data  [Read More.](/nll/){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/levset_cartoon.pdf){: .align-left}{: width="275" } It is often necessary to make predictions in the presence of limited or incomplete data, which can lead to formidable model overfitting. The Nonlinear Level-set Learning (NLL) method of [Guannan Zhang](https://sites.google.com/view/guannan-zhang/home) et al. aims to combat this issue by building an invertible neural network mapping which concentrates the change in the function in some small number of active directions.  This project improves the NLL algorithm by reposing it as the minimization of an almost-Dirichlet energy functional, leading to a mapping which is faster to compute and always reduces the number of active inputs to one.  
<br>
(Joint with [Max Gunzburger](https://people.sc.fsu.edu/~mgunzburger/), [Lili Ju](https://people.math.sc.edu/ju/), [Yuankai Teng](https://slooowtyk.github.io/), and [Zhu Wang](https://people.math.sc.edu/wangzhu/).)
{: .notice--info}

### Pseudo-Reversible Neural Networks  [Preprint](https://arxiv.org/abs/2112.01438#){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/prnn.png){: .align-left}{: width="275" } **Abstract:** Due to the curse of dimensionality and limitations on training data, approximating high-dimensional functions is a very challenging task even for powerful deep neural networks. Inspired by the Nonlinear Level set Learning (NLL) method that uses the reversible residual network (RevNet), in this paper we propose a new method for function approximation called Dimension Reduction via Learning Level Sets (DRiLLS). Our method contains two major components: one is the pseudo-reversible neural network (PRNN) module that effectively transforms high-dimensional input variables to low-dimensional active variables, and the other is the synthesized regression module for approximating function values based on the transformed data in the low-dimensional space.  Extensive experimental results demonstrate that DRiLLS outperforms both the NLL and Active Subspace methods, especially when the target function possesses critical points in the interior of its input domain.
<br><br>
(Joint with [Lili Ju](https://people.math.sc.edu/ju/), [Yuankai Teng](https://slooowtyk.github.io/), [Zhu Wang](https://people.math.sc.edu/wangzhu/), and [Guannan Zhang](https://sites.google.com/view/guannan-zhang/home).)
{: .notice--info}

### Active Manifolds: Geometric Data Analysis for Dimension Reduction  [Read More.](/am/){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/AMpic.png){: .align-left}{: width="215" }  Scientists and engineers are frequently presented with mathematical models that are difficult to analyze due to their reliance on a large number of parameters. This project is inspired by the Active Subspaces idea of [Paul Constantine](https://scholar.google.com/citations?user=7x-Q4Y8AAAAJ&hl=en), and provides an algorithm which reduces the dimension of an unknown function to one regardless of the size of the original input space.
<br><br>
(Joint with [Robert Bridges](https://sites.google.com/site/robertbridgeshomepage/), [Christopher Felder](https://www.math.wustl.edu/~cfelder/), and [Miki Verma](https://scholar.google.com/citations?user=1jUa6nwAAAAJ&hl=en).) <br><br><br><br>
{: .notice--info}

</details>


Rigidity Results for Immersed Submanifolds
-----
![image-left](/images/Willmore-Hopf-5-1.jpeg){: .align-left}{: width="210" } Many practical problems involving shape deformation can be understood in the context of "allowable" mappings between Riemannan spaces.  When these mappings are constrained by natural geometric conditions on e.g. curvature, their existence is governed by overdetermined PDEs which are difficult to approach using classical analytic techniques.  These projects establish characterization results in my preferred style for certain classes of mappings which I have encountered in applications.  
<br>
(Hopf torus courtesy of [Álvaro Pámpano](https://www.math.ttu.edu/~apampano/index.html).)

<details markdown="1"><summary><b>Projects</b></summary>
{: .notice}

### Planar Immersions with Prescribed Curl and Jacobian Determinant are Unique  [Preprint](https://arxiv.org/abs/2107.13707#){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/crossfld.png){: .align-left}{: width="210" } **Abstract:** We prove that immersions of planar domains are uniquely specified by their Jacobian determinant, curl function, and boundary values. This settles the two-dimensional version of an outstanding conjecture related to a particular grid generation method in computer graphics. <br><br><br><br><br><br><br>
{: .notice--info}

### Parallel Codazzi Tensors with Submanifold Applications  [Preprint](https://arxiv.org/abs/2004.03103#){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/equations.png){: .align-left}{: width="300" } **Abstract:** A decomposition theorem is established for a class of closed Riemannian submanifolds immersed in a space form of constant sectional curvature. In particular, it is shown that if $$M$$ has nonnegative sectional curvature and admits a Codazzi tensor with “parallel mean curvature”, then $$M$$ is locally isometric to a direct product of irreducible factors determined by the spectrum of that tensor. This decomposition is global when $$M$$ is simply connected, and generalizes what is known for immersed submanifolds with parallel mean curvature vector.
{: .notice--info}

</details>


Quaternionic Surface Theory for Graphics and Meshing
-----
![image-left](/images/confcartoon.pdf){: .align-left}{: width="350" } Just as classical complex analysis facilitates study of the conformal geometry of planar domains, the rich algebraic structure of the quaternions enables a useful framework for describing the conformal geometry of surfaces in Euclidean space.  These projects develop and use quaternionic surface theory for graphics and meshing applications.

<details markdown="1"><summary><b>Projects</b></summary>
{: .notice}

### Quasiconformal Mappings for Surface Mesh Optimization  [Read More.](/quasiconformal/){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/QCfront.png){: .align-left}{: width="275" } Computational quasiconformal mappings are flexible tools for everything from surface remeshing to object deformation.  This project develops a single-stage genus-agnostic algorithm for computing Teichm&uuml;ller quasiconformal mappings from surfaces represented as manifold meshes in $$ \mathbb{R}^3 $$.
<br><br>
(Joint with [Eugenio Aulisa](http://www.math.ttu.edu/~eaulisa/).) <br><br>
{: .notice--info}

### Modeling the p-Willmore Flow of Surfaces  [Read More.](/surfaceFlow/){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/cows.pdf){: .align-left}{: width="250" } Geometric flows are beautiful and powerful tools for prescribing a change in the geometry of a surface.  This project is a computational study of the p-Willmore flow, with the aim to develop a finite-element model that is amenable to geometric constraints on surface area and enclosed volume.
<br><br>
(Joint with [Eugenio Aulisa](http://www.math.ttu.edu/~eaulisa/).) <br><br><br><br><br>
{: .notice--info}

</details>


Curvature Functionals and p-Willmore Energy
------
![image-left](/images/dogs.pdf){: .align-left}{: width="300" } Functionals involving surface curvature are widely used as models for elastic phenomena, and their critical points are frequently representative of physically relevant structures such as biomembranes or material interfaces.  These projects involve a variational characterization of curvature functionals and their critical surfaces, both from a general perspective and in multiple specific cases of interest.

<details markdown="1"><summary><b>Projects</b></summary>
{: .notice}

### On p-Willmore Disks with Boundary Energies  [Preprint](https://arxiv.org/abs/2110.14778#){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/bubble.jpg){: .align-left}{: width="200" } **Abstract:** We consider an energy functional on surface immersions which includes contributions from both boundary and interior. Inspired by physical examples, the boundary is modeled as the center line of a generalized Kirchhoff elastic rod, while the interior term is arbitrarily dependent on the mean curvature and linearly dependent on the Gaussian curvature. We study equilibrium configurations for this energy in general among topological disks, as well as specifically for the class of examples known as p-Willmore energies.
<br><br>
(Joint with [Magdalena Toda](http://www.math.ttu.edu/~mtoda/) and [Álvaro Pámpano](https://www.math.ttu.edu/~apampano/index.html).)
{: .notice--info}

### Regarding the Euler-Plateau Problem with Elastic Modulus  [Preprint](https://arxiv.org/abs/2010.00149#){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/elastic_modulus.png){: .align-left}{: width="200" } **Abstract:** We study equilibrium configurations for the Euler-Plateau energy with elastic modulus, which couples an energy functional of Euler-Plateau type with a total curvature term often present in models for the free energy of biomembranes. It is shown that the potential minimizers of this energy are highly dependent on the choice of physical rigidity parameters, and that the area of critical surfaces can be computed entirely from their boundary data. When the elastic modulus does not vanish, it is shown that axially symmetric critical immersions and critical immersions of disk type are necessarily planar domains bounded by area-constrained elasticae. The cases of topological genus zero with multiple boundary components and unrestricted genus with control on the geodesic torsion are also discussed, and sufficient conditions are given which establish the same conclusion in these cases.
<br><br>
(Joint with [Magdalena Toda](http://www.math.ttu.edu/~mtoda/) and [Álvaro Pámpano](https://www.math.ttu.edu/~apampano/index.html).)
{: .notice--info}

### Stationary Surfaces with Boundaries  [Preprint](https://arxiv.org/abs/1912.07103#){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/sswb_visual.pdf){: .align-left}{: width="250" } **Abstract:** This article investigates stationary surfaces with boundaries, which arise as the critical points of functionals dependent on curvature. Precisely, a generalized "bending energy" functional $$\mathcal{W}$$ is considered which involves a Lagrangian that is symmetric in the principal curvatures. The first variation of $$\mathcal{W}$$ is computed, and a stress tensor is extracted whose divergence quantifies deviation from $$\mathcal{W}$$-criticality. Boundary-value problems are then examined, and a characterization of free-boundary $$\mathcal{W}$$-surfaces with rotational symmetry is given for scaling-invariant $$\mathcal{W}$$-functionals. In case the functional is not scaling-invariant, certain boundary-to-interior consequences are discussed. Finally, some applications to the conformal Willmore energy and the p-Willmore energy of surfaces are presented.
<br><br>
(Joint with [Magdalena Toda](http://www.math.ttu.edu/~mtoda/) and [Hung Tran](https://www.math.uci.edu/~hungtt1/).)
{: .notice--info}

### On the Variation of Curvature Functionals in a Space Form with Applications to a Generalized Willmore Energy  [Preprint](https://arxiv.org/abs/1905.01759#){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/variationfig.pdf){: .align-left}{: width="220" } **Abstract:** Functionals involving surface curvature are important across a range of scientific disciplines, and their extrema are representative of physically meaningful objects such as atomic lattices and biomembranes. Inspired in particular by the relationship of the Willmore energy to lipid bilayers, we consider a general functional depending on a surface and a symmetric combination of its principal curvatures, provided the surface is immersed in a 3-D space form. We compute the first and second variations of this functional, leading to expressions given entirely in terms of the surface fundamental forms. We then apply the stability criteria afforded by our calculations to a generalization of the Willmore functional, proving a result regarding the stability of spheres.
<br><br>
(Joint with [Magdalena Toda](http://www.math.ttu.edu/~mtoda/) and [Hung Tran](https://www.math.uci.edu/~hungtt1/).)
{: .notice--info}

### Curvature Functionals and p-Willmore Energy  [Read More.](/cf/){: .btn .btn--info .btn--small}{: .align-right}
![image-left](/images/virus_end.png){: .align-left}{: width="200" } My PhD thesis, which investigates many aspects of general curvature functionals in the abstract, and applies some of them to the particular case of the p-Willmore energy. <br><br><br><br><br><br><br><br>
{: .notice--info}

</details>
