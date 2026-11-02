# Special Topics in Finite Element Modeling for IC Engines

**A practical course on finite element modeling of internal combustion engine components**

This course introduces the implementation of the **finite element method (FEM)** using **Python** and **Jupyter Notebook**. Through engineering examples, it covers the mathematical formulation of boundary-value problems, shape functions, element matrices, global assembly, boundary conditions, numerical solution, and post-processing.

The emphasis is on **understanding and implementing numerical methods from first principles**, rather than relying on a ready-made FEM solver. **Gmsh** is used for geometry preparation, mesh generation, and the definition of physical groups.

The repository contains **Seminars 00–06**, student exercises, and PDF presentations with mathematical derivations and methodological guidance. Most notebooks and presentations are written in English.

## Course outline

The table below links directly to the notebooks in this repository. The **Required materials** column distinguishes between files **already provided**, files **generated during the exercise**, and additional files **not included** in the repository.

| Seminar / notebook | Description | Python libraries | Required materials |
|---|---|---|---|
| **00. Introduction to Python and IC engine data processing**<br>[Main notebook](Short_introduction_python/sem00-Introduction_eng-imrpoved.ipynb) · [Student version](Short_introduction_python/sem00-Introduction_eng_st.ipynb) | NumPy fundamentals, numerical calculations, and visualization; cylinder pressure diagrams, signal filtering, heat-release characteristics, and a double-Wiebe combustion model. | `numpy`, `pandas`, `matplotlib`, `scipy` | **Not included:** `engine450hp.ind`, `IndDiagExp01.csv`; the main notebook also uses `materials/meter.txt` in an additional example. The corresponding cells cannot be reproduced without these files. |
| **01. Plane truss analysis**<br>[Main notebook](S01-Truss_modeling/sem01-truss-EN.ipynb) · [Student version](S01-Truss_modeling/sem01-truss-st-EN.ipynb) | Bar element stiffness matrix, global assembly, displacement constraints, nodal displacements, support reactions, and axial forces. | `numpy`, `matplotlib` | **Provided:** helper module [`udf_classes.py`](S01-Truss_modeling/udf_classes.py), located alongside the notebooks. No additional input files are needed. |
| **02. Steady-state heat conduction in a plate**<br>[Notebook](S02-Thermal_State_of_a_Plate/SimpleHeatTask-01-EN.ipynb) | Two-dimensional linear triangular finite elements, mesh generation, thermal conductivity matrix, and Dirichlet, Neumann, and Robin boundary conditions. | `numpy`, `matplotlib`, `gmsh` | **Provided:** CAD geometry [`_geom/geom.stp`](S02-Thermal_State_of_a_Plate/_geom/geom.stp). **Generated:** `_geom/mesh.msh`. |
| **03. Axisymmetric thermal analysis of a piston**<br>[Mesh preparation](S03-Thermal_State_of_a_Piston/Sem03-GeomPrepGmsh-EN.ipynb) · [Thermal analysis](S03-Thermal_State_of_a_Piston/Sem03-PistonHeatTask-EN.ipynb) | Defining Gmsh Physical Groups and exporting mesh data; variational formulation and solution of axisymmetric heat conduction with convective boundary conditions. | `numpy`, `matplotlib`, `gmsh` (mesh preparation); `numpy`, `matplotlib`, `scipy` (thermal analysis) | **Provided:** labeled geometry [`_geom/test_geo.xao`](S03-Thermal_State_of_a_Piston/_geom/test_geo.xao), CAD model [`_geom/geom_step.stp`](S03-Thermal_State_of_a_Piston/_geom/geom_step.stp), mesh [`_geom/piston.msh`](S03-Thermal_State_of_a_Piston/_geom/piston.msh), and prepared files `_mesh/nodes.csv`, `_mesh/elements.csv`, `_mesh/boundary.json`. The mesh preparation can be repeated; the thermal analysis notebook reads the files in `_mesh`. |
| **04. Independent assignment: thermal analysis of an intake valve**<br>[Assignment notebook](S04-Thermal_State_of_a_Int-Valve%28test%29/Sem04-Valve_Heat_St-EN.ipynb) | Independent definition of valve boundary groups, axisymmetric meshing, implementation of convective boundary conditions, heat-balance verification, and temperature export. | `numpy`, `matplotlib`, `gmsh` | **Provided:** CAD model [`_geom/intake_valve.stp`](S04-Thermal_State_of_a_Int-Valve%28test%29/_geom/intake_valve.stp). **To be created during the assignment:** `_geom/valve_geo.xao` with Physical Groups, `_geom/valve.msh`, and results in `_export_data/`. The notebook contains `TODO` cells and is intentionally not a fully implemented end-to-end solution. |
| **05. Plane stress analysis of a plate with a circular hole**<br>[Notebook](S05-Stress_Kirsch-plate/Sem05_Kirsch_Stress-EN.ipynb) | Plane elasticity, constant-strain triangular elements, mechanical boundary conditions, Cartesian and polar stress components, and comparison with the analytical Kirsch solution. | `numpy`, `matplotlib`, `gmsh` | **Provided:** labeled geometry [`_geom/kirsch.xao`](S05-Stress_Kirsch-plate/_geom/kirsch.xao) and original CAD file [`_geom/kirsch.stp`](S05-Stress_Kirsch-plate/_geom/kirsch.stp). **Generated:** `_geom/kirsch.msh`. |
| **06. Axisymmetric thermal stress analysis of a valve**<br>[Notebook](S06-Thermal_Stress_of_a_Valve/Valve-Thermal-Stress_axisymmetric-EN.ipynb) | Axisymmetric linear elasticity, mechanical loading, a sliding constraint at the valve seat, equivalent thermal load vectors, strain recovery, and stress analysis. | `numpy`, `matplotlib` | **Provided in `_import/`:** `nodes.csv`, `elements.csv`, `boundary.json`, and `temp.csv`, forming a consistent set of mesh nodes, elements, boundary groups, and nodal temperatures. Additional geometry files include [`_geom/valve_geo.xao`](S06-Thermal_Stress_of_a_Valve/_geom/valve_geo.xao). Gmsh is **not required to run this notebook**, because it reads the preprocessed input files. |

