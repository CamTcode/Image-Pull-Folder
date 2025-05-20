Image Scraper Unsplash
Microservice for Lydia

To request an image:
-Write your search term into input.txt Ex.:

with open("input.txt", "w") as f:
    f.write("happy")
    
-Then run the Microservice:
python ImagePull.py


To recieve the data:
After the microservice runs, read the output from output.txt Ex.:

with open("output.txt", "r") as f:
    image_url = f.read().strip()

    
Communication Contract:
input.txt	Input	Mood/genre from the caller
output.txt	Output	Image URL returned from the service!

UML sequence diagram:
https://github.com/user-attachments/assets/f7f6bf81-0925-422d-ad1f-1453425d1a7c
