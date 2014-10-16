## Vogogo Development Exercise Solution

This packages iterates over an Account Number file line by line building 
Digits. Digits are "Glifs" in specific positions converted to 3x3 matrices.
Once all Glifs of a Digit have been specified matrix operations are used to match the specific Digit to a known corresponding integer value.
Account Numbers are composed of n number of Digits (in this case 9 Digits).
Said Account Numbers can be validated assuming their Digits are all determinable.


### Dependencies:

	* Python (2.7.6) (Earlier and later versions will likely work but are untested)
	* [NumPy](http://www.numpy.org/)(1.8.2) (Again earlier and later version will likely work)

### Installing Python Dependencies (NumPy)

> On a Ubuntu/Debian system this is likely as easy as:

 	sudo apt-get install python-numpy


### Running Instructions:

After downloading or checking out this repo run:

	python vogogo.py

>_Note: Currently the AccountNumber.txt file is assumed to be in the root of the project; the same directory as vogogo.py

output prints to standard out


### Example Run:

Assuming AccountNumbers.txt is:

	 _  _  _  _  _  _  _     _ 
	|_||_||_|  |  ||_|  |  | _|
	 _| _| _|  |  ||_|  |  | _|

	 _  _  _  _  _  _  _  _    
	| || || || || || || ||_   |
	|_||_||_||_||_||_||_||_|  |

	 _  _  _  _  _  _  _  _    
	| || || || || || || |  |  |
	|_||_||_||_||_||_||_|  |  |

	 _  _  _  _  _  _  _     _ 
	| || || || || || || |  ||_|
	|_||_||_||_||_||_||_|  | _|

	 _  _  _  _  _  _  _  _  _ 
	  || ||_ | || || || ||_|  |
	 _| _||_| _||_| _||_ |_||_|

	 _  _  _  _  _  _  _  _  _ 
	| || || || || || || | _|  |
	|_||_||_||_||_||_||_||_   |

Program Output is:

	999778713 ERR
	000000061 ERR
	000000071 ERR
	000000019
	??6?0??8? ILL
	000000027


