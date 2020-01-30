import warnings
warnings.filterwarnings('ignore')
import oml
from oml import automl
from oml import algo
from oml.automl import FeatureSelection


# Connectiong to Database with automl as True
mydsn = "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=myhost)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=PDB)))"
dsn_pool = "(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=myhost)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=PDB)(SERVER=POOLED)))"

oml.connect(user='pyquser', password='mypassword',dsn=mydsn, automl=dsn_pool)

# Testing the Connection            
oml.isconnected()


import pandas as pd
data = pd.read_csv(r"D:\Assignments\40. OML4PY\wisc_bc_data.csv")
data.columns 

# Dropping the table BREASTCANCER if already exists
try:
    oml.drop(table="BREASTCANCER")
except:
    pass


# Creating a table 'BREASTCANCER' from Pandas DataFrame data
BREASTCANCER = oml.create(data, table="BREASTCANCER")

# Printing the Shape and top 5 rows of the BREASTCANCER dataset 
print("Shape:",BREASTCANCER.shape)
BREASTCANCER.head(5)


# Checking for available funtions on the oml DataFrame
res = [x for x in BREASTCANCER.__dir__() if not x.startswith('_')]
res.sort()
res


# Calculating Attribute importance ranking of variables
from oml import ai
train_dat, test_dat = oml.sync(table = "BREASTCANCER").split()  # here we use sync to get a handle to an existing table
train_x = train_dat.drop('diagnosis')
train_y = train_dat['diagnosis']
setting = {'ODMS_SAMPLING':'ODMS_SAMPLING_DISABLE'}

ai_obj = ai(**setting)
ai_obj = ai_obj.fit(train_x, train_y)

ai_obj


# Random Forest 
dat = BREASTCANCER.split()
dat[0]
dat[1]
train_x = dat[0].drop('diagnosis')
train_y = dat[0]['diagnosis']
test_dat = dat[1]


from oml import rf

rf_mod = rf(tree_term_max_depth = '4')
rf_mod = rf_mod.fit(train_x, train_y)
rf_mod

pred = rf_mod.predict(test_dat.drop('diagnosis'),supplemental_cols = test_dat[:, test_dat.columns])
print("Shape:",pred.shape)
pred.head(10)


res_ct = pred.crosstab('diagnosis','PREDICTION',pivot=True)
print("Type:",type(res_ct))
print("Columns:",res_ct.columns)

res_ct.sort_values(by='diagnosis')


# Model Accuracy
rf_mod.score(test_dat.drop('diagnosis'),test_dat[:,['diagnosis'])

