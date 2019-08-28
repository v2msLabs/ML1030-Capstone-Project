# this set-up file defines KASI Insight scripts to be installed as a module locally
import setuptools

setuptools.setup(
    name="kasi",
    version="0.7.8",
    packages=setuptools.find_packages(),
    description="This package comprises code to clean KASI Insight raw data and train the simulator and evaluator models",
    entry_points={
        'console_scripts': ['kasi_process_data=kasi.processing.data_processor:main',
                            'kasi_train_simulator=kasi.training.train_simulator:main',
                            'kasi_train_evaluator=kasi.training.train_evaluator:main',
                            'kasi_tune=kasi.training.tuning:main']
    },
    install_requires=[
        'joblib>=0.13.0'
        'pandas>=0.24.1',
        'numpy>=1.16.1',
        'scipy>=1.2.0',
        'scikit-learn>=0.20'
        'imbalanced-learn>=0.5'
    ],
    extras_require={
        'interactive': ['matplotlib>=3.0.0', 'jupyter','seaborn'],
    }
)
