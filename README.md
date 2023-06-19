# group_project
 Classification of Emotional expressions ​ as a function of orientation and expression​

# How to run the code:
Hopenet was acquired from the link below. To run, it requires a license and some initial setup to be done. Here is a guide that we followed: https://github.com/axinc-ai/ailia-models/blob/master/TUTORIAL.md

The models (direction-model.ipynb, proposed-model.ipynb, baseline-model.ipynb) were trained on Kaggle platform which allows to download the dataset directly and use a better GPU so just upload the notebooks and required csvs there and it should work without any issues.

In FUN.ipynb is data analysis and processing of annotated csvs from affectnet dataset. It shouldn’t be run lineary (cell by cell) because there will be errors.

‘Direction data.ipynb’ contains manual algorithm for calculating direction from ThePointing03 dataset.

‘affectnet-annotate.ipynb’ loads the pretrained direction model and uses it to annotate the affectnet dataset with direction data.

# Steps (notebooks) in order:
1. Use hopenet to annotate affectnet
2. Use ‘Direction data.ipynb’ to get direction from ThePointing03 dataset
3. Use hopenet to annotate ThePointing03
4. Train (on Kaggle) ‘direction-model.ipynb’
5. Use ‘affectnet-annotate’ with trained direction model (the checkpoint is already in ‘models/’ directory) to extend the data with direction
6. Use ‘FUN.ipynb’ to have do data analysis and have some fun 🙂
7. Use acquired csvs with proposed and baseline models (proposed-model.ipynb, baseline-model.ipynb) on Kaggle to train the models.
8. Do data analysis on the trained models
