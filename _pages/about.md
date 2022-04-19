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

![image-left](/images/me.png){: width="400" } ![image-right](/files/gifs/knotFandB.gif){: width="300" }

I am a mathematician interested in the pure and applied questions that arise in the context of data science, nonlinear partial differential equations (PDEs), and scientific machine learning.  A differential geometer by training, I received my PhD from Texas Tech University under the guidance of [Magdalena Toda](http://www.math.ttu.edu/~mtoda/), with co-advisors [Eugenio Aulisa](http://www.math.ttu.edu/~eaulisa/) and [Hung Tran](https://www.math.uci.edu/~hungtt1/).  


<details><summary><b>More about me</b></summary>

<br>
During my PhD, I applied techniques from Riemannian geometry, variational calculus, and differential topology to study functionals involving surface curvature, with the ultimate goal of understanding their extrema. Moreover, I was (and still am) interested in understanding the possible immersions of a given topological space inside another, including what configurations are "preferred" (usually energy-minimizing) in this case.  I also spent quite a bit of time thinking about the computational modeling of geometric objects, sparking a standing interest in computer graphics which can be seen in the various simulation videos found on the <a href="/gallery/">Gallery</a> page.

<br><br>

Catalyzed by an internship at Oak Ridge National Lab toward the end of graduate school, I became involved post-PhD in scientific algorithm development for dimension reduction, function approximation, and the reduced-order modeling of PDEs.  At the same time as my application-driven interests were shifting, my purer "side project" work also moved in the direction of rigidity results for geometric objects constrained by curvature conditions.

<br><br>

Lately, my focus is primarily on developing structure-informed numerical methods for scientific applications.  Doing this generally involves identifying/reasoning about some abstract mathematical structure which is important for a particular phenomenon, formulating a smart discretization (based on e.g. a finite element or artificial neural network backbone) which takes this structure into account, and writing mathematical software in Python or C++ which implements the proposed discretization.  Over time, I've found that my preferred "flavor" of research problem creates ample opportunity for algebraic reasoning, flashy visuals, and short "punchy" arguments which are characteristic of my personal style.

<br><br>

Broad research keywords which tend to interest me include: scientific machine learning, computational and discrete geometry, conservation laws, reduced-order modeling, manifold learning, harmonic maps, surface immersions, and integrability problems.  A more detailed description of my interests can be found in my <a href="/files/Research_Statement.pdf">academic research statement</a> (current as of 9/21).

</details>

<br>
Below are some coarse categories containing (some of) my work. Each has its own page for further reading.  Finishing and updating this part of the website is on my to-do list.


Comparing Neural Architectures for Reduced-Order Modeling
------
![image-left](/images/GCNN_recon2.png){: .align-left}{: width="300" }  Advances in artificial neural network technology have let to recent breakthroughs in the reduced-order modeling of parameterized PDEs. Crucial to this is the idea of the autoencoder, a network archetype which learns a nonlinear projection-expansion that enables low-dimensional methods of solution.  This project compares popular autoencoder architectures against a novel design based on graph convolution.
[Read More.](/autoencoder-rom/){: .btn .btn--info .btn--small}{: .align-right}

(Joint with [Max Gunzburger](https://people.sc.fsu.edu/~mgunzburger/), [Lili Ju](https://people.math.sc.edu/ju/), and [Zhu Wang](https://people.math.sc.edu/wangzhu/).)


Quasiconformal Mappings for Surface Mesh Optimization
------
![image-left](/images/QCfront.png){: .align-left}{: width="275" } Computational quasiconformal mappings are flexible tools for everything from surface remeshing to object deformation.  This project develops a single-stage genus-agnostic algorithm for computing Teichm&uuml;ller quasiconformal mappings from surfaces represented as manifold meshes in $$ \mathbb{R}^3 $$.  [Read More.](/quasiconformal/){: .btn .btn--info .btn--small}{: .align-right}

(Joint with [Eugenio Aulisa](http://www.math.ttu.edu/~eaulisa/).)


Learning the Structure of Level Sets from Sparse Data
------
![image-left](/images/ex4_mine.png){: .align-left}{: width="225" } It is often necessary to make predictions in the presence of limited or incomplete data, which can lead to formidable model overfitting. The Nonlinear Level-set Learning (NLL) method of [Guannan Zhang](https://sites.google.com/view/guannan-zhang/home) et al. aims to combat this issue by building an invertible neural network mapping which concentrates the change in the function in some small number of active directions.  This project improves the NLL algorithm by reposing it as the minimization of an almost-Dirichlet energy functional, leading to a mapping which is faster to compute and always reduces the number of active inputs to one.  [Read More.](/nll/){: .btn .btn--info .btn--small}{: .align-right}

(Joint with [Max Gunzburger](https://people.sc.fsu.edu/~mgunzburger/), [Lili Ju](https://people.math.sc.edu/ju/), [Yuankai Teng](https://slooowtyk.github.io/), and [Zhu Wang](https://people.math.sc.edu/wangzhu/).)


Modeling the p-Willmore Flow of Surfaces
------
![image-left](/images/cows.png){: .align-left}{: width="250" } Geometric flows are beautiful and powerful tools for prescribing a change in the geometry of a surface.
This project is a computational study of the p-Willmore flow, with the aim to develop a finite-element model that is amenable to geometric constraints on surface area and enclosed volume.  [Read More.](/surfaceFlow/){: .btn .btn--info .btn--small}{: .align-right}

(Joint with [Eugenio Aulisa](http://www.math.ttu.edu/~eaulisa/).)


Active Manifolds: Geometric Data Analysis for Dimension Reduction
------
![image-left](/images/AMpic.png){: .align-left}{: width="250" }  Scientists and engineers are frequently presented with mathematical models that are difficult to analyze due to their reliance on a large number of parameters. This project is inspired by the Active Subspaces idea of [Paul Constantine](https://scholar.google.com/citations?user=7x-Q4Y8AAAAJ&hl=en), and provides an algorithm which reduces the dimension of an unknown function to one regardless of the size of the original input space.  [Read More.](/am/){: .btn .btn--info .btn--small}{: .align-right}

(Joint with [Robert Bridges](https://sites.google.com/site/robertbridgeshomepage/), [Christopher Felder](https://www.math.wustl.edu/~cfelder/), and [Miki Verma](https://scholar.google.com/citations?user=1jUa6nwAAAAJ&hl=en).)


Curvature Functionals and p-Willmore Energy
------
![image-left](/images/virus_end.png){: .align-left}{: width="200" } Functional involving surface curvature are important across a wide variety of disciplines, and their minima are frequently representative of physically relevant structures, such as biomembranes or interfaces between materials.  This project involves a variational characterization of such functionals, with particular interest given to a generalization of the Willmore functional.  [Read More.](/cf/){: .btn .btn--info .btn--small}{: .align-right}

(Joint with [Magdalena Toda](http://www.math.ttu.edu/~mtoda/), [Hung Tran](https://www.math.uci.edu/~hungtt1/), and [Álvaro Pámpano](https://www.math.ttu.edu/~apampano/index.html).)
