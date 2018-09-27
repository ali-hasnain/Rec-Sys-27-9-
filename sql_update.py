import csv

 
def update_csv(contentId,personId,eventType):
    myData=[[contentId,personId,eventType]]
    
    with open('user_interactions_ghn.csv', 'a') as myFile:
        writer = csv.writer(myFile,lineterminator='\n')
        writer.writerows(myData)

#update_csv(10,44,'BUY')     
print("Writing complete")
