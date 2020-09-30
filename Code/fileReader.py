import csv
#Gabriel Dichi
#5 paises mas productores de gases invernadero en 2010
#5 paises mas poblados 2010
#se relacionan estos datos?

arr= []
arr2 = []
with open("../TextFiles/greenhouse_gas_inventory_data_data.csv") as csvFile:
    reader = csv.reader(csvFile)
    
    for row in reader:
        if (row[3].startswith("greenhouse_gas_ghgs_emissions_including") and row[1] == "2010"):
            arr.append((float(row[2]),row[0]))
   
    arr.sort(reverse = True)
                     
    print("5 paises mas productores de gases invernadero en 2010: " , arr[:5])
    
  
    

with open("../TextFiles/populationbycountry19802010millions.csv") as csvFile:
    reader = csv.reader(csvFile)
    
    error = ["--", "NA"]
    exceptions = ["World", "Country", "Asia & Oceania", "Africa", "Europe", "Central & South America", "North America", "Eurasia", "Middle East"]

    for row in reader:
        if row[30] not in error and row[0] not in exceptions:
            arr2.append((float(row[30]),row[0]))
    arr2.sort(reverse = True)
    print()
    print("5 paises mas poblados 2010: ", arr2[:5])

print()
print("se relacionan estos datos?")
print ("solo USA se repite en ambas listas")
    


   
    
    



    


    #reader = csv.DictReader(csvFile)
    
    #print(reader.fieldnames)


    