---
permalink: /
title: "About Me"
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---
![image-center](/images/frontpage.jpg){: .align-center}

I am a mathematician interested in the pure and applied questions that arise during the study of computer graphics and data science.  A differential geometer by training, I received my PhD from Texas Tech University under the guidance of [Magdalena Toda](http://www.math.ttu.edu/~mtoda/), with co-advisors [Eugenio Aulisa](http://www.math.ttu.edu/~eaulisa/) and [Hung Tran](https://www.math.uci.edu/~hungtt1/).  

<!-- ![Alt Text](/files/gifs/knotFandB.gif) -->

During my PhD, I applied techniques from Riemannian geometry, variational calculus, and differential topology to study functionals involving surface curvature, with the ultimate goal of understanding their extrema. Moreover, I was (and still am) interested in understanding the possible immersions of a given topological space inside another, including what configurations are "preferred" (usually energy-minimizing) in this case.

Lately, I'm involved in developing artificial neural network based methods for dimension reduction, function approximation, and the reduced-order modeling of PDEs.  In addition, I enjoy working on the computer visualization of geometric objects -- as can be seen in the various simulation videos found on the "Gallery" page.

Broad research keywords which tend to interest me include: computational and discrete geometry, machine learning theory, deep learning for PDEs, surface immersions, Willmore energy, conservation laws, and integrability problems.  A more detailed description of my interests can be found in my [academic research statement](/files/Research_Statement.pdf) (current as of 9/21).

Below are some selected snapshots of my work. Each has its own page for further reading.

[//]: # (![image-center](/images/frontpage.jpg){: .align-center} )


Comparing Neural Architectures for Reduced-Order Modeling
------
![image-left](/images/GCNN_recon2.png){: .align-left}{: width="300" }  Advances in artificial neural network technology have let to recent breakthroughs in the reduced-order modeling of parameterized PDEs. Crucial to this is the idea of the autoencoder, a network archetype which learns a nonlinear projection-expansion that enables low-dimensional methods of solution.  This project compares popular autoencoder architectures against a novel design based on graph convolution.  (Joint with [Max Gunzburger](https://people.sc.fsu.edu/~mgunzburger/), [Lili Ju](https://people.math.sc.edu/ju/), and [Zhu Wang](https://people.math.sc.edu/wangzhu/).) [Read More.](/ROMautoencoder/){: .btn .btn--inverse}


Quasiconformal Mappings for Surface Mesh Optimization
------
![image-left](/images/QCfront.png){: .align-left}{: width="250" } Computational quasiconformal mappings are flexible tools for everything from surface remeshing to object deformation.  This project develops a single-stage genus-agnostic algorithm for computing Teichm&uuml;ller quasiconformal mappings from surfaces represented as manifold meshes in $$ \mathbb{R}^3 $$.  (Joint with [Eugenio Aulisa](http://www.math.ttu.edu/~eaulisa/).) [Read More.](/quasiconformal/){: .btn .btn--inverse}


Learning the Structure of Level Sets from Sparse Data
------
![image-left](/images/ex4_mine.png){: .align-left}{: width="200" } It is often necessary to make predictions in the presence of limited or incomplete data, which can lead to formidable model overfitting. The Nonlinear Level-set Learning (NLL) method of [Guannan Zhang](https://sites.google.com/view/guannan-zhang/home) et al. aims to combat this issue by building an invertible neural network mapping which concentrates the change in the function in some small number of active directions.  This project improves the NLL algorithm by reposing it as the minimization of an almost-Dirichlet energy functional, leading to a mapping which is faster to compute and always reduces the number of active inputs to one.  (Joint with [Max Gunzburger](https://people.sc.fsu.edu/~mgunzburger/), [Lili Ju](https://people.math.sc.edu/ju/), [Yuankai Teng](https://slooowtyk.github.io/), and [Zhu Wang](https://people.math.sc.edu/wangzhu/).) [Read More.](/nll/){: .btn .btn--inverse}


Modeling the p-Willmore Flow of Surfaces
------
![image-left](/images/cows.png){: .align-left}{: width="250" } Geometric flows are beautiful and powerful tools for prescribing a change in the geometry of a surface.
This project is a computational study of the p-Willmore flow, with the aim to develop a finite-element model that is amenable to geometric constraints on surface area and enclosed volume.  (Joint with [Eugenio Aulisa](http://www.math.ttu.edu/~eaulisa/).) [Read More.](/surfaceFlow/){: .btn .btn--inverse}


Active Manifolds: Geometric Data Analysis for Dimension Reduction
------
![image-left](/images/AMpic.png){: .align-left}{: width="225" }  Scientists and engineers are frequently presented with mathematical models that are difficult to analyze due to their reliance on a large number of parameters. This project is inspired by the Active Subspaces idea of [Paul Constantine](https://scholar.google.com/citations?user=7x-Q4Y8AAAAJ&hl=en), and provides an algorithm which reduces the dimension of an unknown function to 1 regardless of the size of the original input space. (Joint with [Robert Bridges](https://sites.google.com/site/robertbridgeshomepage/).) [Read More.](/am/){: .btn .btn--inverse}


Curvature Functionals and p-Willmore Energy
------
![image-left](/images/virus_end.png){: .align-left}{: width="180" } Functional involving surface curvature are important across a wide variety of disciplines, and their minima are frequently representative of physically relevant structures, such as biomembranes or interfaces between materials.  This project involves a variational characterization of such functionals, with particular interest given to a generalization of the Willmore functional. (Joint with [Magdalena Toda](http://www.math.ttu.edu/~mtoda/), [Hung Tran](https://www.math.uci.edu/~hungtt1/), and [Álvaro Pámpano](https://orcid.org/0000-0003-2239-2247).)  [Read More.](/cf/){: .btn .btn--inverse}

Why is this not working anymore??????
