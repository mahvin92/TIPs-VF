# TIPs-VF
TIPs-VF (or the Translator-Interpreter Pre-seeding for Variable-length Fragments) is a member of the TIPs family of encoding schemes for augmented representation of genetic sequences in machine learning, specifically for genetic engineering and synthetic biology applications.

For more information about TIPs, please visit https://tips.logiacommunications.com/

## Computational environment
Note that the implementation of TIPs for machine learning studies was tested only on Google Colab, but we welcome any contributions and improvements for local implementation using the recent Python version.

## Installation
1. The TIPs-VF encoding scheme is a backend-hosted tool that requires no installation. TIPs-VF submission is available at https://tips.logiacommunications.com/submission
2. Google Colab comes pre-installed with many popular libraries. However, if required please install the following dependencies: NumPy, Pandas, Matplotlib, umap-learn, seaborn, and TensorFlow. Use the command: !pip install <library_name>

## Representation
1. Representation of sequence data can be done at the TIPs portal page.
2. Please visit [https://tips.logiacommunications.com/](https://tips.logiacommunications.com/tips-encoding) for more information.


## Implementation 
1. The implementation of TIPs-VF is availale on Google Colab.
2. Please visit [https://colab.research.google.com/drive/1dXYjzRBdmhm5RKBjm5xO2ry6vmhutQ3h ](https://colab.research.google.com/drive/1dXYjzRBdmhm5RKBjm5xO2ry6vmhutQ3h) for more information.


## FAQs
***

# Running the TIPs-VF workflow
1. Download the TIPs-VF data for: 1) Truncation and fragmentation 'chr genes TIPS_FR.tsv', 2) Sequence homology 'viral genes TIPS_FR.tsv', 3) Sequence motif 'plasmid_sequences TIPS_FR.txt', 4) Splice junction 'fusion genes TIPS_FR.tsv'.
2. Open the script and load the notebook (.ipynb) on Google Colab.
3. Execute the program, ensuring to change the file names of the data whenever running a different workflow.

# Custom representation
1. Prepare your data in a FASTA format and store it in a .txt file.
2. You can optionally check the 'pre-processing' tools available if you need to clean or pre-process your data according to the needs of your workflow.
3. Visit [https://tips.logiacommunications.com/submission](https://tips.logiacommunications.com/submission) to encode your data.
4. Implement, inspect, and visualize the representation by following the execution at [https://colab.research.google.com/drive/1dXYjzRBdmhm5RKBjm5xO2ry6vmhutQ3h ](https://colab.research.google.com/drive/1dXYjzRBdmhm5RKBjm5xO2ry6vmhutQ3h).


# Contact and support
Please send your inquiries at tipsencoding@gmail.com or visit https://tips.logiacommunications.com/tips-contact


# License notice
This repository contains supporting materials, sample datasets, and example notebooks for TIPs-VF research and experimentation. The core TIPs-VF software, including its underlying codebase and algorithms, is proprietary and not included in this repository. These materials are for educational and illustrative purposes only.
