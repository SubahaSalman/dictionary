student_data = {'id1':
    {'Name' : ['Sarah'],
     'Class' : ['V'],
     'Subject_integration' : ['english, math, science']
    },
  'id2':
   {'Name' : ['David'],
    'Class': ['V'],
    'Subject_integration': ['geography, math, science']
   },
   'id3':
    {'Name': ['Sarah'],
     'Class': ['V'],
     'Subject_integration': ['english, math, science']
    },
   'id4':
    {'Name': ['Surya'],
     'Class': ['V'],
     'Subject_integration': ['History, math, science']
    }
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key]= value

print(result)