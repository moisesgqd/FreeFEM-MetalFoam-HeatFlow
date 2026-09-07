# Release notes

## Version v5.0.0

- Mayor refactorization of variables to make them more intuitive, e.g., the `u` field describing the longitudinal velocity component of the fluid was renamed as `uFluid`.
- Macros were integrated to account for different parameters or repated sequences of code.
- P1 and P0 finite element spaced were introduced to save discontinuous fields or fields that require to be at least once differentiable.
- Iterative loops were optimized.

## Version v4.0.0

- Initial and usused solvers were removed.
- User-defined functions were declared in another file and introduced in the main solvers.
- Non-relevant comment blocks were deleted.
- Print logs were also deleted, but it's planned to later be introduced in a more order manner.
- Mesh generation program was modfied.

## Version v3.1.0

- Porosity profile details were moved to specific file in data folder.

## Version v3.0.2

- Minor corrections on the post-processing program.
- The "replace NaN" function was added to the post-processing program.

## Version v3.0.1

- The function to replace NaN values from fields was introduced in the heat solver.

## Version v3.0.0

- Solvers were review in order to get results closer to the experimental data available, i.e., the code was validated.
- Input parameters on the iterations were added. It's possible to select start and end, and check convergence, export results every given number of iterations.

## Version v2.2.0

- Solvers do, in order, the following: extract input data, generate mesh, create finite element spaces, declare porous media properties, import initial fields (if necessary), define variational problem, run main loop.
- Compacto programs were reorganized and comment blocks were added in order to explain each part of the code and increase readability.
- Parameters to configure loop checking were introduced, as well as a function to replace NaN values from vector spaces. Loop checking was divided into three sections: write to logs, export fields if necessary, and check convergence criteria (L2 difference between old and new velocity and pressure inlet).
- Parameters like number of total iterations, difference in L2 difference in velocity fields, and so on, are imported from an EDP file in the data folder.

## Version v2.1.1

- The base post-processing program imports input data, reads result fields, and estimates porous media properties. These are the essential data required to do more calculations on the results, like calculating pressure difference, writing DAT files or CSV files, computing non-equilibrium difference, and so on.

## Version v2.1.0

- Mesh generation program reads inputs from EDP-format file, instead of the TXT-format file.
- Inlet velocity profile is declared after the non-slip boundary condition.
- A Python script was created and executed inside the FreeFEM++ scripts to create the directories inside the results folder.
- Stiffness matrices and RHS vectors are declared and constructed in the same line, instead of using two lines.
- A Release Notes markdown file was created. Most recent changes are written first.
- The README file is in development.

## Version v2.0.1

- NaN values were replaced from the vector of square root of longitudinal velocity.

## Version v2.0.0

- Compact solvers were programmed in order to simplify the simulations for a better understanding. These compact solvers take the minimum parameters required to solve the non-dimensional flow and heat problems.
- A post-processing program was developed in order to get the insights from the results obtained from the compact solvers. The main calculations are on the friction factor, wall Nusselt number and the non-equilibrium difference, though, other post-processing programs will be required to obtain velocity and temperature profiles.

## Version v1.1.0

- The normalized equations were rewritten in order to present diferent dimensionless parameters.
- The time variable was normalized, instead the parameter dtau was introduced.
- The boolean parameter to stop iteration when divergence is detected was removed from the estimation of divergence of the uToutlet parameter.
- Some calculations that are carried out once were removed from components in the main loop, in order to reduced execution time.

## Version v1.0.0

- Both the dependent variables (u, v, P, Of, and Os) and independent variables (x and y) were normalized in the weak formulations.
- The time variable remains dimensional, for now.

## Version v0.1.0

- Main source codes were divided into smaller chucks of code which are later imported into the main solvers. This other pieces of codes correspond, mostly, of inputs like mesh information, phases properties, functions, and debuging options.

## Version v0.0.1

- Some comment lines were added for clarity of the code, while some unnecessary line of comments were eliminated.

## Version v0.0.0

- Mesh generating source code was copied from the discarded version.
- Functional codes for the fluid and heat solver were also copied from verified cases.
- Exporting to VTU format is disabled since these files take up too much space.
- Source codes now reference to the current folder structure.
