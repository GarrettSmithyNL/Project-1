from Gar_Util import Gar_Validate as validator
from Gar_Util import Gar_Format as formater
from Gar_Util import Gar_Utility as utility

import datetime

today = datetime.datetime.now()
print(formater.dateMedium(today))
print(formater.dateLong(today))
print(formater.dateShort(today))
