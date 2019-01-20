# A module is basically a file containing a set of functions to include in your application. there are care python
# modules, modules you can install using the pip package mananger (include Django) as well as custom modules 


#Core modules

# import datetime

from datetime import date

from time import time

#pipmodule

import camelcase


# today = datetime.date.today()
# timestamps = time()

# today = date.today()

# print(timestamps)

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))