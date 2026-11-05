# Special Topics in Finite Element Modeling for IC Engines

**A practical course on finite element modeling of internal combustion engine components**

This course introduces the implementation of the **finite element method (FEM)** using **Python** and **Jupyter Notebook**. Through engineering examples, it covers the mathematical formulation of boundary-value problems, shape functions, element matrices, global assembly, boundary conditions, numerical solution, and post-processing.

The emphasis is on **understanding and implementing numerical methods from first principles**, rather than relying on a ready-made FEM solver. **Gmsh** is used for geometry preparation, mesh generation, and the definition of physical groups.

The repository contains **Seminars 00–06**, student exercises, and PDF presentations with mathematical derivations and methodological guidance. 



Course outline

The table below links directly to the notebooks in this repository. The **Included materials** column lists the files and datasets available in each seminar directory.

|Seminar / notebook|Description|Python libraries|Included materials|
|-|-|-|-|
|**00. Introduction to Python and IC engine data processing**<br>[Main notebook](Short_introduction_python/sem00-Introduction_eng-imrpoved.ipynb) · [Student version](Short_introduction_python/sem00-Introduction_eng_st.ipynb)|NumPy fundamentals, numerical calculations, and visualization; cylinder pressure diagrams, signal filtering, heat-release characteristics, and a double-Wiebe combustion model.|`numpy`, `pandas`, `matplotlib`, `scipy`|Main and student Jupyter notebooks.|
|**01. Plane truss analysis**<br>[Main notebook](S01-Truss_modeling/sem01-truss-EN.ipynb) · [Student version](S01-Truss_modeling/sem01-truss-st-EN.ipynb)|Bar element stiffness matrix, global assembly, displacement constraints, nodal displacements, support reactions, and axial forces.|`numpy`, `matplotlib`|Main and student notebooks; helper module [`udf\_classes.py`](S01-Truss_modeling/udf_classes.py).|
|**02. Steady-state heat conduction in a plate**<br>[Notebook](S02-Thermal_State_of_a_Plate/SimpleHeatTask-01-EN.ipynb)|Two-dimensional linear triangular finite elements, mesh generation, thermal conductivity matrix, and Dirichlet, Neumann, and Robin boundary conditions.|`numpy`, `matplotlib`, `gmsh`|CAD geometry: [`\_geom/geom.stp`](S02-Thermal_State_of_a_Plate/_geom/geom.stp).|
|**03. Axisymmetric thermal analysis of a piston**<br>[Mesh preparation](S03-Thermal_State_of_a_Piston/Sem03-GeomPrepGmsh-EN.ipynb) · [Thermal analysis](S03-Thermal_State_of_a_Piston/Sem03-PistonHeatTask-EN.ipynb)|Defining Gmsh Physical Groups and exporting mesh data; variational formulation and solution of axisymmetric heat conduction with convective boundary conditions.|`numpy`, `matplotlib`, `gmsh` (mesh preparation); `numpy`, `matplotlib`, `scipy` (thermal analysis)|CAD model [`\_geom/geom\_step.stp`](S03-Thermal_State_of_a_Piston/_geom/geom_step.stp); labeled geometry [`\_geom/test\_geo.xao`](S03-Thermal_State_of_a_Piston/_geom/test_geo.xao); Gmsh mesh [`\_geom/piston.msh`](S03-Thermal_State_of_a_Piston/_geom/piston.msh); prepared mesh data: `\_mesh/nodes.csv`, `\_mesh/elements.csv`, `\_mesh/boundary.json`.|
|**04. Independent assignment: thermal analysis of an intake valve**<br>[Assignment notebook](S04-Thermal_State_of_a_Int-Valve%28test%29/Sem04-Valve_Heat_St-EN.ipynb)|Independent definition of valve boundary groups, axisymmetric meshing, implementation of convective boundary conditions, heat-balance verification, and temperature export.|`numpy`, `matplotlib`, `gmsh`|Intake valve CAD model: [`\_geom/intake\_valve.stp`](S04-Thermal_State_of_a_Int-Valve%28test%29/_geom/intake_valve.stp).|
|**05. Plane stress analysis of a plate with a circular hole**<br>[Notebook](S05-Stress_Kirsch-plate/Sem05_Kirsch_Stress-EN.ipynb)|Plane elasticity, constant-strain triangular elements, mechanical boundary conditions, Cartesian and polar stress components, and comparison with the analytical Kirsch solution.|`numpy`, `matplotlib`, `gmsh`|CAD model [`\_geom/kirsch.stp`](S05-Stress_Kirsch-plate/_geom/kirsch.stp); labeled geometry [`\_geom/kirsch.xao`](S05-Stress_Kirsch-plate/_geom/kirsch.xao).|
|**06. Axisymmetric thermal stress analysis of a valve**<br>[Notebook](S06-Thermal_Stress_of_a_Valve/Valve-Thermal-Stress_axisymmetric-EN.ipynb)|Axisymmetric linear elasticity, mechanical loading, a sliding constraint at the valve seat, equivalent thermal load vectors, strain recovery, and stress analysis.|`numpy`, `matplotlib`|Valve CAD model [`\_geom/valve.stp`](S06-Thermal_Stress_of_a_Valve/_geom/valve.stp); labeled geometry [`\_geom/valve\_geo.xao`](S06-Thermal_Stress_of_a_Valve/_geom/valve_geo.xao); Gmsh mesh [`\_geom/valve.msh`](S06-Thermal_Stress_of_a_Valve/_geom/valve.msh); prepared input data: `\_import/nodes.csv`, `\_import/elements.csv`, `\_import/boundary.json`, `\_import/temp.csv`.|

### Additional exercise

|Material|Description|Python libraries|Included materials|
|-|-|-|-|
|[Video processing and droplet detection](Extra01/extra-vp.ipynb)|Video frame processing, image analysis, contour detection, and an introduction to pretrained object-detection and segmentation models.|`opencv-python`, `numpy`, `pandas`, `matplotlib`, `seaborn`, `Pillow`, `tqdm`, `torch`, `ultralytics`|Jupyter notebook with video-processing, image-analysis, and object-detection examples.|

## Seminar presentations

The `Seminar\_Materials/` directory contains **PDF presentations** with problem statements, theoretical background, mathematical derivations, and practical guidance. These materials support the hands-on seminars; they are **not a separate lecture series**.

|Seminar|Presentation|
|-|-|
|01 — Plane truss analysis|[View PDF](Seminar_Materials/0.%20Plane_Truss_Analysis_EN.pdf)|
|02 — Heat conduction in a plate|[View PDF](Seminar_Materials/1.%20Plate_Heat_EN.pdf)|
|03 — Thermal analysis of a piston|[View PDF](Seminar_Materials/2.%20Piston_Heat_Analysis_EN.pdf)|
|04 — Plane stress analysis|[View PDF](Seminar_Materials/3.%20Plane_Stress_Analysis_EN.pdf)|
|05 — Valve_thermoelastic analysis|[View PDF](Seminar_Materials/4.%20Valve_thermoelastic_FEA_EN.pdf)|


## License

This repository includes a [LICENSE](LICENSE) file containing the **GNU General Public License v3.0**.

