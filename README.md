# Project 4:  Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax

## ACP controle times

student name: Hang Li

ACP rules:
1. error messages will pop up when users input numbers not in the range between 0 and 110% * brevet. This check function is implemented in flask_brevet.py.
2. If a control distance is more than the brevet distance but less than 110% * brevet distance, the control distance would be regarded as the brevet distance
3. The starting point will be closed in one hour by ACP rule.


## AJAX and Flask reimplementation

The current RUSA controle time calculator is a Perl script that takes
an HTML form and emits a text page. The reimplementation will fill in
times as the input fields are filled.  Each time a distance is filled
in, the corresponding open and close times should be filled in.   

I will leave much of the design to you.   

## Testing

A suite of nose test cases is a requirement of this project.  Design
the test cases based on an interpretation of rules at
https://rusa.org/octime_alg.html .  Be sure to test your test
cases:  You can use the current brevet time calculator (
https://rusa.org/octime_acp.html ) to check that your expected test
outputs are correct. While checking these values once is a manual
operation, re-running your test cases should be automated in the usual
manner as a Nose test suite.

To make automated testing more practical, your open and close time
calculations should be in a separate module.  Because I want to be 
able to use my test suite as well as yours, I will require that 
module be named acp_times.py and contain the two functions I have 
included in the skeleton code (though revised, of course, to 
return correct results).

With your virtual environment activated, we should be able to run your
test suite by changing to the "brevets" directory and typinng
"nosetests".   All tests should pass.  You should have at least 5
test cases, and more importantly, your test cases should be chosen to
distinguish between an implementation that correctly interprets the
ACP rules and one that does not.

## Replace this README

This README is currently written primarily as instructions to CIS 322
students.  Replace it with a proper README for an ACP time
calculator.  Think about what should be included for users and for
developers.  If it is growing too long, factor details into one or
more separate documents, with references from the README.

