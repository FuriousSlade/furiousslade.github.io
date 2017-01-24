Title:new_year.py
Date:2017-01-24
Category:Blog
Tags:Python

	
	class Year(object):
	
	    def __init__(self):
	        self.do_better()
	
	    def do_better(self, day=1):
	        if day < 365:
	            day += 1
	            self.do_better(day)
	
	if __name__ == '__main__':
	    new_year = Year()
