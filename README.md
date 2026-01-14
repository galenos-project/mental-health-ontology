# mental-health-ontology
This repository contains the data for GALENOS mental health Ontology. 

# Project Overview
The [GALENOS project](https://www.galenos.org.uk/) involves conducting multiple Living Systematic Reviews (LSRs); systematic reviews that are continuously updated to reflect the latest evidence. To organise and make this information easily accessible, the GALENOS Mental Health Ontology is being developed. This ontology will structure data from the LSRs into an intuitive [Data Browser](https://galenos-data.aliveevidence.org/data_browser), enabling users to review and reuse the data in the future.
To support this evidence integration, we are creating an ontology focused on the domain of mental health, with particular emphasis on anxiety, depression, and psychosis. The scope of the Mental Health Ontology includes:
1) Human mental health conceptualizations: constructs representing symptoms, diagnoses, and wellbeing, with attention to promoting mental health rather than solely treating dysfunction.
2) Mental health interventions: coordinated activities designed to improve specific aspects of mental health, including details on their delivery.
3) Settings where interventions are implemented.
4) Populations receiving interventions.
5) Intervention mechanisms and biomarkers associated with mental health outcomes.
6) Intervention outcomes, including risk prediction and spillover effects related to mental health.
7) Research methods relevant to mental health studies.
For more details on the methodology, please access the [protocol paper](https://wellcomeopenresearch.org/articles/9-40/v3?gtmKey=GTM-5P673KJ&immUserUrl=https%3A%2F%2Fwor-proxy.f1krdev.com%2Feditor%2Fmember%2Fshow%2F&otid=23226e40-fdd0-4acd-97a3-d9bad93befed&s3BucketUrl=https%3A%2F%2Fwellcomeopenresearch-files.f1000.com&submissionUrl=%2Ffor-authors%2Fpublish-your-research&transcendEnv=cm&transcendId=ef49a3f1-d8c1-47d6-88fc-50e41130631f). 

# Folder structure:
The following folders contain .xlsx files with the different ontology classes:
1) Intervention content and delivery,
2) Intervention mechanism,
3) Intervention outcomes and spillover effects,
4) Intervention population,
5) Intervention setting,
6) Research methods and
7) UpperLevel.

The following folder contains the .xlsx file with the mapping from LSR variables to ontology classes, used to develop the Browser. In this folder you will also find the acronyms.csv file containing the acronyms used in LSR data and the hierarchy.yml file used to develop the hierarchy of classes in the Data Browser. 
8) Mapping to LSRs

These folders are used to make OWL versions of the ontology and enable the use of [OntoSpread-Ed](https://wellcomeopenresearch.org/articles/10-360) to edit it:
9) .github/workflows
10) .onto-ed
11) inputs
12) scripts

# Download OWL file of the ontology:
You can find the gmho.owl file in this main repository folder.

# How to cite:
When using the ontology, please cite our [protocol paper](https://wellcomeopenresearch.org/articles/9-40/v3?gtmKey=GTM-5P673KJ&immUserUrl=https%3A%2F%2Fwor-proxy.f1krdev.com%2Feditor%2Fmember%2Fshow%2F&otid=23226e40-fdd0-4acd-97a3-d9bad93befed&s3BucketUrl=https%3A%2F%2Fwellcomeopenresearch-files.f1000.com&submissionUrl=%2Ffor-authors%2Fpublish-your-research&transcendEnv=cm&transcendId=ef49a3f1-d8c1-47d6-88fc-50e41130631f)

# Contact information:
If you would like extra information on the ontology, you can contact Micaela Santilli by email (micaela.santilli.21@ucl.ac.uk)

# Suggest changes:
If you would like to suggest changes to the ontology or propose new classes, please do [raise an issue](https://github.com/galenos-project/mental-health-ontology/issues) on GitHub platform. 

