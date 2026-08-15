## AUG 14 2026 Week 3 Exceptions -- Fuel.py
**Worked on:** reprompt looping, E/F edge cases

**Broke:** infinite loop printing values, program printed "E" then kept running

**Fixes:** "pass" doesnt restart the loop, it falls to the next line of code, continue is what restarts the loop (nonintuitive grammatically imo). Every terminal branch needs break inside a loop

**Notes:** 
1. Multiple times today I had missing return values, missed return entirely, or forgot to add break. This needs to be checked and worked on.
2. Lack of initial code design, program decomposition and pseudocode really hindered me to solve this problem. I need to work on:
    - starting with code design and decomposition of functions
    - implement pseudocode and test not only to improve logic, but for myself when returning to the code (habit building)
    - checking my code repeadtly instead of at the end
3. Review: while loops and break, continue, pass logic
   
**What I Would Do Differently:**
1. Have a clear plan before comitting to writing code, as well as pseudocode of running through the logic of each of my functions
