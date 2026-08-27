## AUG 27 2026 Week 3 Exceptions -- Outdated.py
**Worked on:** Multiple case edges in different branches, dict indexing

**Broke:** Here we go:
1. Initially looked into enumerating to build a dict, wasted time.
2. "if months in date" was checking a dict against a string
3. Where to put .split(), I kept putting it BEFORE the format check, so it was checking for nothing.
4. Tried padding a str (Ex: f"{date:02}) 
5. Having .strip(",") in the wrong branch, and was confused why .split(",") wouldn't remove the commma.
6. using built in functions on variables before they were defined resulting in UnboundLocalError.
7. and vs or in the rejection guard.

**Fixes:** 
1. Moved .split() inside the if "/" branch format check
2. Made day and year as ints for padding, kept month as it was an int from indexing the dict
3. Separated split and strip as two steps
4. UnboundLocalError: Moved the check on to split[1] instead of day since it wasn't declared a variable yet
5. Missing comma case, having endswith(",") guard before the strip.

**Notes:**
    -This felt like my first "difficult" pset compared to the rest ive done so far, conceptualizing each part from the beginnning isn't a winning strategy anymore.
    -I'm glad I did alter what was given slightly, and made the list into a dict.

**What I Would've Done Differently:**
    -I'll need to really practice what I preach and work section by section, testing output as I go.

## AUG 26 2026 Week 3 Exceptions -- Groceries.py
**Worked on:** building counters, organizing user input

**Broke:** Struggled to try to make the users input fit into indexes of a list for a while 
and got frustrated. My if/else statements were not counting properly, they were outside the while loop.

**Fixes:** Came back the next day, went back to my notes and lectures and used a dict instead

**Notes:** 
1. Variables can be keys in dicts
2. Lists store sequences, a dict stores a mapping

**What I Would Do Differently:** 
1. Stepping away when frustrated
2. Not being afraid to strip apart the problem section by section and restart to debug
3. Tracing input by hand before writing code.

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
