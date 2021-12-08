import csv

def save_to_file(contexts):
    file = open("jobs.csv", mode = "w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])             
    for context in contexts :
        writer.writerow(list(context.values())) 
           
    return file