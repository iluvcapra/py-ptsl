Getting Started with PTSL
=========================

The Pro Tools Scripting Library (PTSL) allows another program to control Pro Tools. 

Following below is a brief guide for people who might want to get started using PTSL

Create an Avid Developer Account 
--------------------------------

Go to the `Avid Developer Website`__ and create a developer account.

__ https://developer.avid.com/



Download the PTSL SDK
---------------------
The SDK (software development kit) has all of the documentation of PTSL, which is 
obligatory. The documentation lists all of the different *Commands* PTSL can make 
Pro Tools perform, how to run them and how to get information back from Pro Tools.


Experiment with the Engine 
--------------------------

``py-ptsl`` provides the :class:``Engine`` interface to PTSL, which exposes some PTSL 
Commands with an easy-to-use and documented interface, but you should only
consider these examples; your own applications may use the Engine or the lower-level
:class:`Client`.

Troubleshoot with the Client or the Command-Line Interface 
----------------------------------------------------------

You may run into problems running PTSL Commands exclusively from the Engine: Commands 
may not work correctly or at all, request parameters may not be recognized or undestood 
by Pro Tools, and so on. When you encounter a problem, the first thing you should try 
is running the same command using the Client or by running it in the command-line 
interface to ``py-ptsl``. The Engine provides an interface to commands, but 