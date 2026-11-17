Report
======

.. important::

   To make sure you are using correct values to compute any final results, we
   will verify each of your calculated outputs **before** you start writing
   the protocol. To do so, you will have to fill out the
   :download:`results.csv <../exercises/results.csv>` file and send it to one
   of your tutors for verification.

   .. raw:: html

      <div style="background: rgba(128,128,128,0.15);
                  padding: 12px 16px;
                  border-radius: 5px;
                  margin: 16px 0;">
         We will <strong>not</strong> accept protocol submission
         without prior verification of the results!
      </div>

   Please provide all data in units as specified in ``results.csv``. Use six
   decimal places for absolute energies in atomic units, four decimal places
   for values in kcal/mol, and do **not** change the structure of the file as
   this would hamper with our verification process.

Email only the completed ``results.csv`` to one of your tutors for this
initial check. Also, allow enough time for verification and any corrections before
submitting your report **well before** the final submission deadline as communicated
via eCampus/email.

General Requirements
--------------------

The report is also an exercise in scientific writing, specificallyin theoretical chemistry.
Write in complete English sentences, use scientific terminology,
and cite the methods, programs, and published work you use.

Organize the report by exercise and answer **every question in the exercise
script**. Within each exercise, describe the methods and relevant equations,
present the data, and then discuss the results. The discussion is the
most important part of your report!

Introduce every symbol and abbreviation at first use, including those used in
equations, and provide units for all reported quantities. For derived quantities and values,
clearly state how they were calculated. Use consistent notation throughout.

Computational Details
---------------------

Provide the following information where applicable:

- **System and geometry.** Mention if you reoptimized geometries.
- **Type of calculation.** Specify whether you performed a single-point
  calculation, geometry optimization, frequency calculation, distance scan,
  or a separate calculation of an energy contribution or correction.
- **Program and version.** Name each program and give its version, including
  any program used to compute a separate correction.
- **Method.** State the specific electronic structure method, such as
  Hartree–Fock, MP2, or CCSD(T). For DFT, name the concrete density functional
  approximation. For SAPT, state the SAPT level and the method used for the monomers
  calculations.
- **Basis set.** Name the basis set used with each method.
- **Additional Corrections.** Specify the use of a dispersion correction (including
  the employed damping scheme), and whether a three-body contribution was included.
  Identify thermochemical corrections or considerations of solvation effects where relevant.

Report methodological choices that matter for understanding the results and
possible sources of error. State shared details once and make clear which
calculations they apply to, without overly emphasizing technical details
with minor importance for this practical course.

Results and Discussion
----------------------

Describe **and** explain your results. Support your answers with specific
values or trends. For each comparison, identify the quantities, systems,
methods, or basis sets being compared and quantify the relevant differences.
Use the underlying theory to explain why a method gives a particular result,
why agreement may be good, and where deviations may come from. If several
methodological choices change together, state what the comparison can
establish.

Check what each literature or experimental value represents before using it
as a reference, while distinguishing electronic energy differences (:math:`\Delta E`),
enthalpy differences (:math:`\Delta H`), and Gibbs free energy differences
(:math:`\Delta G`). Check whether the reported quantities and conditions
permit a direct comparison and explain possible limitations.

Be mindful of any “chemical accuracy” statements and prevent overclaims
in this report by critically assessing all results. State the actual
deviation in the context of the relevant energy scale of the problem at
hand. A deviation below 1 kcal/mol does not by itself establish that a
method describes an interaction or trend well!

Figures, Tables, and Numerical Data
-----------------------------------

- Include all plots requested in the Exercises. Use plots to show trends and
  compact tables to compare values.

- Choose axis limits such that they include key features to allow for a
  practical discussion without cutting off or compressing important features.

- Number and caption every figure, table, and scheme. Introduce each by
  number in the text and discuss the observation it supports. Make captions
  understandable on their own. Label plot axes and use a legend or direct
  labels to identify individual curves. When comparing levels of theory, make
  clear which level was used to obtain what data.

- As in ``results.csv``, report absolute energies in Hartree to six
  decimal places and energies in kcal/mol to four decimal places.

- Place extensive (raw) data tables and complete numerical series needed to
  document the results in the appendix. Only refer to them within the main text.

Citations and Bibliography
--------------------------

Cite all methods and programs used throughout, following their recommended
citations where available. Evidently, also cite literature claims, reference
values, and reproduced or adapted material at the point of use. If you use
data from literature sources, make clear which results you obtained yourself.

Check that every cited source actually supports the claim or contains the
value or data cited. If you derive a reference value from published data,
state how/where you obtained it (e.g., provide a table or section number if
it could help locate the values). Include a complete, consistently formatted
bibliography.

Scope and Acceptance
--------------------

Separate theory sections and general technical explanations of methods such
as HF or DFT are not required. Introduce the equations used to obtain the results
and provide any background needed for interpretation of the results.

To get accepted, your report must contain answers to every exercise question, discuss
the results properly, and include the essential computational details and citations.