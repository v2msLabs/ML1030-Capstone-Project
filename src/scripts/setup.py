# this set-up file defines KASI Insight scripts to be installed as a module locally
import setuptools


setuptools.setup(
    name="kasi",
    version="1.0.4",
    packages=setuptools.find_packages(),
    description="This package comprises code to clean KASI Insight raw data and to tune and train the simulator and evaluator models",
    entry_points={
        'console_scripts': ['kasi_process=kasi.processing.data_processor:main',
                            'kasi_tune=kasi.training.tune_model:main',
                            'kasi_train=kasi.training.train_model:main'
                            ]
    },
    install_requires=[
        'pandas>=0.24.1',
        'joblib>=0.13.0',
        'scipy>=1.2.0',
        'scikit-learn>=0.20',
        'imbalanced-learn>=0.5',
        'seaborn'
    ]
)
