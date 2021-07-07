## Informations générales communes aux deux architectures :

* 1,861 lines
* Dynamic learning rate (start: 0.001, then application of a 0.75 factor each 10 epochs)
* Input: height 64
* Batch of 1
* Epochs : 30, with early stopping
* Training set : 10 XML (total: 1,692 lines, train: 1,524 lines, val: 168)
* Testing set : 1 XML (168 lines): p48.xml
* No unicode normalization
* No data augmentation

ToDo: add learning curve to experiments for each architecture

## Experiments
### Without abbreviations, with spaces:
* classes : 60
* accuracy HTR-CB : 95.11%
* accuracy HTR-WB : 95.29%
=> see pred_htr-cb_d-abb1.txt

### Without abbreviations, without spaces:
* classes : 59
* accuracy HTR-CB : 95.45%
* accuracy HTR-WB : 95.45%
=> see pred_htr-cb_d-abb2.txt

### With abbreviations, with spaces:
* classes : 34
* accuracy HTR-CB : 89.41%
* accuracy HTR-WB : 96.24%
=> see pred_htr-wb_d-exp1.txt

### With abbreviations, without spaces:
* classes : 33
* accuracy HTR-CB : 90.31%
* accuracy HTR-WB : 97.04%
=> see pred_htr-wb_d-exp2.txt