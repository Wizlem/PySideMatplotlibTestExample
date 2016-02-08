all: design.py testmodal.py

%.py: %.ui
	pyside-uic $*.ui -o $*.py 
