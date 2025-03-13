# Diamond Price Prediction

## Overview

The Diamond Price Prediction project leverages machine learning techniques with `85.4% accuracy` to forecast diamond prices based on various attributes. By analyzing factors such as carat weight, cut, color, clarity, and other physical dimensions, the model aims to provide accurate price predictions, assisting both buyers and sellers in making informed decisions.

## Dataset

The project utilizes the [Kaggle Diamond Dataset](https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv), which includes over 54,000 diamonds with 10 attributes, including the target variable 'Price'. The dataset encompasses features like:

- **Carat**: Weight of the diamond.
- **Cut**: Quality of the diamond's cut.
- **Color**: Color grade of the diamond.
- **Clarity**: Clarity grade of the diamond.
- **Depth**: Total depth percentage.
- **Table**: Width of the diamond's table.
- **x, y, z**: Dimensions of the diamond.

## Techniques
- [x] Pandas 
- [x] Numpy   
- [x] Seaborn
- [x] Scikit-Learn
- [x] Flask

## Project Structure
```
Diamond-Price-Prediction/
│
├── artifacts/         
│   ├── model.pkl                
│   ├── preprocessor.pkl
│   ├── raw.csv
│   ├── train.csv
│   └── test.csv
│   
│
├── notebooks/                      
│   ├── data/                 
│      ├── gamestone.csv                 
│   ├── EDA.ipnb                
│   └── model_training.ipynb       
│
├── src/                        
│   ├── components/
│   |   ├── __init__.py
│   |   ├── data_ingestion.py
│   |   ├── data_transformation.py
│   |   └── model_trainer.py
│   ├── pipelines/
│   |    ├── __init__.py
│   |    ├── prediction_pipeline.py
│   |    └── training_pipeline.py
|   ├── __init__.py                
│   ├── exception.py  
│   ├── logging.py
│   └── utils.py
│
├── templates/                          
│   ├── form.html                     
│   └── index.html                  
│
├── .gitignore               
├── README.md                      
├── application.py                        
├── requirements.txt                      
└── setup.py                       
```




## Installation Instruction

1. **Clone the repository**:

   ```bash
   https://github.com/gaur8126/DiamondPricePrediction.git

2. **Nevigate to the project directory**
   ```bash
   cd DiamondPricePrediction
   
3. **Set up Virtual Environment**:

   ```bash
   conda create -p python==3.10 -y   , #  conda environment
   python -m venv env                  #   python environment

  4. **Activate the Virtual Environment**
     ```bash
     conda activate venv/  # windows [cmd]
     source activate venv  # Linux  [bash]

  
     .\env\Scripts\activate    # windows
     source env/bin/activate   # Linux

  5. **Install requirements**
     ```bash
     pip install -r requirements.txt

  **Run the Flask Applicaion**
  ```bash
python application.py


