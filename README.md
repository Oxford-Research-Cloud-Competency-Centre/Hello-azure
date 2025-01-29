© Chancellors, Masters and Scholars of The University of Oxford. All rights reserved.

# Explore different providers

This course is available for multiple cloud providers. Choose your preferred platform:

- [Hello Google Cloud](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-gcloud)
- [Hello Microsoft Azure](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-mazure)
- [Hello Amazon Web Services](https://github.com/Oxford-Research-Cloud-Competency-Centre/Hello-aws) (⭐ Most popular)
- Hello Oracle Cloud *(Coming Soon)*
- Hello IBM Cloud *(Coming Soon)*
- Hello Tencent Cloud *(Coming Soon)*
- Hello Alibaba Cloud *(Coming Soon)*
- Hello Baidu AI Cloud *(Coming Soon)*

*Note: Entries marked with "Coming Soon" are planned versions that are currently under development.*

# Instructions

Step 1. Fork (or make a copy of) this repository
<details>
<summary>Step 2. Go to the Microsoft Azure front page and type "App Services" in the search bar</summary>

![Step 2](README_images/img1.png)

***
</details>
<details>
<summary>Step 3. Go to Create -> Web App</summary>

![Step 3](README_images/img2.png)

***
</details>
<details>
<summary>Step 4. Create a new resource group for your application</summary>

![Step 4](README_images/img6.png)

***
</details>
<details>
<summary>Step 5. Choose an instance name. Select Python, Linux, and a region (UK South)</summary>

![Step 5](README_images/img3.png)

***
</details>
<details>
<summary>Step 6. Go to Deployment, set "Continuous Deployment" to "Enable" and select your repository</summary>

![Step 6](README_images/img4.png)

***
</details>
<details>
<summary>Step 7. Internet access should already be enabled. Keep it on.</summary>

![Step 7](README_images/img7.png)

***
</details>
Create the app and wait for deployment. Voilà! Access the URL.

![Voilà](README_images/img5.png)

***

# Going further

## Modifying the code

You can commit some changes to your repository and watch how the service is updated automatically. 

***

## Cleaning up

<details>
<summary>The simplest way to delete all the resources you just created is to type "Resource Groups" in the search bar and delete the group that you created earlier.</summary>

![Deleting a service](README_images/resource_group.png)

***
</details>
## Adding an API endpoint

<details>
<summary>Add the following code in app.py </summary>

```	
@app.route("/hello_api")
def hello_api():
    return {
		"name": "Wrinkle Five Star",
		"species": "Duck",
		"breed": "American Pekin",
		"hatching_date": "2020-09-09",
		"sex": "Male"
    }
```

***
</details>
Then test your endpoint

![API endpoint](README_images/hello_api.png)

***

## User interface

<details>
<summary>...</summary>
Missing content
</details>

## Database writing/reading

<details>
<summary>Go to the AWS Console and type "RDS" in the search bar</summary>
Missing content
</details>

## Storage bucket writing/reading

<details>
<summary>Go to the AWS Console and type "S3" in the search bar</summary>
Missing content
</details>


