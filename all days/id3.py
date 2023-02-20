import pandas as pd
import numpy as np

eps = np.finfo(float).eps

df = pd.read_csv("/content/drive/MyDrive/Computer_Sales.csv", encoding='unicode_escape')
df


# find entropy of entire dataset
def find_entropy(df):
    Class = df.keys()[-1]
    entropy = 0
    values = df[Class].unique()
    for value in values:
        fraction = df[Class].value_counts()[value]/len(df[Class])
        entropy += -fraction*np.log2(fraction)
    return entropy
  
  
# entropy of each attribute
def find_entropy_attribute(df,attribute):
  Class = df.keys()[-1]   
  target_variables = df[Class].unique()  
  variables = df[attribute].unique()    # This gives different features in that attribute (like 'Hot','Cold' in Temperature)
  entropy2 = 0
  for variable in variables:
      entropy = 0
      for target_variable in target_variables:
          num = len(df[attribute][df[attribute]==variable][df[Class] ==target_variable])
          den = len(df[attribute][df[attribute]==variable])
          fraction = num/(den+eps)
          entropy += -fraction*np.log2(fraction+eps)
      fraction2 = den/len(df)
      entropy2 += -fraction2*entropy
  return abs(entropy2)


# Get attribute with maximum information gain
def find_winner(df):
    IG = []
    for key in df.keys()[:-1]:
        IG.append(find_entropy(df)-find_entropy_attribute(df,key))
    return df.keys()[:-1][np.argmax(IG)]
  

# Get subtable for values (e.g. node=Outlook, value=sunny -> return rows with outlook=sunny only)
def get_subtable(df,node,value):
  return df[df[node] == value].reset_index(drop=True)


# Start ID3 algorithm
def buildTree(df,tree=None): 
    Class = df.keys()[-1]   # To make the code generic, changing target variable class name
    
    # Here we build our decision tree

    # Get attribute with maximum information gain
    node = find_winner(df)
    
    # Get distinct value of that attribute e.g Salary is node and Low,Med and High are values
    attValue = np.unique(df[node])
    
    # Create an empty dictionary to create tree    
    if tree is None:                    
        tree={}
        tree[node] = {}
    
    # We make loop to construct a tree by calling this function recursively. 
    # In this we check if the subset is pure and stops if it is pure. 

    for value in attValue:
        subtable = get_subtable(df,node,value)
        clValue,counts = np.unique(subtable[Class],return_counts=True)                        
        
        # Checking purity of subset
        if len(counts)==1: 
            tree[node][value] = clValue[0]                                                    
        else:        
            tree[node][value] = buildTree(subtable) 
                   
    return tree




import pprint
t = buildTree(df)
pprint.pprint(t)