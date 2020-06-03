import csv
import re

tweets = open('clean.reddit.valid','w')  
  
with open('/home/controller-two/Downloads/training.1600000.processed.noemoticon.csv', mode='r', encoding = "ISO-8859-1") as csv_file:
# with open('/home/controller-two/Codes/project/reddit_v1.csv', mode='r', encoding = "ISO-8859-1") as csv_file:  
    csv_reader = csv.DictReader(csv_file, fieldnames=['status', 'user_id', 'timestamp', 'query', 'user_handle', 'text'])
    line = 0
    offset = 0
    for row in csv_reader:
        # Clean the training data
        # First we lower case the text

        offset+=1

        if line == 0:
            line+=1
            continue
        
        if line < 53200:
            line+=1
            continue
        if line > 56976:
            break

        line = line + 1
        
        if line%16 == 0:


            text = row["text"].lower()
            # # remove links
            text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',text)
            # #Remove usernames
            text = re.sub('@[^\s]+','', text)
            # # replace hashtags by just words
            text = re.sub(r'#([^\s]+)', r'\1', text)
            text = re.sub('(?<=[a-z])\'(?=[a-z])', ' ', text)
            # #correct all multiple white spaces to a single white space
            text = re.sub('[\s]+', ' ', text)
            # # Additional clean up : removing words less than 3 chars, and remove space at the beginning and teh end
            # text = re.sub(r'\W*\b\w{1,3}\b', '', text)
            text = re.sub(r'[^\x00-\x7F]+',' ', text)
            
            text = re.sub(r'[^\w\s]','',text)
            # text = text.strip()

            # Split data into train and validation

            print(f'__label__nonsuicidal {text}', file=tweets)

    print(line)