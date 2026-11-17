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
   for values in kcal\  mol\ :sup:`-1`, and do **not** change the structure of the file as
   this would hamper with our verification process.

Email only the **complete** (not a partially filled) ``results.csv`` file to one of your tutors for this
initial check. Also, allow enough time for verification and any corrections on your end
before submitting your report **well before** the final submission deadline as
communicated via eCampus/email. 

We are not responsible to  "last-minute-correct" ``results.csv``
submissions and thus your calculations the day before the general protocol submission
deadline!

.. important::

   After having validated your results, read the following instructions carefully
   before starting to write your final report for the Grimme part to avoid lengthy
   revisions later on! Feel free to ask your tutors for clarification if needed.

General Requirements
--------------------

The report is also an exercise in scientific writing, specifically in theoretical chemistry:

*Write in complete English sentences, use scientific terminology,
and cite the methods, programs, and published work you use.*

Organize the report by exercise and answer **every question in the exercise
script**. Within each exercise, describe the methods and relevant equations,
present the data, and then discuss the results. Remember, the discussion
and interpretation of your results is the most important part of your report!

Introduce every symbol and abbreviation at first use, including those used in
equations, and provide units for all reported quantities. For derived quantities and values,
clearly state how they were calculated (e.g., by providing relevant equations and/or references), 
and use consistent notation throughout.

Computational Details
---------------------

Provide the following information to allow for reproducibility and reasonable
interpretation of your findings, especially for key results that are method-dependent:

- **System and geometry.** Mention if you have reoptimized geometries or used additional
  structures *not* taken from the Github repository (**only** use the provided
  geometries from Github to avoid errors with ``results.csv`` validation).
- **Type of calculation.** *Briefly* specify each step of your applied workflow,
  including single-point calculation(s), geometry optimization(s), frequency calculation(s),
  PES scan(s), or any other calculation(s) relevant to reproduce any separate contribution(s)
  used to obtain your final values.
- **Program and version.** Name each program and mention the employed version number.
- **Method.** State the specific electronic structure method, such as
  Hartree–Fock, MP2, or CCSD(T). For DFT, always name the concrete density functional
  approximation. For SAPT, state the SAPT level and the method used for to compute the
  monomers.
- **Basis set.** Name the basis set used in combination with each of the methods.
- **Additional Corrections.** Specify the use of a dispersion correction (including
  the employed damping scheme), and whether a three-body contribution was included in
  case the method does not already include it by default. Mention thermochemical
  corrections or the inclusion of solvation effects where applicable.

*Key takeaways*: Report methodological choices and settings that matter for
understanding the results and possible sources of errors. State shared computational
details once and make clear which calculations they apply to, without overly
emphasizing technical details with minor importance for this practical course.

Results and Discussion
----------------------

Briefly describe **and** explain your results. Support your answers with specific
values or trends observed. Use the underlying theory to explain why a method gives
a particular result, and where deviations may originate from.

Check what each literature or experimental value represents before using it
as a reference for your calculated values (i.e., compare "apples to apples"), while
distinguishing electronic energy differences (:math:`\Delta E`),
enthalpy differences (:math:`\Delta H`), and Gibbs free energy differences
(:math:`\Delta G`) throughout.

Be mindful of any “chemical accuracy” statements and prevent overclaims
in this report by critically assessing all results. Hence, comment on deviations
in the context of the relevant energy scale of the problem at hand. E.g., deviations
below 1 kcal\  mol\ :sup:`-1` do not by itself establish that a method describes an interaction
or trend consistently well for a broad range of molecular systems.

Figures, Tables, and Numerical Data
-----------------------------------

Include all plots requested in the Exercises. Plots and compact tables can
be used to visualize or highlight certain trends, but are only effective, for instance,
if captions describe the contents clearly and plot axis limits are chosen appropriately to
not cutoff or overly compress important features.

Use a consistent numbering scheme for figures, tables, and schemes and make all captions
self-contained. When comparing levels of theory, make clear which level of theory was
used to obtain what data.

Different from your input into ``results.csv``, report final energy (differences) up to
**only two** decimal places when provided in units of kcal\  mol\ :sup:`-1`. Only the dispersion energies
from Exercise 1.3 require reporting with more decimal places.

Do **not** include your (raw) data in the protocol and move large tables into the appendix
if provided at all.

Citations and Bibliography
--------------------------

Cite all methods and programs used throughout, following their recommended
citations where available. Evidently, also cite literature claims, reference
values, and reproduced or adapted material at the point of use. If you use
data from literature sources, make clear which results you obtained yourself.
Include a complete, consistently formatted bibliography.

Scope and Acceptance
--------------------

Separate theory sections and general technical explanations of methods such
as HF or DFT are **not** required. Only briefly introduce the equations used
to obtain your results and provide any background needed for interpretation.

To complete your report, it must contain answers to every exercise question, discuss
the results properly, and include the essential computational details and citations. 
Please ensure all these criteria are met. We typically only allow one round of extensive
revisions prior to acceptance of the reports.