### Additional exercise

| Material | Description | Python libraries | Required materials |
|---|---|---|---|
| [Video processing and droplet detection](Extra01/extra-vp.ipynb) | Video frame processing, image analysis, contour detection, and an introduction to pretrained object-detection and segmentation models. | `opencv-python`, `numpy`, `pandas`, `matplotlib`, `seaborn`, `Pillow`, `tqdm`, `torch`, `ultralytics` | **Not included:** `data/simple-droplet.avi`, `data/org_img.png`, `data/org_mask.png`, and `data/paper_img.jpg`. The deep learning section may also require model weights. Outputs are saved in `artifacts/`. |

## Seminar presentations

The `Seminar_Materials/` directory contains **PDF presentations** with problem statements, theoretical background, mathematical derivations, and practical guidance. These materials support the hands-on seminars; they are **not a separate lecture series**.

| Seminar | Presentation |
|---|---|
| 01 — Plane truss analysis | [View PDF](Seminar_Materials/0.%20Plane_Truss_Analysis_EN.pdf) |
| 02 — Heat conduction in a plate | [View PDF](Seminar_Materials/1.%20Plate_Heat_EN.pdf) |
| 03 — Thermal analysis of a piston | [View PDF](Seminar_Materials/2.%20Piston_Heat_Analysis_EN.pdf) |
| 05 — Plane stress analysis | [View PDF](Seminar_Materials/3.%20Plane_Stress_Analysis_EN.pdf) |

## Getting started

1. **Install Python, Jupyter Notebook (or JupyterLab), and the core dependencies:**

   ```bash
   python -m pip install jupyter numpy pandas scipy matplotlib gmsh
   ```

   The optional computer vision exercise may additionally require `opencv-python`, `Pillow`, `seaborn`, `tqdm`, `torch`, and `ultralytics`.

2. **Launch each notebook from its own seminar directory.** Relative paths such as `_geom/...`, `_mesh/...`, and `_import/...` assume that the seminar directory is the current working directory. For example:

   ```bash
   cd S03-Thermal_State_of_a_Piston
   jupyter notebook Sem03-PistonHeatTask-EN.ipynb
   ```

3. **Use a Python environment with `gmsh` installed** for the seminars involving geometry and mesh generation. Some Physical Group labeling steps may also require the Gmsh graphical interface.

4. **Run the cells in order.** After preparing the necessary input files, use **Restart Kernel → Run All** to check reproducibility.

## Data transfer between seminars

The repository demonstrates two consecutive stages of finite element modeling:

- **Thermal analysis:** the nodal temperature field is obtained by solving \(\mathbf K_T\mathbf T=\mathbf F_T\).
- **Thermoelastic analysis:** that field is used to determine free thermal strains and equivalent nodal loads in \(\mathbf K_U\mathbf U=\mathbf F_{mech}+\mathbf F_{thermal}\).

**Seminar 04** includes an export step for `nodes.csv`, `elements.csv`, `boundary.json`, and `temp.csv` in `_export_data/`. **Seminar 06** reads these four files from `_import/`; a **ready-to-use `_import/` dataset is already provided** in the repository.

To use your own results from Seminar 04 in Seminar 06, transfer all four files into `_import/` as one consistent dataset. Verify that node coordinates, triangle connectivity, boundary indices, and nodal temperatures refer to the **same mesh and node ordering**.

**Units:** axisymmetric models use meters for coordinates and degrees Celsius for temperatures; temperature differences have the same numerical value in Celsius and kelvin. Mechanical loads and stresses use SI units internally. Check any conversions to millimeters or MPa when plotting results.

## Reproducibility notes

- **Seminar 04** is deliberately an independent assignment: providing the STEP geometry does not mean that every computational cell has already been implemented.
- **Seminar 00** and the **additional exercise** reference experimental data, images, and video files that are not included in the published archive. The external files listed above are required for full execution of those examples.
- The directories have distinct purposes: `_geom` stores source geometry, `_mesh` stores prepared mesh data, `_import` contains input datasets for subsequent analyses, and `_export_data` contains exported results. Do not rename them without updating the corresponding notebook paths.
- The Seminar 04 template currently exports `temp.csv` using the integer format `fmt="%d"`. When transferring temperatures to the thermoelastic analysis, save them as floating-point values (for example, `fmt="%.17g"`) to avoid unnecessary rounding.

## License

This repository includes a [LICENSE](LICENSE) file containing the **GNU General Public License v3.0**.
