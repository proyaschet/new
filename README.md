# 🤐 PII Redactor

## Overview

Welcome to Montu's technical challenge challenge for Machine Learning Engineers! 🎉 In this challenge, you will build a service that can automatically identify and redact Personally Identifiable Information (PII) from text data.

- The challenge is divided into two parts ([Model Development](#part-1-model-development) and [Service Development](#part-2-service-development)) and a bonus part ([Deployment](#bonus-part-deployment)).
  - You can complete the first two parts without deploying your service, but if you have the time, we encourage you to complete the deployment as well.
- We value your time and understand that you may not be able to complete the deployment part, so it is purely optional and we could tease that out a bit further in the techincal interview.
  - On an average, we expect the challenge to take around 3-4 hours to complete, but feel free to take as much time as you need and do let us know if you are time-constrained.

### Assessment Criteria

Your solution will be assessed based on the following criteria (leaving this a bit open-ended to see how you interpret it):

- If we think of building a Machine Learning / Data Science application as building a lego castle, we are more interested in seeing how you would assemble all the individual pieces (data processing, model development, service development, deployment) to build the castle, rather than the shine on individual pieces themselves. We are looking for a solution that is well-structured, modular, and easy to understand.
- Unlike a lego castle where it could be built in one go and then played with, building a Machine Learning application is more iterative, has more moving pieces, lot more prone to errors and can sometimes be bit of a moving target. So, we are looking for a solution that is robust, well-tested, operationally sound, and can easily be deployed/maintained/extended.
- If you go down the route of deploying it, bonus points if you are able to tease out efficiency, scalablility, security and perhaps even cost-effectiveness of your solution.

**_p.s._**

- Throughout the challenge, feel free to make any assumptions you like, please document them in your code/submission.
- Also, feel free to use any off-the-shelf libraries you like, but please be mindful that you are missing out on an opportunity to showcase your skills by using them (so, use them wisely). 
- And as a general rule of thumb, we would recommend spending more time on the service development/operationalising your solution end-to-end than model development.

**Please do not hesitate to reach out to us if you have any questions or need any clarifications. We are here to help! And most importantly, we hope you have some fun along the way! 🥳**


## Initial Setup and Submission Instructions

- you'll need the following tools to complete this challenge:
  - Python 3.9 or higher
  - Docker
  - Any other tool/library you decide to use
  - A cloud provider account (e.g. [AWS](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all), [GCP](https://cloud.google.com/free?hl=en)) if you choose to do the bonus part of the challenge. Both these providers offer free tiers that you can use to deploy your service, click on the links to learn more about their free tiers.

- **_Setup_**:
  - create a **private** fork of this repository and clone it to your local machine
    - a private fork is necessary to keep your solution private, which is important for the integrity of the challenge and can be done as follows:

        ```bash
        git clone --bare <this_repo>
        cd <this_repo>
        git push --mirror <your_repo>
        cd ..
        rm -rf <this_repo>
        ```

    - you can then clone your private fork as follows:

        ```bash
        git clone <your_repo>
        ```

    - feel free to commit & push (as you usually would) to this newly created fork as you work on your solution
  
- **_Submission_**:
  - once you have completed the challenge, please zip your solution and email/link it back to us
    - please ensure that your solution includes all the code you wrote, as well as any instructions on how to run your code, your `.git` folder, trained models if any, any additional data if use, and any other relevant information (notes, assumptions, etc..) that you think we should know about your solution.

    ```bash
    # from the root of your repository
    zip -r <your_name>_pii_redactor.zip .
    ```

## Problem Statement

### Background

Personally Identifiable Information (PII) in general is any data that could potentially identify a specific individual. Any information that can be used to distinguish one person from another and can be used for de-anonymizing anonymous data can be considered PII. Examples of PII include names, addresses, phone numbers, email addresses, social security numbers, etc.

### Part 1: Model Development

In this part, you will build a model that can automatically identify PII in text data and replace it with identified `PII category`. To limit the scope of this problem, we will only consider the following PII categories:

- `NAME` - Names of people or organizations
- `ORGANIZATION` - Names of organizations
- `ADDRESS` - Addresses of people or organizations
- `EMAIL` - Email addresses
- `PHONE_NUMBER` - Phone numbers

1. 💽 **Data**: We have provided a seed dataset `data/pii_data.json` in this repository to train your model. The dataset contains list of data points where each data point is a dictionary with two keys: `text` and `redacted_text`. The `text` key contains a piece of text with PII in it and the `redacted_text` key contains the redacted text with PII replaced by its category in-place. Here is an example data point:

    ```json
    [
      {
        "text": "Please contact Sarah Thompson at sarah.thompson@company.com.au or 0422 111 222 to schedule a meeting.",
        "redacted_text": "Please contact [NAME] at [EMAIL] or [PHONE_NUMBER] to schedule a meeting."
      }
    ]
    ```

   - [ ] **Task**: Load the dataset and preprocess the text data. You can use any preprocessing techniques you like (e.g. tokenization, lemmatization, etc.).
   - [ ] **Optional**: You can also use any other datasets you like to train your model. You can also use any other techniques you like to augment the text data. Any additional data you use should be included in the submission and the data augmentation should be part of your code.

2. 🧠 **Model**: You will build a model that can identify PII in text data. You are free to frame the problem as you see fit. You can either start modelling from scratch or use a pre-trained model and fine-tune it on the preprocessed text data.

   - Generally speaking, we are not looking for a perfect model, but a model that can identify PII in text data with reasonable accuracy. If you are time constrained and are debating spending time here or on the service development part, we would recommend spending more time on the service development part.

   - [ ] **Task**: Build a model according to the problem you have framed.
   - [ ] **Task**: Train your model on the preprocessed data from the previous data setp. You can use any evaluation metric that is appropriate to evaluate your model.
   - [ ] **Optional**: You can also use any techniques you like (e.g. `cross-validation`, `hyperparameter tuning`, etc.) to improve your model accuracy but it is not necessary.

### Part 2: Service Development

In this part, you will build a service that can redact PII from text data. You will use the model you built in the first part to identify PII in text data and redact it.

3. 🕸️ **Service Development**: You will build a service that can redact PII from text data. You are free to define the interface of your service as you like.

   - [ ] **Task**: Build a service that can accept a piece of text as input and return the redacted text with PII replaced by its category.

4. 🎡 **_NOTE_**: Please be mindful that building a robust ML/DS application is not about doing modelling and service development in isolation, but rather making them work together hand in hand. So, please consider operationalizing your pipelines end-to-end, testing as appropriate, linting and packaging your code/models, adding CI/CD workflows etc... as necessary. Refer to the [assessment criteria](#assessment-criteria) for some more intuition.

### Bonus Part: Deployment

In this part, you will deploy your service to a cloud provider of your choice.

5. 🌩️ **Deployment**: You will deploy your service to a cloud provider of your choice. You can use any cloud provider you like (e.g. AWS, GCP).
  
   - Ideally, we would deploy our entire end-to-end pipelines to the cloud, that would be a bit of an overkill for this challenge. So, instead if you choose to do this bit, you can just deploy your end service to the cloud.
   - Consider the efficiency, scalability, security, and cost-effectiveness of your deployment. Again, this is purely optional and we could tease that out a bit further in the techincal interview.
   - [ ] **Optional**: Deploy your service to a cloud provider of your choice as per your architecture of choice.


And that's it! 🎊 We can't wait to see what you come up with! 🚀