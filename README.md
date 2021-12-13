# TapasQA - Question Answering on Statistical Plots using Google TAPAS
It is a Visual Question Answering system which accepts statistical plots along with questions on the plot (with respect to the elements of the plot) to provide answers to the questions posed.

**Benefit**: Helps data analysts question and understand plots on a large scale, and automate the decision-making capabilities.

**Scope**: <br>
Plots = _Dot, Line, Bar (Vertical, Horizontal, Grouped)_ <br>
Questions = _Open-ended, Boolean (Yes / No)_


## Authors

[Himanshu Jain](https://github.com/nhimanshujain) <br>
[Sooryanath IT](https://github.com/SooryanathIT) <br>
[Sneha Jayaraman](https://github.com/SnehaJayaraman) <br>



# *TapasQA Architecture*
[<img src="/Results/img/architecture.png" width="1080"/>](/Results/architecture.png)






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
1) [JSON Generation](/Training/PED/Plot_Elements_Detection_JSON_Generation.ipynb) - Extracts bounding box predictions using Detectron2

## *Optical Character Recognition stage*
1) [OCR Recognition](/Evaluation/src/ocr_table_generation/) - Extracts text data from the bounding box of the plots

## *Semi-Structured Table Generation stage*
1) [Table Fillup](/Evaluation/src/ocr_table_generation/) - Information extracted out of textual and visual elements is structured into a table


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

Execute the Testing Section in [PED_Testing](/Training/PED/Plot_Elements_Detection_JSON_Generation.ipynb) using the weights of the final saved model . The metrics alongside the json predictions will be generated .





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

#### AVERAGE PRECISION AT DIFFERENT NUMBER OF ITERATIONS
> [<img src="/Results/img/ped_results.png" width="210" height="230"/>](/Results/img/ped_results.png) <br>

#### PED EVALUATION
> [<img src="/Results/img/average_precision.png" width="512" height="150"/>](/Results/img/average_precision.png)

### Table QA Stage
#### AVERAGE ACCURACY FOR DIFFERENT PLOT TYPES
> [<img src="/Results/img/table_qa_result.png" width="750" />](/Results/img/table_qa_result.png)









# *Web App* (To be filled)
1) Setup
2) Start




