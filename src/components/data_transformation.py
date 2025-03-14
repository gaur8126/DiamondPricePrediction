from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import os
import sys 
from src.logger import logging
from src.exception import CustomException
import pandas as pd 
from dataclasses import dataclass
import numpy as np 
from src.utils import save_object

@dataclass
class DataTransformationconfig:
    preprocessor_ob_file_path = os.path.join('artifacts','preprocessor.pkl')



class DataTransformation:
    def __init__(self) :
        self.data_transformation_config = DataTransformationconfig()

    def get_data_transformation_object(self):

        try:
            logging.info('Data Transformation Initiated')

            categorical_col  =['cut', 'color', 'clarity']
            numerical_col = ['carat', 'depth', 'table', 'x', 'y', 'z']


            cut_categories = ['Premium', 'Very Good', 'Ideal', 'Good', 'Fair']
            clarity_categories = ['VS2', 'SI2', 'VS1', 'SI1', 'IF', 'VVS2', 'VVS1', 'I1']
            color_categories = ['F', 'J', 'G', 'E', 'D', 'H', 'I']

            logging.info('Pipeline initaited')

            num_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )
        
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('encoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                    ('scaler',StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_col),
                ('cat_pipeline',cat_pipeline,categorical_col)
            ]) 

            return preprocessor
        except Exception as e :

            logging.info("Error in Data Transformation")
            raise CustomException(e,sys)
        

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)


            logging.info("Read train and test data completed")
            logging.info(f'Train Trandformed Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Trandformed Head : \n{test_df.head().to_string()}')

            logging.info('obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_object()
            
            target_column_name = 'price'
            drop_column = [target_column_name,'id']

            input_feature_train_df = train_df.drop(columns=drop_column,axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=drop_column,axis=1)
            target_feature_test_df = test_df[target_column_name]


            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr  = preprocessing_obj.transform(input_feature_test_df)

            logging.info('Applying preprocessing object on training and testing datasets')

            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_ob_file_path,
                obj=preprocessing_obj
            )

            logging.info('Preproceesor pickel is created and saved')

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_ob_file_path
            )
        
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys)