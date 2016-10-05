# -*- coding: utf-8 -*-
"""


@author: jayson
"""

import re

phoneNumber='650-555-1212'

phonePattern=re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})$')
formattedNumber=phonePattern.search(phoneNumber).groups()
print(formattedNumber)

