# TapasQA - Question Answering on Statistical Plots using Google TAPAS
Details....

## Authors

[Himanshu Jain](https://github.com/nhimanshujain) <br>
[Sooryanath IT](https://github.com/SooryanathIT) <br>
[Sneha Jayaraman](https://github.com/SnehaJayaraman) <br>



# *TapasQA Architecture*
[<img src="/Results/architecture.png" width="1080"/>](/Results/architecture.png)






# *Folder Description*
1) [Training](/Training) - Contains binary classifier model and configuration files
2) [Testing](/Testing) - Contains test files for PED stage and Table QA stage
3) [Evaluation](/Evaluation) - Contains code for CSV generation and Evaluation of Table QA stage
4) [Results](/Results) - Contains results for 8k images tested
5) [WebApp](/WebApp) - Contains code files related to the Flask application of the project
6) [End-To-End](/End-To-End) - Contains python notebook for complete end-to-end execution of the TapasQA model
7) [Miscellaneous](/Miscellaneous) - Contains additional code files
8) [Documents](/Documents) - Contains all the documents from project Phase-1 and Phase-2









# *Files Description*
## *Plot Element Detection stage*
1) [JSON Generation](/PED/Plot_Elements_Detection_JSON_Generation.ipynb) - Extracts bounding box predictions using Dectectron2

## *Optical Character Recognition stage*
1) [OCR Recognition](/Evaluation/src/ocr_table_generation/) - Extracts text data from the bounding box of the plots

## *Semi-Structured Table Generation stage*
1) [TO Fill](/Evaluation/src/ocr_table_generation/) - 


## *Table QA stage*

### *Binary Classifier*
1) [Training](/Training/Binary_Classifier/binary_classifier_training.ipynb) - This file is used to train the binary classifier model
2) [Evaluation](/Training/Binary_Classifier/models) - Saved model is used to infer open-ended question or Yes/No question

### *Tapas and Tabfact model*
1) [Testing](/Testing) - Tapas and Tabfact models are tested for Horizontal, Vertical, Dot and Dot-Line plots
2) [Evaluation](/Evaluation) - Tapas and Tabfact models are evaluated for 8k images (2k per category)








# *Data*
> *[PlotQA dataset](https://github.com/NiteshMethani/PlotQA/blob/master/PlotQA_Dataset.md)* is used for visual question answering on statistical plots








# *Evaluation of PED model*
To be filled









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
Run the following files after csv file generation and environment setup, to produce the results
> Vertical.ipynb <br>
> Horizontal.ipynb <br>
> DOT_LINE.ipynb











# *Results*

### PED Stage
Insert results img here

### Table QA Stage
[<img src="/Results/tapas_qa_results.jpg" width="1080"/>](/Results/tapas_qa_results.jpg)









# *Web App* (To be filled)
1) Setup
2) Start




