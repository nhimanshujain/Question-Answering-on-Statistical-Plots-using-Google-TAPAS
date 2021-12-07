# TapasQA - Question Answering on Statistical Plots using Google TAPAS
Details....

## Authors

[Himanshu Jain](https://github.com/nhimanshujain) <br>
[Sooryanath IT](https://github.com/SooryanathIT) <br>
[Sneha Jayaraman](https://github.com/SnehaJayaraman) <br>

# *Folder Description*
1) [Traning](/Training) - Contains binary classifier model and configuration files
2) [Testing](/Testing) - Contains test files for PED stage and Table QA stage
3) [Evaluation](/Evaluation) - Contains code for CSV generation and Evaluation of Table QA stage
4) [Results](/Results) - Contains results for 8k images tested
5) [WebApp](/WebApp) - Contains code files related to the Flask application of the project
6) [Documents](/Documents) - Contains all the documents from project Phase-1 and Phase-2
7) [End-To-End](/End-To-End) - Contains python notebook for complete end-to-end execution of the TapasQA model
8) [Miscellaneous](/Miscellaneous) - Contains additional code files



# *TapasQA Architecture*
[<img src="/Results/architecture.png" width="1080"/>](/Results/architecture.png)

# *Plot Element Detection stage*
## *Object Detection*
Content...

## *Feature Extraction*
Content...

# *Optical Character Recognition stage*
Content...

# *Semi-Structured Table Generation stage*
Content...


# *Table QA stage*
Content...

## *Binary Classifier*
Content...
[<img src="/Training/Binary_Classifier/binary_classifier_architecture.png" height="256"/>](/Training/Binary_Classifier/binary_classifier_architecture.png)

## *Tapas*
Content...

## *Tabfact*
Content...





# *Data*
[PlotQA dataset](https://github.com/NiteshMethani/PlotQA/blob/master/PlotQA_Dataset.md) is used for visual question answering on statistical plots




# *Evaluation of TapasQA model*

### 1) *CSV Generation*
```
+
|--- csv_generation
|     |
|     |--- GetAllCSV_1.ipynb
|     |--- GetAllCSV_2.ipynb
|
+
```
Execute the files under *[csv_generation](/Evaluation/csv_generation)* directory to generate CSV files required for testing Table QA stage

### 2) *Setup*
```bash
> conda create -n brevis python=3.6
> conda activate brevis
> pip install -r requirements.txt
> conda install nb_conda_kernels
> jupyter notebook
```
Requirements file can be found [here](/Evaluation/requirements.txt)


### 3) *Folder Structure*
```
+
|--- Evaluation
|     |
|     |--- Binary_Classifier (dir)
|     |--- plotqa
|            |--- TEST
|                  |--- final_csv (dir)
|                  |--- png (dir)
|                  |--- annotations.json
|                  |--- qa_pairs.json
|     |--- results
|     |--- tabfact_model (auto-generated)
|     |--- tapas_model (auto-generated)
|     |--- Vertical.ipynb (file)
|     |--- Horizontal.ipynb (file)
|     |--- DOT_LINE.ipynb (file)
|
+
```
Create the folder structure as mentioned


### 4) Execution 
Run the files - Vertical.ipynb, Horizontal.ipynb, DOT_LINE.ipynb
after csv file generation and environment setup, to produce the results






# *Results*

### PED Stage
Insert results img here

### Table QA Stage
[<img src="/Results/tapas_qa_results.jpg" width="1080"/>](/Results/tapas_qa_results.jpg)




# *Web App* (To be filled)
1) Setup
2) Start




